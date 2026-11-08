from pathlib import Path
from fractions import Fraction as Q
from math import prod,gcd
from collections import defaultdict
import hashlib,json,subprocess
ROOT=Path('/tmp/codex-glazer389-review-3j08z564/precision')
OUT=Path('/tmp/quartic-independent-review/higher-precision')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
paths={'AGENTS.md'}
for b in read(ROOT/'research/higher-detector-precision/SOURCE_BINDINGS.json')['files']:
 assert sha(ROOT/b['path'])==b['sha256'],b['path']
 paths.add(b['path'])
for p in (ROOT/'research/higher-detector-precision').iterdir():
 if p.is_file():paths.add(str(p.relative_to(ROOT)))
# Check that the final prose revision did not alter any computational source.
changed=subprocess.check_output(['git','diff','--name-only','4c669cc','HEAD'],cwd=ROOT,text=True).splitlines()
assert set(changed)=={'research/higher-detector-precision/'+x for x in ['PROOF.md','APPLICATION_CONTRACT.json','SOURCE_BINDINGS.json']}
manifest={'reviewer':'/root/independent_math_review','commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
 'files':[{'path':p,'sha256':sha(ROOT/p)} for p in sorted(paths)]}
(OUT/'SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')

# Product form of the actual recurrence, using exact reduced fractions.
a13=Q(-2*prod(4*k-5 for k in range(2,14)),5*prod(4*k+1 for k in range(2,14)))
assert a13.denominator==5**2*7*17*29*37*41*53 and a13.numerator%53
assert 11**2-2*6**2==49
# Floor step checks are periodic identities, not finite truncation of the tail.
assert all((r+4)//10-r//10 in [0,1] for r in range(10))
assert 4*14-(4*14+1)//10==51
assert all((r+4)//52-r//52 in [0,1] for r in range(52))
assert 4*14-(4*14+1)//52==55
# Thus for all j>=14 the lower bound increases by >=3 each step.
# For r>=1 each added depth increases 4jr-51r by (4j-51)>=5.
# The first omitted term at 53 depth one is exactly 52-1=51.
# Circuit exponents use (q1,delta), with E=q1*delta^2.
q1=(1,0);E=(1,2);delta=(0,1)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda a,k:tuple(x*k for x in a)
q12=add(scale(E,11),scale(q1,12))
mixed=scale(q12,2)
circuits={}
for m,factor in [(46,delta),(47,E)]:
 lift=add(mixed,factor)
 out=add(scale(lift,2),scale(q1,-1))
 assert out==(2*m-1,2*m-2)
 assert out==add(scale(E,m-1),scale(q1,m))
 circuits[str(m)]={'liftExponentsInQ1Delta':lift,'outputExponentsInQ1Delta':out}

H=3*2**106*(2**32*3**9)**6*46410**18+128
c,b=2*3**1007,3**1007
scalarLeft=c**415;scalarRight=(4*H)**992
assert scalarLeft>scalarRight
lucas=[]
for m in range(46,52):
 alpha=Q(577,32)
 assert 2-4*alpha/m==Q(16*m-577,8*m)
 left=b**(16*m-577);right=(24*H)**(8*m)
 assert left>right
 lucas.append({'order':m,'ratioFloorBits':(left//right).bit_length()})
assert (2*3**1004)**415<scalarRight
assert b**143<(24*H)**360
assert 40*H<2**670 and b>67000 and b>152

expansions=[]
for m,count in [(46,26046),(47,26037)]:
 base=OUT/('order'+str(m))
 gate=read(base/'gate-check.json')
 assert gate['status']=='passed_exact_algebra_checks'
 assert not gate['gateIdentities']['unverified'] and gate['quarticTableCompared']
 compiled=read(base/'compiled/compiled-ir.json');active=read(base/'active-ir.json')
 assert compiled['residuals']==active['residuals']
 activeids={c['id'] for c in active['coordinates']}
 removed=[c for c in compiled['coordinates'] if c['id'] not in activeids]
 assert sorted(c['name'] for c in removed)==['scalar.preparationU','scalar.preparationV']
 assert not any(c['id'] in t['monomial'] for c in removed for row in compiled['residuals'] for t in row['terms'])
 ir=read(base/'balanced/integer-ir.json');poly=read(base/'balanced/polynomial.json')
 compact={c['sourceId']:c['id'] for c in poly['coordinates']}
 d=defaultdict(int)
 for row in ir['residuals']:
  terms=[(tuple(compact[i] for i in t['monomial']),int(t['coefficient'])) for t in row['terms']]
  for x,a in terms:
   for y,z in terms:d[tuple(sorted(x+y))]+=a*z
 d={x:a for x,a in d.items() if a}
 assert d=={tuple(t['monomial']):int(t['coefficient']) for t in poly['terms']}
 assert len(d)==count and len(ir['coordinates'])==386 and len(ir['residuals'])==355
 assert max(map(len,d))==4 and d[(0,0,0,0)]==1 and gcd(*d.values())==1
 assert set(i for monomial in d for i in monomial)==set(range(386))
 maximum=max(map(abs,d.values()))
 assert maximum==28902*3**1344
 expansions.append({'order':m,'variables':386,'residuals':355,'monomials':count,
 'maximumDigits':len(str(maximum)),'maximumBits':maximum.bit_length(),
 'allGatesVerified':True,'allQuarticCoefficientsCompared':True,
 'polynomialSha256':sha(base/'balanced/polynomial.json'),'tableSha256':sha(base/'quartic-386-balanced-decimal.txt'),
 'measuredSha256':sha(base/'MEASURED.json')})
report={'reviewer':'/root/independent_math_review','status':'PASS',
 'scope':'Finite exact algebra and arithmetic. Infinite-tail coverage is established by the separate monotonicity proof; no inherited global theorem acceptance.',
 'commit':manifest['commit'],'sourceFiles':len(paths),'a13':str(a13),
 'tail':{'allJGe14BaseAtR1':51,'allJGe14IncreaseLowerBound':3,'p53FirstOmittedDepthOne':51,'p53LaterTermsLowerBound':55,
 'uniformRelativePrecision':51},'circuits':circuits,
 'height':{'Hbits':H.bit_length(),'scalarRatioFloorBits':(scalarLeft//scalarRight).bit_length(),'lucas':lucas,'allInputMargins':True,
 'anchor2010FailsScalarSufficientInequality':True,'order45At2016FailsLucasSufficientInequality':True},
 'expansions':expansions}
(OUT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
