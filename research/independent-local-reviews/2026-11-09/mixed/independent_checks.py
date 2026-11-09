"""Reviewer-owned exact checks, with no author checker imports."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import re

ROOT=Path('/tmp/quartic-mixed-review')
RUN=ROOT/'replay'
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
before=json.loads((RUN/'baseline/raw-translated-ir.json').read_text())
after=json.loads((RUN/'raw-translated-ir.json').read_text())
assert (RUN/'baseline/raw-translated-ir.json').read_bytes()==Path('/tmp/quartic-height-review/order45/raw-translated-ir.json').read_bytes()
def canonical(x):
    if isinstance(x,str):
        return x.replace('.q46','.q45').replace('.E46','.E45').replace('symmetric.46.','symmetric.45.').replace('testSquare.46.','testSquare.45.')
    if isinstance(x,list):return [canonical(y) for y in x]
    if isinstance(x,dict):return {canonical(k):canonical(v) for k,v in x.items()}
    return x
canon=canonical(after)
assert before.keys()==canon.keys()
assert all(before[k]==canon[k] for k in before.keys()-{'fixedParameter','variant','residuals','gates'})
assert before['fixedParameter']['value']=='3^2118' and after['fixedParameter']['value']=='3^2010'
oldrows={x['name']:x for x in before['residuals']}
newrows={x['name']:x for x in canon['residuals']}
changed={f'detector{i}.q45.definition' for i in range(3)}
assert oldrows.keys()==newrows.keys()
assert {k for k in oldrows if oldrows[k]!=newrows[k]}==changed
changed_ids={newrows[k]['id'] for k in changed}
assert len(before['gates'])==len(canon['gates'])
assert {b['definitionResidualId'] for a,b in zip(before['gates'],canon['gates']) if a!=b}==changed_ids

# Decode actual affine aliases and defining rows in Q[t,u,z], where u=q1
# and z is the free final weight. Positivity, separately proved, allows division.
ONE={(0,0,0):Q(1)};T={(1,0,0):Q(1)};U={(0,1,0):Q(1)};Z={(0,0,1):Q(1)}
def add(*ps):
    out=defaultdict(Q)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return {m:c for m,c in out.items() if c}
def scale(p,c):return {m:a*c for m,a in p.items() if a*c}
def mul(p,q):
    out=defaultdict(Q)
    for m,c in p.items():
        for n,d in q.items():out[tuple(a+b for a,b in zip(m,n))]+=c*d
    return {m:c for m,c in out.items() if c}
def power(p,n):
    out=ONE
    for _ in range(n):out=mul(out,p)
    return out
roots=[Q(0),Q(1,49),Q(1,50),Q(1,2450),Q(32,1225)]
cs=[Q(1)]
for root in roots:
    nxt=[Q(0)]*(len(cs)+1)
    for i,c in enumerate(cs):nxt[i]-=root*c;nxt[i+1]+=c
    cs=nxt
delta=add(scale(T,98),scale(ONE,-1));e=mul(U,delta)
def block(data,i,order):
    prefix=f'detector{i}.';mapping={}
    values={k[len(prefix):]:v['terms'] for k,v in data['values'].items() if k.startswith(prefix)}
    rows={r['name']:r['terms'] for r in data['residuals']}
    def decode(terms):
        out={}
        for term in terms:
            assert term['sPower']==0
            p=scale(ONE,Q(term['coefficient']))
            for ident in term['monomial']:p=mul(p,mapping[ident])
            out=add(out,p)
        return out
    def identify(name,target):
        terms=values[name]
        assert all(len(t['monomial'])<=1 for t in terms)
        unknown=[t for t in terms if t['monomial'] and t['monomial'][0] not in mapping]
        assert len(unknown)==1,(name,unknown)
        term=unknown[0]
        mapping[term['monomial'][0]]=scale(add(target,scale(decode([t for t in terms if t is not term]),-1)),1/Q(term['coefficient']))
        assert decode(terms)==target
    targets=[('t',T),('Fsquare',power(T,2)),
             ('Fmiddle',add(power(T,3),scale(power(T,2),cs[4]),scale(T,cs[3]),scale(ONE,cs[2]))),
             ('q1',U),('eDelta',mul(U,power(delta,2))),
             ('q1SquaredForWeights',power(U,2)),('q1CubedForWeights',power(U,3)),
             ('eCubed',power(e,3)),('eSixth',power(e,6)),('eTwelfth',power(e,12)),
             ('q12',mul(power(U,23),power(delta,22))),
             ('mixedHigh',mul(power(U,46),power(delta,44))),('q'+str(order),Z)]
    for name,target in targets:identify(name,target)
    assert decode(values['delta2'])==power(delta,2)
    assert decode(values['deltaCubed'])==power(delta,3)
    for name,_ in targets:
        if name not in ['t','q1','q'+str(order)]:assert not decode(rows[prefix+name+'.definition']),name
    actual=decode(rows[prefix+'q'+str(order)+'.definition'])
    expected=add(mul(power(U,3 if order==45 else 1),Z),scale(mul(power(U,92),power(delta,88)),-1))
    pivot=min(expected);ratio=actual[pivot]/expected[pivot]
    assert ratio and actual==scale(expected,ratio)
    return {'detector':i,'order':order,'exactConstraint':'q1^3*q45=q1^92*delta^88' if order==45 else 'q1*q46=q1^92*delta^88'}
blocks=[block(data,i,order) for i in range(3) for data,order in [(before,45),(after,46)]]

# Literal n=N(W)/(2W0) and E*B=n^2 are independently compared as raw polynomials.
def rawpoly(terms):
    out=defaultdict(Q)
    for t in terms:
        assert t['sPower']==0
        out[tuple(sorted(t['monomial']))]+=Q(t['coefficient'])
    return {m:c for m,c in out.items() if c}
def rawmul(p,q):
    out=defaultdict(Q)
    for m,c in p.items():
        for n,d in q.items():out[tuple(sorted(m+n))]+=c*d
    return {m:c for m,c in out.items() if c}
def same_up_to_nonzero(a,b):
    assert a.keys()==b.keys()
    pivot=min(b);ratio=a[pivot]/b[pivot]
    assert ratio and a==scale(b,ratio)
rows={r['name']:r['terms'] for r in after['residuals']}
for i in range(3):
    p=f'detector{i}.'
    v=lambda n:rawpoly(after['values'][p+n]['terms'])
    w0,w1,n,E,B=[v(n) for n in ['W.0','W.1','normOver2w0','eDelta','Bsemantic']]
    same_up_to_nonzero(rawpoly(rows[p+'normOver2w0.definition']),
                      add(scale(rawmul(w0,n),2),scale(rawmul(w0,w0),-1),scale(rawmul(w1,w1),2)))
    same_up_to_nonzero(rawpoly(rows[p+'B.definition']),add(rawmul(E,B),scale(rawmul(n,n),-1)))

orders=[46,12,1,1,1,1,1,1,1,1,12,46,46,46,46,46]
assert [orders.count(i) for i in [1,12,46]]==[8,2,6]
for index in range(16):
    for component in range(2):assert before['values'][f'test{index}.{component}']==after['values'][f'test{index}.{component}']
source=(RUN/'builder.cjs').read_text()
assert 'i===0?46:i===1?12:1' in source and 'order:i===1?12:46' in source
assert 'value:fsub(L[1],[beta,zero]),order:46' in source and 'value:FF,order:46' in source

# Local normalized powers and finite-prime slopes. This finite algebra is
# evidence for, not a replacement for, the common-place/completeness proofs.
weights=[]
for m,j,e_power,d_power in [(1,1,1,-1),(12,12,23,-1),(46,47,91,-3)]:
    assert (2*m-1,2*m-1-2*j)==(e_power,d_power)
    slope,constant=-d_power,5*e_power+d_power
    weights.append({'order':m,'deltaDenominatorInLemmaInput':j,'weightPowers':[e_power,d_power],'smallPrimeNuAndS':[slope,constant]})
assert [x['smallPrimeNuAndS'] for x in weights]==[[1,4],[1,114],[3,452]]
assert [98*t-1 for t in roots]==[Q(-1),Q(1),Q(24,25),Q(-24,25),Q(39,25)]
def prime_support(n):
    out=set();n=abs(n);p=2
    while p*p<=n:
        while n%p==0:out.add(p);n//=p
        p+=1
    if n>1:out.add(n)
    return out
for d in [98*t-1 for t in roots]:assert prime_support(d.numerator)|prime_support(d.denominator)<={2,3,5,7,13,17}

H=3*2**106*(2**32*3**9)**6*46410**18+128
c=2*3**1004;b=c-1;P=2*b**4+6*b**3+5*b**2+1
scalar_left=8**992*c**415;scalar_right=(25*H)**992
lucas_left=(2*(b*b-6))**1472;lucas_right=(3*H+14)**1472*P**577
assert scalar_left>scalar_right and lucas_left>lucas_right
assert 64*46-2308==636 and 40*H<2**670 and b>67000
assert Q(384,19100)+Q(577,191)*Q(8,25)==Q(4712,4775)
assert Q(577,191)*Q(8,25)==Q(4616,4775)
assert 301-3-(Q(4712,4775)*301+Q(4616,4775))==Q(22,4775)

# Check every diagonal substitution and nonzero row factor directly.
original=json.loads((RUN/'final/integer-candidate-ir.json').read_text())
ir=json.loads((RUN/'balanced/integer-ir.json').read_text())
table=json.loads((RUN/'balanced/polynomial.json').read_text())
cert=json.loads((RUN/'balanced/diagonal-certificate.json').read_text())
mapping={c['sourceId']:c['id'] for c in table['coordinates']}
assert len(mapping)==380 and len(ir['residuals'])==349
scale_by_id={c['sourceId']:Q(2)**c['twoPower']*Q(3)**c['threePower'] for c in table['coordinates']}
assert scale_by_id[0]==1
divisors={r['id']:Q(int(r['divisorNumerator']),int(r['divisorDenominator'])) for r in cert['rows']}
old={r['id']:r for r in original['residuals']}
for row in ir['residuals']:
    assert divisors[row['id']]
    expected=defaultdict(Q)
    for t in old[row['id']]['terms']:
        coeff=Q(t['coefficient'])*3**(2010*t['sPower'])/divisors[row['id']]
        for ident in t['monomial']:coeff*=scale_by_id[ident]
        expected[tuple(sorted(t['monomial']))]+=coeff
    assert rawpoly(row['terms'])=={m:c for m,c in expected.items() if c}
expanded=defaultdict(int)
for row in ir['residuals']:
    terms=[]
    for t in row['terms']:
        assert t['sPower']==0 and len(t['monomial'])<=2
        terms.append((tuple(sorted(mapping[i] for i in t['monomial'])),int(t['coefficient'])))
    for i,(m,c0) in enumerate(terms):
        expanded[tuple(sorted(m+m))]+=c0*c0
        for n,d in terms[i+1:]:expanded[tuple(sorted(m+n))]+=2*c0*d
expanded={m:c for m,c in expanded.items() if c}
assert expanded=={tuple(t['monomial']):int(t['coefficient']) for t in table['terms']}
assert len(expanded)==26025 and max(map(len,expanded))==4
assert {i for m in expanded for i in m}==set(mapping.values())
assert math.gcd(*expanded.values())==1 and expanded[(0,0,0,0)]==1
maximum=max(map(abs,expanded.values()));assert maximum==28902*3**1340
path=RUN/'quartic-380-balanced-decimal.txt';parsed={}
for line in path.read_text().splitlines():
    if line.startswith('#'):continue
    coefficient,word=line.split('\t');monomial=[]
    if word!='1':
        for f in word.split('*'):
            pieces=f.split('^');monomial.extend([int(pieces[0][1:])]*(int(pieces[1]) if len(pieces)==2 else 1))
    assert tuple(monomial) not in parsed
    parsed[tuple(monomial)]=int(coefficient)
assert parsed==expanded
report={'status':'PASS','reviewer':'/root/independent_math_review','date':'2026-11-09',
        'noAuthorCheckerImports':True,'baselineMatchesEarlierIndependentHeightReplay':True,
        'outsideRowsGuardsAndAliasesUnchangedAfterExplicitOrderRename':True,
        'identityCaveat':'Formal coordinate expressions are unchanged; the changed weight changes evaluated W, trace and pole input. No witness projection equivalence is asserted.',
        'changedRawRows':sorted(changed),'weightBlocks':blocks,'actualPoleInput':'R/Tr(W^-1)^2',
        'actualOrderList':orders,'normalizationsAndLocalSlopes':weights,
        'height':{'order':46,'anchorExponent':2010,'HBits':H.bit_length(),'uniformRatioExponent':636,
                  'scalarBitLengths':[scalar_left.bit_length(),scalar_right.bit_length()],
                  'lucasBitLengths':[lucas_left.bit_length(),lucas_right.bit_length()],
                  'inputGapAt301':'22/4775'},
        'allDiagonalRowsChecked':True,'coordinates':380,'residuals':349,'monomials':26025,
        'degree':4,'content':1,'inputFixed':True,'inputFourthCoefficient':1,'allCoordinatesActive':True,
        'maximum':'28902*3^1340','maximumDigits':len(str(maximum)),'maximumBits':maximum.bit_length(),
        'tableSha256':digest(path),'rawSha256':digest(RUN/'raw-translated-ir.json'),
        'scope':'Finite identities, coefficient expansion and endpoint certificates supporting the independently read uniform arguments, not a global arithmetic proof.'}
(ROOT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
