from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd
import hashlib,json,subprocess
ROOT=Path('/tmp/codex-glazer389-review-3j08z564/pr383')
OUT=Path('/tmp/quartic-independent-review/preparation-zero')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
paths={'AGENTS.md','docs/audit-history/PROTOCOL.md'}
for entry in read(ROOT/'research/scalar-preparation-zero/SOURCE_BINDINGS.json')['files']:
 assert sha(ROOT/entry['path'])==entry['sha256'],entry['path']
 paths.add(entry['path'])
for p in (ROOT/'research/scalar-preparation-zero').iterdir():
 if p.is_file(): paths.add(str(p.relative_to(ROOT)))
for packet in ['factored-pole-reduction','scalar-chain-reduction']:
 for p in (ROOT/'research'/packet).iterdir():
  if p.is_file():
   r=str(p.relative_to(ROOT));paths.add(r)
   assert subprocess.check_output(['git','show','e3444641dffc2d1cf5a9791111d584110e5dd111:'+r],cwd=ROOT)==p.read_bytes()
manifest={'reviewer':'/root/independent_math_review','commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'files':[{'path':p,'sha256':sha(ROOT/p)} for p in sorted(paths)]}
(OUT/'SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')

# Independent Laurent-polynomial algebra for normalization and the real limit.
n=8
unit=(0,)*n
const=lambda c:{unit:F(c)} if c else {}
def v(i):
 z=list(unit);z[i]=1;return {tuple(z):F(1)}
def add(*args):
 d=defaultdict(F)
 for p in args:
  for m,c in p.items():d[m]+=c
 return {m:c for m,c in d.items() if c}
def scale(p,k):return {m:c*k for m,c in p.items() if c*k}
def mul(a,b):
 d=defaultdict(F)
 for m,c in a.items():
  for t,e in b.items():d[tuple(x+y for x,y in zip(m,t))]+=c*e
 return {m:c for m,c in d.items() if c}
def powp(p,k):
 assert k>=0
 out=const(1)
 for _ in range(k):out=mul(out,p)
 return out
def invvar(i,k):
 t=list(unit);t[i]=-k;return {tuple(t):F(1)}
b,e,p,q,s=[v(i) for i in range(5)]
E=scale(e,17);sourceH=mul(e,add(scale(b,17),scale(powp(b,2),-1)))
sourceBH=scale(mul(b,sourceH),17)
assert sourceBH==mul(powp(b,2),mul(E,add(const(17),scale(b,-1))))
r1=add(powp(p,2),scale(mul(scale(b,17),mul(add(const(1),scale(e,-1)),add(const(1),scale(e,3)))),-1))
P=mul(p,invvar(0,1));Q=mul(q,invvar(0,2));S=mul(s,invvar(0,1))
n1=add(scale(mul(b,powp(P,2)),17),scale(mul(add(const(17),scale(E,-1)),add(const(17),scale(E,3))),-1))
assert mul(n1,scale(b,F(1,17)))==r1
r2=add(scale(mul(b,powp(q,2)),17),scale(mul(add(powp(s,2),scale(sourceBH,-1)),add(powp(s,2),scale(sourceBH,3))),-1))
NH=mul(E,add(const(17),scale(b,-1)))
n2=add(scale(mul(b,powp(Q,2)),17),scale(mul(add(powp(S,2),scale(NH,-1)),add(powp(S,2),scale(NH,3))),-1))
assert mul(n2,powp(b,4))==r2
# Laurent chain and exactly C=D=y=0. A,B remain fixed in this limit.
A,B,C,D,y,r=[v(i) for i in range(6)]
k=invvar(5,15)
J3=add(powp(D,2),mul(k,powp(y,2)))
J2=add(powp(C,2),mul(k,powp(J3,2)))
J1=add(powp(B,2),mul(k,powp(J2,2)))
N=mul(invvar(5,1),add(powp(A,2),mul(k,powp(J1,2))))
limit=lambda poly:{m:c for m,c in poly.items() if all(m[i]==0 for i in [2,3,4])}
expected=mul(invvar(5,1),add(powp(A,2),mul(k,powp(B,4))))
assert limit(N)==expected
assert limit(scale(mul(r,powp(N,2)),42))==scale(mul(r,powp(expected,2)),42)
# Complete residue classes, justified for the integer polynomial rho.
def rho(x):
 beta=2401+2754*(2*x+1)**2
 return 42*beta*(beta-1)*(32*beta+343)
for mod,residue in [(32,4),(243,81),(17,13)]:
 assert {rho(x)%mod for x in range(mod)}=={residue}
assert pow(8,2,17)==13

base=OUT/'replay'
compiled=read(base/'candidate/compiled/compiled-ir.json')
active=read(base/'candidate/compiled/active-ir.json')
assert compiled['residuals']==active['residuals']
ids={c['id'] for c in active['coordinates']}
removed=[c for c in compiled['coordinates'] if c['id'] not in ids]
assert sorted(c['name'] for c in removed)==['scalar.preparationU','scalar.preparationV']
assert not any(c['id'] in t['monomial'] for c in removed for row in compiled['residuals'] for t in row['terms'])
assert all(c['kind']=='base' and not c.get('protected',False) for c in removed)
# Expand the actual scaled residuals anew, independently of producer/checkers.
ir=read(base/'factored/balanced/integer-ir.json');poly=read(base/'factored/balanced/polynomial.json')
compact={c['sourceId']:c['id'] for c in poly['coordinates']}
d=defaultdict(int)
for row in ir['residuals']:
 ts=[(tuple(compact[i] for i in t['monomial']),int(t['coefficient'])) for t in row['terms']]
 for m,a in ts:
  for t,c in ts:d[tuple(sorted(m+t))]+=a*c
d={m:c for m,c in d.items() if c}
assert d=={tuple(t['monomial']):int(t['coefficient']) for t in poly['terms']}
assert len(d)==26019 and len(ir['coordinates'])==383 and len(ir['residuals'])==352
assert max(map(len,d))==4 and gcd(*d.values())==1 and d[(0,0,0,0)]==1
assert set(i for m in d for i in m)==set(range(383))
maximum=max(map(abs,d.values()));assert maximum==28902*3**1420
report={'reviewer':'/root/independent_math_review','status':'PASS','scope':'Exact finite checks, not a proof of inherited arithmetic or simultaneous completeness.',
 'sourceFiles':len(paths),'sourceCommit':manifest['commit'],'normalizationResidualFactors':{'normalizedFirstToSource':'b/17','normalizedSecondToSource':'b^4'},
 'chainRealLimitChecked':True,'rhoCompleteResidues':{'32':4,'243':81,'17':13},
 'unusedCoordinates':removed,'allCompiledResidualsPreserved':True,
 'coefficients':{'variables':383,'residuals':352,'monomials':26019,'maxDigits':len(str(maximum)),'maxBits':maximum.bit_length(),
 'polynomialSha256':sha(base/'factored/balanced/polynomial.json'),'tableSha256':sha(base/'factored/quartic-383-balanced-decimal.txt')}}
(OUT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
