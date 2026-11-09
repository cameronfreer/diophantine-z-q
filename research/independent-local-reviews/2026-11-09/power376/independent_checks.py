"""Reviewer-owned power, consumer, conic and full-table checks.
Reuses this reviewer's earlier polynomial helpers; no author checker imports.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
ROOT=Path('/tmp/quartic-power376-review');RUN=ROOT/'replay'
REPO=Path('/tmp/codex-glazer389-review-3j08z564/power376')
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def add(*ps):
    result=defaultdict(Q)
    for p in ps:
        for m,c in p.items():result[m]+=c
    return {m:c for m,c in result.items() if c}
def scale(p,c):return {m:a*c for m,a in p.items() if a*c}
def const(c):return {():Q(c)} if c else {}
def var(s):return {(s,):Q(1)}
def mul(p,q):
    result=defaultdict(Q)
    for m,c in p.items():
        for n,d in q.items():result[tuple(sorted(m+n))]+=c*d
    return {m:c for m,c in result.items() if c}
def sub(p,mapping):
    result={}
    for m,c in p.items():
        term=const(c)
        for x in m:term=mul(term,mapping.get(x,var(x)))
        result=add(result,term)
    return result
def derivative(p,x):
    result={}
    for m,c in p.items():
        if x in m:
            n=list(m);n.remove(x);result[tuple(n)]=c*m.count(x)
    return result
def proportional(p,q):
    assert p and q and p.keys()==q.keys()
    pivot=min(q);a=p[pivot]/q[pivot]
    assert a and p==scale(q,a)
    return str(a)
def decode(data):
    names={c['id']:c['name'] for c in data['coordinates']}
    assert len(names)==len(set(names.values()))==len(data['coordinates'])
    def poly(terms):
        result=defaultdict(Q)
        for term in terms:
            result[tuple(sorted([names[i] for i in term['monomial']]+['$S']*term['sPower']))]+=Q(term['coefficient'])
        return {m:c for m,c in result.items() if c}
    rows={r['name']:poly(r['terms']) for r in data['residuals']}
    assert len(rows)==len(data['residuals'])
    return names,poly,rows


old=read(RUN/'baseline/raw-translated-ir.json');new=read(RUN/'raw-translated-ir.json')
assert (RUN/'baseline/raw-translated-ir.json').read_bytes()==Path('/tmp/quartic-row379-review/replay/raw-translated-ir.json').read_bytes()
on,op,O=decode(old);nn,np,N=decode(new)
assert old['fixedParameter']==new['fixedParameter']=={'name':'S','value':'3^2010','coordinate':False}
removed={f'detector{i}.{s}.definition' for i in range(3) for s in ['eCubed','eSixth','eTwelfth']}
added={f'detector{i}.{s}.definition' for i in range(3) for s in ['q1Sixth','q1Twelfth']}
changed={f'detector{i}.q12.definition' for i in range(3)}
assert O.keys()-N.keys()==removed and N.keys()-O.keys()==added
assert {k for k in O.keys()&N.keys() if O[k]!=N[k]}==changed
assert len(on)-len(nn)==len(O)-len(N)==3
assert set(on.values())-set(nn.values())=={x.replace('.definition','.quadratic') for x in removed}
assert set(nn.values())-set(on.values())=={x.replace('.definition','.quadratic') for x in added}
old_values={k:op(v['terms']) for k,v in old['values'].items()}
new_values={k:np(v['terms']) for k,v in new['values'].items()}
assert old_values.keys()-new_values.keys()=={x.removesuffix('.definition') for x in removed}
assert new_values.keys()-old_values.keys()=={x.removesuffix('.definition') for x in added}
assert all(old_values[k]==new_values[k] for k in old_values.keys()&new_values.keys())
def guards(data,p):return {g['name']:(p(g['expression']),p(g['inverse'])) for g in data['guards']}
assert guards(old,op)==guards(new,np)

# Verify every actual named chain residual after decoding its affine aliases
# to monomials in one free indeterminate u=q1; all exponents are exact.
chain=[('q1SquaredForWeights',2),('q1CubedForWeights',3),('q1Sixth',6),('q1Twelfth',12),('q12',23),('mixedHigh',46),('q46',91),('E46.power2',182),('E46.power3',273)]
blocks=[]
for i in range(3):
    prefix=f'detector{i}.';mapping={}
    def identify(name,power):
        alias=new_values[prefix+name]
        unknown=[m for m in alias if len(m)==1 and m[0] not in mapping]
        assert len(unknown)==1 and all(len(m)<=1 for m in alias)
        m=unknown[0];c=alias[m]
        known={a:b for a,b in alias.items() if a!=m}
        mapping[m[0]]=scale(add({('$u',)*power:Q(1)},scale(sub(known,mapping),-1)),1/c)
        assert sub(alias,mapping)=={('$u',)*power:Q(1)}
    identify('q1',1)
    for name,power in chain:
        identify(name,power)
        assert not sub(N[prefix+name+'.definition'],mapping),name
    blocks.append({'detector':i,'powers':{name:p for name,p in chain},'actualRowsZeroIdentitiesOverQ[u]':True})
    # The q12 and q46 quotient rows are constrained by the same positive q1.
    for name in ['q12','q46']:
        row=next(r for r in new['residuals'] if r['name']==prefix+name+'.definition')
        gate=next(g for g in new['gates'] if g['definitionResidualId']==row['id'])
        assert gate['operation']=='rational_quotient' and np(gate['denominator'])==new_values[prefix+'q1']
    # Exact physical norm/trace equation, including its factor of two.
    val=lambda name:new_values[prefix+name]
    w0,w1,n,E,B=[val(name) for name in ['W.0','W.1','normOver2w0','eDelta','Bsemantic']]
    proportional(N[prefix+'normOver2w0.definition'],add(scale(mul(w0,n),2),scale(mul(w0,w0),-1),scale(mul(w1,w1),2)))
    proportional(N[prefix+'B.definition'],add(mul(E,B),scale(mul(n,n),-1)))
    # The order12 pair is genuinely (1+q12*D1^2)(1+q12*D10^2).
    # Its mixedHigh=q12^2 row and both test aliases are retained; the complete
    # unchanged product recursion is inspected in the source, not sampled.

orders=[46,12,1,1,1,1,1,1,1,1,12,46,46,46,46,46]
assert [orders.count(x) for x in [1,12,46]]==[8,2,6]
for i in range(16):
    for j in range(2):assert old_values[f'test{i}.{j}']==new_values[f'test{i}.{j}']
source=(RUN/'builder.cjs').read_text()
assert 'i===0?46:i===1?12:1' in source and 'order:i===1?12:46' in source
assert 'value:fsub(L[1],[beta,zero]),order:46' in source and 'value:FF,order:46' in source
# Full G12 coefficient recurrence and exceptional first-tail denominator.
a=Q(-2,5)
for j in range(2,14):a*=Q(4*j-5,4*j+1)
assert a==Q(-54756974,6936596275)
assert a.denominator==5**2*7*17*29*37*41*53
assert 4*14-(4*14+1)//10==51 and 4*14-(4*14+1)//52==55
# The general tail proof uses a floor increment at most1, hence increment>=3;
# this finite residue check confirms that step uniformly modulo10.
assert all(((4*j+5)//10-(4*j+1)//10)<=1 for j in range(10))
normalizations=[]
for m in [1,12,46]:
    j=2*m-1
    assert (2*m-1,2*m-1-2*j)==(j,-j)
    # v(e)=5s;v(delta)=s-nu gives j*nu+4j*s.
    assert (j,-j)==(2*m-1,1-2*m)
    normalizations.append({'order':m,'deltaDenominatorInLemmaInput':j,'nuAndS':[j,4*j],'realDecayPower':-j})
roots=[Q(0),Q(1,49),Q(1,50),Q(1,2450),Q(32,1225)]
deltas=[98*x-1 for x in roots]
assert deltas==[Q(-1),Q(1),Q(24,25),Q(-24,25),Q(39,25)]
for x in deltas:
    for n in [abs(x.numerator),x.denominator]:
        for p in [2,3,5,7,13,17]:
            while n%p==0:n//=p
        assert n==1
H=3*2**106*(2**32*3**9)**6*46410**18+128;c=2*3**1004;b=c-1
assert 8**992*c**415>(25*H)**992
assert (2*(b*b-6))**1472>(3*H+14)**1472*(2*b**4+6*b**3+5*b*b+1)**577
assert 64*46-2308==636 and 40*H<2**670 and b>67000
assert Q(384,19100)+Q(577,191)*Q(8,25)==Q(4712,4775)
assert Q(577,191)*Q(8,25)==Q(4616,4775)
assert 298-Q(4712,4775)*301-Q(4616,4775)==Q(22,4775)

# Reapply all four conic maps to the actual compiled rows, deriving H from a
# polynomial derivative, and check every exterior row and private consumer.
pre=read(RUN/'candidate-ir.json');post=read(RUN/'final/integer-candidate-ir.json')
pn,pp,P=decode(pre);qn,qp,Qrows=decode(post);conics=[];touched=set()
for prefix in ['detector0','detector1','detector2','scalar']:
    sname,qname,hname,s2name,q2name=[prefix+x for x in ['.s','.q','.Bh.quadratic','.s2.quadratic','.q2.quadratic']]
    vname=prefix+'.factored_v';s,q,h,s2,q2,v=[var(x) for x in [sname,qname,hname,s2name,q2name,vname]]
    p=P[prefix+'.secondConic']
    H=scale(sub(derivative(p,s2name),{s2name:{}}),Q(-1,2))
    b=scale(derivative(p,q2name),Q(1,17))
    expected=add(scale(mul(b,q2),17),scale(mul(H,H),3),scale(mul(s2,H),-2),scale(mul(s2,s2),-1))
    assert p==expected
    alpha=H[(hname,)];rest=add(H,scale(h,-alpha));assert alpha
    lift={hname:scale(add(mul(s,v),scale(rest,-1)),1/alpha),qname:mul(s,q),q2name:mul(mul(s,s),q2),s2name:mul(s,s)}
    expected_names={prefix+x for x in ['.Bh.definition','.s2.definition','.q2.definition','.secondConic']}
    consumers={name for name,p0 in P.items() if any(set(m)&{hname,qname,s2name,q2name} for m in p0)}
    assert consumers==expected_names
    assert not sub(P[prefix+'.s2.definition'],lift)
    ratios={}
    for suffix in ['.Bh.definition','.q2.definition','.secondConic']:
        target=Qrows[prefix+suffix]
        if suffix!='.Bh.definition':target=mul(mul(s,s),target)
        ratios[suffix]=proportional(sub(P[prefix+suffix],lift),target)
    zero=sub(p,{s2name:{},q2name:mul(q,q)})
    assert zero==add(scale(mul(b,mul(q,q)),17),scale(mul(H,H),3))
    assert not sub(Qrows[prefix+'.secondConic'],{sname:{},vname:{},q2name:{}})
    touched|=expected_names
    conics.append({'prefix':prefix,'actualH':{'*'.join(m) or '1':str(c) for m,c in H.items()},'liftRowFactors':ratios,'allPrivateConsumersChecked':True,'zeroBranch':'17*b*q^2+3*H^2=0 with b>0; choose v=Q=Q2=0'})
assert all(P[name]==Qrows[name] for name in P.keys()-touched)
assert P.keys()-Qrows.keys()=={x+'.s2.definition' for x in ['detector0','detector1','detector2','scalar']}

# Derive the fixed diagonal factors directly from the supplied weights, check
# every target row by a nonzero coefficient ratio and integer primitivity,
# then expand all squared rows without importing the producer/checker.
weights=read(REPO/'research/odd-power-detectors/DIAGONAL_WEIGHTS.json')
parent_weights=read(REPO/'research/scalar-row-reduction/DIAGONAL_WEIGHTS.json')
assert weights.keys()==parent_weights.keys()
assert {k for k in weights if weights[k]!=parent_weights[k]}=={'H.chart.j0'}
assert parent_weights['H.chart.j0'][0]==0 and weights['H.chart.j0'][0]==1
assert parent_weights['H.chart.j0'][1]==weights['H.chart.j0'][1]
ir=read(RUN/'balanced/integer-ir.json');table=read(RUN/'balanced/polynomial.json')
assert len(weights)==35 and all(len(v)==2 and all(type(i)==int for i in v) for v in weights.values())
assert len(post['coordinates'])==len(table['coordinates'])==376 and len(post['residuals'])==345
assert weights.keys()<=set(qn.values()) and 'input' not in weights
factors={i:Q(3)**weights.get(name,[0,0])[0]*Q(2)**weights.get(name,[0,0])[1] for i,name in qn.items()}
assert factors[0]==1 and all(factors.values())
ids=sorted(qn);compact={i:j for j,i in enumerate(ids)}
assert table['coordinates']==[{'id':compact[i],'sourceId':i,'name':qn[i],'oldCoordinateEqualsTwoPowerTimesThreePowerTimesNew':True,'twoPower':weights.get(qn[i],[0,0])[1],'threePower':weights.get(qn[i],[0,0])[0]} for i in ids]
old_by_id={r['id']:r for r in post['residuals']};divisors=[];expanded=defaultdict(int)
for row in ir['residuals']:
    oldrow=old_by_id[row['id']];assert row['name']==oldrow['name']
    p=defaultdict(Q)
    for t in oldrow['terms']:
        assert len(t['monomial'])<=2
        c=Q(t['coefficient'])*3**(2010*t['sPower'])
        for i in t['monomial']:c*=factors[i]
        p[tuple(t['monomial'])]+=c
    p={m:c for m,c in p.items() if c}
    actual={tuple(t['monomial']):int(t['coefficient']) for t in row['terms']}
    assert all(t['sPower']==0 for t in row['terms']) and len(actual)==len(row['terms'])
    ratio=Q(p[min(p)],actual[min(p)])
    assert ratio and p==scale(actual,ratio) and math.gcd(*actual.values())==1 and actual[min(actual)]>0
    divisors.append(str(ratio))
    terms=[(tuple(compact[i] for i in m),c) for m,c in actual.items()]
    for i,(m,c) in enumerate(terms):
        expanded[tuple(sorted(m+m))]+=c*c
        for n,d in terms[i+1:]:expanded[tuple(sorted(m+n))]+=2*c*d
expanded={m:c for m,c in expanded.items() if c}
assert expanded=={tuple(t['monomial']):int(t['coefficient']) for t in table['terms']}
assert len(expanded)==len(table['terms'])==25964 and max(map(len,expanded))==4
assert {i for m in expanded for i in m}==set(range(376))
assert math.gcd(*expanded.values())==1 and expanded[(0,0,0,0)]==1
maximum=max(map(abs,expanded.values()));assert len(str(maximum))==425 and maximum.bit_length()==1410
textpath=RUN/'quartic-376-balanced-decimal.txt';parsed={}
for line in textpath.read_text().splitlines():
    if line.startswith('#'):continue
    coefficient,word=line.split('\t');monomial=[]
    if word!='1':
        for factor in word.split('*'):
            parts=factor.split('^');monomial.extend([int(parts[0][1:])]*(int(parts[1]) if len(parts)==2 else 1))
    assert tuple(monomial) not in parsed
    parsed[tuple(monomial)]=int(coefficient)
assert parsed==expanded

report={'status':'PASS','reviewer':'/root/independent_math_review','date':'2026-11-09','noAuthorCheckerImports':True,
        'baselineMatchesEarlierIndependentRow379Replay':True,'removedRows':sorted(removed),'addedRows':sorted(added),'changedRows':sorted(changed),
        'unchangedCommonRows':len(O.keys()&N.keys())-len(changed),'rawCoordinateAndRowSaving':3,
        'commonFormalAliasesAndGuardsIdentical':True,'identityCaveat':'Changed q12/q46 values change evaluated W, trace and pole input; only R and underlying tests are fixed.',
        'actualChains':blocks,'actualOrderList':orders,'actualPoleInput':'R/Tr(W^-1)^2','normalizations':normalizations,
        'precision':{'a13':str(a),'uniformRelativeBound':51,'uniform52NotUsed':True},
        'height':{'anchorExponent':2010,'scalarOrder':31,'highOrder':46,'inputOrder':12,'uniformLucasRatioExponent':636,'inputGapAt301':'22/4775'},
        'fourConics':conics,'all345DiagonalRowIdentitiesChecked':True,'weights':{'specified':35,'ternary':sum(bool(x[0]) for x in weights.values()),'dyadic':sum(bool(x[1]) for x in weights.values()),'inputFixed':True},
        'coordinates':376,'residuals':345,'monomials':25964,'degree':4,'content':1,'allCoordinatesActive':True,'inputFourthPowerCoefficient':1,
        'completeExpansionAndTextCompared':True,'maximumAbsoluteCoefficient':str(maximum),'maximumDigits':425,'maximumBits':1410,
        'tableSha256':digest(textpath),'rawSha256':digest(RUN/'raw-translated-ir.json'),
        'scope':'Finite exact identities and measurements supporting separately reviewed uniform arithmetic applications; no global theorem acceptance.'}
(ROOT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
