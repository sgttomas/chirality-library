"""Exercise the current setup path without manufacturing lifecycle records."""
import concurrent.futures
import os
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

HERE = Path(__file__).resolve().parent
CHECK = HERE.parent / 'validation/check_min_viable_fileset.sh'


def run(tool, *args):
    return subprocess.run(['zsh', str(tool), '--current', *map(str, args)],
                          capture_output=True, text=True,
                          env=dict(os.environ, PYTHON=sys.executable))


def prepare(root):
    result = run(HERE/'scaffold_package.sh', root, 'PKG-01', 'Accepted package')
    assert result.returncode == 0, result.stderr
    result = run(HERE/'scaffold_deliverable.sh', root/'PKG-01',
                 'DEL-01-02_accepted-name', 'A name: with / source punctuation')
    assert result.returncode == 0, result.stderr
    return root/'PKG-01/DEL-01-02'


def scope(folder, **overrides):
    fields = dict(schema='chirality-deliverable-sow/v1', deliverable_id='DEL-01-02',
                  package_id='PKG-01')
    fields.update(overrides)
    (folder/'ScopeOfWork.md').write_text('---\n'+yaml.safe_dump(fields)+'---\n', encoding='utf-8')


def test_current_preparation_authoring_boundary_and_preservation(tmp_path):
    folder = prepare(tmp_path)
    assert {p.name for p in tmp_path.iterdir()} == {'PKG-01'}
    assert {p.name for p in folder.iterdir()} == {'Work', 'deliverable.yaml'}
    data = yaml.safe_load((folder/'deliverable.yaml').read_text())
    assert data == {'id': 'DEL-01-02', 'name': 'A name: with / source punctuation', 'needs': []}
    assert run(CHECK, '--prepared', folder, 'DEL-01-02_accepted-name').returncode == 0
    assert run(CHECK, folder).returncode == 1  # Production contract still absent.
    scope(folder)
    assert run(CHECK, folder, 'DEL-01-02').returncode == 0
    (folder/'Work/current.md').write_text('existing reasoning\n')
    data['needs'] = [{'from': 'unknown', 'condition': 'usable input for this case'}]
    (folder/'deliverable.yaml').write_text(yaml.safe_dump(data))
    before = {p.relative_to(folder): (p.read_bytes(), p.stat().st_mtime_ns)
              for p in folder.rglob('*') if p.is_file()}
    result = run(HERE/'scaffold_deliverable.sh', folder.parent, 'DEL-01-02', 'Other label')
    assert result.returncode == 0, result.stderr
    assert 'CREATED_PATH:' not in result.stdout
    assert before == {p.relative_to(folder): (p.read_bytes(), p.stat().st_mtime_ns)
                      for p in folder.rglob('*') if p.is_file()}
    assert not (folder/'_STATUS.md').exists()


@pytest.mark.parametrize('name', ['Work', 'deliverable.yaml', 'ScopeOfWork.md'])
def test_current_refuses_symlink_resources_without_writing_through_them(tmp_path, name):
    folder = prepare(tmp_path)
    external = tmp_path/'outside'
    if name == 'Work':
        external.mkdir()
        (folder/name).rmdir()
    else:
        external.write_text('id: DEL-01-02\nneeds: []\n')
        (folder/name).unlink(missing_ok=True)
    (folder/name).symlink_to(external, target_is_directory=name == 'Work')
    before = external.stat().st_mtime_ns
    result = run(HERE/'scaffold_deliverable.sh', folder.parent, 'DEL-01-02', 'Name')
    assert result.returncode != 0
    assert 'CREATED_PATH:' not in result.stdout
    assert external.stat().st_mtime_ns == before
    assert run(CHECK, '--prepared', folder).returncode != 0


@pytest.mark.parametrize('level', ['package', 'deliverable'])
def test_current_refuses_symlink_localities(tmp_path, level):
    outside = tmp_path/'outside'; outside.mkdir()
    if level == 'package':
        (tmp_path/'PKG-01').symlink_to(outside, target_is_directory=True)
        result = run(HERE/'scaffold_package.sh', tmp_path, 'PKG-01', 'Name')
    else:
        package = tmp_path/'PKG-01'; package.mkdir()
        (package/'DEL-01-02').symlink_to(outside, target_is_directory=True)
        result = run(HERE/'scaffold_deliverable.sh', package, 'DEL-01-02', 'Name')
        assert run(CHECK, '--prepared', package/'DEL-01-02').returncode != 0
    assert result.returncode != 0
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize('contents', ['', 'id: DEL-02-02\nneeds: []\n',
                                     'id: DEL-01-02\nid: DEL-01-02\nneeds: []\n',
                                     'id: DEL-01-02\nneeds: invalid\n'])
