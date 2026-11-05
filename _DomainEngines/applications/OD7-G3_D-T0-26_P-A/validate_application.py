#!/usr/bin/env python3
"""Validate the exact D-T0-26 / OD7-G3 P-A application."""

from __future__ import annotations

import base64
import csv
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
BASIS = "2c8e4168220b49f1e83a45aa916a6eb29856f0b4"
D25 = "b9fa9074987bf96d569c5af20e54e7601d4284e13becc51e8c240aa5e2caef4f"
GATE = "f0714f38b902bbee074e5588da0b84a6e49661aaf0211a7360a457fad39797db"
SEMANTIC_INPUT = "95263e4fa5c72840a5053a91da904ea76acbef7050dae344e4e1e94cf4a22152"
REBUILT_PACKAGE = "7940a9bd8f26497c8e3050b8a31cf6d89c09dbd2934c8e8ead04f1b016ab14d2"
P_A_TRANCHE = "8913d5b6654128da60e889822833b84bee477129fe291201ed98605d00195c22"
REGISTER = "ab0f75ee11524cf6797e8b5a008eb628cf080a699a0cd1bc4efeb365d3501a5e"
INDEX = "d0822ebe28fcd037664790baf3518ad363796a4d5ea3abf61ea426ef4d1b5cdf"
PROFILE = "0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6"
PROFILE_REPORT = "5ad9d87d9b19cb6f6d54ba535d1516e47ba0a24ff83853f4e64ec80ab964ace8"
DECISION = "d3c1968dbd27b39975af6367403c7f0ff3cc88222608c543a5bc7b5a007cc630"
RECEIPTS = "e948b6e68ed96afefecc0bc41687e396f51e54885a9fe6eaea24084fd659c019"
LIVE_PIN = "38314c98fe6ae1109e24286582d16e8555a21c7b3a11d4e74c75fc7c8a3fbaed"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
    check(
        len(rows) == expected_count and not errors,
        f"{path.relative_to(ARCHIVE)} {expected_count}/{expected_count}",
    )


check(
    git("merge-base", "--is-ancestor", BASIS, "HEAD", check=False).returncode == 0,
    "application basis ancestral to current HEAD",
)
check(
    git("merge-base", "--is-ancestor", BASIS, "HEAD", check=False).returncode == 0,
    "D-T0-25 durable predecessor ancestral",
)
check(
    sha(REPO / "_DomainEngines/_DECISIONS/D-T0-25_d_t0_23_residual_classification.md")
    == D25,
    "D-T0-25 exact durable predecessor",
)
check(sha(ACCEPTED / "ACCEPTED_INPUT.md") == SEMANTIC_INPUT, "accepted semantic input")
check(sha(ACCEPTED / "TRANCHE_HASHES.sha256") == P_A_TRANCHE, "P-A tranche identity")
original_manifest = base64.b64decode(
    (ACCEPTED / "APPLICATION_MANIFEST.csv.original.base64").read_text()
)
normalized_manifest = (ACCEPTED / "APPLICATION_MANIFEST.csv").read_bytes()
check(
    sha_bytes(original_manifest)
    == "eca70cea456f464bf3ddfbd732b6e8fe9d60259fa2701578dbcb9bd0476cf894",
    "accepted CRLF manifest original identity",
)
check(
    original_manifest.replace(b"\r\n", b"\n") == normalized_manifest
    and sha_bytes(normalized_manifest)
    == "1d6b55b256697e93de4c0eb40f084e00bec0ef6ff1949e7372345f06c30a3c76",
    "bounded CRLF-to-LF normalization",
)
tranche_rows = [
    row
    for row in (ACCEPTED / "TRANCHE_HASHES.sha256").read_text().splitlines()
    if row
]
tranche_errors: list[str] = []
for row in tranche_rows:
    match = re.fullmatch(r"([0-9a-f]{64})  (.+)", row)
    if not match:
        tranche_errors.append(f"malformed:{row}")
        continue
    expected, rel = match.groups()
    if rel == "APPLICATION_MANIFEST.csv":
        if sha_bytes(original_manifest) != expected:
            tranche_errors.append(f"original-hash:{rel}")
        continue
    target = ACCEPTED / rel
    if not target.is_file():
        tranche_errors.append(f"missing:{rel}")
    elif sha(target) != expected:
        tranche_errors.append(f"hash:{rel}")
check(
    len(tranche_rows) == 8 and not tranche_errors,
    "accepted candidate 8/8 with CRLF reconstruction",
)

