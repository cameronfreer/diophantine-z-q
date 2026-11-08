"""Measure complete higher-order variants above the 383-variable packet.

Research experiment: compiler replay is not arithmetic acceptance.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CONSTRUCTION = HERE.parent / 'conditional-quartic-reduction/construction'
TRANSPORT = HERE.parent / 'factored-pole-reduction'
sys.path.insert(0, str(HERE.parent / 'scalar-chain-reduction'))
sys.path.insert(0, str(HERE.parent / 'scalar-preparation-zero'))
from chain_patch import transform as chain
from zero_patch import transform as zero
from check_zero import omit_unused


def transform(source, order, exponent):
    source = zero(chain(source, exponent=exponent))
    if order == 45:
        return source
    old = "let q45=rquot('detector'+r+'.q45',sq(mixedHigh),q1cube,'positive_order_one_weight');"
    if order == 46:
        new = """let highLift=rm('detector'+r+'.highLift',mixedHigh,delta);
 let q45=rquot('detector'+r+'.q45',sq(highLift),q1,'positive_order_one_weight');"""
    elif order == 47:
        new = """let highLift=rm('detector'+r+'.highLift',mixedHigh,eDelta);
 let q45=rquot('detector'+r+'.q45',sq(highLift),q1,'positive_order_one_weight');"""
    else:
        raise ValueError('Unsupported weight circuit')
    assert source.count(old) == 1
    result = re.sub(r'\b45\b', str(order), source.replace(old, new))
    return result.replace('q45', 'q' + str(order)).replace('E45', 'E' + str(order))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--order', type=int, choices=[46, 47], required=True)
    ap.add_argument('--exponent', type=int, required=True)
    args = ap.parse_args()
    bindings = json.loads((HERE / 'SOURCE_BINDINGS.json').read_text())
    def check_bindings():
        for bound in bindings['files']:
            assert hashlib.sha256((REPO / bound['path']).read_bytes()).hexdigest() == bound['sha256'], bound['path']
    check_bindings()
    out = args.output.resolve()
    assert args.exponent == 2016
    assert not out.exists() or not any(out.iterdir())
    assert REPO / 'research' not in out.parents
    out.mkdir(parents=True, exist_ok=True)

    def run(*command):
        print('Run', Path(str(command[1])).name if len(command) > 1 else command[0], flush=True)
        with (out / 'replay.log').open('a') as log:
            subprocess.run(list(map(str, command)), cwd=REPO, stdout=log,
                           stderr=subprocess.STDOUT, check=True)

    source = transform((CONSTRUCTION / 'builder.cjs').read_text(), args.order, args.exponent)
    baseline = out / 'baseline383'
    baseline.mkdir()
    (baseline / 'builder.cjs').write_text(transform((CONSTRUCTION / 'builder.cjs').read_text(), 45, 2130))
    run('node', baseline / 'builder.cjs')
    (out / 'builder.cjs').write_text(source)
    run('node', out / 'builder.cjs')
    run(sys.executable, '-B', HERE / 'check_precision.py', baseline / 'raw-translated-ir.json',
        out / 'raw-translated-ir.json', '--order', args.order, '--report', out / 'precision-check.json')
    run(sys.executable, '-B', CONSTRUCTION / 'tools/compile_ir.py', out / 'raw-translated-ir.json', out / 'compiled')
    run('node', CONSTRUCTION / 'tools/checker.cjs', '--input', out / 'raw-translated-ir.json',
        '--compiled', out / 'compiled/compiled-ir.json', '--certificate', out / 'compiled/reduction-certificate.json',
        '--coordinate-map', out / 'compiled/coordinate-map.json', '--quartic', out / 'compiled/polynomial.json',
        '--report', out / 'gate-check.json')
    active, removed = omit_unused(json.loads((out / 'compiled/compiled-ir.json').read_text()),
                                 json.loads((out / 'compiled/coordinate-map.json').read_text()))
    (out / 'active-ir.json').write_text(json.dumps(active, indent=2) + '\n')
    run(sys.executable, '-B', CONSTRUCTION / 'tools/run_pipeline.py', out / 'active-ir.json', out / 'before-factor', '--orders', 2)
    original = out / 'before-factor/integer-candidate-ir.json'
    ir = json.loads(original.read_text())
    n, m = len(ir['coordinates']) - 4, len(ir['residuals']) - 4
    shutil.copyfile(original, out / 'candidate-ir.json')
    for name in ['build_transport.py', 'check_transport.py']:
        code = (TRANSPORT / name).read_text().replace('baseline389-ir.json', 'candidate-ir.json')
        code = code.replace('385', str(n)).replace('353', str(m))
        code = code.replace("'monomial':[279]", "'monomial':[next(c['id'] for c in a['coordinates'] if c['name']=='detector0.Bh.quadratic')]")
        code = code.replace("c['id']==280", "c['name']=='detector0.s2.quadratic'")
        (out / name).write_text(code)
        run(sys.executable, '-B', out / name, out)
    run(sys.executable, '-B', CONSTRUCTION / 'balance_coefficients.py', out)
    summary = json.loads((out / 'balanced/summary.json').read_text())
    expected = json.loads((HERE / 'EXPECTED.json').read_text())[str(args.order)]
    assert summary == expected['summary']
    run(sys.executable, '-B', HERE.parent / 'conditional-quartic-reduction/audit/check_diagonal_scaling.py',
        out, '--expected-exponent', 2016, '--expected-coordinates', 386, '--expected-residuals', 355,
        '--expected-monomials', 26046 if args.order == 46 else 26037,
        '--expected-max-digits', 646, '--expected-max-bits', 2146, '--report', out / 'diagonal-check.json')
    report_statuses = {'precision-check.json': 'PASS', 'gate-check.json': 'passed_exact_algebra_checks',
                       'transport-check.json': 'PASS', 'diagonal-check.json': 'PASS'}
    for name, status in report_statuses.items():
        assert json.loads((out / name).read_text())['status'] == status, name
    polynomial = json.loads((out / 'balanced/polynomial.json').read_text())
    assert max(abs(int(t['coefficient'])) for t in polynomial['terms']) == 28902*3**1344
    for name, digest in expected['files'].items():
        assert hashlib.sha256((out / name).read_bytes()).hexdigest() == digest, name
    check_bindings()
    print(json.dumps(summary), flush=True)
    receipt = {'order': args.order, 'anchorExponent': args.exponent, 'summary': summary,
               'omittedCoordinates': removed, 'arithmeticAcceptance': False,
               'files': {p: hashlib.sha256((out / p).read_bytes()).hexdigest() for p in
                         ['builder.cjs', 'raw-translated-ir.json', 'final/integer-candidate-ir.json', 'balanced/polynomial.json',
                          *report_statuses]}}
    (out / 'MEASURED.json').write_text(json.dumps(receipt, indent=2) + '\n')


if __name__ == '__main__':
    main()
