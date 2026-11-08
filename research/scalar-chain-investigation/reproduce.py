"""Build the two scalar-chain candidates; finite replay is not acceptance."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

from chain_patch import transform

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PARENT = HERE.parent / 'conditional-quartic-reduction'
CONSTRUCTION = PARENT / 'construction'
TRANSPORT = HERE.parent / 'factored-pole-reduction'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    bindings = json.loads((HERE / 'SOURCE_BINDINGS.json').read_text())
    for bound in bindings['files']:
        if sha(REPO / bound['path']) != bound['sha256']:
            raise ValueError('Changed source: ' + bound['path'])
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    if any(root.iterdir()):
        raise ValueError('Output must be empty')
    sys.path.insert(0, str(HERE.parent / 'quartic-followup'))
    from scalar_patch import transform as zero
    original = (CONSTRUCTION / 'builder.cjs').read_text()
    with (root / 'source-check.log').open('w') as log:
        subprocess.run([sys.executable, '-B', str(PARENT / 'reproduce.py'), '--check-source'],
                       cwd=REPO, stdout=log, stderr=subprocess.STDOUT, check=True)
        baseline = root / 'baseline'
        baseline.mkdir()
        (baseline / 'builder.cjs').write_text(original)
        subprocess.run(['node', str(baseline / 'builder.cjs')], cwd=REPO,
                       stdout=log, stderr=subprocess.STDOUT, check=True)
    reports = []
    for label, source, count, residuals in [
        ('chain31', transform(original), 389, 357),
        ('chain31-zero', transform(zero(original)), 387, 356),
    ]:
        folder = root / label
        folder.mkdir()
        def run(*command):
            with (folder / 'reproduction.log').open('a') as log:
                subprocess.run(list(map(str, command)), cwd=REPO, stdout=log,
                               stderr=subprocess.STDOUT, check=True)
        (folder / 'builder.cjs').write_text(source)
        run('node', folder / 'builder.cjs')
        run(sys.executable, '-B', HERE / 'check_chain.py', folder / 'raw-translated-ir.json',
            '--baseline', baseline / 'raw-translated-ir.json', '--report', folder / 'source-check.json',
            *(['--zero'] if label == 'chain31-zero' else []))
        run(sys.executable, '-B', CONSTRUCTION / 'tools/compile_ir.py',
            folder / 'raw-translated-ir.json', folder / 'compiled')
        run('node', CONSTRUCTION / 'tools/checker.cjs',
            '--input', folder / 'raw-translated-ir.json',
            '--compiled', folder / 'compiled/compiled-ir.json',
            '--certificate', folder / 'compiled/reduction-certificate.json',
            '--coordinate-map', folder / 'compiled/coordinate-map.json',
            '--quartic', folder / 'compiled/polynomial.json',
            '--report', folder / 'gate-check.json')
        compiled = folder / 'compiled/compiled-ir.json'
        coordinate_map = json.loads((folder / 'compiled/coordinate-map.json').read_text())
        free = set(coordinate_map['omittedFreeCoordinates'])
        if free:
            assert label == 'chain31-zero'
            data = json.loads(compiled.read_text())
            removed = [c for c in data['coordinates'] if c['id'] in free]
            assert sorted(c['name'] for c in removed) == ['scalar.preparationU', 'scalar.preparationV']
            assert all(c['kind'] == 'base' and not c.get('protected', False) for c in removed)
            assert not any(set(t['monomial']) & free for r in data['residuals'] for t in r['terms'])
            data['coordinates'] = [c for c in data['coordinates'] if c['id'] not in free]
            compiled = folder / 'compiled/active-ir.json'
            compiled.write_text(json.dumps(data, indent=2) + '\n')
        run(sys.executable, '-B', CONSTRUCTION / 'tools/run_pipeline.py',
            compiled, folder / 'final', '--orders', 2)
        source_ir = folder / 'final/integer-candidate-ir.json'
        data = json.loads(source_ir.read_text())
        actual = (len(data['coordinates']), len(data['residuals']))
        print(label, 'before conics:', actual, flush=True)
        assert actual == (count, residuals), actual
        factored = folder / 'factored'
        factored.mkdir()
        shutil.copyfile(source_ir, factored / 'baseline-input-ir.json')
        for name in ['build_transport.py', 'check_transport.py']:
            text = (TRANSPORT / name).read_text().replace('baseline389-ir.json', 'baseline-input-ir.json')
            text = text.replace('385', str(count - 4)).replace('353', str(residuals - 4))
            text = text.replace("'monomial':[279]", "'monomial':[next(c['id'] for c in a['coordinates'] if c['name']=='detector0.Bh.quadratic')]")
            text = text.replace("c['id']==280", "c['name']=='detector0.s2.quadratic'")
            (factored / name).write_text(text)
            run(sys.executable, '-B', factored / name, factored)
        run(sys.executable, '-B', CONSTRUCTION / 'balance_coefficients.py', factored)
        run(sys.executable, '-B', PARENT / 'audit/check_diagonal_scaling.py', factored,
            '--expected-exponent', 2130, '--expected-coordinates', count - 4,
            '--expected-residuals', residuals - 4, '--expected-max-digits', 682,
            '--expected-max-bits', 2266, '--report', factored / 'diagonal-check.json')
        summary = json.loads((factored / 'balanced/summary.json').read_text())
        polynomial = json.loads((factored / 'balanced/polynomial.json').read_text())
        assert max(abs(int(t['coefficient'])) for t in polynomial['terms']) == 28902 * 3**1420
        reports.append({'experiment': label, 'summary': summary,
                        'sourceReportSha256': sha(folder / 'source-check.json'),
                        'gateReportSha256': sha(folder / 'gate-check.json'),
                        'conicReportSha256': sha(factored / 'transport-check.json'),
                        'coefficientReportSha256': sha(factored / 'diagonal-check.json')})
        print(label, summary, flush=True)
    for bound in bindings['files']:
        assert sha(REPO / bound['path']) == bound['sha256'], bound['path']
    (root / 'results.json').write_text(json.dumps({'status': 'PASS', 'independentAcceptance': False,
                                                 'sourceBindingsSha256': sha(HERE / 'SOURCE_BINDINGS.json'),
                                                 'experiments': reports}, indent=2) + '\n')


if __name__ == '__main__':
    main()
