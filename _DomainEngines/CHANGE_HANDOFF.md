# CHANGE Handoff — commit the tier-0 `_DomainEngines/` package (PROPOSAL)

**From:** DOMAIN_ENGINE (tier-0). **To:** CHANGE. **Date:** 2026-06-21.
DOMAIN_ENGINE does not stage/commit/push — this is the handoff CHANGE acts on. Nothing here authorizes a force-push or any edit outside `_DomainEngines/`.

## Purpose

Commit the tier-0 OpenPipeStress bridge prep package **so the owner's 8 rulings (2026-06-21) become SHA-bound** (K-AUTH-2) and citable by the app-dev / piping RES-RECONCILE agents.

## Git hygiene

- **Branch first** — session started on `main` (the default). Do **not** commit to `main`. Suggested branch: `codex/domain-engine-tier0-bridge`.
- **Scope:** stage **`_DomainEngines/` only**. Exclude `.DS_Store`. Do **not** stage `init/init-prompt.md`, `execution/`, or `projects/chirality-piping/plans/artifacts/` (pre-existing, unrelated working-tree entries — leave untouched).
- No merge/rebase/force. Push behind-guard. Concurrent loops are live.
- Verify before staging: `git status --short --untracked-files=all -- _DomainEngines/` and `git add` only that path.

## File list, grouped by artifact role (all new; all PROPOSAL / unratified)

**Control-area index & pointers (mutable):**
- `_DomainEngines/DOMAIN_ENGINE_INDEX.md`
- `_DomainEngines/_LATEST.md`
- `_DomainEngines/RULINGS_PUBLISHED.md` — the 8 rulings + RES-RECONCILE (green-light signal)
- `_DomainEngines/NEXT_INSTANCE_PROMPT.md` — sequencing
- `_DomainEngines/CHANGE_HANDOFF.md` — this file (self-referential)

**Domain Engine Profile (DRAFT — not validated, not adopted):**
- `open_pipe_stress.DRAFT.yaml` (historical filename, since removed from the profiles directory) — *historical: as committed 2026-06-21; since VALIDATED → ADOPTED (owner Gate 2, D-T0-06) and renamed to `profiles/open_pipe_stress.yaml` 2026-07-01 per D-GOV-06*

**Decision records (owner rulings recorded; SHA binds at this commit):**
- `_DomainEngines/_DECISIONS/_REGISTER.md`
- `_DomainEngines/_DECISIONS/D-T0-01_precedence.md` … `D-T0-08_fence3_sequence.md` (8 files)

**Prep snapshot (immutable run record) — `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/`:**
- `Brief.md`, `RUN_SUMMARY.md`, `PROFILE_STATUS.md`, `ARTIFACT_INVENTORY.md`
- `BRIEF_human_decisions.md`, `PLAN_cross_tier.md`, `CONTRACT_DIRECTION.md`, `Handoff_State.md`
- `TOOLMAKER_BRIEF-profile_schema_validator.md`, `TOOLMAKER_BRIEF-headless_cli_entrypoint.md`

**Gated canon DIFFS (proposals — NOT canon edits; not applied) — `.../framework_maintenance/`:**
- `FM-01_ProfileStatus_enum_fix.md`, `FM-02_K-DOMAIN_promotion_to_root.md`, `FM-03_OpenPipeStress_example_binding_reauthor.md`, `FM-04_OperationProposal_merge.md`

> Expected: ~29 content files under `_DomainEngines/` (plus an empty `proposals/open_pipe_stress/` dir). CHANGE confirms the exact set via `git status` and excludes any `.DS_Store`.

## Generated/derived vs human-accepted

- **No framework canon is edited** (`agents/`, root `docs/`, `AGENTS.md` untouched). FM-01..04 are *reviewable diffs*, not applied — committing them does not change canon.
- **No project subtree is touched** (`projects/**` untouched).
- The **owner's rulings** are recorded (in-session 2026-06-21); this commit is what SHA-binds them. The profile remains **DRAFT** and **not ADOPTED**; no professional status, approval, or external-validation is claimed.

## Closure status & remaining work (not blocking this commit)

- **Done:** tier-0 prep + adversarial verification + all 8 rulings recorded.
- **Pending (other owners, post-commit):** apply FM-01..04 via a human-gated framework-maintenance pass; **RES-RECONCILE** (app-dev F1 + piping OPS-K-PRIV-1, via their loops); build the profile-schema validator (TOOLMAKER) before any `VALIDATED`; app-dev / piping author their slices.
- **Rerun requirements for this package:** none.

## Recommended commit message (PROPOSAL)

```
domain-engine: tier-0 OpenPipeStress bridge prep + owner rulings (2026-06-21)

Add _DomainEngines/ control area: DRAFT open_pipe_stress profile, the tier-0
bridge prep snapshot (BRIEF/PLAN/contract-direction + readiness verdict),
8 owner-ruled decision records (D-T0-01..08), 4 gated canon diffs (FM-01..04,
not applied), 2 TOOLMAKER requirement briefs, and the RULINGS_PUBLISHED signal.

All artifacts are PROPOSAL/unratified; no framework canon or project subtree is
modified. Rulings bind to this SHA (K-AUTH-2). Profile stays DRAFT/not-ADOPTED.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
```
