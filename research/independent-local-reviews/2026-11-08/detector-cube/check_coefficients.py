"""Expand every squared primitive row independently, including cross terms."""
from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import math

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--output-root',type=Path,default=Path('/tmp/quartic-cube-review'))
ap.add_argument('--prior-zero',type=Path,default=Path('/tmp/quartic-independent-review/preparation-zero/replay/candidate/raw-translated-ir.json'))
ap.add_argument('--prior47',type=Path,default=Path('/tmp/quartic-independent-review/higher-precision/order47/raw-translated-ir.json'))
args=ap.parse_args()
OUT=args.output_root
results=[]
for order, count, rows, monomials, exponent in [(45,380,349,26025,2130),(47,383,352,26043,2016)]:
    root=OUT/f'order{order}'
    source=json.loads((root/'balanced/integer-ir.json').read_text())
    table=json.loads((root/'balanced/polynomial.json').read_text())
    ids={c['sourceId']:c['id'] for c in table['coordinates']}
    assert len(ids)==count and len(source['residuals'])==rows
    assert table['coordinates'][0]['name']=='input'
    assert table['coordinates'][0]['twoPower']==table['coordinates'][0]['threePower']==0
    result=defaultdict(int)
    for row in source['residuals']:
        terms=[]
        for term in row['terms']:
            assert term['sPower']==0 and len(term['monomial'])<=2
            terms.append((tuple(sorted(ids[i] for i in term['monomial'])),int(term['coefficient'])))
        for i,(m,c) in enumerate(terms):
            result[tuple(sorted(m+m))]+=c*c
            for n,d in terms[i+1:]:
                result[tuple(sorted(m+n))]+=2*c*d
    result={m:c for m,c in result.items() if c}
    assert result=={tuple(t['monomial']):int(t['coefficient']) for t in table['terms']}
    assert all(t['sPower']==0 for t in table['terms'])
    assert len(result)==monomials and max(map(len,result))==4
    assert set(ids.values())=={i for m in result for i in m}
    assert math.gcd(*result.values())==1 and result[(0,0,0,0)]==1
    maximum=max(map(abs,result.values()))
    assert maximum==28902*3**(2*exponent//3)
    text_path=root/f'quartic-{count}-balanced-decimal.txt'
    parsed={}
    for line in text_path.read_text().splitlines():
        if line.startswith('#'):continue
        coefficient,word=line.split('\t')
        m=[]
        if word!='1':
            for factor in word.split('*'):
                parts=factor.split('^')
                m.extend([int(parts[0][1:])]*(int(parts[1]) if len(parts)==2 else 1))
        assert tuple(m) not in parsed
        parsed[tuple(m)]=int(coefficient)
    assert parsed==result
    before=(root/'baseline/raw-translated-ir.json').read_bytes()
    after=(root/'raw-translated-ir.json').read_bytes()
    prior=args.prior_zero if order==45 else args.prior47
    assert before==prior.read_bytes()
    results.append({'order':order,'coordinates':count,'residuals':rows,'monomials':monomials,
                    'degree':4,'integerContent':1,'inputFourthPowerCoefficient':1,
                    'everyCoordinateActive':True,'inputFixed':True,
                    'maximumCoefficient':f'28902*3^{2*exponent//3}',
                    'maximumDigits':len(str(maximum)),'maximumBits':maximum.bit_length(),
                    'tableSha256':hashlib.sha256(text_path.read_bytes()).hexdigest(),
                    'baselineRawSha256':hashlib.sha256(before).hexdigest(),
                    'candidateRawSha256':hashlib.sha256(after).hexdigest(),
                    'baselineEqualsPreviouslyReviewedRawSource':True})
report={'status':'PASS','reviewer':'/root/independent_math_review',
        'method':'Independent triangular square expansion over integers, exact full decimal-table parse and complete coefficient equality; no author checker imported.',
        'results':results,'scope':'Finite full expansion/count/height verification, not global arithmetic proof.'}
(OUT/'COEFFICIENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
