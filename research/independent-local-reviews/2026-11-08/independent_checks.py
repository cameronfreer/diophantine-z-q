from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd
import hashlib, json, subprocess

ROOT = Path('/tmp/codex-glazer389-review-3j08z564/prchain')
OUT = Path('/tmp/quartic-independent-review')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())

# Freeze every reviewed packet file, every contract source, and the supplying
# primary passages. Validate declared hashes instead of refreshing them.
paths = {'AGENTS.md', 'docs/audit-history/PROTOCOL.md', 'manuscripts/quartic_v10.tex',
 'research/conditional-quartic-reduction/PR_DEPENDENCIES.md',
 'research/conditional-quartic-reduction/proofs/prior/round2/scalar-preparation-proof.txt',
 'research/conditional-quartic-reduction/proofs/prior/round2/further_arithmetic_body.tex'}
for packet in ['factored-pole-reduction', 'scalar-chain-reduction']:
    base = ROOT/'research'/packet
    paths.update(str(p.relative_to(ROOT)) for p in base.iterdir() if p.is_file())
    c = read(base/'APPLICATION_CONTRACT.json')
    for bound in c['sources'] + c.get('boundFiles', []):
        p = ROOT/bound['path']
        assert sha(p) == bound['sha256'], str(p)
        paths.add(bound['path'])
for bound in read(ROOT/'research/scalar-chain-reduction/SOURCE_BINDINGS.json')['files']:
    assert sha(ROOT/bound['path']) == bound['sha256'], bound['path']
    paths.add(bound['path'])
records=[]
for relative in sorted(paths):
    p=ROOT/relative
    records.append({'path':relative, 'sha256':sha(p), 'bytes':p.stat().st_size})
# The primary manuscript consulted is byte-identical to the frozen upstream.
old = subprocess.check_output(['git','show','036cebe4f1a4aa7ca89820a9b48f3629b4c364d6:manuscripts/quartic_v10.tex'],cwd=ROOT)
assert old == (ROOT/'manuscripts/quartic_v10.tex').read_bytes()
for p in (ROOT/'research/factored-pole-reduction').iterdir():
    if p.is_file():
        b = subprocess.check_output(['git','show','6fd131e7ca150d7a023bcb6ac4f1971912705fab:'+str(p.relative_to(ROOT))],cwd=ROOT)
        assert b==p.read_bytes()
(OUT/'SOURCE_HASHES.json').write_text(json.dumps({'reviewer':'/root/independent_math_review','files':records},indent=2)+'\n')

# Independent valuation descent, starting at N > -R/2. At each norm,
# unequal parities force each summand separately above its parent bound.
parent=Q(-1,2)
bounds={}
for leaf,right,coeff_left,coeff_right in [('A','J1',-1,-16),('B','J2',0,-15),('C','J3',0,-15),('D0','y',0,-15)]:
    assert (coeff_left-coeff_right)%2
    bounds[leaf]=(parent-coeff_left)/2
    bounds[right]=(parent-coeff_right)/2
    parent=bounds[right]
bounds['Tproxy']=bounds['y']+16
assert bounds['Tproxy']==Q(963,32)
assert all(bounds[k]>0 for k in ['A','B','C','D0'])
assert bounds['Tproxy'].numerator//bounds['Tproxy'].denominator+1==31
# Sufficient finite-preparation bounds as affine pairs (R coefficient, constant).
# Conservatively reset each child to 16R+1 before the next node.
for v in [(32,2),(17,2)]:
    assert v[0]>=16 and v[1]>=1
assert min(32-1,32-15-1)==16
# At p=41 the two sqrt(2) residues give fixed h_P residues 39 and 0.
roots=[i for i in range(41) if i*i%41==2]
hres=[(-1+7*pow(4,-1,41)*i)%41 for i in roots]
assert sorted(hres)==[0,39]
trace_real=(-sum(hres)*pow(2,-1,41))%41
assert trace_real==1

alpha=Q(577,32)
H=3*2**106*(2**32*3**9)**6*46410**18+128
c=2*3**1064; b=3**1064
assert 1-alpha/31==Q(415,992)
assert 2-4*alpha/45==Q(143,360)
scalar_left=c**415; scalar_right=(4*H)**992
lucas_left=b**143; lucas_right=(24*H)**360
assert scalar_left>scalar_right and lucas_left>lucas_right
assert 40*H<2**670 and 100*670<b and b>152
assert Q(12,5)*Q(1,100)+Q(19,5)*Q(1,4)==Q(487,500)
assert (1-Q(487,500))*153>3+Q(19,20)

# Expand the actual scaled residuals anew; compare all coefficients against
# the delivered polynomial, independently of producer/certificate algorithms.
expansion=[]
for label,base,expected_terms,expected_power in [
 ('PR9',OUT/'pr9-replay/candidate385',26235,1576),
 ('PR11',OUT/'pr11-replay/factored',26200,1420)]:
    ir=read(base/'balanced/integer-ir.json')
    poly=read(base/'balanced/polynomial.json')
    compact={c['sourceId']:c['id'] for c in poly['coordinates']}
    accumulator=defaultdict(int)
    for row in ir['residuals']:
        ts=[(tuple(compact[i] for i in t['monomial']),int(t['coefficient'])) for t in row['terms']]
        for m,a in ts:
            for n,z in ts:
                accumulator[tuple(sorted(m+n))]+=a*z
    accumulator={m:a for m,a in accumulator.items() if a}
    actual={tuple(t['monomial']):int(t['coefficient']) for t in poly['terms']}
    assert accumulator==actual
    assert len(actual)==expected_terms
    assert max(map(len,actual))==4
    assert actual[(0,0,0,0)]==1
    assert gcd(*actual.values())==1
    assert set(i for m in actual for i in m)==set(range(385))
    maximum=max(map(abs,actual.values()))
    assert maximum==28902*3**expected_power
    expansion.append({'pr':label,'residuals':len(ir['residuals']),'monomials':len(actual),
                      'maximumDigits':len(str(maximum)),'maximumBits':maximum.bit_length(),
                      'balancedIrSha256':sha(base/'balanced/integer-ir.json'),
                      'polynomialSha256':sha(base/'balanced/polynomial.json')})
report={'reviewer':'/root/independent_math_review','status':'PASS',
 'scope':'Finite source binding, exact arithmetic, fixed split-41 residues, and complete coefficient recomputation. Not proof of inherited arithmetic.',
 'sourceFiles':len(records),'bounds':{k:str(v) for k,v in bounds.items()},
 'split41':{'sqrt2Residues':roots,'hPResidues':hres,'negativeHalfTraceResidue':trace_real},
 'height':{'heightConstantBits':H.bit_length(),'scalarRatioFloorBits':(scalar_left//scalar_right).bit_length(),
           'lucasRatioFloorBits':(lucas_left//lucas_right).bit_length(),
           'allThreeMargins':True},'expansions':expansion}
(OUT/'INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
