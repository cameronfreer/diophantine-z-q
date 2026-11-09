"""Freeze exact reviewed source blobs and final comment-only correction."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
import sys

REPO=Path('/tmp/codex-glazer389-review-3j08z564/mixed')
ROOT=Path('/tmp/quartic-mixed-review')
HEAD='eb00b7c9c5be2e8666c0403c750c6c780cf78563'
INITIAL='6b4c2b58c871e35dada6bd15cd359b863e45838f'
PARENT='59c59e5589d86036ee41994c82a2b900fce85c2d'
PACKET='research/mixed-detector-normalization/'
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def sha(data):return hashlib.sha256(data).hexdigest()
assert git('rev-parse','HEAD').decode().strip()==HEAD
assert not git('status','--porcelain').strip()
manifest_bytes=git('show',HEAD+':'+PACKET+'SOURCE_BINDINGS.json')
assert sha(manifest_bytes)=='6b887df56ffe26e86422d464b3a951a5e29e1166e49c7af005c93be1f015b629'
manifest=json.loads(manifest_bytes)
assert len(manifest['files'])==100
for f in manifest['files']:
    committed=git('show',HEAD+':'+f['path'])
    assert sha(committed)==f['sha256'] and committed==(REPO/f['path']).read_bytes()
changes=git('diff','--name-only',PARENT,HEAD).decode().splitlines()
assert all(p.startswith(PACKET) or p=='.github/workflows/mixed-detector-normalization.yml' for p in changes)
correction_paths=git('diff','--name-only',INITIAL,HEAD).decode().splitlines()
assert set(correction_paths)=={PACKET+p for p in ['normalize_patch.py','EXPECTED.json','FINDINGS.json','SOURCE_BINDINGS.json','SOURCE_BINDINGS_SHA256.txt']}
for p in ['PROOF.md','APPLICATION_CONTRACT.json','check_mixed.py','reproduce.py']:
    assert git('show',INITIAL+':'+PACKET+p)==git('show',HEAD+':'+PACKET+p)

# Generate final builder through the author source transformations, then compare
# the actual text/executable content and independently rerun Node. This is not
# the reviewer-owned algebra checker; its inputs are frozen above.
sys.path.insert(0,str(REPO/PACKET))
spec=importlib.util.spec_from_file_location('mixed_replay_for_freeze',REPO/PACKET/'reproduce.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
original=(module.CONSTRUCTION/'builder.cjs').read_text()
final=module.mixed(module.cube(module.transform(original,45,2010)))
initial=(ROOT/'replay/builder.cjs').read_text()
# Actual difference is three standalone // comments. Keep all noncomment lines
# byte for byte; no general JS parsing or string-literal stripping is assumed.
noncomments=lambda s:''.join(line for line in s.splitlines(keepends=True) if not line.lstrip().startswith('//'))
assert noncomments(initial)==noncomments(final)
out=ROOT/'final-comment-rebuild';out.mkdir(exist_ok=True)
(out/'builder.cjs').write_text(final)
expected=json.loads((REPO/PACKET/'EXPECTED.json').read_text())['46']
assert sha((out/'builder.cjs').read_bytes())==expected['files']['builder.cjs']
with (out/'node.log').open('wb') as log:
    subprocess.run(['node',str(out/'builder.cjs')],cwd=REPO,stdout=log,stderr=subprocess.STDOUT,check=True)
assert (out/'raw-translated-ir.json').read_bytes()==(ROOT/'replay/raw-translated-ir.json').read_bytes()
assert sha((out/'raw-translated-ir.json').read_bytes())==expected['files']['raw-translated-ir.json']

# Review-history location claimed in the new handoff: preserve actual originals.
history_commit='a5ffef4019cd68b48c40e9f9d52d0a1cf8217859'
history_dir='research/independent-local-reviews/2026-11-09/height/'
historical=[]
for name in ['REPORT.md','FINDINGS.json']:
    data=git('show',history_commit+':'+history_dir+name)
    local=(Path('/tmp/quartic-height-review')/name).read_bytes()
    assert data==local
    historical.append({'commit':history_commit,'path':history_dir+name,'sha256':sha(data),'matchesReviewerOriginal':True})
record={'reviewer':'/root/independent_math_review','reviewType':'independent internal AI review; not human peer review',
        'date':'2026-11-09','head':HEAD,'initialHead':INITIAL,'parent':PARENT,
        'hashAlgorithm':'SHA-256','sourceBindingManifestSha256':sha(manifest_bytes),
        'files':manifest['files'],'allBoundFilesMatchCommittedBlobs':True,
        'incrementalPaths':changes,'correctionPaths':correction_paths,
        'proofSha256':sha((REPO/PACKET/'PROOF.md').read_bytes()),
        'contractSha256':sha((REPO/PACKET/'APPLICATION_CONTRACT.json').read_bytes()),
        'finalBuilderSha256':sha((out/'builder.cjs').read_bytes()),
        'initialBuilderSha256':sha(initial.encode()),
        'nonCommentExecutableLinesByteIdentical':True,
        'freshFinalRawIrMatchesInitialFullReplay':True,
        'rawSha256':sha((out/'raw-translated-ir.json').read_bytes()),
        'priorReviewArchiveChecks':historical,
        'scope':'Local immutable source and history validation. No public PR or App readback authorization.'}
(ROOT/'SOURCE_HASHES.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['files','incrementalPaths']},indent=2))