source_package = Path(
    "/private/tmp/OD7-G3_TIER0_DURABLE_PREDECESSOR_SUCCESSOR_2026-07-27_4AC8348E0"
)
source_manifest = source_package / "ARTIFACT_HASHES.sha256"
check(
    source_manifest.is_file() and sha(source_manifest) == REBUILT_PACKAGE,
    "rebuilt source-package identity",
)
if source_manifest.is_file():
    source_rows = [row for row in source_manifest.read_text().splitlines() if row]
    source_ok = True
    for row in source_rows:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", row)
        if not match:
            source_ok = False
            continue
        expected, rel = match.groups()
        target = source_package / rel
        source_ok = source_ok and target.is_file() and sha(target) == expected
    check(len(source_rows) == 32 and source_ok, "rebuilt source package 32/32")

expected_roots = {
    "_DomainEngines/DOMAIN_ENGINE_INDEX.md",
    "_DomainEngines/_DECISIONS/_REGISTER.md",
    "_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md",
    "_DomainEngines/bridge/LOOP_RECEIPTS.md",
    "_DomainEngines/profiles/_validation/pec.validation.json",
    "_DomainEngines/profiles/pec.yaml",
    "tools/practitioner_harness/test_live_baseline.py",
}
tracked = set(filter(None, git("diff", BASIS, "--name-only").stdout.splitlines()))
untracked = set(
    filter(None, git("ls-files", "--others", "--exclude-standard").stdout.splitlines())
)
all_changed = tracked | untracked
outside_archive = {
    rel
    for rel in all_changed
    if not rel.startswith("_DomainEngines/applications/OD7-G3_D-T0-26_P-A/")
}
check(outside_archive == expected_roots, "exact eight-surface write envelope")

register = REPO / "_DomainEngines/_DECISIONS/_REGISTER.md"
index = REPO / "_DomainEngines/DOMAIN_ENGINE_INDEX.md"
profile = REPO / "_DomainEngines/profiles/pec.yaml"
report = REPO / "_DomainEngines/profiles/_validation/pec.validation.json"
decision = REPO / "_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md"
receipts = REPO / "_DomainEngines/bridge/LOOP_RECEIPTS.md"
live_pin = REPO / "tools/practitioner_harness/test_live_baseline.py"
check(sha(register) == REGISTER, "exact accepted register postimage")
check(sha(index) == INDEX, "exact rebuilt index postimage")
check(sha(profile) == PROFILE, "exact rebuilt profile postimage")
check(sha(report) == PROFILE_REPORT, "exact regenerated profile report")
check(sha(decision) == DECISION, "exact D-T0-26 decision postimage")
check(sha(receipts) == RECEIPTS, "exact Receipt-30 postimage")
check(sha(live_pin) == LIVE_PIN, "exact conscious live-pin postimage")

accepted_profile = (ACCEPTED / "candidate_live/pec.yaml").read_text()
rebuilt_profile = accepted_profile
profile_substitutions = [
    (
        "STALE legacy binding (OD7-G3 P-A exact candidate; not applied)",
        "STALE legacy binding (D-T0-26; applied 2026-07-28)",
    ),
    ("Current candidate", "Current"),
    ("This candidate preserves", "D-T0-26 preserves"),
    (
        "OD7-G3 P-A exact candidate: semantic demotion only",
        "D-T0-26 P-A application: semantic demotion only",
    ),
    ("this STALE candidate grants", "this STALE profile grants"),
]
for old, new in profile_substitutions:
    check(rebuilt_profile.count(old) == 1, f"profile rebuild source once: {old}")
    rebuilt_profile = rebuilt_profile.replace(old, new)
check(rebuilt_profile == profile_text if "profile_text" in globals() else rebuilt_profile == profile.read_text(), "profile effective-state rebuild exact")

accepted_index = (ACCEPTED / "candidate_live/DOMAIN_ENGINE_INDEX.md").read_text()
index_substitutions = [
    (
        "The OD7-G3 P-A candidate would preserve that adoption as history while making the current profile **STALE** and ineligible for governed profile-mediated invocation; no candidate is applied by this index preview.",
        "D-T0-26 preserves that adoption as history while making the current profile **STALE** and ineligible for governed profile-mediated invocation.",
    ),
    ("OD7-G3 P-A candidate", "D-T0-26"),
]
rebuilt_index = accepted_index
for old, new in index_substitutions:
    check(rebuilt_index.count(old) == 1, f"index rebuild source once: {old}")
    rebuilt_index = rebuilt_index.replace(old, new)
check(rebuilt_index == index.read_text(), "index effective-state rebuild exact")

