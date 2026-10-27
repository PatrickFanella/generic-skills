#!/usr/bin/env python3
"""Validate the public skill package without installing or running its skills."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'provenance.json').read_text())
errors = []
expected = manifest['files']
actual = {str(p.relative_to(root)): p for p in root.rglob('*')
          if p.is_file() and '.git' not in p.relative_to(root).parts
          and '__pycache__' not in p.parts and p.suffix != '.pyc'
          and p != root / 'provenance.json'}
for name in sorted(set(expected) | set(actual)):
    if name not in actual:
        errors.append('Missing packaged file: ' + name)
    elif name not in expected:
        errors.append('Unreviewed packaged file: ' + name)
    elif hashlib.sha256(actual[name].read_bytes()).hexdigest() != expected[name]:
        errors.append('Review and refresh changed file: ' + name)

listed = {row['name'] for row in manifest['skills']}
folders = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
if listed != folders:
    errors.append('Skill inventory does not match packaged directories')
for name in sorted(folders):
    folder = root / 'skills' / name
    entry = folder / 'SKILL.md'
    if not entry.is_file():
        errors.append('Missing entrypoint: ' + name)
        continue
    text = entry.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        errors.append('Missing YAML frontmatter: ' + name)
        continue
    front = yaml.safe_load(match.group(1))
    if front.get('name') != name or not isinstance(front.get('description'), str) or not front['description'].strip():
        errors.append('Invalid name or description: ' + name)
    allowed = {'name', 'description', 'license', 'metadata', 'allowed-tools'}
    if set(front) - allowed:
        errors.append('Unsupported frontmatter fields: ' + name)
    if not any((folder / file).is_file() for file in ['LICENSE', 'LICENSE.txt']):
        errors.append('Missing skill license: ' + name)
    # Entrypoint links are executable navigation, unlike illustrative code samples.
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^)]+)\)', prose):
        target = target.strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        target = unquote(target.split('#')[0])
        if target and not (folder / target).exists():
            errors.append(name + ': missing linked resource ' + target)
for path in root.rglob('*'):
    if '.git' in path.parts:
        continue
    if path.is_symlink():
        errors.append('Symlinks are not portable package resources: ' + str(path.relative_to(root)))
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'Validated {len(folders)} skills and {len(expected)} reviewed files')
