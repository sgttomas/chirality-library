#!/usr/bin/env python3
"""Drift guards for the tools/ test-routing profile.

PRs run selected checks; manual dispatch runs the full estate. A stale
profile could let a PR skip a suite it should have run. These tests pin it to
reality: every test-bearing tools/ directory must be routed, every rule
must reference real checks, and the selector + runner must agree with
the profile.
"""
from __future__ import annotations

import json
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

from software_workflow_common import matches_rule

REPO_ROOT = Path(__file__).resolve().parents[2]
PROFILE_PATH = REPO_ROOT / "tools" / "tools-test-routing.json"
RUNNER = REPO_ROOT / "tools" / "run_affected_tests.py"


def load_runner():
    spec = importlib.util.spec_from_file_location("chirality_run_affected_tests", RUNNER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_profile() -> dict:
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def _test_bearing_dirs() -> set[str]:
    return {
        f"tools/{path.parent.name}"
        for path in (REPO_ROOT / "tools").glob("*/test_*.py")
    }


def test_profile_schema_loads_via_ratified_loader():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        from software_workflow_common import load_profile as ratified_load
    finally:
        sys.path.pop(0)
    project_root, data = ratified_load(PROFILE_PATH)
    assert project_root == REPO_ROOT
    assert data["always_checks"] == []


def test_every_test_bearing_dir_is_routed():
    profile = load_profile()
    covered_dirs = {
        pytest_path
        for check in profile["checks"].values()
        for pytest_path in check["pytest_paths"]
    }
    missing = _test_bearing_dirs() - covered_dirs
    assert not missing, (
        f"test-bearing dirs absent from the routing profile: {sorted(missing)} "
        "— add a check + path_rule to tools/tools-test-routing.json"
    )


def test_every_routed_check_dir_exists_and_bears_tests():
    profile = load_profile()
    for check_id, check in profile["checks"].items():
        for pytest_path in check["pytest_paths"]:
            directory = REPO_ROOT / pytest_path
            assert directory.is_dir(), f"{check_id}: {pytest_path} missing"
            assert list(directory.glob("test_*.py")), (
                f"{check_id}: {pytest_path} contains no test files"
            )


def test_every_non_always_check_is_reachable_by_some_rule():
    # software_workflow itself has no dedicated rule by design: its dir is
    # routing infrastructure, covered by the force-everything rule.
    profile = load_profile()
    always = set(profile["always_checks"])
    assert always <= set(profile["checks"])
    reachable: set[str] = set()
    for rule in profile["path_rules"]:
        reachable.update(rule["checks"])
    unrouted = set(profile["checks"]) - always - reachable
    assert not unrouted, (
        f"checks with neither always status nor any path rule: "
        f"{sorted(unrouted)}"
    )


def test_rules_reference_only_known_checks():
    profile = load_profile()
    known = set(profile["checks"])
    for rule in profile["path_rules"]:
        unknown = set(rule["checks"]) - known
        assert not unknown, f"rule {rule['paths']} references {sorted(unknown)}"


def _dry_run(*args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--dry-run", *args],
        capture_output=True, text=True, check=True, cwd=REPO_ROOT,
    )
    # Selection JSON is the only multi-line JSON object on stdout; it is
    # printed before the [run-affected] summary line.
    payload = result.stdout[result.stdout.index("{"):result.stdout.rindex("}") + 1]
    return json.loads(payload)


def test_runner_isolated_change_selects_owner():
    selection = _dry_run("--paths", "tools/pdf2md/render_table_xlsx.py")
    assert set(selection["checks"]) == {
        "pdf2md",
    }


def test_document_headers_select_validation():
    selection = _dry_run("--paths", "docs/SOME_DOC.md")
    assert selection["checks"] == ['validation']


def test_runner_routing_infrastructure_change_selects_everything():
    profile = load_profile()
    for trigger in ("tools/tools-test-routing.json",
                    "tools/run_affected_tests.py",
                    ".github/workflows/governance-harness.yml",
                    "pyproject.toml",
                    "tools/validation/conftest.py"):
        selection = _dry_run("--paths", trigger)
        assert set(selection["checks"]) == set(profile["checks"]), trigger


def test_runner_all_flag_covers_the_full_estate():
    selection = _dry_run("--all")
    assert set(selection["checks"]) == set(load_profile()["checks"])


def test_runner_streams_path_sets_larger_than_linux_argmax():
    runner = load_runner()
    paths = [f"domains/demo/deep/path/file-{index:05d}.md" for index in range(40_000)]
    selection = runner.select_checks(paths)
    assert selection["paths"] == paths
    assert set(selection["checks"]) == set(load_profile()["checks"])


def test_no_selected_suites_does_not_invoke_pytest(monkeypatch):
    runner = load_runner()
    def forbidden(*args, **kwargs):
        raise AssertionError('No selection must not run pytest on the whole repository')
    monkeypatch.setattr(runner.subprocess, 'run', forbidden)
    assert runner.run_pytest([]) == 0


@pytest.mark.parametrize('path', [
    'tools/new-tool/implementation.py', 'new-code/implementation.py',
    '.github/workflows/new-workflow.yml', 'new-prose/unknown.md',
    'docs/new-contract.json',
    'execution/new-input.bin',
])
def test_unknown_input_anywhere_selects_full_coverage(path):
    selection = _dry_run('--paths', path)
    assert set(selection['checks']) == set(load_profile()['checks'])
    assert set(selection['repository_checks']) == {'instructions', 'deliverables'}
    assert selection['reasons']['unknown-inputs'] == [path]
    assert all(load_runner().workflow_outputs(selection).values())


def test_dependency_edits_select_structure_check_without_product_tests(tmp_path, monkeypatch):
    output = tmp_path / 'outputs'
    monkeypatch.setenv('GITHUB_OUTPUT', str(output))
    for path, expected in [
        ('projects/chirality-app-v4/execution/PKG-01/DEL-01-01/deliverable.yaml', True),
        ('README.md', False),
        ('tools/deliverables/cli.py', True),
    ]:
        output.write_text('')
        subprocess.run([sys.executable, str(RUNNER), '--dry-run', '--paths', path],
                       cwd=REPO_ROOT, check=True, capture_output=True)
        assert f"deliverables={str(expected).lower()}" in output.read_text()


def test_every_tracked_path_has_a_deliberate_classification():
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=REPO_ROOT, text=True).split('\0')
    profile = load_profile()
    missing = [p for p in paths if p and not any(matches_rule(p, r) for r in profile['path_rules'])]
    assert not missing, f'Classify tracked inputs in tools/tools-test-routing.json: {missing}'