preimages: dict[str, str] = {}
with (ARCHIVE / "PREIMAGE_MANIFEST.csv").open(newline="") as handle:
    for row in csv.DictReader(handle):
        if row["PreimageState"] == "PRESENT":
            preimages[row["Path"]] = row["PreimageSHA256"]
for rel, expected in preimages.items():
    shown = git("show", f"{BASIS}:{rel}").stdout.encode()
    check(sha_bytes(shown) == expected, f"exact preimage: {rel}")

profile_text = profile.read_text()
for needle in [
    'profile_version: "0.3"',
    'profile_status: "STALE"',
    'integration_level: "MANUAL_BRIDGE"',
    'execution_policy: "DENY_ALL_PROFILE_MEDIATED_INVOCATIONS"',
    "historical_binding_only: true",
]:
    check(needle in profile_text, f"profile semantic assertion: {needle}")

report_json = json.loads(report.read_text())
check(
    report_json.get("valid") is True
    and report_json.get("result") == "VALID"
    and report_json.get("profile_status") == "STALE"
    and report_json.get("findings") == [],
    "Git-pinned profile validator VALID / STALE / zero findings",
)

owner_quote = (
    '"Finish out your plan now (attaining your goal) with self merge of PRs '
    "and auto approve for owners rulings, which should still be recorded in "
    'the usual manner with your recommendation standing as what I approved."'
)
for target in [ARCHIVE / "OWNER_RULING.md", decision]:
    check(owner_quote in target.read_text(), f"verbatim owner direction: {target.name}")

decision_text = decision.read_text()
check(GATE in decision_text, "accepted P-A gate identity recorded")
check(SEMANTIC_INPUT in decision_text, "accepted P-A semantic identity recorded")
check("**Status:** `RULED_EFFECTIVE`" in decision_text, "D-T0-26 RULED_EFFECTIVE")
check(register.read_text().count("| D-T0-26 |") == 1, "D-T0-26 register row once")

receipt_text = receipts.read_text()
receipt_ids = [
    int(value)
    for value in re.findall(
        r"(?m)^-\s+\*\*\d{4}-\d{2}-\d{2}\s+—\s+Receipt\s+(\d+)\*\*",
        receipt_text,
    )
]
check(receipt_ids.count(30) == 1 and max(receipt_ids) == 30, "Receipt 30 once and last")

with (ARCHIVE / "APPLIED_PATHS_AND_HASHES.csv").open(newline="") as handle:
    applied_rows = list(csv.DictReader(handle))
check(len(applied_rows) == 8, "applied manifest enumerates eight surfaces")
for row in applied_rows:
    if row["State"] == "APPLIED":
        check(
            sha(REPO / row["Path"]) == row["SHA256"],
            f"applied manifest hash: {row['Path']}",
        )

for prohibited in [
    "projects/pec/",
    "docs/PRD",
    "execution/_Decomposition/",
    "ScopeOfWork",
    "runtime/",
]:
    check(
        not any(prohibited in rel for rel in all_changed),
        f"excluded surface class unchanged: {prohibited}",
    )

check(git("diff", "--check", BASIS, check=False).returncode == 0, "git diff --check")

generated = {"ARTIFACT_HASHES.sha256", "VALIDATION_RESULT.json"}
for path in ARCHIVE.rglob("*"):
    if path.is_file() and path.name not in generated:
        data = path.read_bytes()
        check(
            not re.search(rb"[ \t]+\n", data),
            f"no trailing whitespace: {path.relative_to(ARCHIVE)}",
        )
        check(
            not data.endswith(b"\n\n"),
            f"single terminal newline: {path.relative_to(ARCHIVE)}",
        )

artifact_manifest = ARCHIVE / "ARTIFACT_HASHES.sha256"
if artifact_manifest.exists():
    expected_count = len(
        [
            path
            for path in ARCHIVE.rglob("*")
            if path.is_file() and path.name != "ARTIFACT_HASHES.sha256"
        ]
    )
    check_manifest(artifact_manifest, ARCHIVE, expected_count)

result = {
    "schema_version": "1.0",
    "basis": BASIS,
    "verdict": "PASS" if not failed else "FAIL",
    "passed": len(passed),
    "failed": len(failed),
    "checks": passed,
    "failures": failed,
    "notes": [
        "Application is confined to the eight approved P-A classification surfaces.",
        "The profile is STALE / MANUAL_BRIDGE and denies governed profile-mediated invocation.",
        "No product, runtime, implementation, migration, release, or reliance work was performed.",
        "Git closeout remains separate.",
    ],
}
print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if not failed else 1)
