"""Independent finite integrity checks; not proof or protocol-App acceptance."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='/tmp/codex-glazer389-review-3j08z564/pr389')
    parser.add_argument('--archive', default='/home/freer/glazer_389_draft_pr_package.zip')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    repo = Path(args.repo)
    base = repo / 'docs/reviews/quartic-stack-2026-11-08'
    git = lambda *a: subprocess.check_output(['git', '-C', str(repo), *a])
    errors = []
    evidence = json.loads((base / 'EVIDENCE_MANIFEST.json').read_text())
    artifacts = json.loads((base / 'ARTIFACTS.json').read_text())
    handoff = json.loads((base / 'HANDOFF_MANIFEST.json').read_text())
    selection = json.loads((base / 'DELIVERY_SELECTION.json').read_text())
    before = {str(p.relative_to(base)): digest(p.read_bytes())
              for p in base.rglob('*') if p.is_file()}
    groups = {}
    for f in evidence['files']:
        blob = git('show', f['commit'] + ':' + f['path'])
        if digest(blob) != f['sha256']:
            errors.append(['evidence-digest', f['path']])
        owner = ('elliotglazer' if f['group'] == 'unchanged-current-release'
                 else 'cameronfreer')
        expected_url = ('https://github.com/' + owner + '/diophantine-z-q/blob/'
                        + f['commit'] + '/' + f['path'])
        if f['url'] != expected_url:
            errors.append(['url-mapping', f['path']])
        groups.setdefault(f['group'], []).append(f['path'])
    for a in artifacts['artifacts']:
        files = git('ls-tree', '-r', '--name-only', a['commit'], '--',
                    a['directory']).decode().splitlines()
        if sorted(files) != sorted(groups[a['id']]) or len(files) != a['fileCount']:
            errors.append(['packet-inventory', a['id']])
    for f in handoff['files']:
        if digest((base / f['path']).read_bytes()) != f['sha256']:
            errors.append(['handoff-digest', f['path']])
    expected_files = ({f['path'] for f in handoff['files']}
                      | {'HANDOFF_MANIFEST.json', 'HANDOFF_SHA256.txt'})
    if set(before) != expected_files:
        errors.append(['handoff-inventory', sorted(set(before) ^ expected_files)])
    if ((base / 'HANDOFF_SHA256.txt').read_text().split()[0]
            != digest((base / 'HANDOFF_MANIFEST.json').read_bytes())):
        errors.append(['handoff-external-digest'])
    archive = Path(args.archive)
    if digest(archive.read_bytes()) != selection['originalArchiveSha256']:
        errors.append(['archive-digest'])
    with zipfile.ZipFile(archive) as z:
        root = 'glazer_draft_pr_package/'
        external = {n[len(root):] for n in z.namelist()
                    if n.startswith(root) and not n.endswith('/')
                    and not n.startswith(root + 'payload/')}
        if external != {f['originalPath'] for f in selection['files']}:
            errors.append(['outside-overlay-inventory'])
        for f in selection['files']:
            blob = z.read(root + f['originalPath'])
            if digest(blob) != f['sha256'] or len(blob) != f['bytes']:
                errors.append(['archive-entry', f['originalPath']])
            if f['publishedPath'] and (base / f['publishedPath']).read_bytes() != blob:
                errors.append(['retained-original-bytes', f['originalPath']])
        a = next(a for a in artifacts['artifacts'] if a['id'] == 'pr8')
        for p in groups['pr8']:
            if z.read(root + 'payload/' + p) != git('show', a['commit'] + ':' + p):
                errors.append(['original-payload-vs-pr8', p])
    after = {str(p.relative_to(base)): digest(p.read_bytes())
             for p in base.rglob('*') if p.is_file()}
    if before != after:
        errors.append(['source-changed-during-check'])
    policy_commit = '9c0b3aba60d90fdcac82115f0582a6f52f1054f7'
    policy_files = ['AGENTS.md', 'docs/audit-history/PROTOCOL.md',
                    'docs/research-review/PROTOCOL.md', 'docs/release-policy.md',
                    'CONTRIBUTING.md', '.github/pull_request_template.md',
                    'docs/research-review/README.md']
    result = {
        'reviewer': '/root/independent_math_review',
        'reviewType': 'independent internal AI review',
        'date': '2026-11-08',
        'status': 'PASS' if not errors else 'FAIL',
        'errors': errors,
        'checks': ['All evidence SHA256 values against exact Git blobs',
                   'Complete tracked inventories of nine declared packet directories',
                   'Immutable URL commit/path/owner mapping, not HTTP availability',
                   'Complete handoff file inventory, bytes and external manifest digest',
                   'Original ZIP digest and complete outside-overlay selection inventory',
                   'All retained outside-overlay records equal original ZIP bytes',
                   'All 156 frozen PR8 payload files equal original ZIP bytes',
                   'Handoff unchanged during this check'],
        'evidenceCount': len(evidence['files']),
        'handoffBoundFileCount': len(handoff['files']),
        'outsideOverlayFileCount': len(selection['files']),
        'retainedOutsideOverlayFileCount': sum(bool(f['publishedPath']) for f in selection['files']),
        'groups': {k: len(v) for k, v in groups.items()},
        'handoffFiles': after,
        'policyCommit': policy_commit,
        'policyFileHashes': {p: digest(git('show', policy_commit + ':' + p)) for p in policy_files},
        'scopeLimit': 'Integrity and inventory checks only; no global proof, HTTP readback, branch approval, or designated App authorization.'
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {'handoffFiles', 'policyFileHashes'}}, indent=2))


if __name__ == '__main__':
    main()
