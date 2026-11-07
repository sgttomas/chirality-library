#!/usr/bin/env python3
"""Registry-mode tests for validate_agent_instructions.py.

Registry shape and delegation rules are exercised in test_four_role_contract.py.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import validate_agent_instructions as validator

SCRIPT = Path(validator.__file__).resolve()
ROOT = SCRIPT.parents[2]


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)


def test_live_registry_has_no_errors() -> None:
    result = run("--json")
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(result.stdout)
    assert report["errors"] == 0
    assert report["files_checked"] == 5


def test_live_help_human_declares_narrow_agent0_direct_agent2_metadata() -> None:
    role = json.loads((ROOT / "agents/registry.json").read_text())["roles"]["HELP_HUMAN"]
    assert "TASK" in role["delegates_to"]
    assert role["allow_generalist_agent2"] is True
    assert role["direct_entry"] is True


def test_repository_without_registry_is_an_input_failure(tmp_path: Path) -> None:
    (tmp_path / "agents").mkdir()
    (tmp_path / "agents" / "AGENT_TASK.md").write_text("# TASK\n", encoding="utf-8")
    result = run("--repo-root", str(tmp_path))
    assert result.returncode == 2
    assert "agent registry not found" in result.stderr
