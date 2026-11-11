"""Shared header compatibility, schema rejection, and live rollout coverage."""
import json
from pathlib import Path

import jsonschema
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / 'docs/document-metadata.schema.json').read_text())
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA)
HISTORICAL_MANUAL = ROOT / 'docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v9.md'


def documents():
    return [ROOT / 'AGENTS.md', ROOT / 'init-prompt.md',
            *sorted((ROOT / 'agents').glob('AGENT_*.md')),
            *sorted((ROOT / 'tools').rglob('README.md')),
            *sorted(p for p in (ROOT / 'docs').rglob('*.md') if p != HISTORICAL_MANUAL),
            *sorted((ROOT / 'workflows').glob('*/WORKFLOW.md')),
            *sorted((ROOT / '.agents/skills').glob('*/SKILL.md'))]


def header(path):
    lines = path.read_text().splitlines()
    assert lines[0] == '---', path
    return yaml.safe_load('\n'.join(lines[1:lines.index('---', 1)]))


@pytest.mark.parametrize('path', documents(), ids=lambda p: str(p.relative_to(ROOT)))
def test_live_document_header(path):
    VALIDATOR.validate(header(path))


def test_metadata_schema_is_valid_and_extensions_survive():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
    data = header(ROOT / 'AGENTS.md')
    data['metadata']['applicability'] = 'Authorized project maintenance'
    data['metadata']['category'] = 'Entry'
    data['allowed-tools'] = 'Read'
    VALIDATOR.validate(data)


@pytest.mark.parametrize('field', ['status', 'date', 'revision'])
@pytest.mark.parametrize('nested', [False, True])
def test_history_fields_are_rejected(field, nested):
    data = header(ROOT / 'AGENTS.md')
    (data['metadata'] if nested else data)[field] = 'current'
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(data)


@pytest.mark.parametrize('change', [
    {'name': 'HELP_HUMAN'}, {'description': ''}, {'description': 'two\nlines'},
    {'description': 'trailing\n'}, {'metadata': {'kind': 'accepted', 'surface': 'role'}},
    {'metadata': {'kind': 'instruction', 'surface': 'session'}},
    {'metadata': {'surface': 'role'}},
])
def test_invalid_metadata_is_rejected(change):
    data = header(ROOT / 'AGENTS.md')
    data.update(change)
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(data)


def test_bootstrap_wrapper_and_claude_entry_are_preserved():
    text = (ROOT / 'init-prompt.md').read_text()
    assert text.index('\n---\n') < text.index('<init-prompt>')
    assert text.count('<init-prompt>') == text.count('</init-prompt>') == 1
    assert (ROOT / 'CLAUDE.md').read_text() == '@AGENTS.md\n'


@pytest.mark.parametrize('edition', ['library-v3.2.1', 'library-v3.3.0'])
def test_adapted_project_header_records_source_and_reconciled_library_edition(edition):
    data = header(ROOT / 'AGENTS.md')
    data['metadata']['upstream'] = {
        'source': 'workflows/project-setup/resources/project-entry.md',
        'edition': edition,
    }
    data['metadata']['applicability'] = 'Project-specific entry instructions'
    VALIDATOR.validate(data)


@pytest.mark.parametrize('upstream', [
    None, 'library-v3.3.0', {},
    {'source': 'workflows/project-setup/resources/project-entry.md'},
    {'edition': 'library-v3.3.0'},
    {'source': '', 'edition': 'library-v3.3.0'},
    {'source': ' \t', 'edition': 'library-v3.3.0'},
    {'source': 'workflows/source.md\n', 'edition': 'library-v3.3.0'},
    {'source': 'workflows/source.md', 'edition': 'latest'},
    {'source': 'workflows/source.md', 'edition': '3.3.0'},
    {'source': 'workflows/source.md', 'edition': 'library-v3.3.0\n'},
    {'source': 'workflows/source.md', 'edition': 3.3},
    {'source': 'workflows/source.md', 'edition': 'library-v3.3.0', 'revision': 'local'},
    {'source': 'workflows/source.md', 'edition': 'library-v3.3.0', 'version': 'local'},
])
def test_incomplete_or_malformed_reconciliation_claim_is_rejected(upstream):
    data = header(ROOT / 'AGENTS.md')
    data['metadata']['upstream'] = upstream
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(data)
