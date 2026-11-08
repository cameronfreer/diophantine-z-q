"""Independent exact algebra checks; no imports from author checkers."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json

ZERO = (0, 0, 0)
ONE = {ZERO: Q(1)}
T = {(1, 0, 0): Q(1)}
U = {(0, 1, 0): Q(1)}
Z = {(0, 0, 1): Q(1)}


def add(*ps):
    out = defaultdict(Q)
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}


def scale(p, c):
    return {m: a*c for m, a in p.items() if a*c}


def mul(p, q):
    out = defaultdict(Q)
    for m, c in p.items():
        for n, d in q.items():
            out[tuple(a+b for a, b in zip(m, n))] += c*d
    return {m: c for m, c in out.items() if c}


def power(p, n):
    result = ONE
    for _ in range(n):
        result = mul(result, p)
    return result


def check_block(data, index, new):
    """Decode semantic affine aliases; check actual rows in Q[t,u,z]."""
    prefix = f'detector{index}.'
    mapping = {}
    rows = {r['name']: r['terms'] for r in data['residuals']}
    values = {k[len(prefix):]: v['terms'] for k, v in data['values'].items()
              if k.startswith(prefix)}

    def decode(terms):
        total = {}
        for term in terms:
            assert term['sPower'] == 0
            p = scale(ONE, Q(term['coefficient']))
            for coordinate in term['monomial']:
                p = mul(p, mapping[coordinate])
            total = add(total, p)
        return total

    def identify(name, target):
        terms = values[name]
        assert all(t['sPower'] == 0 and len(t['monomial']) <= 1 for t in terms)
        unknown = [t for t in terms if t['monomial'] and t['monomial'][0] not in mapping]
        assert len(unknown) == 1, (name, unknown)
        term = unknown[0]
        known = [t for t in terms if t is not term]
        mapping[term['monomial'][0]] = scale(add(target, scale(decode(known), -1)), 1/Q(term['coefficient']))
        assert decode(terms) == target

    coefficients = [Q(1)]
    for root in (Q(0), Q(1,49), Q(1,50), Q(1,2450), Q(32,1225)):
        result = [Q(0)] * (len(coefficients)+1)
        for k, c in enumerate(coefficients):
            result[k] -= root*c
            result[k+1] += c
        coefficients = result
    middle = add(power(T,3), scale(power(T,2),coefficients[4]),
                 scale(T,coefficients[3]), scale(ONE,coefficients[2]))
    delta = add(scale(T,98), scale(ONE,-1))
    E = mul(U,power(delta,2))
    e = mul(U,delta)
    targets = [('t',T),('Fsquare',power(T,2)),('Fmiddle',middle),('q1',U),
               ('eDelta',E),('q1SquaredForWeights',power(U,2)),
               ('q1CubedForWeights',power(U,3))]
    # delta2 is already an affine alias of t and Fsquare, not an unknown.
    for name, target in targets:
        identify(name,target)
    assert decode(values['delta2']) == power(delta,2)
    if new:
        assert all(len(t['monomial']) <= 1 for t in values['deltaCubed'])
        assert decode(values['deltaCubed']) == power(delta,3)
        extra = [('eCubed',power(e,3)),('eSixth',power(e,6)),('eTwelfth',power(e,12))]
    else:
        extra = [('mixA',power(E,2)),('mixB',power(E,3)),
                 ('mixC',power(e,6)),('mixD',power(e,12))]
    for name, target in extra:
        identify(name,target)
    identify('q12',Z)
    checked = ['Fsquare','Fmiddle','eDelta','q1SquaredForWeights',
               'q1CubedForWeights'] + [name for name, _ in extra]
    for name in checked:
        assert decode(rows[prefix+name+'.definition']) == {}, prefix+name
    actual = decode(rows[prefix+'q12.definition'])
    expected = add(mul(E,Z),scale(power(e,24),-1))
    pivot = min(expected)
    ratio = actual[pivot]/expected[pivot]
    assert ratio and actual == scale(expected,ratio)
    # At q1=0 the cleared quotient constraint is zero for arbitrary q12.
    assert all(m[1] > 0 for m in expected)
    # At delta=0, i.e. t=1/98, it is likewise zero for arbitrary q1/q12.
    specialized = defaultdict(Q)
    for (t,u,z), c in expected.items():
        specialized[(u,z)] += c*Q(1,98)**t
    assert not any(specialized.values())
    return {'block':index,'route':'new' if new else 'old',
            'checkedDefiningRows':len(checked)+1,
            'q12Constraint':'q1*delta^2*q12-(q1*delta)^24=0',
            'zeroQ1AndZeroDeltaBranchesPreserved':True}


def named(data):
    coordinates = {c['id']:c['name'] for c in data['coordinates']}
    assert len(coordinates)==len(data['coordinates'])
    assert len(set(coordinates.values()))==len(coordinates)
    assert len({r['name'] for r in data['residuals']})==len(data['residuals'])
    def poly(terms):
        out = defaultdict(Q)
        for term in terms:
            key = (term['sPower'],tuple(sorted(coordinates[i] for i in term['monomial'])))
            out[key] += Q(term['coefficient'])
        return {k:v for k,v in out.items() if v}
    return {r['name']:poly(r['terms']) for r in data['residuals']}


def named_structure(data, value):
    coordinates={c['id']:c['name'] for c in data['coordinates']}
    def convert(x,key=None):
        if key=='monomial':return [coordinates[i] for i in x]
        if isinstance(x,list):return [convert(v) for v in x]
        if isinstance(x,dict):return {k:convert(v,k) for k,v in x.items()}
        return x
    return convert(value)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('before',type=Path)
    ap.add_argument('after',type=Path)
    ap.add_argument('--report',type=Path,required=True)
    args=ap.parse_args()
    before,after=[json.loads(p.read_text()) for p in (args.before,args.after)]
    assert before['fixedParameter']==after['fixedParameter']
    a,b=named(before),named(after)
    deleted={f'detector{i}.{n}.definition' for i in range(3) for n in ['mixA','mixB','mixC','mixD']}
    added={f'detector{i}.{n}.definition' for i in range(3) for n in ['eCubed','eSixth','eTwelfth']}
    changed={f'detector{i}.q12.definition' for i in range(3)}
    assert a.keys()-b.keys()==deleted
    assert b.keys()-a.keys()==added
    assert {k for k in a.keys()&b.keys() if a[k]!=b[k]}==changed
    assert named_structure(before,before['guards'])==named_structure(after,after['guards'])
    av=named_structure(before,before['values'])
    bv=named_structure(after,after['values'])
    assert all(av[k]==bv[k] for k in av.keys()&bv.keys())
    assert len(before['coordinates'])-len(after['coordinates'])==3
    assert len(before['residuals'])-len(after['residuals'])==3
    blocks=[check_block(d,i,new) for i in range(3) for d,new in [(before,False),(after,True)]]
    result={'status':'PASS','reviewer':'/root/independent_math_review',
            'method':'Independent exact polynomial decoding over Q[t,q1,q12], with q12 free; actual normalized rows, zero branches, every outside row and raw cost checked; no author checker imported.',
            'beforeSha256':hashlib.sha256(args.before.read_bytes()).hexdigest(),
            'afterSha256':hashlib.sha256(args.after.read_bytes()).hexdigest(),
            'allOutsideRowsIdentical':True,'allGuardsIdentical':True,
            'allSharedSemanticAliasesIdentical':True,
            'rawCoordinateSaving':3,'rawResidualSaving':3,
            'blocks':blocks,
            'scope':'Finite identities and raw coordinate counts; not global arithmetic proof.'}
    args.report.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
