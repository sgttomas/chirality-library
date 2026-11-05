# HELPS_HUMANS proposal packet — PEC tooling/skill-contract consolidation

**Date:** 2026-07-25 · **Author:** HELPS_HUMANS (Agent 1), managed by HELP_HUMAN
**Status:** OPEN — items P1–P7 await explicit owner approval. Nothing in this
packet has been applied.
**Scope:** owner-directed OI-013 cleanup plus intake/disposition of the routed
8-item request at
`projects/pec/execution/_Coordination/REQUEST_2026-07-25_helps_humans_tooling_consolidation.md`.
**Write containment:** this checkout only. No `projects/pec/**` surface was
written. No Git commit was made.

## Revision

**v2, 2026-07-25** — revised under Agent 0's fan-in disposition of a sealed
adversarial refutation (3 CRIT / 6 MAJ / 3 MIN, all accepted). Corrections of
record, because each was a *false basis*, not a presentation choice:

- **P5** claimed two live SOFTWARE documents; there are **three**. Its
  normalization rule resolved only 1 of 4 bindings against the live `pec`
  document and would have been worse than the status quo. Now carries an
  explicit normalization spec, verified against all three (§3).
- **P5 §5** claimed the `pec` document's own `§` cross-references were defective
  and needed PEC repair. **They are correct**, and are independent corroboration
  that the agent tables are wrong. The claim is withdrawn and inverted; the
  coordination notice no longer requests that repair.
- **P1 §2d** claimed `STATUS_POLICY` had "zero hits anywhere" and
  `DECOMP_VARIANT` was "only an enum". Both false — a live three-value
  `STATUS_POLICY` vocabulary exists in `semantic-matrix-build`/`lens-register`,
  and `DECOMP_VARIANT` is a protocol variable in five agent files. The
  two-value proposal is withdrawn in favour of the existing vocabulary.
- **P1 §2e** placed QA item 4 in the CONVERT-only set while arguing it was
  mode-agnostic, and gave two different conversion-only counts. Resolved: item 4
  is mode-agnostic; the partition is three-way and totals 18.

## Claim calibration

Every finding below is either **VERIFIED** (reproduced by execution or read at
byte level in this run) or **ASSERTED-UPSTREAM** (carried from the routed
request or a PEC fan-in record and not independently re-derived here). Each
proposal file marks its own basis. Structural PASS of a validator is not
semantic acceptance of the registers it scans.

## Disposition matrix

| # | Request item | Disposition | Where |
|---|---|---|---|
| 1 | scope-of-work INIT-mode companion-file branches | **ADOPTED-PROPOSED (AMENDED)** — adopted, and widened: the request named 3 files; the INIT gap is in 4 (QA_CHECKS item 3 is actively wrong, and 9 of 18 QA items are conversion-only — see P1 §2e for the reconciled three-way partition). Also found: `TOOL_POLICY.md` has 8 steps, not 7. | `P1_sow_init_mode_branches.md` |
| 2 | **OI-013 — no durable register validator** | **ADOPTED-IMPLEMENTED** | `tools/validation/validate_decomposition_registers.py` + `test_validate_decomposition_registers.py`; registry row in `tools/REGISTRY.md` |
| 3 | `count_workspace_state.sh` history-substring defect | **ADOPTED-PROPOSED** — confirmed and quantified; fix is caller-free | `P2_count_workspace_state_fix.md` |
| 4 | `validate_semantic_pipeline_scope.py` missing `--step init` | **ADOPTED-PROPOSED** | `P3_semantic_pipeline_init_guard.md` |
| 5 | AUDIT_DECOMP contract inconsistencies | **ADOPTED-PROPOSED (AMENDED)** — the request's `CheckNumber 1–11 → 12` framing is insufficient: check `9b` is non-integer, so the declared *type* must change too. Two further undocumented emissions found beyond the two named fields. | `P4_audit_decomp_contract_repairs.md` |
| 6 | OI-A — hard-coded `SOFTWARE_DECOMP` section numbers | **ADOPTED-PROPOSED (AMENDED)** — escalated from "lower priority": all four distinct SOFTWARE citations (across five `§`-bearing cells; `Change Log §8` is in `AGENT_SCOPE_CHANGE.md` only) are currently wrong, not merely fragile. Carries an explicit heading-normalization spec verified against **three** live SOFTWARE documents. | `P5_heading_text_binding.md` |
| 7 | No upstream-ID citation convention for INIT contracts | **ADOPTED-PROPOSED (AMENDED)** — adopted as a contract rule; the request's `DEL-NN-NN/REQ-NNN` qualified form is **not currently safe** (verified: it is extracted as a bare local ref and fails validation), so the tool must change with the contract or the form must not be blessed. | `P6_sow_upstream_id_citation.md` |
| 8 | `derive_review_checklist.py` row-scoped AC→VER union | **ADOPTED-PROPOSED** — recommended as a contract row-semantics rule **plus** a deriver warning, not a linkage change (a linkage change would break QA item 18 byte-identity for accepted contracts). | `P7_sow_matrix_row_semantics.md` |
| — | B8 boundary-owner validator candidate (fan-in §3.1) | **DECLINED for this validator; ADOPTED-PROPOSED elsewhere** — see below. | `P7_sow_matrix_row_semantics.md` §4 |

