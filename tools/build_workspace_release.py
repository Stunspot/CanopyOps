#!/usr/bin/env python3
"""Build the portable v0.3.0 crop workspace without changing accepted releases."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import shutil
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RELEASES = REPO / 'releases'
BASELINE = '0.2.0'
VERSION = '0.3.0'
SLUG = 'canopyops'
TITLE = 'CanopyOps'
STAMP = (2026, 9, 28, 0, 0, 0)
IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc', '*.pyo')

def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def file_records(root: Path) -> list[dict]:
    return [{'path': p.relative_to(root).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)}
            for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts]

def zip_tree(archive: Path, root: Path, prefix: str = '') -> None:
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for p in sorted(root.rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts or p.suffix in ('.pyc', '.pyo'):
                continue
            name = (prefix + '/' if prefix else '') + p.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name, STAMP)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if p.suffix == '.command' else 0o100644) << 16
            output.writestr(info, p.read_bytes())

def remove_generated(path: Path, expected_name: str) -> None:
    resolved = path.resolve()
    if resolved.parent != RELEASES.resolve() or resolved.name != expected_name or path.is_symlink():
        raise SystemExit(f'Unsafe generated directory: {path}')
    if path.exists():
        shutil.rmtree(path)

def verifier_at(path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('canopyops_workspace_verifier', path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module

def main() -> int:
    baseline = RELEASES / f'v{BASELINE}'
    target = RELEASES / f'v{VERSION}'
    stage = RELEASES / f'.workspace-{SLUG}-{VERSION}'
    if not baseline.is_dir():
        raise SystemExit('Accepted portable baseline is missing')
    # These exact generated targets are the only directories this builder replaces.
    remove_generated(target, f'v{VERSION}')
    remove_generated(stage, f'.workspace-{SLUG}-{VERSION}')
    shutil.copytree(baseline, target, ignore=shutil.ignore_patterns('*.zip', '*.sha256', '__pycache__', '*.pyc', 'receipt.json', 'verification-report.json'))
    skill = target / 'codex' / SLUG / 'skills' / SLUG
    workspace = skill / 'workspace'
    # Existing workspace is generated candidate content beneath the verified target.
    if workspace.resolve() != (target / 'codex' / SLUG / 'skills' / SLUG / 'workspace').resolve():
        raise SystemExit('Unsafe workspace target')
    if workspace.exists():
        shutil.rmtree(workspace)
    shutil.copytree(REPO / SLUG / 'workspace', workspace, ignore=IGNORE)
    shutil.copy2(REPO / SLUG / 'SKILL.md', skill / 'SKILL.md')
    changelog = skill / 'CHANGELOG.md'
    original = changelog.read_text(encoding='utf-8')
    entry = ('## 0.3.0\n\nAdded room/zone exploration, through-date evidence views, compatible discrete measurement plots, '
             'observation comparison and the Understory, Lampblack and Clearspan environments. Preserved native record '
             'capture, original imports, history and conflict-aware saves. No sensor or equipment integration.\n\n')
    changelog.write_text(original.replace('# Changelog\n\n', '# Changelog\n\n' + entry, 1), encoding='utf-8', newline='\n')
    for p in (REPO / 'release-docs' / 'workspace').glob('*.md'):
        shutil.copy2(p, target / 'docs' / p.name)
    shutil.copy2(REPO / SLUG / 'workspace' / 'README.md', target / 'OPEN-THE-CROP-DESK.md')
    # Relative links in the outer entry point need the payload prefix.
    entrypoint = target / 'OPEN-THE-CROP-DESK.md'
    body = entrypoint.read_text(encoding='utf-8').replace('(SKINS.md)', '(codex/canopyops/skills/canopyops/workspace/SKINS.md)').replace('(WORKSPACE-GUIDE.md)', '(codex/canopyops/skills/canopyops/workspace/WORKSPACE-GUIDE.md)')
    body += '\nThe launchers are in `codex/canopyops/skills/canopyops/workspace/` inside this extracted bundle.\n'
    entrypoint.write_text(body, encoding='utf-8', newline='\n')
    sidecars = target / 'delivery-sidecars'
    if sidecars.exists():
        shutil.rmtree(sidecars)
    sidecars.mkdir()
    for name in [f'{TITLE}.png', f'{TITLE} v{VERSION}.md', f'{TITLE} v{VERSION} Extra.md']:
        shutil.copy2(REPO / 'delivery-sidecars' / name, sidecars / name)
    plugin_path = target / 'codex' / SLUG / '.codex-plugin' / 'plugin.json'
    plugin = json.loads(plugin_path.read_text(encoding='utf-8'))
    plugin['version'] = VERSION
    dump(plugin_path, plugin)
    decision = json.loads((REPO / 'verification/workspace/release-decision-v0.3.0.json').read_text(encoding='utf-8'))
    dump(target / 'release-decision.json', decision)
    shutil.copy2(REPO / f'RELEASE-NOTES-v{VERSION}.md', target / f'RELEASE-NOTES-v{VERSION}.md')
    claude = target / 'claude' / f'{SLUG}-v{VERSION}.zip'
    zip_tree(claude, skill)
    manifest = json.loads((target / 'manifest.json').read_text(encoding='utf-8'))
    manifest['family']['version'] = VERSION
    manifest['family']['backup_filename'] = f'{TITLE}-v{VERSION}.zip'
    manifest['source_records'] = [{'handle': SLUG, 'files': file_records(skill)}]
    manifest['claude_archives'] = [{'handle': SLUG, 'file': 'claude/' + claude.name, 'sha256': digest(claude)}]
    manifest['delivery_sidecars'] = {'path': 'delivery-sidecars', 'files': file_records(sidecars)}
    manifest['package_claim_boundary'] = 'Fresh static package verification; local browser evidence is recorded separately. macOS, fresh customer hosts and field outcomes remain unverified.'
    dump(target / 'manifest.json', manifest)
    dump(target / 'package-receipt.json', {'schema': 'cd-settled-family-package-receipt/v1', 'family': SLUG, 'version': VERSION, 'status': 'static-package-built', 'claim_boundary': manifest['package_claim_boundary']})
    verifier = verifier_at(target / 'tools' / 'verify_release.py')
    report = verifier.verify(target)
    if not report['ok']:
        print(json.dumps(report, indent=2), file=sys.stderr)
        return 1
    dump(target / 'verification-report.json', report)
    shutil.copytree(target, stage, ignore=IGNORE)
    archive = target / f'{TITLE}-v{VERSION}.zip'
    zip_tree(archive, stage, f'{SLUG}-v{VERSION}')
    remove_generated(stage, f'.workspace-{SLUG}-{VERSION}')
    checksum = digest(archive)
    (target / (archive.name + '.sha256')).write_text(checksum + '  ' + archive.name + '\n', encoding='utf-8', newline='\n')
    with zipfile.ZipFile(archive) as z:
        members = len(z.infolist())
    dump(target / 'receipt.json', {'schema': 'cd-settled-family-build-receipt/v1', 'family': SLUG, 'version': VERSION, 'canonical_zip': archive.name, 'canonical_zip_sha256': checksum, 'canonical_checksum': archive.name + '.sha256', 'canonical_zip_member_count': members, 'status': 'canonical-built', 'backup': None, 'copy_not_move_verified': False})
    final_report = verifier.verify(target)
    if not final_report['ok']:
        print(json.dumps(final_report, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({'archive': str(archive), 'sha256': checksum, 'members': members, 'verification': final_report}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
