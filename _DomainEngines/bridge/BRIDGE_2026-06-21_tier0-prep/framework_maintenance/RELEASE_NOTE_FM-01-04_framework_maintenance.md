# Release Note - FM-01..04 Framework-Maintenance Draft Application

**Status:** APPLIED and PUBLISHED at `77a327727` (committed + pushed to origin/main; owner-directed 2026-06-21).
**Applying SHA:** `77a327727`.
**Drafted:** 2026-06-22 by HELPS_HUMANS framework-maintenance pass.
**Draft base HEAD observed:** `16e723f45813`.

## Authorization and Provenance

| Item | Basis |
|---|---|
| FM-01 | `D-T0-02` owner ruling: keep 7-token `ProfileStatus` enum. |
| FM-02 | `D-T0-01` owner ruling: framework-root persona canonical as new framework policy; promote K-DOMAIN to root. |
| FM-03 | Correctness fix: current `AGENT_DOMAIN_ENGINE.md` OpenPipeStress example diverged from verified piping layout. |
| FM-04 | `D-T0-01` owner ruling: merge app-dev's richer generic OperationProposal shape up into canon. |
| Tier-0 latest commit cited by handoff | `6c2366fff`. |
| Tier-0 package/rulings commit cited by handoff | `6e70b5aac`. |

## Changed Canon

- `agents/AGENT_DOMAIN_ENGINE.md`
  - Reconciled `ProfileStatus` to `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN` at intake, profile validity, integration-record, and handoff-state sites.
  - Replaced the prose-only OperationProposal validity criteria with a structured generic field contract, including lifecycle `draft | ready_for_review | accepted | rejected | applied`.
  - Added generic `operation_risk_class: engine_checkable | engine_silent` and `provenance_on_judgment_values` requirements.
  - Added profile-level hooks for validate/apply result schemas and deterministic-check result schemas.
  - Re-authored the OpenPipeStress example binding to the verified schema-driven layout: `core/**`, `schemas/**`, engine-owned project store, and `core/handoff/**`; no `project.ops.yaml` or static `states/`, `runs/`, `comparisons/` tree.
- `docs/CONTRACT.md`
  - Added framework-root `K-DOMAIN-1..4` under new section `1.12 Domain Engine Integration`.
  - Updated the invariant count from 23 to 27 and subsection count from 11 to 12.
  - Added K-DOMAIN rows to the K-* index and enforcement summary.

## Gate and Non-Claims

These edits are **published** at `77a327727` but are **not yet ratified governance** — root `docs/CONTRACT.md` is DRAFT-pending-ratification per its own header, and its K-DOMAIN additions ride that broader ratification. This note does not claim professional approval, external validation, profile adoption, or an accepted engineering state. `K-AUTH-1` and `K-AUTH-2` apply; approval binds to the published SHA `77a327727`.

## Follow-Ons Deferred to App-Dev Loop

- Annotate `projects/chirality-app-dev/docs/CONTRACT.md` K-DOMAIN-1..4 as specializing framework `docs/CONTRACT.md` section 1.12 and not weakening it.
- SHA-pin the ruled `agents/AGENT_DOMAIN_ENGINE.md` revision into app-dev DEL-10-01/03 `_REFERENCES.md` after CHANGE publishes the approved canon.
