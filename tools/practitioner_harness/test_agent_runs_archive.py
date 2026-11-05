"""Compatibility tests for reading historical archive indexes."""
from __future__ import annotations

import json

import agent_runs_archive
from agent_runs_archive import archive_tag



def test_resolves_archived_runs_inner_paths_and_files(tmp_path):
    index = tmp_path / 'projects/p/execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json'
    index.parent.mkdir(parents=True)
    run = 'projects/p/execution/_Coordination/AgentRuns/OLD-RUN'
    kept_binary = 'projects/p/execution/_Coordination/AgentRuns/ACTIVE/trace.zip'
    index.write_text(json.dumps({'archives': [{'tag': 'archive/t', 'runs': [run], 'files': [kept_binary]}]}))
    agent_runs_archive._entries.cache_clear()
    assert archive_tag(tmp_path, run) == 'archive/t'
    assert archive_tag(tmp_path, run + '/nested/RESULT.md') == 'archive/t'
    assert archive_tag(tmp_path, tmp_path / run / 'x.json') == 'archive/t'
    assert archive_tag(tmp_path, kept_binary) == 'archive/t'
    for other in ['projects/p/execution/_Coordination/AgentRuns/OLD-RUN-2/x.md',
                  'projects/p/execution/_Coordination/AgentRuns/ACTIVE/other.zip',
                  run + '/../ELSEWHERE/x.md', '/etc/passwd']:
        assert archive_tag(tmp_path, other) is None


def test_index_entries_outside_run_records_never_resolve(tmp_path):
    index = tmp_path / 'execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json'
    index.parent.mkdir(parents=True)
    index.write_text(json.dumps({'archives': [{'tag': 'archive/t', 'runs': [
        'docs', 'execution/PKG-01', 'execution/_Coordination/AgentRuns/../../PKG-01', 'execution/_Coordination/AgentRuns/'],
        'files': ['tools/config/example.yaml', 'execution/_Coordination/AgentRuns/R/t.zip']}]}))
    agent_runs_archive._entries.cache_clear()
    for path in ['docs/SPEC.md', 'execution/PKG-01/x.md', 'tools/config/example.yaml',
                 'execution/_Coordination/AgentRuns/OTHER/x.md']:
        assert archive_tag(tmp_path, path) is None, path
    assert archive_tag(tmp_path, 'execution/_Coordination/AgentRuns/R/t.zip') == 'archive/t'
