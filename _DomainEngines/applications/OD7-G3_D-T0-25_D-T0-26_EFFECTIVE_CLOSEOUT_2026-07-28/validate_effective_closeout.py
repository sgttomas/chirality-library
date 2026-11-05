#!/usr/bin/env python3
"""Validate the additive D-T0-25 / D-T0-26 effective-state closeout."""

from __future__ import annotations

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
        "CHIRALITY_EFFECTIVE_CLOSEOUT_REPO",
        str(Path(__file__).resolve().parents[3]),
    )
)
ARCHIVE = Path(__file__).resolve().parent
BASIS = "dc89356eb4db715bfe8357b25d8831c752cb822e"
D25_PUB = "1e08b927928fe77407e2cd43692a7bf04accba4a"
D25_EFF = "2c8e4168220b49f1e83a45aa916a6eb29856f0b4"
D26_PUB = "7948eef43fe27eacd482688d9249a1ad2b92471c"
D26_EFF = "dc89356eb4db715bfe8357b25d8831c752cb822e"
D25_PRE = "b9fa9074987bf96d569c5af20e54e7601d4284e13becc51e8c240aa5e2caef4f"
D26_PRE = "d3c1968dbd27b39975af6367403c7f0ff3cc88222608c543a5bc7b5a007cc630"
D25_POST = "990031bbeaf4048ba55528a4fd173e30b598a8039ea55ccfd385ba37635ce95b"
D26_POST = "c284ccd8db58a0aa6ef2efcec0ac48d6e12fe03ba811448df2fea628d53aeef9"
REGISTER_POST = "7ff6079f1dffac44a985ef2a2832a1f1b4c4df3ee67c7ffd91d12efc7685e59a"
RECEIPTS_POST = "2aa966c60710372ef478da26ac32604c838b71e9a24bdf5b6f16587b70a7e706"
D25_PACKAGE_MANIFEST = "1e9c13ee8ba0f28b105af10cbae64c0f77295d6127fff11499e207d1b0cef250"
D26_PACKAGE_MANIFEST = "cca5fb058465c42d0570258aafe1ae304472722b59934268992b19298871ac1c"
PROFILE = "0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6"
PROFILE_REPORT = "5ad9d87d9b19cb6f6d54ba535d1516e47ba0a24ff83853f4e64ec80ab964ace8"
HARNESS_PIN = "38314c98fe6ae1109e24286582d16e8555a21c7b3a11d4e74c75fc7c8a3fbaed"
PROFILE_EVIDENCE = "bd5828d4b8843e0e2f99a64fbdc3d9b024f41b6963c968a937877d4f1f1a8a1a"


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


def check_manifest(path: Path, root: Path, expected_count: int, label: str) -> None:
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
    check(len(rows) == expected_count and not errors, f"{label} {expected_count}/{expected_count}")


check(
    git("merge-base", "--is-ancestor", BASIS, "HEAD", check=False).returncode == 0,
    "closeout basis ancestral to current HEAD",
)

for effective, publication, label in [
    (D25_EFF, D25_PUB, "D-T0-25"),
    (D26_EFF, D26_PUB, "D-T0-26"),
]:
    parents = git("rev-list", "--parents", "-n", "1", effective).stdout.split()
    check(
        len(parents) >= 3 and parents[2] == publication,
        f"{label} publication is effective merge second parent",
    )
    check(
        git("merge-base", "--is-ancestor", effective, BASIS, check=False).returncode == 0,
        f"{label} effective merge ancestral",
    )

d25_rel = "_DomainEngines/_DECISIONS/D-T0-25_d_t0_23_residual_classification.md"
d26_rel = "_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md"
d25_app = "_DomainEngines/applications/OD7-G3_D-T0-25_R-A"
d26_app = "_DomainEngines/applications/OD7-G3_D-T0-26_P-A"

for publication, rel, expected, label in [
    (D25_PUB, d25_rel, D25_PRE, "D-T0-25"),
    (D26_PUB, d26_rel, D26_PRE, "D-T0-26"),
]:
    published = git("show", f"{publication}:{rel}").stdout.encode()
    baseline = git("show", f"{BASIS}:{rel}").stdout.encode()
    check(
        sha_bytes(published) == expected and published == baseline,
        f"{label} decision publication/basis byte identity",
    )

for publication, path, label in [
    (D25_PUB, d25_app, "D-T0-25"),
    (D26_PUB, d26_app, "D-T0-26"),
]:
    check(
        git("diff", "--quiet", publication, BASIS, "--", path, check=False).returncode == 0,
        f"{label} frozen application byte identity",
    )

d25_manifest = REPO / d25_app / "ARTIFACT_HASHES.sha256"
d26_manifest = REPO / d26_app / "ARTIFACT_HASHES.sha256"
check(sha(d25_manifest) == D25_PACKAGE_MANIFEST, "D-T0-25 package-manifest identity")
check(sha(d26_manifest) == D26_PACKAGE_MANIFEST, "D-T0-26 package-manifest identity")
check_manifest(d25_manifest, REPO / d25_app, 26, "D-T0-25 package")
check_manifest(d26_manifest, REPO / d26_app, 21, "D-T0-26 package")

