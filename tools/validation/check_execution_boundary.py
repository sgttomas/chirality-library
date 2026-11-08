#!/usr/bin/env python3
"""Keep runnable source outside execution/; declarative inputs remain readable."""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
# Exact paths only. Adding an exception requires verifying that it is a
# documentation example, with no execution, compilation or import consumer.
DOCUMENTATION_ONLY_EXAMPLES: frozenset[str] = frozenset()
SOURCE_SUFFIXES = frozenset({
    '.py', '.pyw', '.pyi', '.pyc', '.pyo', '.rs', '.c', '.cc', '.cpp', '.h',
    '.hpp', '.cs', '.fs', '.go', '.java', '.class', '.kt', '.kts', '.scala',
    '.swift', '.m', '.mm', '.js', '.jsx', '.cjs', '.mjs', '.ts', '.tsx', '.sh',
    '.bash', '.zsh', '.fish', '.ps1', '.bat', '.cmd', '.rb', '.pl', '.php',
    '.lua', '.r', '.jl', '.sql', '.ipynb', '.wasm', '.so', '.dylib', '.dll',
    '.exe', '.o', '.a',
})
BUILD_ENTRYPOINTS = frozenset({
    'cargo.toml', 'pyproject.toml', 'setup.py', 'setup.cfg', 'package.json',
    'makefile', 'gnumakefile', 'cmakelists.txt', 'meson.build', 'build.gradle',
    'build.gradle.kts', 'dockerfile', 'justfile', 'pytest.ini', 'tox.ini',
})


def check_file(path: str, mode: str, data: bytes, *, executable: bool = False,
               examples: frozenset[str] = DOCUMENTATION_ONLY_EXAMPLES) -> list[str]:
    relative = PurePosixPath(path)
    if not relative.parts or relative.parts[0] != 'execution':
        return []
    if mode != '100644' or executable:
        return [f'{path}: execution inputs must be regular, non-executable files']
    if path in examples:
        return []
    source = (relative.suffix.lower() in SOURCE_SUFFIXES
              or relative.name.lower() in BUILD_ENTRYPOINTS
              or data.removeprefix(b'\xef\xbb\xbf').startswith(b'#!')
              or data.startswith((b'\x7fELF', b'MZ', b'\x00asm')))
    return [f'{path}: move runnable source/build entrypoints outside execution/'] if source else []


def check_repository(root: Path, *, examples: frozenset[str] = DOCUMENTATION_ONLY_EXAMPLES) -> tuple[int, list[str]]:
    entries = subprocess.check_output(
        ['git', 'ls-files', '--stage', '-z', '--', 'execution/'], cwd=root)
    errors: list[str] = []
    seen: set[str] = set()
    for entry in filter(None, entries.split(b'\0')):
        metadata, encoded_path = entry.split(b'\t', 1)
        mode, _, stage = metadata.decode().split()
        path = encoded_path.decode()
        seen.add(path)
        if stage != '0':
            errors.append(f'{path}: unresolved index entry')
            continue
        target = root / path
        if target.is_symlink():
            errors.append(f'{path}: execution inputs must not be symlinks')
            continue
        errors.extend(check_file(path, mode, target.read_bytes(),
                                 executable=bool(target.stat().st_mode & 0o111), examples=examples))
    errors.extend(f'{path}: documentation exception is not a tracked execution input'
                  for path in sorted(examples - seen))
    return len(seen), errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        count, errors = check_repository(args.root.resolve())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f'ERROR: execution boundary could not be checked: {error}', file=sys.stderr)
        return 2
    for error in errors:
        print(error)
    print(f'{"FAIL" if errors else "PASS"}: {count} tracked execution inputs; {len(errors)} boundary errors')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
