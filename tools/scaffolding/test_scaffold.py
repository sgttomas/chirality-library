import os
from pathlib import Path
import subprocess
import sys

import pytest

from tools.deliverables.cli import parse

HERE=Path(__file__).resolve().parent


def test_created_manifest_and_no_overwrite(tmp_path):
    args=['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'DEL-01-01','Test','--memory']
    first=subprocess.run(args,text=True,capture_output=True,check=True)
    created=[line.split(': ',1)[1] for line in first.stdout.splitlines() if line.startswith('CREATED_PATH:')]
    assert len(created)==7
    created=[p for p in created if Path(p).is_file()]
    assert len(created)==6
    assert (tmp_path/"DEL-01-01_Test"/"MEMORY.md").is_file()
    assert not (tmp_path/"DEL-01-01_Test"/"_MEMORY.md").exists()
    assert parse((tmp_path/'DEL-01-01_Test/deliverable.yaml').read_text(), 'scaffold') == {'id': 'DEL-01-01', 'needs': []}
    assert not (tmp_path/'DEL-01-01_Test/_DEPENDENCIES.md').exists()
    assert not (tmp_path/'DEL-01-01_Test/Dependencies.csv').exists()
    assert all(Path(p).is_file() for p in created)
    for p in created:Path(p).write_text('human content')
    second=subprocess.run(args,text=True,capture_output=True,check=True)
    assert 'CREATED_PATH:' not in second.stdout
    assert all(Path(p).read_text()=='human content' for p in created)


def _check(folder, accepted_id=None):
    args = ['zsh', str(HERE.parent/'validation/check_min_viable_fileset.sh'), str(folder)]
    if accepted_id:
        args.append(accepted_id)
    return subprocess.run(args, text=True, capture_output=True,
                          env=dict(os.environ, PYTHON=sys.executable))


def test_existing_dependency_artifacts_and_empty_metadata_are_preserved(tmp_path):
    folder = tmp_path/'DEL-123-02_Kept'
    folder.mkdir()
    for name, content in {'_CONTEXT.md': '', '_DEPENDENCIES.md': 'original', 'Dependencies.csv': 'original csv'}.items():
        (folder/name).write_text(content)
    before = {path.name: path.read_bytes() for path in folder.iterdir()}
    result = subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), 'DEL-123-02', 'Kept'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    assert all((folder/name).read_bytes() == content for name, content in before.items())
    assert _check(folder, 'DEL-123-02').returncode == 0


@pytest.mark.parametrize('identity', ['DEL-01-01', 'DEL-123-02', 'DEL-12-03_Accepted-suffix'])
def test_native_scaffold_and_identity_binding(tmp_path, identity):
    result = subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), identity, 'Test'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    folder = tmp_path/f'{identity}_Test'
    assert _check(folder, identity).returncode == 0
    assert _check(folder, 'DEL-99-99').returncode == 1
    (folder/'deliverable.yaml').write_text('id: DEL-99-99\nneeds: []\n')
    mismatch = _check(folder, identity)
    assert mismatch.returncode == 1
    assert 'owning deliverable folder' in mismatch.stdout


@pytest.mark.parametrize('contents', ['id: DEL-01-01\nneeds: invalid\n', 'id: DEL-01-01\nid: DEL-01-01\nneeds: []\n', 'id: DEL-01-01\nneeds:\n - from: unknown\n   condition: ""\n'])
def test_min_fileset_rejects_malformed_native_needs(tmp_path, contents):
    subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), 'DEL-01-01', 'Test'], check=True, capture_output=True)
    folder = tmp_path/'DEL-01-01_Test'
    (folder/'deliverable.yaml').write_text(contents)
    assert _check(folder).returncode == 1


def test_scope_identity_is_checked_without_requiring_production_completion(tmp_path):
    subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), 'DEL-01-01', 'Test'], check=True, capture_output=True)
    folder = tmp_path/'DEL-01-01_Test'
    assert _check(folder).returncode == 0  # Scaffold has no production contract yet.
    (folder/'ScopeOfWork.md').write_text('---\ndeliverable_id: DEL-01-01\n---\n')
    assert _check(folder).returncode == 0  # Only identity is assessed here.
    (folder/'ScopeOfWork.md').write_text('---\ndeliverable_id: DEL-02-01\n---\n')
    mismatch = _check(folder)
    assert mismatch.returncode == 1
    assert 'ScopeOfWork.md deliverable_id' in mismatch.stdout


@pytest.mark.parametrize('name,contents', [
    ('deliverable.yaml', 'id: DEL-01-01\nneeds: []\n'),
    ('ScopeOfWork.md', '---\ndeliverable_id: DEL-01-01\n---\n'),
])
def test_min_fileset_rejects_external_identity_symlinks(tmp_path, name, contents):
    subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), 'DEL-01-01', 'Test'], check=True, capture_output=True)
    folder = tmp_path/'DEL-01-01_Test'
    external = tmp_path/'external_identity'
    external.write_text(contents)
    identity_source = folder/name
    if identity_source.exists():
        identity_source.unlink()
    identity_source.symlink_to(external)
    result = _check(folder, 'DEL-01-01')
    assert result.returncode == 1
    assert 'identity source must be a contained regular file' in result.stdout
    assert external.read_text() == contents


