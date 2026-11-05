"""Preserve shared release checks without inventing a dependency subject."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
import check_release_readiness as readiness


def test_release_documents_remain_required_without_fixed_dependency_subject(tmp_path):
    documents = (
        "docs/BUILD_AND_RELEASE.md",
        "docs/RELEASE_NOTES_TEMPLATE.md",
        "docs/RELEASE_QUALITY_GATES.md",
        "docs/VALIDATION_STRATEGY.md",
        "docs/IP_AND_DATA_BOUNDARY.md",
        "docs/PROFESSIONAL_BOUNDARY.md",
    )
    assert readiness.check_required_paths(tmp_path) == list(documents)
    for name in documents:
        path = tmp_path / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("release document\n")
    # No fixed DAG or local-needs fixture is a release subject selected by this
    # helper. Their absence must not replace the actual document requirements.
    assert readiness.check_required_paths(tmp_path) == []
    (tmp_path / documents[3]).unlink()
    assert readiness.check_required_paths(tmp_path) == [documents[3]]


def test_profiles_retain_their_actual_checks_without_dependency_assessment(tmp_path):
    script_tests = (sys.executable, "-m", "pytest", "-q", "tests/test_release_readiness_script.py")
    python_tests = (sys.executable, "-m", "pytest", "-q", "tests")
    coordination_tests = (sys.executable, "-m", "pytest", "-q", "tools/coordination")
    security_tests = (sys.executable, "-m", "pytest", "-q", "tests/security")
    assert [step.command for step in readiness.build_plan("skeleton", tmp_path)] == [script_tests]
    assert [step.command for step in readiness.build_plan("python", tmp_path)] == [
        script_tests, python_tests, coordination_tests,
    ]
    assert [step.command for step in readiness.build_plan("security", tmp_path)] == [security_tests]
    assert [step.command for step in readiness.build_plan("all", tmp_path)] == [
        script_tests, python_tests, coordination_tests, security_tests,
    ]


def test_dry_run_plans_checks_without_claiming_dependency_readiness(tmp_path, capsys):
    for name in readiness.REQUIRED_PATHS:
        path = tmp_path / name
        path.parent.mkdir(exist_ok=True)
        path.touch()
    assert readiness.main(["--repo-root", str(tmp_path)]) == 0
    output = capsys.readouterr()
    assert "release readiness script tests" in output.out
    assert "planned checks: 1" in output.out
    assert output.err == ""
