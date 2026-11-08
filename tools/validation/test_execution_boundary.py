"""Source placement must not turn spec inputs into executable entrypoints."""
from pathlib import Path
import subprocess

import pytest

from check_execution_boundary import check_file, check_repository


@pytest.mark.parametrize('path,data', [
    ('execution/PKG-01/DEL-01-01/ScopeOfWork.md', b'# Scope\n```python\nprint(1)\n```'),
    ('execution/PKG-01/DEL-01-01/deliverable.yaml', b'checks: [tools/check.py]'),
    ('execution/_ScopeChange/bindings.json', b'{"script": "tools/check.py"}'),
    ('execution/_Decomposition/ACCEPTED_MANIFEST.csv', b'Path,SHA256\n'),
    ('execution/_ScopeChange/amendment.patch', b'+++ b/tools/example.py\n+print(1)'),
])
def test_declarative_inputs_and_documented_examples_are_allowed(path, data):
    assert check_file(path, '100644', data) == []


@pytest.mark.parametrize('path,mode,data', [
    ('execution/Work/fixture.rs', '100644', b'#[test] fn example() {}'),
    ('execution/Work/module.py', '100644', b'pass'),
    ('execution/Work/package.json', '100644', b'{}'),
    ('execution/Work/Cargo.toml', '100644', b'[package]'),
    ('execution/Work/runner', '100755', b'command'),
    ('execution/Work/runner', '100644', b'#!/bin/sh\ntrue'),
    ('execution/Work/library', '100644', b'\x7fELFcontent'),
])
def test_operational_source_or_entrypoints_are_rejected(path, mode, data):
    assert check_file(path, mode, data)


def test_documentation_exception_is_exact_and_still_non_executable():
    path = 'execution/Work/example.py'
    examples = frozenset({path})
    assert check_file(path, '100644', b'print(1)', examples=examples) == []
    assert check_file(path, '100755', b'print(1)', examples=examples)
    assert check_file('execution/Work/other.py', '100644', b'pass', examples=examples)
    assert check_file('execution/Work/example.py', '100644', b'pass', executable=True, examples=examples)


def test_tracked_inventory_rejects_code_and_missing_exceptions(tmp_path):
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    folder = tmp_path / 'execution/Work'
    folder.mkdir(parents=True)
    (folder / 'spec.md').write_text('# Spec')
    (folder / 'fixture.rs').write_text('fn example() {}')
    subprocess.run(['git', 'add', '.'], cwd=tmp_path, check=True)
    count, errors = check_repository(tmp_path)
    assert count == 2
    assert len(errors) == 1 and 'fixture.rs' in errors[0]
    _, errors = check_repository(tmp_path, examples=frozenset({'execution/Work/fixture.rs'}))
    assert not errors
    _, errors = check_repository(tmp_path, examples=frozenset({'execution/missing.py'}))
    assert any('not a tracked execution input' in error for error in errors)


def test_execution_symlink_cannot_hide_external_code(tmp_path):
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    (tmp_path / 'execution').mkdir()
    (tmp_path / 'tool.py').write_text('pass')
    (tmp_path / 'execution/spec.md').symlink_to(Path('../tool.py'))
    subprocess.run(['git', 'add', '.'], cwd=tmp_path, check=True)
    _, errors = check_repository(tmp_path)
    assert any('must not be symlinks' in error for error in errors)
