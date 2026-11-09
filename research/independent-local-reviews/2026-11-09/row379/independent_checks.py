"""Reviewer-owned exact algebra, conic and coefficient checks. Standard library only."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math

ROOT=Path('/tmp/quartic-row379-review');RUN=ROOT/'replay'
REPO=Path('/tmp/codex-glazer389-review-3j08z564/row379')
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
assert (RUN/'baseline/raw-translated-ir.json').read_bytes()==Path('/tmp/quartic-mixed-review/replay/raw-translated-ir.json').read_bytes()
on,op,O=decode(old);nn,np,N=decode(new)
assert old['fixedParameter']==new['fixedParameter']=={'name':'S','value':'3^2010','coordinate':False}
changed={name for name in O.keys()&N.keys() if O[name]!=N[name]}
assert changed=={'scalar.shiftedS.rootTimesInverseRoot.definition.0','scalar.shiftedS.rootTimesInverseRoot.definition.1','scalar.preparationT.definition','scalar.Bh.definition','scalar.secondConic'}
assert O.keys()-N.keys()=={'scalar.W2.definition'} and not N.keys()-O.keys()
assert len(O.keys()&N.keys())-len(changed)==358

# Solve for the two row-combination constants from actual polynomial differences,
# rather than taking the claimed multipliers as checker inputs.
g0,g1=[O[f'S.chart.x.{i}.definition'] for i in (0,1)]
support=sorted(g0.keys()|g1.keys());basis=None
for a in support:
    for b in support:
        det=g0.get(a,0)*g1.get(b,0)-g0.get(b,0)*g1.get(a,0)
        if det:basis=(a,b,det);break
    if basis:break
assert basis
row_ops=[]
for i in (0,1):
    name=f'scalar.shiftedS.rootTimesInverseRoot.definition.{i}';d=add(N[name],scale(O[name],-1))
    a,b,det=basis
    c0=(d.get(a,0)*g1.get(b,0)-d.get(b,0)*g1.get(a,0))/det
    c1=(g0.get(a,0)*d.get(b,0)-g0.get(b,0)*d.get(a,0))/det
    assert d==add(scale(g0,c0),scale(g1,c1))
    row_ops.append([str(c0),str(c1)])
assert row_ops==[['-39/8','18'],['9/2','-39/4']]

Zname='scalar.W2.quadratic';T0name='scalar.preparationT.quadratic';Tname='scalar.preparationT'
bhname='scalar.Bh.quadratic';ename='scalar.normalized_e';riname='scalar.rInverse';nname='scalar.N'
Z,T0,T,B,e,ri,n=[var(x) for x in [Zname,T0name,Tname,bhname,ename,riname,nname]]
n2=mul(n,n)
assert set(on.values())-set(nn.values())=={Zname,T0name}
assert set(nn.values())-set(on.values())=={Tname}
r=derivative(O['scalar.rInverse.definition'],riname)
assert O['scalar.rInverse.definition']==add(mul(r,ri),const(-1))
L=scale(derivative(O['scalar.preparationT.definition'],Zname),-1)
assert O['scalar.preparationT.definition']==add(T0,scale(mul(L,Z),-1))
assert O['scalar.W2.definition']==add(Z,scale(n2,-1))
k=-O['scalar.Bh.definition'][tuple(sorted([ename,T0name]))]
mu=42*r[()]/(1+k*L.get((),0))
assert mu==184460384539620 and k==Q(521079743268,81331739215)
assert scale(add(const(1),scale(L,k)),mu)==scale(r,42)
assert O['scalar.Bh.definition']==add(B,scale(mul(e,Z),-1),scale(mul(e,T0),-k))
assert N['scalar.preparationT.definition']==add(mul(ri,T),scale(n2,-42))
assert N['scalar.Bh.definition']==add(B,scale(mul(e,T),-1))

# Full forward ideal identities, including the unchanged inverse row.
forward={Tname:scale(mul(r,Z),42),bhname:scale(B,mu)}
newT=sub(N['scalar.preparationT.definition'],forward)
assert newT==add(scale(mul(Z,O['scalar.rInverse.definition']),42),scale(O['scalar.W2.definition'],42))
newBh=sub(N['scalar.Bh.definition'],forward)
assert newBh==add(scale(O['scalar.Bh.definition'],mu),scale(mul(e,O['scalar.preparationT.definition']),mu*k))
assert sub(N['scalar.secondConic'],forward)==O['scalar.secondConic']

# Reverse identities: Z and T0 reconstruct polynomially; only mu is divided out.
reverse={Zname:n2,T0name:mul(L,n2),bhname:scale(B,1/mu)}
assert not sub(O['scalar.W2.definition'],reverse)
assert not sub(O['scalar.preparationT.definition'],reverse)
physical=add(T,scale(mul(r,n2),-42))
assert physical==add(mul(r,N['scalar.preparationT.definition']),scale(mul(T,N['scalar.rInverse.definition']),-1))
assert sub(O['scalar.Bh.definition'],reverse)==scale(add(N['scalar.Bh.definition'],mul(e,physical)),1/mu)
assert sub(O['scalar.secondConic'],reverse)==N['scalar.secondConic']
private={Zname,T0name,Tname,bhname};uses={}
for label,data in [('old',O),('new',N)]:
    uses[label]={x:sorted(name for name,p in data.items() if any(x in m for m in p)) for x in private if x in (on.values() if label=='old' else nn.values())}
    allowed={'scalar.W2.definition','scalar.preparationT.definition','scalar.Bh.definition','scalar.secondConic'}
    assert all(set(names)<=allowed for names in uses[label].values())
def guards(data,poly):return {g['name']:(poly(g['expression']),poly(g['inverse'])) for g in data['guards']}
assert guards(old,op)==guards(new,np)
# All actual test functions and chart/proxy aliases retain their formal values.
common_values=set(old['values'])&set(new['values']);alias_changes=[]
for name in common_values:
    a=op(old['values'][name]['terms']);b=np(new['values'][name]['terms'])
    if a!=b:alias_changes.append(name)
    if name.startswith('test') or name.startswith('scalar.shiftedS.') or name.startswith('scalar.ratioProxy'):
        assert a==b,name
assert set(alias_changes)<={'scalar.Bsemantic','scalar.preparationT','scalar.Bh'}

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
weights=read(REPO/'research/scalar-row-reduction/DIAGONAL_WEIGHTS.json')
ir=read(RUN/'balanced/integer-ir.json');table=read(RUN/'balanced/polynomial.json')
assert len(weights)==35 and all(len(v)==2 and all(type(i)==int for i in v) for v in weights.values())
assert len(post['coordinates'])==len(table['coordinates'])==379 and len(post['residuals'])==348
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
assert len(expanded)==len(table['terms'])==26021 and max(map(len,expanded))==4
assert {i for m in expanded for i in m}==set(range(379))
assert math.gcd(*expanded.values())==1 and expanded[(0,0,0,0)]==1
maximum=max(map(abs,expanded.values()));assert len(str(maximum))==425 and maximum.bit_length()==1410
textpath=RUN/'quartic-379-balanced-decimal.txt';parsed={}
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
        'baselineMatchesEarlierIndependentMixedReplay':True,'derivedARowMultipliers':row_ops,'derivedMu':str(mu),'derivedK':str(k),
        'forwardAndReverseIdealIdentities':True,'allPrivateConsumerRows':uses,'changedRawRows':sorted(changed),'unchangedCommonRows':358,
        'guardsIdentical':True,'testChartProxyAliasesIdentical':True,'changedCommonAliases':sorted(alias_changes),'fourConics':conics,
        'weights':{'specifiedCoordinates':35,'ternaryScaled':sum(bool(x[0]) for x in weights.values()),'dyadicScaled':sum(bool(x[1]) for x in weights.values()),'inputFixed':True},
        'all348DiagonalRowIdentitiesChecked':True,'allRowsPrimitive':True,'completeExpansionAndTextCompared':True,
        'coordinates':379,'residuals':348,'monomials':26021,'degree':4,'content':1,'allCoordinatesActive':True,'inputFourthPowerCoefficient':1,
        'maximumAbsoluteCoefficient':str(maximum),'maximumDigits':425,'maximumBits':1410,
        'tableSha256':digest(textpath),'rawSha256':digest(RUN/'raw-translated-ir.json'),
        'scope':'Exact rational algebra and finite measurements, supporting separately reviewed source-domain and zero-branch arguments; not global arithmetic acceptance.'}
(ROOT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
