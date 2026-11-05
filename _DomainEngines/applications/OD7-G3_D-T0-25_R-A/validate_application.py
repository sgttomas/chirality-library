#!/usr/bin/env python3
"""Validate the exact D-T0-25 / OD7-G3 R-A application."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO = Path(
    os.environ.get(
        "CHIRALITY_APPLICATION_REPO",
        str(Path(__file__).resolve().parents[3]),
    )
)
ARCHIVE = Path(__file__).resolve().parent
ACCEPTED = ARCHIVE / "accepted_candidate"
BASIS = "7b0be4d8772a16e5a4774a17988479587d00acca"
PACKET = "67c5af9b736798b3cd22cd3a851b0c98d0192874931f53524c1119564c99ad40"
APPROVED_CANDIDATE_MANIFEST = "2ac9d01be2bd2c36f03d67e4feeb5a47d2860d9e08eccf4d3cb46a05f4fd199c"
APPROVED_ARTIFACT_MANIFEST = "56221e7dc23aa4132d0d506c28c441e2934c7e9acad7f98f42256a5fc467f999"
CORRECTED_CANDIDATE_MANIFEST = "2bdf9a0e6dbf3ec585c0b8d3867112d45192ce40f8a2995ef91dcd4ed1bbd047"
CORRECTED_ARTIFACT_MANIFEST = "2307b38adc6f1190ae86d72a027ddd035ee2ed7566fd6bc4935215a8b481f69b"
ORIGINAL_DIFF = "a6cd22b453c77b5176261fba589e034f0dc448e0d68f7de7ae0ef6b551557168"
CORRECTED_DIFF = "ef1614fd5f3412606a8b9be4c23a5d989361859d7f61874cc6907127f74864eb"
REGISTER = "8ad1787633179ea82984b3738cb2427b48a304247b4673657e85c938f6450656"
INDEX = "517a3bbaf09dc2849220dcca4a2fc8a59a998fb932f1224bc477666938ade5cc"
D23 = "0629e16da62a68ce9648432dfa7293a426fe7278cea1efa43da2a6a00a624ae5"
DECISION = "b9fa9074987bf96d569c5af20e54e7601d4284e13becc51e8c240aa5e2caef4f"
RECEIPTS = "3f5fa5e863835fa194737c7d0d7ffa286072225022f0e52c8bdacddb5341a020"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


passed: list[str] = []
failed: list[str] = []


def check(condition: bool, label: str) -> None:
    (passed if condition else failed).append(label)


def check_manifest(path: Path, root: Path, expected_count: int) -> None:
    rows = [row for row in path.read_text().splitlines() if row]
    errors: list[str] = []
    for row in rows:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", row)
        if not match:
            errors.append(f"malformed:{row}")
            continue
        expected, rel = match.groups()
        target = root / rel
        if not target.is_file():
            errors.append(f"missing:{rel}")
        elif sha(target) != expected:
            errors.append(f"hash:{rel}")
    check(len(rows) == expected_count and not errors, f"{path.name} {expected_count}/{expected_count}")


check(git("rev-parse", "HEAD").stdout.strip() == BASIS, "isolated worktree exact basis")
check(not git("symbolic-ref", "-q", "HEAD", check=False).stdout.strip(), "isolated worktree detached")
check(sha(ACCEPTED / "APPLICATION_PACKET.md") == PACKET, "approved packet identity")
check(
    sha(ACCEPTED / "CANDIDATE_SET_MANIFEST.sha256") == CORRECTED_CANDIDATE_MANIFEST,
    "corrected candidate-manifest identity",
)
check(
    sha(ACCEPTED / "ARTIFACT_HASHES.sha256") == CORRECTED_ARTIFACT_MANIFEST,
    "corrected artifact-manifest identity",
)
check_manifest(ACCEPTED / "CANDIDATE_SET_MANIFEST.sha256", ACCEPTED, 13)
check_manifest(ACCEPTED / "ARTIFACT_HASHES.sha256", ACCEPTED, 17)
correction = ARCHIVE / "CI_WHITESPACE_CORRECTION.md"
correction_text = correction.read_text()
check(
    APPROVED_CANDIDATE_MANIFEST in correction_text
    or APPROVED_CANDIDATE_MANIFEST in (ARCHIVE / "OWNER_RULING.md").read_text(),
    "original approved candidate identity retained",
)
check(
    APPROVED_ARTIFACT_MANIFEST in correction_text
    or APPROVED_ARTIFACT_MANIFEST in (ARCHIVE / "OWNER_RULING.md").read_text(),
    "original approved artifact identity retained",
)
corrected_diff = (ACCEPTED / "DOMAIN_ENGINE_INDEX.diff").read_bytes()
corrected_lines = corrected_diff.splitlines(keepends=True)
check(
    len(corrected_lines) >= 6
    and corrected_lines[3] == b"\n"
    and corrected_lines[5] == b"\n"
    and hashlib.sha256(corrected_diff).hexdigest() == CORRECTED_DIFF,
    "corrected diff removes only named space-only lines",
)
reconstructed = corrected_lines.copy()
reconstructed[3] = b" \n"
reconstructed[5] = b" \n"
check(
    hashlib.sha256(b"".join(reconstructed)).hexdigest() == ORIGINAL_DIFF,
    "corrected diff reconstructs exact approved original",
)

expected_roots = {
    "_DomainEngines/DOMAIN_ENGINE_INDEX.md",
    "_DomainEngines/_DECISIONS/_REGISTER.md",
    "_DomainEngines/_DECISIONS/D-T0-25_d_t0_23_residual_classification.md",
    "_DomainEngines/bridge/LOOP_RECEIPTS.md",
}
tracked = set(filter(None, git("diff", "--name-only").stdout.splitlines()))
untracked = set(
    filter(None, git("ls-files", "--others", "--exclude-standard").stdout.splitlines())
)
all_changed = tracked | untracked
outside_archive = {
    rel
    for rel in all_changed
    if not rel.startswith("_DomainEngines/applications/OD7-G3_D-T0-25_R-A/")
}
check(outside_archive == expected_roots, "exact five-surface write envelope")

register = REPO / "_DomainEngines/_DECISIONS/_REGISTER.md"
index = REPO / "_DomainEngines/DOMAIN_ENGINE_INDEX.md"
decision = REPO / "_DomainEngines/_DECISIONS/D-T0-25_d_t0_23_residual_classification.md"
receipts = REPO / "_DomainEngines/bridge/LOOP_RECEIPTS.md"
check(sha(register) == REGISTER, "exact accepted register postimage")
check(sha(index) == INDEX, "exact accepted index postimage")
check(sha(decision) == DECISION, "exact ruled decision postimage")
check(sha(receipts) == RECEIPTS, "exact Receipt-29 postimage")
check(
    sha(REPO / "_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md") == D23,
    "D-T0-23 byte-identical",
)
check(
    git(
        "merge-base",
        "--is-ancestor",
        "4ac8348e0c15795f33bf2192b2964ee1347aca59",
        "HEAD",
        check=False,
    ).returncode
    == 0,
    "D-T0-24 EffectiveSHA ancestral",
)

owner_lines = [
    "2. R-A / D-T0-25",
    "    Approve exact application:",
    "    * Packet: 67c5af9b736798b3cd22cd3a851b0c98d0192874931f53524c1119564c99ad40",
    "    * Candidate manifest: 2ac9d01be2bd2c36f03d67e4feeb5a47d2860d9e08eccf4d3cb46a05f4fd199c",
    "    * Artifact manifest: 56221e7dc23aa4132d0d506c28c441e2934c7e9acad7f98f42256a5fc467f999",
    "    Apply only five enumerated surfaces, explicitly including Receipt 29. P-A remains excluded; Git closeout returns separately.",
]
for target in [ARCHIVE / "OWNER_RULING.md", decision]:
    quoted = "\n".join(
        line[2:] for line in target.read_text().splitlines() if line.startswith("> ")
    )
    check(quoted == "\n".join(owner_lines), f"verbatim owner ruling: {target.name}")

receipt_text = receipts.read_text()
receipt_ids = [
    int(value)
    for value in re.findall(
        r"(?m)^-\s+\*\*\d{4}-\d{2}-\d{2}\s+—\s+Receipt\s+(\d+)\*\*", receipt_text
    )
]
check(receipt_ids.count(29) == 1 and max(receipt_ids) == 29, "Receipt 29 exactly once and last")
check(register.read_text().count("| D-T0-25 |") == 1, "D-T0-25 register row exactly once")
check("**Status:** `RULED_EFFECTIVE`" in decision.read_text(), "D-T0-25 RULED_EFFECTIVE")
check(
    not (REPO / "_DomainEngines/_DECISIONS/D-T0-26_pec_profile_demotion.md").exists(),
    "D-T0-26 absent",
)
check(
    not (REPO / "_DomainEngines/applications/OD7-G3_D-T0-26_P-A").exists(),
    "P-A archive absent",
)
check(
    not any(rel.startswith("_DomainEngines/profiles/") for rel in all_changed),
    "profile surfaces unchanged",
)
check(git("diff", "--check", check=False).returncode == 0, "git diff --check")

generated = {"ARTIFACT_HASHES.sha256", "VALIDATION_RESULT.json"}
for path in ARCHIVE.rglob("*"):
    if path.is_file() and path.name not in generated and path.suffix != ".diff":
        data = path.read_bytes()
        check(not re.search(rb"[ \t]+\n", data), f"no trailing whitespace: {path.relative_to(ARCHIVE)}")
        check(not data.endswith(b"\n\n"), f"single terminal newline: {path.relative_to(ARCHIVE)}")

application_manifest = ARCHIVE / "ARTIFACT_HASHES.sha256"
if application_manifest.exists():
    check_manifest(application_manifest, ARCHIVE, 26)

result = {
    "schema_version": "1.0",
    "basis": BASIS,
    "verdict": "PASS" if not failed else "FAIL",
    "passed": len(passed),
    "failed": len(failed),
    "checks": passed,
    "failures": failed,
    "notes": [
        "Application is confined to the five owner-approved surfaces.",
        "P-A and D-T0-26 remain excluded.",
        "No Git closeout was performed.",
    ],
}
print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if not failed else 1)
