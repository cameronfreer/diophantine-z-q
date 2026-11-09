"""Independent height endpoints, source consumers and full coefficient expansion."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import math

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--root',type=Path,default=Path('/tmp/quartic-height-review'))
ap.add_argument('--prior-root',type=Path,default=Path('/tmp/quartic-cube-review'))
args=ap.parse_args()
H=3*2**106*(2**32*3**9)**6*46410**18+128
alpha=Q(577,32)
assert 1-alpha/31==Q(415,992)
assert 12/(24-alpha)==Q(384,191)
assert alpha/(24-alpha)==Q(577,191)
assert Q(384,19100)+Q(577,191)*Q(8,25)==Q(4712,4775)
assert Q(577,191)*Q(8,25)==Q(4616,4775)
assert 301-3-(Q(4712,4775)*301+Q(4616,4775))==Q(22,4775)
assert Q(4712,4775)<1
assert 3*H+14<14*H
assert 40*H<2**670
# (2sqrt(2)-1)(2sqrt(2)+1)=7; both factors exceed 1.
assert 4*2-1==7
results=[]
for order,E,count,row_count,monomials in [(45,2118,380,349,26025),(47,2010,383,352,26043)]:
    root=args.root/f'order{order}'
    oldE=2130 if order==45 else 2016
    scalar_n,scalar_d=(4,1) if order==45 else (25,8)
    endpoints=[]
    for exponent in [E,E-6]:
        c=2*3**(exponent//2-1); b=c-1
        P=2*b**4+6*b**3+5*b**2+1
        scalar_left=scalar_d**992*c**415
        scalar_right=(scalar_n*H)**992
        lucas_left=(2*(b*b-6))**(32*order)
        lucas_right=(3*H+14)**(32*order)*P**577
        endpoints.append({'exponent':exponent,'scalar':scalar_left>scalar_right,
                          'lucas':lucas_left>lucas_right,
                          'scalarComparisonBitLengths':[scalar_left.bit_length(),scalar_right.bit_length()],
                          'lucasComparisonBitLengths':[lucas_left.bit_length(),lucas_right.bit_length()]})
        assert b>67000 and b>=301 and b*b>6
    assert endpoints[0]['scalar'] and endpoints[0]['lucas']
    assert not endpoints[1]['lucas' if order==45 else 'scalar']
    assert 64*order-4*577>0
    oldbytes=(root/'baseline/raw-translated-ir.json').read_bytes()
    assert oldbytes==(args.prior_root/f'order{order}/raw-translated-ir.json').read_bytes()
    before=json.loads(oldbytes)
    after=json.loads((root/'raw-translated-ir.json').read_text())
    assert before['fixedParameter']=={'name':'S','value':f'3^{oldE}','coordinate':False}
    assert after['fixedParameter']=={'name':'S','value':f'3^{E}','coordinate':False}
    assert before.keys()==after.keys()
    assert all(before[k]==after[k] for k in before.keys()-{'fixedParameter','variant'})
    names={c['name']:c['id'] for c in after['coordinates']}
    assert len(names)==len(after['coordinates'])
    uses={}
    for name in ['anchor.U','anchor.V','anchor.W','anchor.physicalA.quadratic']:
        ident=names[name]
        uses[name]=[r['name'] for r in after['residuals']
                    if any(ident in t['monomial'] for t in r['terms'])]
        assert set(uses[name])==({'anchor.translatedEquation','anchor.physicalA.definition'}
                               if name=='anchor.physicalA.quadratic' else {'anchor.translatedEquation'})
    parameter_rows=[r['name'] for r in after['residuals'] if any(t['sPower'] for t in r['terms'])]
    assert set(parameter_rows)=={'anchor.translatedEquation','anchor.physicalA.definition'}
    ir=json.loads((root/'balanced/integer-ir.json').read_text())
    table=json.loads((root/'balanced/polynomial.json').read_text())
    mapping={c['sourceId']:c['id'] for c in table['coordinates']}
    assert len(mapping)==count and len(ir['residuals'])==row_count
    assert table['coordinates'][0]['name']=='input'
    assert table['coordinates'][0]['twoPower']==table['coordinates'][0]['threePower']==0
    expanded=defaultdict(int)
    for row in ir['residuals']:
        terms=[]
        for term in row['terms']:
            assert term['sPower']==0 and len(term['monomial'])<=2
            terms.append((tuple(sorted(mapping[i] for i in term['monomial'])),int(term['coefficient'])))
        for i,(m,c) in enumerate(terms):
            expanded[tuple(sorted(m+m))]+=c*c
            for n,d in terms[i+1:]:expanded[tuple(sorted(m+n))]+=2*c*d
    expanded={m:c for m,c in expanded.items() if c}
    assert expanded=={tuple(t['monomial']):int(t['coefficient']) for t in table['terms']}
    assert len(expanded)==monomials and max(map(len,expanded))==4
    assert {i for m in expanded for i in m}==set(mapping.values())
    assert math.gcd(*expanded.values())==1 and expanded[(0,0,0,0)]==1
    maximum=max(map(abs,expanded.values()))
    assert maximum==28902*3**(2*E//3)
    path=root/f'quartic-{count}-balanced-decimal.txt'
    parsed={}
    for line in path.read_text().splitlines():
        if line.startswith('#'):continue
        coefficient,word=line.split('\t'); monomial=[]
        if word!='1':
            for factor in word.split('*'):
                parts=factor.split('^')
                monomial.extend([int(parts[0][1:])]*(int(parts[1]) if len(parts)==2 else 1))
        assert tuple(monomial) not in parsed
        parsed[tuple(monomial)]=int(coefficient)
    assert parsed==expanded
    results.append({'order':order,'anchorExponent':E,'endpoints':endpoints,
                    'uniformRatioPositiveExponent':64*order-2308,
                    'allSymbolicSourceSectionsUnchangedExceptFixedParameterAndVariant':True,
                    'baselineMatchesEarlierIndependentCubeReplay':True,
                    'privateAnchorConsumers':uses,'onlyParameterDependentRows':parameter_rows,
                    'coordinates':count,'residuals':row_count,'monomials':monomials,
                    'degree':4,'integerContent':1,'inputFourthPowerCoefficient':1,
                    'allCoordinatesActive':True,'inputFixed':True,
                    'maximumCoefficient':f'28902*3^{2*E//3}',
                    'maximumDigits':len(str(maximum)),'maximumBits':maximum.bit_length(),
                    'tableSha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'baselineRawSha256':hashlib.sha256(oldbytes).hexdigest(),
                    'candidateRawSha256':hashlib.sha256((root/'raw-translated-ir.json').read_bytes()).hexdigest()})
report={'status':'PASS','reviewer':'/root/independent_math_review','date':'2026-11-09',
        'method':'Independent exact integer/rational endpoints and input constants; actual private-anchor consumers; complete symbolic-source identity; triangular row-square expansion and full decimal-table parsing. No author checker imported.',
        'heightConstantBits':H.bit_length(),'inputThresholdGapAt301':'22/4775',
        'results':results,'scope':'Finite certificates supporting the separately reviewed uniform argument, not a global arithmetic proof.'}
(args.root/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
