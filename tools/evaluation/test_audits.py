"""Native dependency observations and unchanged structure/lifecycle contracts."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from audit_common import sow
from audit_dependencies import audit as dependencies, main as dependency_main
from audit_structure import audit as structure, CONTRACT


@pytest.fixture
def native_project(tmp_path, monkeypatch):
    """Exercise the real native CLI with deterministic Git facts; make no commits."""
    repo = tmp_path / "repo"
    project = repo / "project"
    project.mkdir(parents=True)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    git = bin_dir / "git"
    git.write_text(f"""#!{sys.executable}
import os
import sys
args = sys.argv[1:]
if args == ['rev-parse', '--show-toplevel']:
    print({str(repo)!r})
elif args == ['rev-parse', '--verify', '--end-of-options', 'HEAD^{{commit}}']:
    if os.environ.get('AUDIT_FIXTURE_NO_HEAD'):
        print('HEAD does not resolve to a commit', file=sys.stderr)
        sys.exit(128)
    print('a' * 40)
elif args[:3] == ['status', '--porcelain=v1', '--untracked-files=all']:
    pass
else:
    print('unexpected fixture git command: ' + repr(args), file=sys.stderr)
    sys.exit(128)
""")
    git.chmod(0o755)
    monkeypatch.setenv("PATH", f"{bin_dir}{os.pathsep}{os.environ['PATH']}")
    return project


def put(project, identifier, needs=(), **fields):
    package = "PKG-" + identifier.split("-")[1]
    path = project / "execution" / package / identifier / "deliverable.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(dict(id=identifier, needs=list(needs), **fields)))
    return path


def test_native_query_preserves_cases_unknowns_outputs_and_cycle_limits(native_project):
    (native_project / "basis.md").write_text("presence does not establish suitability")
    source = put(native_project, "DEL-01-01", [
        {"from": "DEL-01-02", "condition": "case A interface"},
        {"from": "DEL-01-02", "condition": "case B rating", "gating": False, "when": "actual material finding"},
        {"from": "DEL-99-99", "condition": "future native input"},
        {"from": "doc:basis.md", "condition": "qualified design basis", "evidence": "basis.md::section"},
        {"from": "doc:missing.md", "condition": "future document"},
        {"from": "external:recipient", "condition": "send actual output", "direction": "downstream", "gating": False},
        {"from": "unknown", "condition": "source binding unresolved"},
    ], code_paths=["basis.md"], checks=["planned-check.py"])
    put(native_project, "DEL-01-02", [{"from": "DEL-01-01", "condition": "reciprocal use", "gating": False}])
    # Obsolete companions must not be read, parsed, or treated as graph inputs.
    source.with_name("Dependencies.csv").write_text('"malformed CSV')
    source.with_name("_DEPENDENCIES.md").write_text("DEL-88-88 blocks everything")
    result = dependencies(native_project)
    assert result["run_status"] == "COMPLETE" and result["subject_status"] == "PASS"
    assert result["summary"] == {"deliverables": 2, "needs": 8, "unknown_references": 4, "native_cycle_components": 1}
    query = result["query"]
    assert query["basis"]["revision"] == "a" * 40
    assert query["basis"]["project"] == "project"
    assert query["cycles"] == [["DEL-01-01", "DEL-01-02"]]
    assert all(row["suitability"] == "unknown" for row in query["needs"])
    assert [row["condition"] for row in query["needs"][:2]] == ["case A interface", "case B rating"]
    assert query["needs"][1]["when"] == "actual material finding"
    assert query["needs"][3]["supplier"]["state"] == "observed"
    assert "no check executed" in query["needs"][3]["evidence_fact"]["meaning"]
    assert query["needs"][5]["direction"] == "downstream"
    assert query["references"]["DEL-01-01"]["checks"][0]["state"] == "unknown"


def test_invalid_native_metadata_reports_partial_structure_without_false_run_failure(native_project, tmp_path):
    put(native_project, "DEL-01-01")
    bad = put(native_project, "DEL-01-02")
    bad.write_text("id: DEL-01-02\nneeds: []\nneeds: []\n")
    report = dependencies(native_project)
    assert report["run_status"] == "COMPLETE" and report["subject_status"] == "FAIL"
    assert "duplicate or non-string YAML key" in report["issues"][0]
    assert report["summary"]["deliverables"] == 1
    output = tmp_path / "report.json"
    assert dependency_main(["--project", str(native_project), "--output", str(output)]) == 0
    assert json.loads(output.read_text())["subject_status"] == "FAIL"


def test_empty_native_scope_is_explicit_not_assessed(native_project):
    report = dependencies(native_project)
    assert report["run_status"] == "COMPLETE" and report["subject_status"] == "NOT_ASSESSED"
    assert report["query"]["state"] == "unknown"
    assert report["query"]["reason"] == "no deliverable metadata found"
    assert report["summary"]["deliverables"] == 0


def test_missing_git_head_and_missing_project_fail_inputs(native_project, monkeypatch, tmp_path):
    put(native_project, "DEL-01-01")
    monkeypatch.setenv("AUDIT_FIXTURE_NO_HEAD", "1")
    report = dependencies(native_project)
    assert report["run_status"] == "FAILED_INPUTS" and report["subject_status"] == "NOT_ASSESSED"
    assert "HEAD does not resolve" in report["issues"][0]
    assert "summary" not in report
    output = tmp_path / "report.json"
    assert dependency_main(["--project", str(native_project), "--output", str(output)]) == 2
    assert dependency_main(["--project", str(tmp_path / "absent"), "--output", str(output)]) == 2
    assert "not a directory" in json.loads(output.read_text())["issues"][0]


def make_workspace(root, state="RETIRED"):
    unit = root / "PKG-01_A/1_Working/DEL-01-01_Item"
    unit.mkdir(parents=True)
    for name in ("_CONTEXT.md", "_REFERENCES.md"):
        (unit / name).touch()
    (unit / "deliverable.yaml").write_text("id: DEL-01-01\nneeds: []\n")
    (unit / "_STATUS.md").write_text(f"# History\nOPEN happened before.\n\n**Current State:** `{state}`\n")
    for name in CONTRACT["partition_directories"]:
        (unit.parent.parent / name).mkdir(exist_ok=True)
    for name in CONTRACT["tool_roots"]:
        (root / name).mkdir(exist_ok=True)
    return unit


def test_retired_state_not_history_and_initialized_missing(tmp_path):
    unit = make_workspace(tmp_path)
    result = structure(tmp_path, "SOFTWARE")
    assert result["subject_status"] == "PASS"
    assert result["units"][0]["current_state"] == "RETIRED"
    (unit / "_STATUS.md").write_text("Current State: INITIALIZED\nHistory OPEN\n")
    result = structure(tmp_path, "SOFTWARE")
    assert result["run_status"] == "COMPLETE" and result["subject_status"] == "FAIL"
    assert result["summary"]["production_formats"] == {"INVALID": 1}


def test_legacy_and_dual_production_formats(tmp_path):
    unit = make_workspace(tmp_path, "INITIALIZED")
    for name in sow.LEGACY_FILES:
        (unit / name).touch()
    assert structure(tmp_path, "PROJECT")["units"][0]["production_format"]["state"] == "LEGACY_FOUR_DOC"
    # Use the actual canonical SOW schema, including matrix and authority marker.
    text = "---\nschema: chirality-deliverable-sow/v1\ndeliverable_id: DEL-01-01\npackage_id: PKG-01\ndecomposition_basis: source@abc\nproject_scope_refs: [S-1]\npackage_objective_refs: [O-1]\n---\n"
    for heading in sow.REQUIRED_HEADINGS:
        text += f"## {heading}\n"
        if heading == "Deliverable Definition — Ontology":
            text += "### OUT-001 — Output\n"
        if heading == "Completion and Reliance Basis — Epistemology":
            text += "### AC-001 — Acceptance\n"
        if heading == "Output and Evaluation Matrix":
            text += "| " + " | ".join(sow.MATRIX_COLUMNS) + " |\n| OUT-001 | S-1 | | AC-001 | HUMAN_REVIEW: owner | proof |\n"
    text += sow.migration_marker(sow.MIGRATION_AUTHORITY) + "\n"
    (unit / "ScopeOfWork.md").write_text(text)
    assert structure(tmp_path, "PROJECT")["units"][0]["production_format"]["state"] == "AMBIGUOUS"
    result = structure(tmp_path, "PROJECT", isolated_migration=True, migration_authority=sow.MIGRATION_AUTHORITY)
    assert result["units"][0]["production_format"]["state"] == "MIGRATION_DUAL"
    assert not result["units"][0]["production_format"]["accepted_baseline"]
    for name in sow.LEGACY_FILES:
        (unit / name).unlink()
    assert structure(tmp_path, "PROJECT")["units"][0]["production_format"]["state"] == "SOW_V1"


def test_explicit_inventory_includes_missing_and_domain(tmp_path):
    manifest = tmp_path / "inventory.json"
    manifest.write_text(json.dumps({"schema_version": 1, "units": [{"path": "CAT-01_A/1_Working/KTY-01-01_B", "required_files": ["Reference.md"]}]}))
    report = structure(tmp_path, "DOMAIN", manifest)
    assert report["summary"]["units"] == 1
    assert report["units"][0]["production_format"]["state"] == "NOT_APPLICABLE"
    assert "missing required file: Reference.md" in report["units"][0]["issues"]
    assert "_DEPENDENCIES.md" not in report["units"][0]["files"]
    assert "Dependencies.csv" not in report["units"][0]["files"]
    assert "deliverable.yaml" not in report["units"][0]["files"]


def test_structure_requires_native_del_metadata_without_legacy_guard(tmp_path):
    unit = make_workspace(tmp_path)
    assert structure(tmp_path, "PROJECT")["subject_status"] == "PASS"
    (unit / "deliverable.yaml").unlink()
    (unit / "_DEPENDENCIES.md").touch()
    result = structure(tmp_path, "PROJECT")
    assert "missing required file: deliverable.yaml" in result["units"][0]["issues"]
    assert "_DEPENDENCIES.md" not in result["units"][0]["files"]
    # Flat native declarations elsewhere no longer reject structure inspection.
    native = tmp_path / "PKG-02/DEL-02-01/deliverable.yaml"
    native.parent.mkdir(parents=True)
    native.write_text("id: DEL-02-01\nneeds: []\n")
    assert structure(tmp_path, "PROJECT")["run_status"] == "COMPLETE"


def test_cli_arbitrary_cwd_and_flat_source_protection(native_project, tmp_path):
    source = put(native_project, "DEL-01-01")
    before = source.read_bytes()
    script = Path(__file__).with_name("audit_dependencies.py")
    output = tmp_path / "report.json"
    run = subprocess.run([sys.executable, str(script), "--project", str(native_project), "--output", str(output)], cwd="/", capture_output=True)
    assert run.returncode == 0, run.stderr
    assert json.loads(output.read_text())["subject_status"] == "PASS"
    for destination in (source, source.parent / "Design/review.json"):
        blocked = subprocess.run([sys.executable, str(script), "--project", str(native_project), "--output", str(destination)], capture_output=True)
        assert blocked.returncode == 2 and source.read_bytes() == before
        assert b"outside production-unit source paths" in blocked.stderr
    assert not (source.parent / "Design").exists()


@pytest.mark.parametrize('suffix', ['', '_Report', '-Report'])
def test_report_cannot_overwrite_source_in_supported_native_locality(native_project, suffix, capsys):
    folder = native_project/'execution/PKG-01'/f'DEL-01-01{suffix}'
    folder.mkdir(parents=True)
    declaration = folder/'deliverable.yaml'
    declaration.write_text('id: DEL-01-01\nneeds: []\n')
    source = folder/'Design/input.md'
    source.parent.mkdir()
    source.write_bytes(b'preserved native source\n')
    before = declaration.read_bytes(), source.read_bytes()
    # The locality is accepted by the actual native loader before testing the
    # report destination boundary; a failed-input query cannot mask the probe.
    observed = dependencies(native_project)
    assert observed['subject_status'] == 'PASS'
    assert observed['summary']['deliverables'] == 1
    assert dependency_main(['--project', str(native_project), '--output', str(source)]) == 2
    assert 'outside production-unit source paths' in capsys.readouterr().err
    assert (declaration.read_bytes(), source.read_bytes()) == before


def test_report_cannot_hide_locality_ownership_through_source_symlink(native_project, tmp_path, capsys):
    declaration = put(native_project, 'DEL-01-01')
    design = declaration.parent/'Design'
    design.mkdir()
    external = tmp_path/'input.md'
    external.write_bytes(b'preserved linked source\n')
    destination = design/'input.md'
    destination.symlink_to(external)
    assert dependencies(native_project)['subject_status'] == 'PASS'
    assert dependency_main(['--project', str(native_project), '--output', str(destination)]) == 2
    assert 'outside production-unit source paths' in capsys.readouterr().err
    assert external.read_bytes() == b'preserved linked source\n'


def test_inventory_scans_all_lifecycle_folders(tmp_path):
    from audit_common import inventory
    make_workspace(tmp_path)
    for folder, number in (("2_Checking", 2), ("3_Issued", 3), ("0_References", 4)):
        (tmp_path / f"PKG-01_A/{folder}/DEL-01-{number:02d}_Item").mkdir(parents=True)
    (tmp_path / "PKG-01_A/1_Working/_Archive/DEL-01-05_Old").mkdir(parents=True)
    found = [path.relative_to(tmp_path).as_posix() for path in inventory(tmp_path)]
    assert found == ["PKG-01_A/1_Working/DEL-01-01_Item", "PKG-01_A/2_Checking/DEL-01-02_Item", "PKG-01_A/3_Issued/DEL-01-03_Item"]
