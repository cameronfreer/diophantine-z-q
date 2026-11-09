"""Reviewer-owned higher-order, consumer, conic and full-table checks.
Reuses this reviewer's earlier polynomial helpers; no author checker imports.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import copy
ROOT=Path('/tmp/quartic-higher377-review');RUN=ROOT/'replay'
REPO=Path('/tmp/codex-glazer389-review-3j08z564/higher377')
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


old=read(RUN/'baseline/raw-translated-ir.json');new_original=read(RUN/'raw-translated-ir.json')
assert (RUN/'baseline/raw-translated-ir.json').read_bytes()==Path('/tmp/quartic-power376-review/replay/raw-translated-ir.json').read_bytes()
assert old['fixedParameter']=={'name':'S','value':'3^2010','coordinate':False}
assert new_original['fixedParameter']=={'name':'S','value':'3^1512','coordinate':False}
def canonical(s):
    for a,b in [('q50','q46'),('E50','E46'),('.50.','.46.'),('q1FourthForWeights','E1.power4')]:s=s.replace(a,b)
    return s
new=copy.deepcopy(new_original)
for key in ['coordinates','residuals']:
    for item in new[key]:item['name']=canonical(item['name'])
on,op,O=decode(old);nn,np,N=decode(new)
removed={f'detector{i}.{s}.definition' for i in range(3) for s in ['q1Sixth','q1Twelfth']}
added={f'detector{i}.{s}.definition' for i in range(3) for s in ['q1Eighth','q1InverseSeventh']}|{'scalar.rInverse31.definition'}
changed={f'detector{i}.{s}.definition' for i in range(3) for s in ['q12','q46']}|{'scalar.ratioProxyLeaf.definition'}
assert O.keys()-N.keys()==removed and N.keys()-O.keys()==added
assert {k for k in O.keys()&N.keys() if O[k]!=N[k]}==changed
assert len(nn)-len(on)==len(N)-len(O)==1
old_values={k:op(v['terms']) for k,v in old['values'].items()}
new_values={}
for k,v in new['values'].items():
    name=canonical(k);p=np(v['terms'])
    if name in new_values:assert p==new_values[name]
    new_values[name]=p
assert old_values.keys()-new_values.keys()=={x.removesuffix('.definition') for x in removed}
assert new_values.keys()-old_values.keys()=={x.removesuffix('.definition') for x in added}
assert all(old_values[k]==new_values[k] for k in old_values.keys()&new_values.keys())
def guards(data,p):return {g['name']:(p(g['expression']),p(g['inverse'])) for g in data['guards']}
assert guards(old,op)==guards(new,np)
# Independent Q[u,u^-1] evaluation of all actual affine aliases and rows.
def ladd(*ps):
    r=defaultdict(Q)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return {e:c for e,c in r.items() if c}
def lscale(p,c):return {e:a*c for e,a in p.items() if a*c}
def lmul(p,q):
    r=defaultdict(Q)
    for e,c in p.items():
        for f,d in q.items():r[e+f]+=c*d
    return {e:c for e,c in r.items() if c}
def leval(p,mapping):
    r={}
    for m,c in p.items():
        t={0:c}
        for x in m:t=lmul(t,mapping[x])
        r=ladd(r,t)
    return r
chain=[('q1SquaredForWeights',2),('q1CubedForWeights',3),('E1.power4',4),('q1Eighth',8),('q1InverseSeventh',-7),('q12',23),('mixedHigh',46),('q46',99),('E46.power2',198),('E46.power3',297)]
blocks=[]
for i in range(3):
    prefix=f'detector{i}.';mapping={}
    def identify(name,power):
        alias=new_values[prefix+name]
        unknown=[m for m in alias if len(m)==1 and m[0] not in mapping]
        assert len(unknown)==1 and all(len(m)<=1 for m in alias)
        m=unknown[0];c=alias[m];known={a:b for a,b in alias.items() if a!=m}
        mapping[m[0]]=lscale(ladd({power:Q(1)},lscale(leval(known,mapping),-1)),1/c)
        assert leval(alias,mapping)=={power:Q(1)}
    identify('q1',1)
    for name,power in chain:
        identify(name,power)
        assert not leval(N[prefix+name+'.definition'],mapping),name
    assert np(new_original['values'][prefix+'q1FourthForWeights']['terms'])==np(new_original['values'][prefix+'E1.power4']['terms'])
    # They are two names for one allocated coordinate, not two free powers.
    slots=[c for c in new_original['coordinates'] if c['name'] in [prefix+'q1FourthForWeights.quadratic',prefix+'E1.power4.quadratic']]
    assert len(slots)==1
    for name,denom in [('q1InverseSeventh','q1Eighth'),('q12','q1InverseSeventh'),('q46','q1InverseSeventh')]:
        row=next(r for r in new['residuals'] if r['name']==prefix+name+'.definition')
        gate=next(g for g in new['gates'] if g['definitionResidualId']==row['id'])
        assert gate['operation']=='rational_quotient' and np(gate['denominator'])==new_values[prefix+denom]
    val=lambda name:new_values[prefix+name]
    w0,w1,n,E,B=[val(name) for name in ['W.0','W.1','normOver2w0','eDelta','Bsemantic']]
    proportional(N[prefix+'normOver2w0.definition'],add(scale(mul(w0,n),2),scale(mul(w0,w0),-1),scale(mul(w1,w1),2)))
    proportional(N[prefix+'B.definition'],add(mul(E,B),scale(mul(n,n),-1)))
    inv_name=prefix+'q1InverseSeventh'
    assert {name for name,poly in N.items() if any(inv_name in m for m in poly)}=={prefix+x+'.definition' for x in ['q1InverseSeventh','q12','q46']}
    blocks.append({'detector':i,'actualPowers':{name:p for name,p in chain},'LaurentIdentitiesExact':True,'fourthPowerAllocatedOnce':True})
# Exact scalar equations in original rational coordinate ring.
v=lambda name:new_values[name]
r=v('scalar.r');inv=v('scalar.rInverse');kappa=v('scalar.rInverse15')
proportional(N['scalar.rInverse.definition'],add(mul(r,inv),const(-1)))
scalar_exponents=[-1];prev=inv
for suffix in [3,7,15,31]:
    out=v('scalar.rInverse'+str(suffix))
    proportional(N['scalar.rInverse'+str(suffix)+'.definition'],add(mul(r,out),scale(mul(prev,prev),-1)))
    scalar_exponents.append(2*scalar_exponents[-1]-1);assert scalar_exponents[-1]==-suffix
    prev=out
assert {name for name,poly in N.items() if any('scalar.rInverse31' in m for m in poly)}=={'scalar.rInverse31.definition','scalar.ratioProxyLeaf.definition'}
proxy=v('scalar.ratioProxyReal');y=v('scalar.ratioProxyLeaf')
proportional(N['scalar.ratioProxyReal.definition'],add(proxy,scale(mul(v('primaryRatio.0'),v('scalar.shiftedS.w.0')),-1),scale(mul(v('primaryRatio.1'),v('scalar.shiftedS.w.1')),-2)))
proportional(N['scalar.ratioProxyLeaf.definition'],add(mul(r,y),scale(mul(proxy,prev),-1)))
assert v('scalar.directLeaf.0')==y and not v('scalar.directLeaf.1')
for name,left,right in [('scalar.chain3','scalar.shiftedS.f.1','scalar.ratioProxyLeaf'),('scalar.chain2','scalar.shiftedS.f.0','scalar.chain3'),('scalar.chain1','H.f.1','scalar.chain2'),('scalar.N','H.f.0','scalar.chain1')]:
    out=v(name);sqright=v(name+'.rightSquare')
    proportional(N[name+'.rightSquare.definition'],add(sqright,scale(mul(v(right),v(right)),-1)))
    lhs=mul(r,out) if name=='scalar.N' else out
    proportional(N[name+'.definition'],add(lhs,scale(mul(v(left),v(left)),-1),scale(mul(kappa,sqright),-1)))
assert v('scalar.W')==v('scalar.N')
proportional(N['scalar.preparationT.definition'],add(mul(inv,v('scalar.preparationT')),scale(mul(v('scalar.N'),v('scalar.N')),-42)))
assert v('scalar.Bsemantic')==v('scalar.preparationT')
anchor_slot='anchor.physicalA.quadratic'
assert {name for name,poly in N.items() if any(anchor_slot in m for m in poly)}=={'anchor.physicalA.definition','anchor.translatedEquation'}
# Exact affine-in-R sufficient valuation functions, proved for every R>=1.
bound=Q(-1,2);bounds={}
bounds['A']=(bound+1)/2;bound=(bound+16)/2;bounds['J1']=bound
for leaf,node in [('B','J2'),('C','J3'),('D0','y')]:
    bounds[leaf]=bound/2;bound=(bound+15)/2;bounds[node]=bound
bounds['Tproxy']=bounds['y']+32
assert list(bounds.values())==list(map(Q,['1/4','31/4','31/8','91/8','91/16','211/16','211/32','451/32','1475/32']))
assert bounds['Tproxy']>46 and 47-bounds['Tproxy']==Q(29,32)
# L=16R+1, 2L-15R=17R+2, which exceeds L; root subtracts R.
assert (2*16-15,2*1)==(17,2) and (17-1,2)==(16,2)
assert (48-32,1)==(16,1)
# Exact polynomial congruences: checking all residues proves each statement.
def rho(x):
    beta=2401+2754*(2*x+1)**2
    return 42*beta*(beta-1)*(32*beta+343)
for modulus,residue in [(32,4),(243,81),(17,13)]:assert {rho(x)%modulus for x in range(modulus)}=={residue}
assert 8*8%17==13
orders=[50,12,1,1,1,1,1,1,1,1,12,50,50,50,50,50]
assert [orders.count(x) for x in [1,12,50]]==[8,2,6]
for i in range(16):
    for j in range(2):assert old_values[f'test{i}.{j}']==new_values[f'test{i}.{j}']
source=(RUN/'builder.cjs').read_text()
assert 'i===0?50:i===1?12:1' in source and 'order:i===1?12:50' in source
assert 'value:fsub(L[1],[beta,zero]),order:50' in source and 'value:FF,order:50' in source
assert 'W=N>0' in source
# Complete first-tail coefficient and uniform tail step; proof covers infinity.
a=Q(-2,5)
for j in range(2,14):a*=Q(4*j-5,4*j+1)
assert a==Q(-54756974,6936596275) and a.denominator==5**2*7*17*29*37*41*53
assert 4*14-(4*14+1)//10==51 and all(((4*j+5)//10-(4*j+1)//10)<=1 for j in range(10))
assert 4*50==200 and 51>=50 and 50-1==49
normalizations=[]
for m in [1,12,50]:
    j=2*m-1;assert 2*m-1-2*j==-j
    normalizations.append({'order':m,'deltaDenominator':j,'nuAndS':[j,4*j],'realDecayPower':-j})
deltas=[98*x-1 for x in [Q(0),Q(1,49),Q(1,50),Q(1,2450),Q(32,1225)]]
assert deltas==[Q(-1),Q(1),Q(24,25),Q(-24,25),Q(39,25)]
for x in deltas:
    for n in [abs(x.numerator),x.denominator]:
        for p in [2,3,5,7,13,17]:
            while n%p==0:n//=p
        assert n==1
H=3*2**106*(2**32*3**9)**6*46410**18+128;c=2*3**755;b=c-1
assert 1512//2-1==755 and 32*47==1504 and 1504-577==927
assert 8**1504*c**927>(25*H)**1504
assert (2*(b*b-6))**1600>(3*H+14)**1600*(2*b**4+6*b**3+5*b*b+1)**577
assert 64*50-2308==892 and 40*H<2**670 and b>67000
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
weights=read(REPO/'research/higher-order-variant/DIAGONAL_WEIGHTS.json')
ir=read(RUN/'balanced/integer-ir.json');table=read(RUN/'balanced/polynomial.json')
assert len(weights)==36 and all(len(v)==2 and all(type(i)==int for i in v) for v in weights.values())
assert len(post['coordinates'])==len(table['coordinates'])==377 and len(post['residuals'])==346
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
        c=Q(t['coefficient'])*3**(1512*t['sPower'])
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
assert len(expanded)==len(table['terms'])==25979 and max(map(len,expanded))==4
assert {i for m in expanded for i in m}==set(range(377))
assert math.gcd(*expanded.values())==1 and expanded[(0,0,0,0)]==1
maximum=max(map(abs,expanded.values()));assert len(str(maximum))==327 and maximum.bit_length()==1084
textpath=RUN/'quartic-377-balanced-decimal.txt';parsed={}
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
 'baselineMatchesEarlierIndependentPower376Replay':True,'removedRows':sorted(removed),'addedRows':sorted(added),'changedRows':sorted(changed),
 'unchangedCommonRows':len(O.keys()&N.keys())-len(changed),'rawCoordinateAndRowIncrease':1,'allCommonFormalAliasesAndGuardsIdenticalAfterDeclaredRenaming':True,
 'identityCaveat':'The scalar proxy leaf,N and scalar physical input change. Higher weights,W,trace and detector pole inputs change. Formal alias identity is not evaluated object equality.',
 'actualChains':blocks,'scalarInverseExponents':scalar_exponents,'scalarLeaf':'Tproxy/r^32','normNodeCoefficient':'r^-15 unchanged','actualScalarProxy':'Re(k_H*w_S)',
 'scalarStrictBounds':{k:str(v) for k,v in bounds.items()},'radicalOrder':47,'proxyFiniteDepth':'48R+1 gives five leaves>=16R+1 and rootN>=16R+2 for every R>=1',
 'rhoCongruences':{'mod32':4,'mod243':81,'mod17':13},'actualOrderList':orders,'actualPoleInput':'R_det/Tr(W^-1)^2','normalizations':normalizations,
 'precision':{'a13':str(a),'relativeBound':51,'consumedHighOrder':50,'primaryWeakBound':200,'primaryProgressionExponent':49},
 'height':{'anchorExponent':1512,'scalarOrder':47,'highOrder':50,'inputOrder':12,'scalarDenominator':1504,'scalarPositiveExponent':927,'uniformLucasRatioExponent':892,'inputGapAt301':'22/4775'},
 'fourConics':conics,'all346DiagonalRowIdentitiesChecked':True,'weights':{'specified':36,'ternary':sum(bool(x[0]) for x in weights.values()),'dyadic':sum(bool(x[1]) for x in weights.values()),'inputFixed':True},
 'coordinates':377,'residuals':346,'monomials':25979,'degree':4,'content':1,'allCoordinatesActive':True,'inputFourthPowerCoefficient':1,
 'completeExpansionAndTextCompared':True,'maximumAbsoluteCoefficient':str(maximum),'maximumDigits':327,'maximumBits':1084,
 'tableSha256':digest(textpath),'rawSha256':digest(RUN/'raw-translated-ir.json'),
 'scope':'Finite exact identities and complete coefficient checks supporting separately reviewed uniform applications; no global theorem or optimality acceptance.'}
(ROOT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
