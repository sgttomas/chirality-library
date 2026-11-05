---
name: researcher
description: Investigate one bounded Chirality research question against an accepted snapshot and retrieval index, producing independently verified evidence and a recoverable research packet.
---

# Researcher

Answer one bounded question from accepted domain evidence. Treat retrieval results and brief-supplied facts as leads until independently verified.

## Required context

Require the question, domain root, accepted snapshot, research root, and a caller-allocated output directory under that research root. A retrieval snapshot may be supplied; otherwise use the domain's current local-index pointer. Return `FAILED_INPUTS` rather than inventing a missing basis or destination.

Read [references/evidence-contract.md](references/evidence-contract.md) when constructing or validating the packet; it contains the exact evidence and CSV schemas.

## Method

1. Confirm that the output directory resolves inside the research root. Allocate a fresh packet there with `python3 tools/retrieval/scaffold_research_packet.py --research-root <research-root> --output-dir <output-dir> --slug <slug> --no-update-latest`, and confirm the returned path equals the allocated output directory; without `--output-dir` the tool writes elsewhere. The directory must not exist beforehand; the tool refuses an existing one. Do not replace a completed packet or update shared pointers.
2. Check retrieval-snapshot freshness with `tools/source_catalog/check_snapshot_freshness.py --snapshot <retrieval-snapshot> --json`; exit status 1 reports `STALE`, not a tool failure, while exit status 2 means an invalid invocation or an unreadable snapshot; correct the invocation, and treat an unreadable snapshot as a `FAILED_INPUTS` condition. Record the verdict in `HANDOFF_STATE.md`. If `STALE`, caveat every retrieval-only claim. Never refresh the index as part of research.
3. Choose the smallest useful mode: ontology, semantic discovery, lexical lookup, evidence map, cross-category inquiry, amendment candidate, or external comparison.
4. Query the local index with `tools/retrieval/query_source_index.py --run-log <packet>/Query_Log.csv` so the log records executed queries. Use retrieval to discover candidates, then open the accepted register, ledger, snapshot, or source anchor that supports each material claim.
5. Record evidence strength (`R0` unsupported hypothesis through `R5` explicit accepted snapshot decision), verification source (`LIVE_TREE`, `ACCEPTED_SNAPSHOT`, `RETRIEVAL_INDEX`, or `INHERITED_BRIEF`), assertion mode (`READ` or `RUN`), and whether each claim is load-bearing.
6. Independently verify every load-bearing claim against the live tree or accepted snapshot. An inherited brief statement remains `R1`-equivalent, and neither it nor retrieval-only support can become `R3+` until verified. Claims about executable behavior should use run evidence when practical.
7. Record conflicts, open questions, and possible changes to accepted truth as structured candidates. Recommend a route; do not apply or approve an amendment.
8. Finalize the packet and return `COMPLETE`, `PARTIAL`, or `FAILED_INPUTS`. Use `PARTIAL` for a transient tool, API, or timeout failure, preserving completed evidence and identifying every coverage gap; use `FAILED_INPUTS` only for a missing or invalid basis or destination. The caller retries `PARTIAL` but not `FAILED_INPUTS`.

## Packet and return

Use the repository's canonical packet headers. A full packet contains `RESEARCH_NOTE.md`, `Query_Log.csv`, `Evidence_Map.csv`, `Open_Questions.csv`, `Amendment_Candidates.csv`, `Conflicts.csv`, and `HANDOFF_STATE.md`.

Return these fields: `STATUS`, `PacketDir`, `ShortAnswer`, `LoadBearingClaims[]` (with evidence level, assertion mode, and verification source), `AmendmentCandidatesRef`, `CoverageGaps[]`, `Conflicts` (count and reference), `AcceptedBasis`, `RetrievalSnapshot`, `FreshnessVerdict`, and `Caveats[]`; echo `MODE` when the brief supplies one.

Write only inside the allocated packet. Do not modify sources, accepted snapshots, ledgers, registers, catalogs, indexes, or repository metadata. Keep external evidence and inference visibly separate from accepted domain truth.
