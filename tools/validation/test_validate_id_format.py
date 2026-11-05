"""Tests for validate_id_format.sh.

The script declares zsh but uses only POSIX shell features, so the tests run it
with zsh when installed and otherwise with bash.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name("validate_id_format.sh")
SHELL = shutil.which("zsh") or shutil.which("bash")

pytestmark = pytest.mark.skipif(SHELL is None, reason="no zsh or bash available")


def run(id_type: str, value: str) -> int:
    return subprocess.run(
        [SHELL, str(SCRIPT), id_type, value],
        capture_output=True,
        text=True,
        check=False,
    ).returncode


@pytest.mark.parametrize(
    ("id_type", "value"),
    [
        ("PKG", "PKG-02"),
        ("PKG", "PKG-001"),
        ("DEL", "DEL-02-08"),
        ("DEL", "DEL-001-01"),
        ("DEP", "DEP-01-01-001"),
        ("DEP", "DEP-001-01-001"),
        ("SOW", "SOW-003"),
        ("SOW", "SOW-0012a"),
        ("OBJ", "OBJ-001"),
        ("CAT", "CAT-001"),
        ("CAT", "CAT-01"),
        ("KTY", "KTY-01-02"),
        ("SUB", "SUB-01-02-03"),
    ],
)
def test_current_id_forms_are_valid(id_type: str, value: str) -> None:
    assert run(id_type, value) == 0


@pytest.mark.parametrize(
    ("id_type", "value"),
    [
        ("PKG", "PKG-1"),
        ("PKG", "PKG-0001"),
        ("DEL", "DEL-01.01"),
        ("DEL", "DEL-01"),
        ("DEP", "DEP-01-01-01"),
        ("DEP", "DEP-01-001"),
        ("SOW", "SOW-03"),
        ("KTY", "KTY-01-02_Guidance"),
        ("XYZ", "XYZ-01"),
    ],
)
def test_malformed_or_unknown_ids_are_invalid(id_type: str, value: str) -> None:
    assert run(id_type, value) == 1