expected_roots = {
    d25_rel,
    d26_rel,
    "_DomainEngines/_DECISIONS/_REGISTER.md",
    "_DomainEngines/bridge/LOOP_RECEIPTS.md",
}
tracked = set(filter(None, git("diff", BASIS, "--name-only").stdout.splitlines()))
untracked = set(
    filter(None, git("ls-files", "--others", "--exclude-standard").stdout.splitlines())
)
all_changed = tracked | untracked
outside_archive = {
    rel
    for rel in all_changed
    if not rel.startswith(
        "_DomainEngines/applications/"
        "OD7-G3_D-T0-25_D-T0-26_EFFECTIVE_CLOSEOUT_2026-07-28/"
    )
}
check(outside_archive == expected_roots, "exact five-surface write envelope")

d25 = REPO / d25_rel
d26 = REPO / d26_rel
register = REPO / "_DomainEngines/_DECISIONS/_REGISTER.md"
receipts = REPO / "_DomainEngines/bridge/LOOP_RECEIPTS.md"
check(sha(d25) == D25_POST, "exact D-T0-25 closeout postimage")
check(sha(d26) == D26_POST, "exact D-T0-26 closeout postimage")
check(sha(register) == REGISTER_POST, "exact register postimage")
check(sha(receipts) == RECEIPTS_POST, "exact Receipt-31 postimage")

preimages: dict[str, str] = {}
with (ARCHIVE / "PREIMAGE_MANIFEST.csv").open(newline="") as handle:
    for row in csv.DictReader(handle):
        if row["PreimageState"] == "PRESENT":
            preimages[row["Path"]] = row["PreimageSHA256"]
for rel, expected in preimages.items():
    shown = git("show", f"{BASIS}:{rel}").stdout.encode()
    check(sha_bytes(shown) == expected, f"exact preimage: {rel}")

identity_pairs = [
    ("D-T0-25", D25_PUB, D25_EFF),
    ("D-T0-26", D26_PUB, D26_EFF),
]
for decision_id, publication, effective in identity_pairs:
    for path in [
        REPO / (
            "_DomainEngines/_DECISIONS/"
            + (
                "D-T0-25_d_t0_23_residual_classification.md"
                if decision_id == "D-T0-25"
                else "D-T0-26_pec_profile_stale_demotion.md"
            )
        ),
        register,
        ARCHIVE / f"{decision_id}_EFFECTIVE_STATE_CLOSEOUT.md",
        receipts,
    ]:
        text = path.read_text()
        check(
            publication in text and effective in text,
            f"{decision_id} identity parity: {path.name}",
        )

owner_quote = (
    '"Finish out your plan now (attaining your goal) with self merge of PRs '
    "and auto approve for owners rulings, which should still be recorded in "
    'the usual manner with your recommendation standing as what I approved."'
)
check(owner_quote in (ARCHIVE / "OWNER_RULING.md").read_text(), "verbatim owner direction")
check(owner_quote in receipts.read_text(), "owner direction in Receipt 31")

receipt_ids = [
    int(value)
    for value in re.findall(
        r"(?m)^-\s+\*\*\d{4}-\d{2}-\d{2}\s+—\s+Receipt\s+(\d+)\*\*",
        receipts.read_text(),
    )
]
check(receipt_ids.count(31) == 1 and max(receipt_ids) == 31, "Receipt 31 once and last")

with (ARCHIVE / "APPLIED_PATHS_AND_HASHES.csv").open(newline="") as handle:
    applied_rows = list(csv.DictReader(handle))
check(len(applied_rows) == 5, "applied manifest enumerates five surfaces")
for row in applied_rows:
    if row["State"] == "APPLIED":
        check(
            sha(REPO / row["Path"]) == row["SHA256"],
            f"applied manifest hash: {row['Path']}",
        )

check(sha(REPO / "_DomainEngines/profiles/pec.yaml") == PROFILE, "PEC profile unchanged")
check(
    sha(REPO / "_DomainEngines/profiles/_validation/pec.validation.json")
    == PROFILE_REPORT,
    "PEC profile report unchanged",
)
check(
    sha(REPO / "tools/practitioner_harness/test_live_baseline.py") == HARNESS_PIN,
    "harness live pin unchanged",
)
profile_evidence = ARCHIVE / "PEC_PROFILE_VALIDATION.json"
check(sha(profile_evidence) == PROFILE_EVIDENCE, "profile validation evidence identity")
profile_evidence_json = json.loads(profile_evidence.read_text())
check(
    profile_evidence_json.get("valid") is True
    and profile_evidence_json.get("result") == "VALID"
    and profile_evidence_json.get("profile_status") == "STALE"
    and profile_evidence_json.get("findings") == [],
    "profile validation evidence VALID / STALE / zero findings",
)
for prohibited in [
    "projects/",
    "docs/PRD",
    "execution/_Decomposition/",
    "ScopeOfWork",
    "runtime/",
    "tools/practitioner_harness/",
    "_DomainEngines/profiles/",
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
    check_manifest(artifact_manifest, ARCHIVE, expected_count, "closeout package")

result = {
    "schema_version": "1.0",
    "basis": BASIS,
    "verdict": "PASS" if not failed else "FAIL",
    "passed": len(passed),
    "failed": len(failed),
    "checks": passed,
    "failures": failed,
    "notes": [
        "Closeout is confined to five additive Tier-0 identity surfaces.",
        "Frozen D-T0-25 and D-T0-26 ruling/application packages remain unchanged.",
        "No profile semantics, product, runtime, implementation, lifecycle, release, or reliance work was performed.",
        "Git closeout remains separate.",
    ],
}
print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if not failed else 1)
