"""Freeze reviewer evidence and check original contributed archive bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

REPO=Path('/tmp/codex-glazer389-review-3j08z564/power376')
ROOT=Path('/tmp/quartic-power376-review')
HEAD='32abb654ec295e28b51f92a51d7f12d4c5a626ec'
PARENT='ce15e8ece219a2bb000075a5a79f6ffd9bea6dfd'
PACKET='research/odd-power-detectors/'
ARCHIVE='research/scalar-row-reduction/'
ORIGINAL=Path('/tmp/claude-1000/-home-freer-math-diophantine-z-q/78a63063-c94e-475f-86a6-1c128ce9e4b9/scratchpad/explore')
VETTING=Path('/tmp/codex-opus-vet-20261109')
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def sha(data):return hashlib.sha256(data).hexdigest()
assert git('rev-parse','HEAD').decode().strip()==HEAD
assert not git('status','--porcelain').strip()
raw=git('show',HEAD+':'+PACKET+'SOURCE_BINDINGS.json');manifest=json.loads(raw)
assert sha(raw)==(REPO/PACKET/'SOURCE_BINDINGS_SHA256.txt').read_text().strip()
assert len(manifest['files'])==337
for f in manifest['files']:
    blob=git('show',HEAD+':'+f['path'])
    assert sha(blob)==f['sha256'] and blob==(REPO/f['path']).read_bytes(),f['path']
changes=git('diff','--name-only',PARENT,HEAD).decode().splitlines()
assert all(p.startswith(PACKET) or p=='.github/workflows/odd-power-detectors.yml' for p in changes)
inventory=REPO/ARCHIVE/'prior-investigation/INVENTORY.json';inv=json.loads(inventory.read_text())
assert len(inv['files'])==208
archive=[]
for f in inv['files']:
    data=(REPO/ARCHIVE/f['path']).read_bytes()
    assert sha(data)==f['sha256']
    if f['origin'].startswith('Codex vetting '):
        source=VETTING/f['origin'].removeprefix('Codex vetting ')
    else:source=ORIGINAL/f['origin']
    assert source.exists(),str(source)
    assert source.read_bytes()==data,str(source)
    archive.append({'path':f['path'],'originalPath':str(source),'sha256':sha(data),'byteIdenticalIncludingWhitespace':True,'status':f['status']})
history=[]
history_commit='a2d259fed72f6310e0ccfac9cdd1bc346b88782e'
history_dir='research/independent-local-reviews/2026-11-09/row379/'
prior_root=Path('/tmp/quartic-row379-review')
prior_manifest=json.loads((prior_root/'ARCHIVE_MANIFEST.json').read_text())
for name in ['ARCHIVE_MANIFEST.json','ARCHIVE_MANIFEST_SHA256.txt']+[r['path'] for r in prior_manifest['files']]:
    blob=git('show',history_commit+':'+history_dir+name)
    assert blob==(prior_root/name).read_bytes()
    history.append({'commit':history_commit,'path':history_dir+name,'sha256':sha(blob),'matchesReviewerOriginal':True})
record={'reviewer':'/root/independent_math_review','reviewType':'independent internal AI review; not human peer review','date':'2026-11-09',
        'head':HEAD,'parent':PARENT,'hashAlgorithm':'SHA-256','sourceBindingManifestSha256':sha(raw),'all337BoundFilesMatchCommittedBlobs':True,
        'proofSha256':sha((REPO/PACKET/'PROOF.md').read_bytes()),'contractSha256':sha((REPO/PACKET/'APPLICATION_CONTRACT.json').read_bytes()),
        'weightsSha256':sha((REPO/PACKET/'DIAGONAL_WEIGHTS.json').read_bytes()),'sourceFiles':manifest['files'],'incrementalPaths':changes,
        'priorReviewArchiveChecks':history,'archiveInventorySha256':sha(inventory.read_bytes()),'all208ArchivedFilesMatchOriginalBytes':True,
        'scope':'Exact source/selected historical byte bindings, not acceptance of all archived exploratory mathematics or public-destination/App verification.'}
(ROOT/'SOURCE_HASHES.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'ARCHIVE_PROVENANCE.json').write_text(json.dumps({'date':'2026-11-09','reviewer':'/root/independent_math_review','head':HEAD,
    'coverage':'All208 declared inventory entries checked against actual original files;199 original Opus research files and9 original Codex vetting files. Bytes including whitespace preserved. Large original build trees, binaries and unselected artifacts are outside the declared archive scope.','files':archive},indent=2)+'\n')
sources=[('manuscripts/quartic_v10.tex',10556,10640,'Preparation-zero pole statement, zero-witness domain and converse'),
         ('manuscripts/quartic_v10.tex',11031,11064,'Actual one-place argument; original cutoff and arbitrary normalized field inputs'),
         ('manuscripts/quartic_v10.tex',11220,11360,'Original simultaneous contact-prime and final H construction'),
         ('manuscripts/quartic_v13.tex',16566,16604,'Fixed-data prime theorem and arbitrary fixed bounds'),
         ('research/conditional-quartic-reduction/proofs/prior/round4/arithmetic_round4.tex',142,153,'Small-prime reapplication'),
         ('research/conditional-quartic-reduction/proofs/prior/round5/arithmetic_round5.tex',90,150,'Actual delta-normalized weights and pole consumers')]
for p in ['AGENTS.md','docs/audit-history/PROTOCOL.md','docs/research-review/PROTOCOL.md','docs/release-policy.md',
          'research/scalar-row-reduction/PROOF.md','research/scalar-row-reduction/APPLICATION_CONTRACT.json','research/scalar-row-reduction/HANDOFF.md',
          'research/odd-power-detectors/PROOF.md','research/odd-power-detectors/APPLICATION_CONTRACT.json','research/odd-power-detectors/HANDOFF.md',
          'research/conditional-quartic-reduction/proofs/detector_round7.tex',
          'research/detector-cube-reuse/references/precision51_PROOF.md',
          'research/mixed-detector-normalization/PROOF.md','research/scalar-preparation-zero/PROOF.md','research/factored-pole-reduction/PROOF.md',
          'research/height-consumer-refinement/PROOF.md',
          'research/scalar-row-reduction/prior-investigation/codex-vetting/VETTING.txt',
          *[f'research/scalar-row-reduction/prior-investigation/opus/{d}/NOTES.md' for d in ['coeffrows','scalarpoles','compose','frontier','weight47','blocks']]]:
    sources.append((p,1,len((REPO/p).read_bytes().splitlines()),'Whole source; argument/consumer locators in report'))
excerpts=[]
for path,start,end,locator in sources:
    data=(REPO/path).read_bytes();assert data==git('show',HEAD+':'+path)
    excerpt=b''.join(data.splitlines(keepends=True)[start-1:end])
    excerpts.append({'path':path,'commit':HEAD,'wholeFileSha256':sha(data),'lineStart':start,'lineEnd':end,'locator':locator,'excerptSha256':sha(excerpt)})
(ROOT/'SOURCE_EXCERPTS.json').write_text(json.dumps({'hashAlgorithm':'SHA-256','rule':'1-based inclusive original byte lines, splitlines(keepends=True); no whitespace/newline normalization','sources':excerpts},indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['sourceFiles','incrementalPaths']},indent=2))
