"""Library required aggregate remains fail-closed after product extraction."""

from pathlib import Path

import json

import yaml

ROOT = Path(__file__).resolve().parents[2]

def workflow(name):
    return yaml.load((ROOT / ".github/workflows" / name).read_text(), Loader=yaml.BaseLoader)

def test_every_pr_reaches_single_required_aggregate_and_reusable_products():
    root = workflow('governance-harness.yml')
    assert 'pull_request' in root['on']
    assert not root['on']['pull_request']
    assert 'schedule' not in root['on']
    assert 'push' not in root['on']  # no duplicate post-merge product run
    jobs = root['jobs']
    assert jobs['harness']['if'] == 'always()'
    assert set(jobs['harness']['needs']) == {'repository-checks'}
    assert 'piping' not in jobs and 'app-v4' not in jobs


def test_single_required_result_fails_for_any_unsuccessful_child(tmp_path):
    import os
    import subprocess
    step = workflow('governance-harness.yml')['jobs']['harness']['steps'][0]
    for state in ['success', 'failure', 'cancelled', 'skipped']:
        results = {name: {'result': 'success'} for name in ['repository-checks']}
        results['repository-checks']['result'] = state
        process = subprocess.run(['bash', '-c', step['run']], env={**os.environ, 'RESULTS': json.dumps(results)}, capture_output=True)
        assert (process.returncode == 0) == (state == 'success')


def test_routing_completeness_runs_on_every_pr_and_zsh_only_when_needed():
    steps = workflow('governance-harness.yml')['jobs']['repository-checks']['steps']
    guards = next(s for s in steps if s.get('name') == 'Routing completeness and workflow contracts')
    assert 'if' not in guards
    assert 'test_tools_test_routing.py' in guards['run']
    assert 'test_hosted_ci_workflows.py' in guards['run']
    provisioning = ['Configure canonical Ubuntu package sources', 'Resolve Ubuntu release',
                    'Restore cached zsh packages', 'Install zsh (write_status.sh guard is a zsh script)']
    for name in provisioning:
        assert next(s for s in steps if s.get('name') == name)['if'] == "steps.selection.outputs.needs_zsh == 'true'"
    renderer = next(s for s in steps if s.get('name') == 'Install selected manual renderer dependencies')
    assert renderer['if'] == "steps.selection.outputs.manual == 'true'"
    assert '-r docs/alignment-manual/requirements.txt' in renderer['run']
    pdf = next(s for s in steps if s.get('name') == 'Install selected PDF dependencies')
    assert pdf['if'] == "steps.selection.outputs.pdf == 'true'"
    assert '.[pdf]' in pdf['run']


def test_execution_boundary_runs_even_when_no_behavior_suite_is_selected():
    steps = workflow('governance-harness.yml')['jobs']['repository-checks']['steps']
    guard = next(s for s in steps if s.get('name') == 'Declarative execution boundary')
    assert 'if' not in guard
    assert guard['run'] == 'python3 tools/validation/check_execution_boundary.py'
