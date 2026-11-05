#!/usr/bin/env python3
"""Deterministically validate the refreshed OD7-G3 R-A application candidate."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
REPO = Path("/Users/<owner>/.codex/worktrees/d8deadbf-f4c8-4203-89bf-b1543c13f926/chirality")
ACCEPTED = Path(
    "/private/tmp/OD7-G3_TIER0_DURABLE_PREDECESSOR_SUCCESSOR_2026-07-27_4AC8348E0"
)
BASIS = "7b0be4d8772a16e5a4774a17988479587d00acca"
PRIOR_BASIS = "553f62672353e782fff6708f9a11ecc7d972c146"
ACCEPTED_ARTIFACT = "7940a9bd8f26497c8e3050b8a31cf6d89c09dbd2934c8e8ead04f1b016ab14d2"
ACCEPTED_R_A = "37ef01978f1d4ea022870414965cf737e5fcbd4d3e48f377a1cf3083affa7457"
ACCEPTED_SEMANTIC = "ecc88817053d754911feab009c69e59ce68a89df6cfc7e0008a1da67f22e30b4"
ACCEPTED_REGISTER = "8ad1787633179ea82984b3738cb2427b48a304247b4673657e85c938f6450656"
ACCEPTED_INDEX = "517a3bbaf09dc2849220dcca4a2fc8a59a998fb932f1224bc477666938ade5cc"
ACCEPTED_INDEX_DIFF = "a6cd22b453c77b5176261fba589e034f0dc448e0d68f7de7ae0ef6b551557168"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=REPO)


def basis_bytes(path: str) -> bytes:
    return git("show", f"origin/main:{path}")


def prior_basis_bytes(path: str) -> bytes:
    return git("show", f"{PRIOR_BASIS}:{path}")


checks: list[str] = []
failures: list[str] = []


def check(condition: bool, label: str) -> None:
    (checks if condition else failures).append(label)


def verify_hash_manifest(path: Path, root: Path) -> tuple[int, list[str]]:
    count = 0
    bad: list[str] = []
    for raw in path.read_text().splitlines():
        if not raw:
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", raw)
        if not match:
            bad.append(f"malformed:{raw}")
            continue
        expected, rel = match.groups()
        target = root / rel
        if not target.is_file():
            bad.append(f"missing:{rel}")
        elif sha_file(target) != expected:
            bad.append(f"hash:{rel}")
        count += 1
    return count, bad


# Git basis and durable predecessor.
check(git("rev-parse", "origin/main").decode().strip() == BASIS, "origin/main exact basis")
check(
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", PRIOR_BASIS, "origin/main"],
        cwd=REPO,
    ).returncode
    == 0,
    "prior accepted basis is ancestor of current basis",
)
five_live_preimages = [
    "_DomainEngines/_DECISIONS/_REGISTER.md",
    "_DomainEngines/DOMAIN_ENGINE_INDEX.md",
    "_DomainEngines/_DECISIONS/D-T0-24_flow_a_root_runtime_identity_separation.md",
    "_DomainEngines/_DECISIONS/D-T0-23_shared_runtime_domain_convergence.md",
    "_DomainEngines/bridge/LOOP_RECEIPTS.md",
]
for rel in five_live_preimages:
    check(basis_bytes(rel) == prior_basis_bytes(rel), f"unchanged from prior basis: {rel}")
d24_path = "_DomainEngines/_DECISIONS/D-T0-24_flow_a_root_runtime_identity_separation.md"
d24 = basis_bytes(d24_path).decode()
check("**Status:** `RULED_EFFECTIVE`" in d24, "D-T0-24 is RULED_EFFECTIVE")
check(
    "**EffectiveSHA:** `4ac8348e0c15795f33bf2192b2964ee1347aca59`" in d24,
    "D-T0-24 effective identity",
)
for label, commit in [
    ("D-T0-24 PublicationSHA", "aed9ef5ea1df7e128739fb6363218f0cc237e248"),
    ("D-T0-24 EffectiveSHA", "4ac8348e0c15795f33bf2192b2964ee1347aca59"),
]:
    check(
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, "origin/main"],
            cwd=REPO,
        ).returncode
        == 0,
        f"{label} is ancestor of current basis",
    )
current_register_text = basis_bytes("_DomainEngines/_DECISIONS/_REGISTER.md").decode()
check(
    "| D-T0-24 |" in current_register_text
    and "EffectiveSHA `4ac8348e0c15795f33bf2192b2964ee1347aca59`" in current_register_text,
    "D-T0-24 register row remains current",
)

# Accepted rebuilt package and its R-A tranche.
check(sha_file(ACCEPTED / "ARTIFACT_HASHES.sha256") == ACCEPTED_ARTIFACT, "accepted package identity")
artifact_count, artifact_bad = verify_hash_manifest(ACCEPTED / "ARTIFACT_HASHES.sha256", ACCEPTED)
check(artifact_count == 32 and not artifact_bad, "accepted package 32/32 hashes")
check(sha_file(ACCEPTED / "01_R-A/TRANCHE_HASHES.sha256") == ACCEPTED_R_A, "accepted R-A tranche identity")
tranche_count, tranche_bad = verify_hash_manifest(
    ACCEPTED / "01_R-A/TRANCHE_HASHES.sha256", ACCEPTED / "01_R-A"
)
check(tranche_count == 7 and not tranche_bad, "accepted R-A tranche 7/7 hashes")

# Package-local accepted semantic bytes.
check(sha_file(PACKAGE / "ACCEPTED_INPUT.md") == ACCEPTED_SEMANTIC, "accepted semantic input exact")
check(sha_file(PACKAGE / "candidate_live/REGISTER.md") == ACCEPTED_REGISTER, "accepted register postimage exact")
check(sha_file(PACKAGE / "candidate_live/DOMAIN_ENGINE_INDEX.md") == ACCEPTED_INDEX, "accepted index postimage exact")
check(sha_file(PACKAGE / "DOMAIN_ENGINE_INDEX.diff") == ACCEPTED_INDEX_DIFF, "accepted index diff exact")

# Current preimages and absence conditions.
with (PACKAGE / "PREIMAGE_MANIFEST.csv").open(newline="") as handle:
    preimages = list(csv.DictReader(handle))
for row in preimages:
    role, rel, expected, state = row["Role"], row["Path"], row["SHA256"], row["State"]
    if role == "BASIS":
        continue
    if state == "EXISTS":
        try:
            actual = sha_bytes(basis_bytes(rel))
        except subprocess.CalledProcessError:
            check(False, f"preimage exists: {rel}")
        else:
            check(actual == expected, f"preimage hash: {rel}")
    elif state == "ABSENT":
        exists = (
            subprocess.run(
                ["git", "cat-file", "-e", f"origin/main:{rel}"],
                cwd=REPO,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        )
        if rel.endswith("/"):
            listing = git("ls-tree", "-r", "--name-only", "origin/main", "--", rel).decode().strip()
            exists = bool(listing)
        check(not exists, f"surface absent: {rel}")

# Next-free IDs and receipt.
decision_listing = git(
    "ls-tree", "-r", "--name-only", "origin/main", "--", "_DomainEngines/_DECISIONS"
).decode()
decision_ids = [int(value) for value in re.findall(r"/D-T0-(\d+)_", decision_listing)]
check(max(decision_ids) == 24 and 25 not in decision_ids, "D-T0-25 is next free decision")
receipts = basis_bytes("_DomainEngines/bridge/LOOP_RECEIPTS.md").decode()
receipt_ids = [
    int(value)
    for value in re.findall(r"(?m)^-\s+\*\*\d{4}-\d{2}-\d{2}\s+—\s+Receipt\s+(\d+)\*\*", receipts)
]
check(max(receipt_ids) == 28 and 29 not in receipt_ids, "Receipt 29 is next free bridge receipt")

# Candidate changes are exactly the accepted R-A transformations.
current_register = basis_bytes("_DomainEngines/_DECISIONS/_REGISTER.md").decode().splitlines()
candidate_register = (PACKAGE / "candidate_live/REGISTER.md").read_text().splitlines()
added_register = [line for line in candidate_register if line not in current_register]
removed_register = [line for line in current_register if line not in candidate_register]
check(
    len([line for line in candidate_register if line.startswith("| D-T0-25 |")]) == 1,
    "candidate register has one D-T0-25 row",
)
check(
    not removed_register
    and [line for line in added_register if line.strip()]
    == [line for line in candidate_register if line.startswith("| D-T0-25 |")],
    "register semantic change is only D-T0-25 row",
)
current_index = basis_bytes("_DomainEngines/DOMAIN_ENGINE_INDEX.md")
diff_check = subprocess.run(
    ["git", "apply", "--check", "--cached", str(PACKAGE / "DOMAIN_ENGINE_INDEX.diff")],
    cwd=REPO,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
# The index diff was generated from the same bytes; direct postimage checks are
# authoritative because the live checkout may not equal origin/main.
check(
    current_index != (PACKAGE / "candidate_live/DOMAIN_ENGINE_INDEX.md").read_bytes(),
    "index candidate changes current preimage",
)
index_diff = (PACKAGE / "DOMAIN_ENGINE_INDEX.diff").read_text()
check(
    index_diff.count("@@") == 2
    and "Shared runtime convergence" in index_diff
    and "D-T0-23" in index_diff,
    "index diff is bounded to accepted shared-runtime paragraph",
)

# Accepted-input anchor map.
with (PACKAGE / "SOURCE_ANCHOR_MAP.csv").open(newline="") as handle:
    anchors = list(csv.DictReader(handle))
check(len(anchors) == 3, "three accepted-input source anchors")
accepted_text = (PACKAGE / "ACCEPTED_INPUT.md").read_text()
for row in anchors:
    check(row["DeclaredAnchor"] in accepted_text, f"declared anchor present: {row['DeclaredAnchor']}")
    local = PACKAGE / row["LocalPackagePath"]
    source = Path(row["AcceptedSourcePath"])
    check(local.is_file() and source.is_file(), f"anchor files exist: {row['LocalPackagePath']}")
    if local.is_file() and source.is_file():
        check(
            sha_file(local) == row["ExpectedSHA256"] == sha_file(source),
            f"anchor exact bytes: {row['LocalPackagePath']}",
        )

# Exact write envelope and P-A exclusion.
with (PACKAGE / "WRITE_SURFACES.csv").open(newline="") as handle:
    surfaces = list(csv.DictReader(handle))
expected_surfaces = {
    "_DomainEngines/_DECISIONS/_REGISTER.md",
    "_DomainEngines/_DECISIONS/D-T0-25_d_t0_23_residual_classification.md",
    "_DomainEngines/DOMAIN_ENGINE_INDEX.md",
    "_DomainEngines/bridge/LOOP_RECEIPTS.md",
    "_DomainEngines/applications/OD7-G3_D-T0-25_R-A/",
}
check(len(surfaces) == 5 and {row["Path"] for row in surfaces} == expected_surfaces, "exact five-surface envelope")
packet_text = (PACKAGE / "APPLICATION_PACKET.md").read_text()
check("Receipt 29 is included as a named additive surface" in packet_text, "receipt mismatch is explicit")
check("P-A remains separately gated" in packet_text, "P-A exclusion is explicit")
generated_outputs = {
    "ARTIFACT_HASHES.sha256",
    "RUN_SUMMARY.md",
    "VALIDATION_RESULT.json",
}
for path in PACKAGE.rglob("*"):
    if (
        path.is_file()
        and path.suffix != ".diff"
        and path.relative_to(PACKAGE).as_posix() not in generated_outputs
    ):
        data = path.read_bytes()
        check(not re.search(rb"[ \t]+\n", data), f"no trailing whitespace: {path.relative_to(PACKAGE)}")
        check(not data.endswith(b"\n\n"), f"single terminal newline: {path.relative_to(PACKAGE)}")

# Candidate-set manifest, when present.
candidate_manifest = PACKAGE / "CANDIDATE_SET_MANIFEST.sha256"
if candidate_manifest.exists():
    candidate_count, candidate_bad = verify_hash_manifest(candidate_manifest, PACKAGE)
    check(candidate_count == 13 and not candidate_bad, "candidate manifest 13/13 hashes")

result = {
    "schema_version": "1.0",
    "basis": BASIS,
    "verdict": "PASS" if not failures else "FAIL",
    "passed": len(checks),
    "failed": len(failures),
    "checks": checks,
    "failures": failures,
    "notes": [
        "No governed repository byte was written.",
        "P-A and D-T0-26 were excluded from preparation.",
        "Receipt 29 is an explicit owner-gated reconciliation of the accepted planning mismatch.",
        "The live checkout may contain unrelated state; all governed preimages were read from origin/main.",
    ],
}
print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if not failures else 1)