def test_pr15_documentation_replay_keeps_consumers_without_code_suites():
    # Exact changed paths of PR #15, head 60ae6f6900f7ff8298c78f9ddbe4f98f74442500.
    selection = _dry_run('--paths',
        'AGENTS.md', 'README.md', 'agents/AGENT_INTERLOCUTOR.md', 'loop/LOOP_INIT.md',
        'tools/deliverables/README.md', 'tools/evaluation/README.md',
        'workflows/create-workflow/WORKFLOW.md', 'workflows/evaluation-protocol/WORKFLOW.md',
        'workflows/integrated-engineering-estimate-schedule/WORKFLOW.md',
        'workflows/project-setup/resources/current-project.md',
        'workflows/reflect-on-work/WORKFLOW.md', 'workflows/review/WORKFLOW.md')
    assert set(selection['checks']) == {'validation', 'workflow_runtime'}
    assert selection['repository_checks'] == ['instructions']
    assert not load_runner().workflow_outputs(selection)['needs_zsh']


@pytest.mark.parametrize('path,checks,contracts', [
    ('tools/software_workflow/README.md', {'validation'}, set()),
    ('docs/document-metadata.schema.json', {'validation'}, set()),
    ('init/init-prompt.md', {'validation'}, set()),
    ('loop/LOOP_INIT.md', {'validation'}, set()),
    ('.agents/skills/researcher/SKILL.md', {'validation', 'workflow_runtime'}, {'instructions'}),
    ('.agents/skills/researcher/execution.json', {'validation', 'workflow_runtime'}, {'instructions'}),
    ('docs/alignment-manual/render_manual.py', {'publication'}, set()),
    ('docs/alignment-manual/requirements.txt', {'publication'}, set()),
    ('tools/evaluation/audit_dependencies.py', {'evaluation'}, set()),
    ('README.md', set(), set()),
])
def test_isolated_consumed_inputs_select_their_checks(path, checks, contracts):
    selection = _dry_run('--paths', path)
    assert set(selection['checks']) == checks
    assert set(selection['repository_checks']) == contracts
    assert selection['unmatched_paths'] == []


def test_guide_exception_does_not_swallow_code_in_a_mixed_change():
    selection = _dry_run('--paths', 'tools/software_workflow/README.md',
                         'tools/software_workflow/select_affected_checks.py')
    assert set(selection['checks']) == set(load_profile()['checks'])
    assert set(selection['repository_checks']) == {'instructions', 'deliverables'}


def test_unavailable_diff_and_manual_dispatch_select_all_standalone_checks():
    for args in [('--base', 'missing-ci-base-ref'), ('--all',)]:
        selection = _dry_run(*args)
        assert set(selection['checks']) == set(load_profile()['checks'])
        assert all(load_runner().workflow_outputs(selection).values())


