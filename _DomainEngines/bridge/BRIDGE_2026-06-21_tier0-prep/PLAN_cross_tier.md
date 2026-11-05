# PLAN — Tier-0 Bridge: gate sequence, integration staging, who-does-what (PROPOSAL)

A **proposed** sequence for owner confirmation (D-T0-05). It maps onto the persona's PROTOCOL Fn 1–8 / Gates 1–5 — no parallel scheme is invented. Sequencing is non-negotiable: **owner rulings first, then each project authors its OWN execution slice.** Tier-0 never writes a project's slice.

> Reconciled 2026-07-02 (agent decision, owner-directed bridge Loop 1 —
> `_DomainEngines/bridge/WORKPLAN_2026-07-02_bridge_loop.md`): tier-1 row items
> marked DONE where the register/tree records completion (D-T0-01 ruled; D-APP-45
> conformance tranche + REF-008 pins landed 2026-06-22; FM-01..04 applied at
> `77a327727`), and the headless CLI entrypoint removed from the tier-2 prep lane —
> DEC-042 (`SOFTWARE_DECOMP.md:612`) does not sanction it. Cited sources govern.

---

## Gates (PROTOCOL-mapped)

| Gate | PROTOCOL fn | Purpose | Human act |
|---|---|---|---|
| **G1** | Fn 1 (Intake) | Confirm classification; rule **D-T0-01** (precedence) + **D-T0-02** (ProfileStatus) | rule precedence + enum |
| **G2** | Fn 2 (Profile & Boundary) | Adopt the profile `DRAFT→VALIDATED→ADOPTED` with the APEGA ceiling baked in; rule **D-T0-06** | adopt profile + protected-write policy |
| **G3** | Fn 3 (Artifact Discovery) | Confirm readable artifacts + protected-path assumptions (per ARTIFACT_INVENTORY) | confirm boundary |
| **G4** | Fn 4 (Adapter Planning) | Approve a read-only-first tool plan (validate/summarize/headless run); rule **D-T0-03** staging | approve invocation plan |
| **G5** | Fn 6 (Operation Proposal) | Per-operation, per-risk-class application; mutating `operation_applier.apply` is human-confirmed | accept/reject each proposal |

Data-residency (**D-T0-04**) and contract-versioning (**D-T0-07**) are cross-cutting and must be ruled before G4/live work.

---

## INTEGRATION_LEVEL staging (RECOMMENDATION — subordinate to D-T0-03)

| Level | Token | What advances | Risk posture |
|---|---|---|---|
| L0 | `MANUAL_BRIDGE` | today: human exports; agents read/organize | safe default |
| L1 | `READ_ONLY` | read manifests / run-summaries; `rule_check_runner` + `completeness_checker` read-only | low — advance early |
| L2 | `DOMAIN_CONTROLLED_WRITE` | **validated-kernel** headless runs (needs CLI entrypoint — TOOLMAKER) | low-moderate — advance after L1 |
| L3 | `OPERATION_PROPOSAL` | proposals **per operation risk class**, not wholesale; `apply` human-gated | per-operation; gated ×4 |
| L4 | `EXTERNAL_RESULT_STATE` | future only | — |

**Bind the human gate to the EXISTING engineering lifecycle, not a new one.** Worker works **up to `HUMAN_REVIEW_REQUIRED`**; only the engineer elevates to `HUMAN_APPROVED_FOR_PROJECT` (external, **SHA-bound** — K-AUTH-2; `schemas/model.schema.yaml:22-32`). This aligns the deliverable lifecycle (`CHECKING→ISSUED`) and the warrant lifecycle (`REVIEWED→AUTHENTICATED`) with the engine's own status machine.

---

## Who-does-what (strict ordering; tiers do not author each other's slices)

| Tier | Owner | Authors (after owner rulings) | Constraint today |
|---|---|---|---|
| **tier-0** | DOMAIN_ENGINE (me) | persona + contract + K-DOMAIN promotion + APEGA ceiling + `domains/` packs | doc-only; shared-root only; canon edits gated (FM-01..04) |
| **tier-1** | app-dev (`WORKING_ITEMS`) | (1) PKG-10 DEL-10-01..05 re-draft to ruled canon — **DONE** (D-T0-01 ruled; D-APP-45 conformance tranche 2026-06-22); (2) `AGENT_DOMAIN_ENGINE.md` @ `77a327727` pinned into DEL-10-01/03 `_REFERENCES.md` — **DONE** (REF-008); (3) Flow-A package versioning — D-T0-07 ruled; awaiting **D-APP-45** (AWAITING_RULING); (4) ProfileStatus/OperationProposal conformance — **DONE** (FM-01..04 applied @ `77a327727`; result-schema cross-refs recorded 2026-07-02); (5) Fence-3 source-type + MCP-tool drafts (doc-only until D-T0-08) | internal refactor **green**; external publish = F2, source types/MCP = F3 — **gated** |
| **tier-2** | piping (`WORKING_ITEMS`) | validate-only trust-probe spike; surface-reconciliation gap list. (Headless CLI entrypoint removed from this lane 2026-07-02: DEC-042 does not sanction it — un-built TOOLMAKER handoff, `open_pipe_stress.yaml:103-107`, brief stub `TOOLMAKER_BRIEF-headless_cli_entrypoint.md`; needs its own piping-loop decision.) | **DEC-042 prep only** (items 1–2 open; item 3 done per DEC-043); **D-21 held** (prep permitted post-D-27); no R7, no live binding |

## Live build — gated by 4 asymmetric conditions (frame + gate; do NOT plan)

1. **tier-0 adoption** (this work → owner rulings).
2. **app-dev fence #3** (R7 domain-engine impl; PKG-10 doc-only until opened).
3. **piping D-21** (held to the R4/R5 lead-up; DEC-042).
4. **DEC-041 automation condition** (**written** at piping `SOFTWARE_DECOMP.md:611`). DEC-041 adopts **harness-as-versioned-packages** (not a stack refactor / re-implementation) for how the v0.2/R7 program consumes the app-dev harness, and gates execution behind D-21 **plus** an automation condition: the harness contract must be a **consumable, highly-automated package pull** (SHA-pinned, no manual cross-repo toil). Success criterion for this gate: the flow-A contract version is pinned and referenced in both repos without hand-copying — see D-T0-07.

Only **prep** is green today. The live build is framed and gated, not planned.

---

## Green-today vs gated (app-dev fence map, verified `D-APP-39_RULING:21-27`)

| Action | Fence | Status |
|---|---|---|
| Extract harness lib into a dependency-free **internal** package | none | GREEN — prep |
| Publish that package externally | F2 | GATED |
| Stand up `DomainEngineProfile`/`OperationProposal` **types in `frontend/src`** | F3 | GATED (doc contracts editable) |
| Add domain MCP tools (e.g. `piping_propose_operation`) | F3 | GATED |
| Live binding / private-data egress to a cloud agent | F1 | GATED (most irreversible) |
| `CHECKING→ISSUED` | F4 | GATED (one-way; deferred) |
