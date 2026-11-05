"""Tests for validate_enum.py, including the D-GOV-46 tracking-mode vocabulary."""

import subprocess
import sys
from pathlib import Path

import validate_enum

SCRIPT = Path(__file__).resolve().parent / "validate_enum.py"


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], capture_output=True, text=True, check=False
    )


def test_tracking_mode_vocabulary_matches_spec_5_3():
    assert validate_enum.ENUMS["TRACKING_MODE"] == ["NOT_TRACKED", "DECLARED", "FULL_GRAPH"]


def test_full_graph_is_valid():
    result = run("TRACKING_MODE", "FULL_GRAPH")
    assert result.returncode == 0
    assert result.stdout.startswith("VALID: FULL_GRAPH")


def test_legacy_tracked_is_read_as_full_graph():
    assert validate_enum.canonical_value("TRACKING_MODE", "TRACKED") == "FULL_GRAPH"
    result = run("TRACKING_MODE", "TRACKED")
    assert result.returncode == 0
    assert "legacy" in result.stdout and "write FULL_GRAPH" in result.stdout


def test_unknown_tracking_mode_is_invalid():
    assert validate_enum.canonical_value("TRACKING_MODE", "PARTIAL") is None
    result = run("TRACKING_MODE", "PARTIAL")
    assert result.returncode == 1
    assert "FULL_GRAPH" in result.stderr


def test_legacy_alias_does_not_leak_into_other_enums():
    assert validate_enum.canonical_value("STATUS", "TRACKED") is None