def test_kty_scaffold_keeps_metadata_without_fabricating_dependency_schema(tmp_path):
    result = subprocess.run(['zsh', str(HERE/'scaffold_deliverable.sh'), str(tmp_path), 'KTY-01-01', 'Test'], text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    folder = tmp_path/'KTY-01-01_Test'
    assert {path.name for path in folder.iterdir()} == {'_CONTEXT.md', '_STATUS.md', '_REFERENCES.md', '_SEMANTIC.md'}
    assert _check(folder).returncode == 0


def test_package_rerun_and_path_boundary(tmp_path):
    args=['zsh',str(HERE/'scaffold_package.sh'),str(tmp_path),'PKG-01','Test']
    assert subprocess.run(args,text=True,capture_output=True).returncode==0
    assert 'CREATED_PATH:' not in subprocess.run(args,text=True,capture_output=True).stdout
    bad=['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'../../outside','Test']
    assert subprocess.run(bad,capture_output=True).returncode==2


def test_native_scaffold_rejects_directory_symlink_escaping_working_root(tmp_path):
    working = tmp_path/'working'
    outside = tmp_path/'outside'
    working.mkdir()
    outside.mkdir()
    retained = outside/'retained.md'
    retained.write_bytes(b'unchanged outside source\n')
    (working/'DEL-01-01_Test').symlink_to(outside, target_is_directory=True)
    result = subprocess.run(
        ['zsh', str(HERE/'scaffold_deliverable.sh'), str(working), 'DEL-01-01', 'Test'],
        text=True, capture_output=True,
    )
    assert result.returncode == 2
    assert 'outside the supplied working root' in result.stderr
    assert 'CREATED_PATH:' not in result.stdout
    assert {path.name: path.read_bytes() for path in outside.iterdir()} == {
        'retained.md': b'unchanged outside source\n',
    }


@pytest.mark.parametrize('relative_target', ['.', 'retained'])
def test_native_scaffold_keeps_in_root_directory_symlink_behavior(tmp_path, relative_target):
    working = tmp_path/'working'
    working.mkdir()
    target = working/relative_target
    target.mkdir(exist_ok=True)
    retained = target/'retained.md'
    retained.write_bytes(b'unchanged in-root source\n')
    (working/'DEL-01-01_Test').symlink_to(target, target_is_directory=True)
    result = subprocess.run(
        ['zsh', str(HERE/'scaffold_deliverable.sh'), str(working), 'DEL-01-01', 'Test'],
        text=True, capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert retained.read_bytes() == b'unchanged in-root source\n'
    assert parse((target/'deliverable.yaml').read_text(), 'scaffold') == {'id': 'DEL-01-01', 'needs': []}


def test_legacy_memory_requires_explicit_consolidation(tmp_path):
    target=tmp_path/'DEL-01-01_Test'
    target.mkdir()
    legacy=target/'_MEMORY.md'
    legacy.write_text('retained human context')
    result=subprocess.run(['zsh',str(HERE/'scaffold_deliverable.sh'),str(tmp_path),'DEL-01-01','Test','--memory'],text=True,capture_output=True)
    assert result.returncode==2
    assert legacy.read_text()=='retained human context'
    assert not (target/'MEMORY.md').exists()
    assert set(target.iterdir())=={legacy}


def _snapshot(tmp_path, root):
    # Pin `date` so runs land in the same minute deterministically.
    stub=tmp_path/'bin'
    stub.mkdir(exist_ok=True)
    (stub/'date').write_text('#!/bin/sh\necho 2026-01-01_1200\n')
    (stub/'date').chmod(0o755)
    env=dict(os.environ,PATH=f"{stub}{os.pathsep}{os.environ['PATH']}")
    return subprocess.run(['zsh',str(HERE/'create_snapshot_folder.sh'),str(root),'REV','DEL-01-01'],text=True,capture_output=True,env=env)


def test_snapshot_folder_is_never_reused(tmp_path):
    root=tmp_path/'_Reviews'
    first=_snapshot(tmp_path,root)
    assert first.returncode==0
    assert first.stdout.strip()==f"{root}/REV_DEL-01-01_2026-01-01_1200"
    (Path(first.stdout.strip())/'Decision_Log.md').write_text('frozen')
    second=_snapshot(tmp_path,root)
    assert second.returncode==0
    assert second.stdout.strip()==f"{root}/REV_DEL-01-01_2026-01-01_1200_02"
    assert list(Path(second.stdout.strip()).iterdir())==[]
    assert (Path(first.stdout.strip())/'Decision_Log.md').read_text()=='frozen'


def test_snapshot_folder_fails_rather_than_reuse(tmp_path):
    root=tmp_path/'_Reviews'
    base=root/'REV_DEL-01-01_2026-01-01_1200'
    base.mkdir(parents=True)
    for n in range(2,100):
        Path(f"{base}_{n:02d}").mkdir()
    result=_snapshot(tmp_path,root)
    assert result.returncode==1
    assert result.stdout==''
    assert 'refusing to reuse' in result.stderr
