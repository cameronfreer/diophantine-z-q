"""Replay follow-up experiments without changing either review PR.

These finite checks do not independently accept the changed arithmetic.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

from chart_patch import transform as chart
from log_patch import transform as rational_log
from scalar_patch import transform as scalar

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PARENT = HERE.parent/'conditional-quartic-reduction'
CONSTRUCTION = PARENT/'construction'
TRANSPORT = HERE.parent/'factored-pole-reduction'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def named_rows(data):
    names = {c['id']: c['name'] for c in data['coordinates']}
    return {r['name']: {(t['sPower'], tuple(sorted(names[i] for i in t['monomial']))):
                        Fraction(t['coefficient']) for t in r['terms']} for r in data['residuals']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    bindings = json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
    for bound in bindings['files']:
        if sha(REPO/bound['path']) != bound['sha256']:
            raise ValueError('Changed source: '+bound['path'])
    if args.output:
        output = args.output.resolve()
        if output.exists() and any(output.iterdir()):
            raise ValueError('Output must be absent or empty')
        if output == HERE or HERE in output.parents:
            raise ValueError('Keep outputs outside the source packet')
        output.mkdir(parents=True, exist_ok=True)
    else:
        (REPO/'build').mkdir(exist_ok=True)
        output = Path(tempfile.mkdtemp(prefix='quartic-followup-', dir=REPO/'build'))

    def run(folder, *command):
        with (folder/'reproduction.log').open('a') as log:
            subprocess.run(list(map(str, command)), cwd=REPO, stdout=log,
                           stderr=subprocess.STDOUT, check=True)

    run(output, sys.executable, '-B', PARENT/'reproduce.py', '--check-source')
    run(output, sys.executable, '-B', HERE/'check_local_claims.py', '--report', output/'local-claims.json')
    original = (CONSTRUCTION/'builder.cjs').read_text()
    reports = []
    for label, transform, count, residuals in [
        ('baseline', lambda s: s, 389, 357),
        ('biquadratic-chart', chart, 389, 357),
        ('rational-log', rational_log, 397, 365),
        ('scalar-zero', scalar, 387, 356),
    ]:
        print('Rebuilding '+label, flush=True)
        folder = output/label
        folder.mkdir()
        (folder/'builder.cjs').write_text(transform(original))
        run(folder, 'node', folder/'builder.cjs')
        run(folder, sys.executable, '-B', CONSTRUCTION/'tools/compile_ir.py',
            folder/'raw-translated-ir.json', folder/'compiled')
        run(folder, 'node', CONSTRUCTION/'tools/checker.cjs',
            '--input', folder/'raw-translated-ir.json',
            '--compiled', folder/'compiled/compiled-ir.json',
            '--certificate', folder/'compiled/reduction-certificate.json',
            '--coordinate-map', folder/'compiled/coordinate-map.json',
            '--quartic', folder/'compiled/polynomial.json', '--report', folder/'gate-check.json')
        compiled = folder/'compiled/compiled-ir.json'
        coordinate_map = json.loads((folder/'compiled/coordinate-map.json').read_text())
        free = set(coordinate_map['omittedFreeCoordinates'])
        omission = None
        if free:
            # The generic compiler already certifies omission in the quartic
            # coordinate map, but keeps free slots in its quadratic IR. Apply
            # that exact omission before the affine-search consumer, which
            # requires a pivot for every coordinate it receives.
            data = json.loads(compiled.read_text())
            removed = [c for c in data['coordinates'] if c['id'] in free]
            assert label == 'scalar-zero'
            assert sorted(c['name'] for c in removed) == ['scalar.preparationU', 'scalar.preparationV']
            assert all(c['kind']=='base' and not c.get('protected',False) for c in removed)
            assert not any(set(t['monomial']) & free for r in data['residuals'] for t in r['terms'])
            before_sha = sha(compiled)
            data['coordinates'] = [c for c in data['coordinates'] if c['id'] not in free]
            active = folder/'compiled/active-ir.json'
            active.write_text(json.dumps(data,indent=2)+'\n')
            assert json.loads(compiled.read_text())['residuals'] == data['residuals']
            omission = {'sourceSha256':before_sha,'activeIrSha256':sha(active),
                        'coordinateMapSha256':sha(folder/'compiled/coordinate-map.json'),
                        'omittedCoordinates':removed,'allResidualsUnchanged':True,
                        'proof':'These two unprotected base slots occur in no residual. Forget them; the inverse extension assigns zero.'}
            (folder/'free-omission.json').write_text(json.dumps(omission,indent=2)+'\n')
            compiled = active
        run(folder, sys.executable, '-B', CONSTRUCTION/'tools/run_pipeline.py',
            compiled, folder/'final', '--orders', 2)
        source = folder/'final/integer-candidate-ir.json'
        data = json.loads(source.read_text())
        assert (len(data['coordinates']), len(data['residuals'])) == (count, residuals)
        if label == 'baseline':
            assert sha(source) == '1e9071816ccb40d562545be08f21ccac76813a64796173d155d0d3ae7dbebb50'
        # Adapt filenames, expected counts and negative-control coordinate
        # lookups; keep all reconstruction and consumer checks present.
        factored = folder/'factored'
        factored.mkdir()
        shutil.copyfile(source, factored/'baseline-input-ir.json')
        for name in ['build_transport.py', 'check_transport.py']:
            text = (TRANSPORT/name).read_text().replace('baseline389-ir.json', 'baseline-input-ir.json')
            text = text.replace('385', str(count-4)).replace('353', str(residuals-4))
            text = text.replace("'monomial':[279]", "'monomial':[next(c['id'] for c in a['coordinates'] if c['name']=='detector0.Bh.quadratic')]")
            text = text.replace("c['id']==280", "c['name']=='detector0.s2.quadratic'")
            (factored/name).write_text(text)
            run(factored, sys.executable, '-B', factored/name, factored)
        run(factored, sys.executable, '-B', CONSTRUCTION/'balance_coefficients.py', factored)
        run(factored, sys.executable, '-B', PARENT/'audit/check_diagonal_scaling.py', factored,
            '--expected-exponent', 2364, '--expected-coordinates', count-4,
            '--expected-residuals', residuals-4, '--expected-max-digits', 757,
            '--expected-max-bits', 2513, '--report', factored/'diagonal-check.json')
        summary = json.loads((factored/'balanced/summary.json').read_text())
        if label == 'scalar-zero':
            assert summary['tableSha256'] == 'd18ae3cf281081e9322969126864a8843f849f2c469e3f7c3b221ed3742166a4'
        reports.append({'experiment': label, 'beforeFactoring': {'coordinates': count, 'residuals': residuals},
                        'coordinateBlocksBeforeFactoring': dict(Counter(c['block'] for c in data['coordinates'])),
                        'compiledIrSha256': sha(source), 'afterFactoring': summary,
                        'freeOmission': omission,
                        'gateReportSha256': sha(folder/'gate-check.json'),
                        'transportReportSha256': sha(factored/'transport-check.json'),
                        'coefficientReportSha256': sha(factored/'diagonal-check.json')})
        print(label+': '+str(count-4)+' variables after factoring', flush=True)
    before = json.loads((output/'baseline/raw-translated-ir.json').read_text())
    after = json.loads((output/'scalar-zero/raw-translated-ir.json').read_text())
    old, new = named_rows(before), named_rows(after)
    scalar_delta = {
        'removedCoordinates': sorted({c['name'] for c in before['coordinates']}-{c['name'] for c in after['coordinates']}),
        'addedRows': sorted(new.keys()-old.keys()), 'deletedRows': sorted(old.keys()-new.keys()),
        'changedRows': sorted(name for name in old.keys() & new.keys() if old[name] != new[name]),
    }
    assert not scalar_delta['removedCoordinates']
    assert before['coordinates'] == after['coordinates']
    active = {i for r in after['residuals'] for t in r['terms'] for i in t['monomial']}
    scalar_delta['unusedRawCoordinates'] = sorted(c['name'] for c in after['coordinates'] if c['id'] not in active)
    assert scalar_delta['unusedRawCoordinates'] == ['scalar.preparationU', 'scalar.preparationV']
    assert not scalar_delta['addedRows']
    assert scalar_delta['deletedRows'] == ['scalar.preparationConic']
    assert scalar_delta['changedRows'] == ['scalar.Bh.definition', 'scalar.preparationT.definition', 'scalar.secondConic']
    for bound in bindings['files']:
        assert sha(REPO/bound['path']) == bound['sha256'], bound['path']
    result = {'status': 'PASS', 'independentAcceptance': False,
              'scope': 'Finite circuit, transport, coefficient and local-algebra checks; changed arithmetic arguments remain author proposals.',
              'sourceBindingsSha256': sha(HERE/'SOURCE_BINDINGS.json'),
              'scalarSourceDelta': scalar_delta, 'experiments': reports}
    (output/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS. Results: '+str(output/'results.json'))


if __name__ == '__main__':
    main()