Nothing was declined outright.

## The B8 boundary-owner rule — explicit disposition

`BATCH_B8_FANIN.md` §3.1 nominated "every act enumerated in a
boundary-exclusion requirement resolves to a named owner in the cited claim"
as a validator candidate for the OI-013 consolidation.

**It does not belong in `validate_decomposition_registers.py`.** That tool's
input domain is CSV registers; the boundary-owner rule reads `ScopeOfWork.md`
prose — requirement bodies and claim bodies — and its "enumerated act" step is
a semantic segmentation of natural language, not a deterministic parse. Putting
it in a register validator would give one tool two input grammars and one
undeclared semantic dependency.

**Recommended home:** `tools/scope_of_work/`, alongside the existing contract
tooling that already parses SOW sections and IDs (`common.py` supplies the
section/ID machinery). Even there, only the *resolution* half is deterministic
("each act's cited owner ID exists and is a defined ID"); the *enumeration*
half ("what counts as an act in this sentence") is semantic and belongs in the
`scope-of-work` skill's QA method, dispatched per contract. The recurrence
record (B6, B7, B8 — three appearances) is good skill-candidate evidence.
This is recorded as a proposal, not built, because it needs a separate design
pass and the owner's ruling on the semantic/deterministic split.

## What was implemented (item 2 only)

| Path | Status |
|---|---|
| `tools/validation/validate_decomposition_registers.py` | NEW, additive |
| `tools/validation/test_validate_decomposition_registers.py` | NEW, 29 tests, all passing |
| `tools/REGISTRY.md` | one added row; no existing row altered |

The validator scans `1_Working`/`2_Checking`/`3_Issued` (a register does not
drop out of the corpus when a deliverable is promoted), treats OS-level read
failures as operational exit 2 rather than findings, and requires `EvidenceFile`
to name a relative regular file.

**Honest-empty waivers.** A dependency can be real and have no quotable source
text. Without a declared route for that, "re-run to exit 0" would be an
instruction to invent a quote. A register may therefore sit beside an optional
`Dependencies_EvidenceWaivers.csv`
(`DependencyID, WaivedCheck, Rationale, DeclaredBy, DeclaredOn`). Only `EVQ-003`
and `EVQ-004` are waivable; a valid waiver downgrades that row to WARNING and
counts it under `waived`, but never hides it. Waivers are themselves checked —
stale (`EVQ-007`), thin/placeholder rationale (`EVQ-008`), or malformed/unknown
(`EVQ-009`) are ERRORs, and `--strict` still fails on the warnings. Exit 0
therefore means every row carries real evidence *or* a declared, attributed,
substantively-reasoned exception.

No live component was removed or altered. `validate_dependencies_schema.py` is
**reused, not replaced** — the new tool imports its `validate()` for the `SCH`
family, so the v3.1 schema contract stays in one place. `analyze_dep_closure.py`
is untouched; its "Evidence coverage" metric remains what it always measured
(EvidenceFile presence). Callers of both are unaffected.

## Handoff state

- **Accepted upstream basis:** the routed request (2026-07-25) and the
  D-PEC-63 wave fan-in records B4–B8 as read-only evidence.
- **Changed authority surfaces:** none. `tools/REGISTRY.md` gained a
  descriptive row for a new tool; no contract, agent, or skill text changed.
- **Derivative status:** this packet is a derivative package. It cites the
  routed request and the live file text as of this run. It is not decomposition
  truth and does not close OI-013 for the PEC loop — see next.
- **Blockers:** P1–P7 are blocked on owner approval. The PEC data repair is
  blocked on nothing in this repo; it is a PEC-loop act.
- **Rerun requirement:** `python3 -m pytest tools/validation/ -q` after any
  change to the new tool or to `validate_dependencies_schema.py`.
- **PEC closure gate (restated after R-04):** the follow-on is *not* "re-run to
  exit 0" taken naively. It is: zero `EVQ-001`; every `EVQ-003`/`EVQ-004` row
  either given a real locus and quote, or covered by a declared waiver with an
  attributed, substantive rationale. Exit 0 is then a truthful gate, because the
  waiver mechanism makes the honest-empty case expressible.
- **Next lawful owner:** the human, via HELP_HUMAN, for P1–P7 approval and for
  routing the coordination notice to the PEC loop.