def test_current_rejects_conflicting_or_empty_existing_declaration(tmp_path, contents):
    package = tmp_path/'PKG-01'; folder=package/'DEL-01-02'; folder.mkdir(parents=True)
    (folder/'deliverable.yaml').write_text(contents)
    result = run(HERE/'scaffold_deliverable.sh', package, 'DEL-01-02', 'Name')
    assert result.returncode != 0
    assert (folder/'deliverable.yaml').read_text() == contents
    assert not (folder/'Work').exists()


@pytest.mark.parametrize('fields', [{'deliverable_id': 'DEL-01-03'},
                                  {'package_id': 'PKG-02'}, {'schema': 'other'}])
def test_current_checks_scope_identity_and_preserves_disagreement(tmp_path, fields):
    folder = prepare(tmp_path); scope(folder, **fields)
    before = (folder/'ScopeOfWork.md').read_bytes()
    assert run(CHECK, folder).returncode == 1
    assert run(HERE/'scaffold_deliverable.sh', folder.parent, 'DEL-01-02', 'Name').returncode != 0
    assert (folder/'ScopeOfWork.md').read_bytes() == before


def test_current_rejects_wrong_package_invalid_id_and_unsupported_options(tmp_path):
    package = tmp_path/'PKG-01'; package.mkdir()
    for identity in ['DEL-02-01', '../../outside', 'KTY-01-01']:
        assert run(HERE/'scaffold_deliverable.sh', package, identity, 'Name').returncode != 0
    assert run(HERE/'scaffold_deliverable.sh', package, 'DEL-01-02', 'Name', '--memory').returncode != 0
    assert not list(package.iterdir())
    assert run(HERE/'scaffold_package.sh', tmp_path, '../outside', 'Name').returncode != 0


def test_current_concurrent_preparation_is_idempotent(tmp_path):
    package = tmp_path/'PKG-01'; package.mkdir()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: run(HERE/'scaffold_deliverable.sh', package,
                                             'DEL-01-02', 'Name'), range(2)))
    assert all(r.returncode == 0 for r in results), [(r.stdout,r.stderr) for r in results]
    folder=package/'DEL-01-02'
    assert run(CHECK, '--prepared', folder, 'DEL-01-02').returncode == 0
    assert run(CHECK, '--prepared', folder, 'DEL-01-03').returncode == 1
    assert {p.name for p in folder.iterdir()} == {'Work', 'deliverable.yaml'}


def test_current_authored_contract_uses_real_validator_without_status(tmp_path):
    folder = prepare(tmp_path)
    text = '''---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-02
package_id: PKG-01
decomposition_basis: execution/_Decomposition/fixture.md@abc123
project_scope_refs: [SOW-001]
package_objective_refs: [OBJ-001]
---
# A current contract fixture

## Purpose and Objective Traceability
Test the current authoring and verification path.

## Deliverable Definition — Ontology
- **OUT-001** — A source-grounded fixture supporting SOW-001 and OBJ-001.

## Completion and Reliance Basis — Epistemology
- **AC-001** — The fixture has a usable declared result.

## Production and Verification Method — Praxeology
- **VER-001** — Inspect the fixture result and its declared sources.

## Governing Values and Decisions — Axiology
This synthetic case asserts no human acceptance or production readiness.

## Output and Evaluation Matrix
| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001, OBJ-001 | OUT-001 | AC-001 | VER-001 | Inspectable result |
'''
    (folder/'ScopeOfWork.md').write_text(text)
    assert run(CHECK, folder, 'DEL-01-02').returncode == 0
    validator = HERE.parent/'scope_of_work/validate_scope_of_work.py'
    result = subprocess.run([sys.executable, str(validator), str(folder), '--json'],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert not (folder/'_STATUS.md').exists()
    assert {p.name for p in folder.iterdir()} == {'ScopeOfWork.md','Work','deliverable.yaml'}