@pytest.mark.parametrize('path,needs_zsh,manual', [
    ('tools/scaffolding/write_status.sh', True, False),
    ('tools/validation/validate_id_format.sh', False, False),
    ('docs/alignment-manual/render_manual.py', False, True),
    ('tools/deliverables/README.md', False, False),
])
def test_environment_requirements_follow_the_selected_tests(path, needs_zsh, manual):
    outputs = load_runner().workflow_outputs(_dry_run('--paths', path))
    assert outputs['needs_zsh'] is needs_zsh
    assert outputs['manual'] is manual


def test_emitted_workflow_outputs_include_unknown_path_safeguards(tmp_path, monkeypatch):
    output = tmp_path / 'outputs'
    monkeypatch.setenv('GITHUB_OUTPUT', str(output))
    _dry_run('--paths', 'new-code/unknown.py')
    assert dict(line.split('=') for line in output.read_text().splitlines()) == {
        'has_tests': 'true', 'instructions': 'true', 'deliverables': 'true',
        'needs_zsh': 'true', 'manual': 'true',
        'pdf': 'true',
    }


@pytest.mark.parametrize('path,checks', [
    ('tools/scope_of_work/common.py', {'scope_of_work', 'validation', 'reporting', 'evaluation', 'scaffolding'}),
    ('tools/scope_of_work/id_catalog.json', {'scope_of_work', 'validation', 'reporting', 'evaluation', 'scaffolding'}),
    ('tools/scope_of_work/validate_scope_of_work.py', {'scope_of_work', 'scaffolding'}),
    ('tools/validation/check_min_viable_fileset.sh', {'validation', 'scaffolding'}),
    ('tools/source_catalog/research_packet.py', {'source_catalog', 'retrieval'}),
    ('tools/source_catalog/source_database.py', {'source_catalog', 'retrieval'}),
    ('tools/deliverables/cli.py', {'deliverables', 'scaffolding', 'evaluation'}),
    ('tools/deliverables/graph.py', {'deliverables', 'scaffolding', 'evaluation'}),
    ('workflows/dbm-concordance-verify/CONTRACT.md', {'validation', 'workflow_runtime', 'publication'}),
    ('workflows/dbm-section-publish/CONTRACT.md', {'validation', 'workflow_runtime', 'publication'}),
    ('workflows/dbm-publish/CONTRACT.md', {'validation', 'workflow_runtime', 'publication'}),
])
def test_shared_inputs_include_their_actual_consumer_suites(path, checks):
    assert set(_dry_run('--paths', path)['checks']) == checks


def test_pdf_dependencies_selected_only_when_pdf_tests_run():
    runner = load_runner()
    assert runner.workflow_outputs(_dry_run('--paths', 'tools/pdf2md/render_table_xlsx.py'))['pdf']
    assert not runner.workflow_outputs(_dry_run('--paths', 'docs/document-metadata.md'))['pdf']


def test_pr24_specification_cleanup_selects_structure_without_behavior_suites():
    # Exact changed paths of cleanup PR #24; actual evidence remains in its PR.
    selection = _dry_run('--paths',
        'execution/PKG-05/DEL-05-01/ScopeOfWork.md',
        'execution/PKG-05/DEL-05-01/Work/ConsumerBasis.md')
    assert selection['checks'] == []
    assert selection['repository_checks'] == ['deliverables']


@pytest.mark.parametrize('path', [
    'execution/PKG-05/DEL-05-01/deliverable.yaml',
    'execution/_Coordination/PUBLICATION_ROADMAP.md',
    'execution/_Decomposition/checkpoint_snapshots/GROUP1-20261031T231127Z/ACCEPTED_MANIFEST.csv',
    'execution/_ScopeChange/SCA-20261101-UNDERTAKING-EVALUATION/candidate-bindings.json',
    'execution/_ScopeChange/SCA-20261101-UNDERTAKING-EVALUATION/amendment.patch',
])
def test_declarative_and_historical_inputs_keep_structure_without_behavior_suites(path):
    selection = _dry_run('--paths', path)
    assert selection['checks'] == []
    assert selection['repository_checks'] == ['deliverables']
    assert selection['unmatched_paths'] == []


def test_moved_external_reproduction_keeps_conservative_code_coverage():
    path = 'tools/workflow_runtime/fixtures/app_workflow_reader.rs'
    assert (REPO_ROOT / path).is_file()
    selection = _dry_run('--paths', path)
    assert set(selection['checks']) == set(load_profile()['checks'])
    assert set(selection['repository_checks']) == {'instructions', 'deliverables'}


def test_every_tracked_execution_input_is_classified_without_behavior_cohorts():
    paths = subprocess.check_output(
        ['git', 'ls-files', '-z', '--', 'execution/'], cwd=REPO_ROOT, text=True).split('\0')
    runner = load_runner()
    for path in filter(None, paths):
        selection = runner.select_checks([path])
        assert not selection['unmatched_paths'], path
        assert selection['checks'] == [], path
        assert selection['repository_checks'] == ['deliverables'], path
