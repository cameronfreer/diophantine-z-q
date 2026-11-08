"""Author checks of exact tail coefficients, circuit consumers and margins."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scalar-chain-reduction'))
from check_chain import poly, add, scale, mul


def mathematics():
    a = F(-2, 5)
    for j in range(2, 14):
        a *= F(4*j-5, 4*j+1)
    assert a.denominator == 5**2 * 7 * 17 * 29 * 37 * 41 * 53
    assert a.numerator % 53 != 0
    # For j>=14, f(j)=4j-51-floor((4j+1)/10) starts at zero.
    # The floor difference is zero or one, so f increases by at least 3.
    assert 4*14-51-(4*14+1)//10 == 0
    assert all((r+4)//10-r//10 in [0, 1] for r in range(10))
    H = 3*2**106*(2**32*3**9)**6*46410**18+128
    c, b = 2*3**1007, 3**1007
    assert c**415 > (4*H)**992
    margins = {}
    for k in range(46, 52):
        assert b**(16*k-577) > (24*H)**(8*k)
        margins[str(k)] = {'lucasExponentNumerator': 16*k-577, 'denominator': 8*k}
    assert 40*H < 2**670 and b > 67000 and b > 152
    # This is a boundary for these sufficient inequalities on the 6Z lattice,
    # not an optimality assertion about anchors or circuits.
    assert (2*3**1004)**415 <= (4*H)**992
    assert b**143 <= (24*H)**360
    maximum = 28902*3**1344
    assert len(str(maximum)) == 646 and maximum.bit_length() == 2146
    return {'a13': str(a), 'relativePrecision': 51, 'anchorExponent': 2016,
            'indexDivisibilityAt3': 1007, 'scalarMargin': True,
            'lucasMargins': margins, 'inputMargin': True,
            'previousAnchorMultipleFailsScalarSufficientMargin': True,
            'order45FailsLucasSufficientMarginAt2016': True}


def check(before, after, order):
    assert order in [46, 47]
    assert before['fixedParameter']['value'] == '3^2130'
    assert after['fixedParameter'] == dict(before['fixedParameter'], value='3^2016')

    def canonical(name):
        return (name.replace('q'+str(order), 'q45').replace('E'+str(order), 'E45')
                .replace('testSquare.'+str(order)+'.', 'testSquare.45.')
                .replace('symmetric.'+str(order)+'.', 'symmetric.45.'))

    def named(data):
        names = {c['id']: canonical(c['name']) for c in data['coordinates']}
        return {canonical(r['name']): {(t['sPower'], tuple(sorted(names[i] for i in t['monomial']))):
                                       F(t['coefficient']) for t in r['terms']} for r in data['residuals']}

    a, b = named(before), named(after)
    added = {'detector'+str(i)+'.highLift.definition' for i in range(3)}
    changed = {'detector'+str(i)+'.q45.definition' for i in range(3)}
    assert b.keys()-a.keys() == added and not a.keys()-b.keys()
    assert {n for n in a.keys() & b.keys() if a[n] != b[n]} == changed
    # Guards refer only to unchanged earlier coordinate IDs or semantic rows;
    # compare them after decoding IDs, because later allocations are shifted.
    def guards(data):
        names = {c['id']: canonical(c['name']) for c in data['coordinates']}
        def convert(x, key=None):
            if key == 'monomial': return [names[i] for i in x]
            if isinstance(x, list): return [convert(i) for i in x]
            if isinstance(x, dict): return {k: convert(v, k) for k, v in x.items()}
            return x
        return convert(data['guards'])
    assert guards(before) == guards(after)
    rows = {r['name']: poly(r['terms']) for r in after['residuals']}
    v = {n: poly(p['terms']) for n, p in after['values'].items()}
    def eq(name, lhs, rhs):
        expected = add(lhs, scale(rhs, -1)); actual = rows[name]
        pivot = min(expected)
        assert actual == scale(expected, actual[pivot]/expected[pivot]), name
    for i in range(3):
        p = 'detector'+str(i)
        delta = add(scale(v[p+'.t'], 98), {(): F(-1)})
        lift = v[p+'.highLift']
        factor = delta if order == 46 else v[p+'.eDelta']
        eq(p+'.highLift.definition', lift, mul(v[p+'.mixedHigh'], factor))
        eq(p+'.q'+str(order)+'.definition', mul(v[p+'.q'+str(order)], v[p+'.q1']), mul(lift, lift))
    return {'addedRows': sorted(added), 'changedRows': sorted(changed),
            'unchangedRows': len(a)-len(changed), 'allGuardsUnchanged': True}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('before', type=Path)
    ap.add_argument('after', type=Path)
    ap.add_argument('--order', type=int, required=True)
    ap.add_argument('--report', type=Path, required=True)
    args = ap.parse_args()
    before, after = [json.loads(p.read_text()) for p in [args.before, args.after]]
    comparison = check(before, after, args.order)
    for rowname in ['detector0.highLift.definition', 'detector1.q'+str(args.order)+'.definition', 'scalar.N.definition']:
        bad = deepcopy(after)
        row = next(r for r in bad['residuals'] if r['name'] == rowname)
        row['terms'][0]['coefficient'] = str(F(row['terms'][0]['coefficient']) + 1)
        try:
            check(before, bad, args.order)
        except (AssertionError, KeyError):
            pass
        else:
            raise AssertionError('Accepted mutation: '+rowname)
    args.report.write_text(json.dumps({'status': 'PASS', 'arithmeticAcceptance': False,
                                      'comparison': comparison, 'mathematics': mathematics(),
                                      'negativeControlsRejected': 3}, indent=2)+'\n')
    print('PASS: exact higher-order rows, outside consumers, finite coefficients and margins')


if __name__ == '__main__':
    main()
