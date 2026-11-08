"""Independently verify policy-only propagation and exact reviewed handoff bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path('/home/freer/math/diophantine-z-q')
OUT = Path('/tmp/quartic-protocol-v12-review')
POLICY = '9c0b3aba60d90fdcac82115f0582a6f52f1054f7'
HANDOFF = 'docs/reviews/quartic-stack-2026-11-08'
HEADS = json.loads(Path('/tmp/quartic-protocol-v12-input/final-heads.json').read_text())
git = lambda *a: subprocess.check_output(['git', '-C', str(ROOT), *a])
sha = lambda b: hashlib.sha256(b).hexdigest()
errors = []
base = git('merge-base', HEADS[0]['previous'], POLICY).decode().strip()
policy_paths = git('diff', '--name-only', base, POLICY).decode().splitlines()
scope = json.loads((OUT / 'SCOPE_BINDING_CHECKS.json').read_text())
manifest_sha = scope['handoffFiles']['HANDOFF_MANIFEST.json']
ack = []
prior = POLICY
for item in HEADS:
    old = git('rev-parse', item['previous']).decode().strip()
    head = item['head']
    for ancestor in (old, POLICY, prior):
        if subprocess.run(['git', '-C', str(ROOT), 'merge-base', '--is-ancestor', ancestor, head]).returncode:
            errors.append(['missing-ancestry', item['pr'], ancestor])
    paths = git('diff', '--name-only', old, head).decode().splitlines()
    unexpected = [p for p in paths if p not in policy_paths and not p.startswith(HANDOFF + '/')]
    if unexpected:
        errors.append(['unexpected-source-delta', item['pr'], unexpected])
    for p in policy_paths:
        if git('show', head + ':' + p) != git('show', POLICY + ':' + p):
            errors.append(['policy-bytes', item['pr'], p])
    actual_handoff = git('ls-tree', '-r', '--name-only', head, '--', HANDOFF).decode().splitlines()
    expected_handoff = [HANDOFF + '/' + p for p in scope['handoffFiles']]
    if sorted(actual_handoff) != sorted(expected_handoff):
        errors.append(['handoff-inventory', item['pr']])
    for p, expected in scope['handoffFiles'].items():
        if sha(git('show', head + ':' + HANDOFF + '/' + p)) != expected:
            errors.append(['handoff-bytes', item['pr'], p])
    if item['handoffManifestSha256'] != manifest_sha:
        errors.append(['parent-manifest-assertion', item['pr']])
    diff = git('diff', '--binary', old, head)
    policy_diff = git('diff', '--binary', old, head, '--', *policy_paths)
    handoff_diff = git('diff', '--binary', old, head, '--', HANDOFF)
    ack.append({'pr': item['pr'], 'previous': old, 'head': head,
                'changedPaths': paths, 'unexpectedChangedPaths': unexpected,
                'fullDiffSha256': sha(diff), 'policyDiffSha256': sha(policy_diff),
                'handoffDiffSha256': sha(handoff_diff),
                'handoffTree': git('rev-parse', head + ':' + HANDOFF).decode().strip(),
                'handoffManifestSha256': manifest_sha})
    prior = head

earlier = {
    'REPORT.md': '00f1accc3f4bc2b9d27da6c9517c536898cea9c035647022fd6534bb349201fd',
    'FINDINGS.json': '4baa6704e2cf7373f43e8ccfac5697a3009e38ea08e93c56949d918c8331d0d4',
    'preparation-zero/REPORT.md': 'd582f20f2917eb81a37e8259b8b761445e6859cef8dad4cf7deee9f0e4c046ab',
    'preparation-zero/FINDINGS.json': '328d702e80fbae58a494d7da0533dcdfef9a82dd7b19cf50cfc76adefce01759',
    'higher-precision/REPORT.md': '79c9b84d571a8798230c77d497a918713e0a22900a8b2f703dc06b09b63a1584',
    'higher-precision/FINDINGS.json': '034a6beca572f93e36e52a05e0c04bbea80b734dc256dbd3547a25cb4fe110c6'
}
for p, expected in earlier.items():
    if sha((Path('/tmp/quartic-independent-review') / p).read_bytes()) != expected:
        errors.append(['earlier-review-changed', p])
result = {'reviewer': '/root/independent_math_review', 'date': '2026-11-08',
          'status': 'PASS' if not errors else 'FAIL', 'errors': errors,
          'policyCommit': POLICY, 'oldStackMergeBase': base,
          'policyDeltaPaths': policy_paths, 'finalBindings': ack,
          'earlierReportsUnchanged': earlier,
          'sourceComparison': 'All tracked files outside eight policy/template paths and the new common handoff are byte-identical to each respective previous head. This includes mathematical packets, inherited source texts, current manuscript/PDF, prior contracts, checkers, workflows and acceptance register.',
          'dependencyAssessment': 'The eight policy/template changes affect review and reporting obligations, not the inputs or conventions of the previously reviewed local arithmetic applications. Every new handoff file is documentation/evidence; no pre-existing runtime or proof dependency is replaced.',
          'limits': 'Local Git ancestry/blobs and reviewer dependency assessment; no HTTP/public ref readback or designated App authorization.'}
(OUT / 'FINAL_HEAD_CHECKS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'errors': errors,
                  'heads': {a['pr']: a['head'] for a in ack},
                  'manifest': manifest_sha, 'changedPathCounts': {a['pr']: len(a['changedPaths']) for a in ack}}, indent=2))
