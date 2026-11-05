# RUN_SUMMARY — Tier-0 Bridge Prep

**Status:** PARTIAL (prep complete; 7 owner decisions open; 4 canon edits gated).
**Date:** 2026-06-21. **Persona:** DOMAIN_ENGINE. **Next owner:** HUMAN.

## What this run did

1. Read the tier-0 operative core first-hand (PROTOCOL Fn 1–8, SPEC, Permission Map, Minimal Profile Shape) + the restored root governance set.
2. Verified both repos + decision records + root second-pass via 8 read-only agents.
3. Formed an independent view, then challenged both supplier contributions against it.
4. Authored: BRIEF (7 framed decisions), PLAN (4-gate + staging + tier map), CONTRACT_DIRECTION, a DRAFT profile, 4 gated canon diffs, 7 decision stubs.

## Files written (all under `_DomainEngines/`, all PROPOSAL)

- `DOMAIN_ENGINE_INDEX.md`, `_LATEST.md`, `NEXT_INSTANCE_PROMPT.md` (sequencing)
- `profiles/open_pipe_stress.DRAFT.yaml`
- `bridge/BRIDGE_2026-06-21_tier0-prep/{Brief,RUN_SUMMARY,PROFILE_STATUS,ARTIFACT_INVENTORY,BRIEF_human_decisions,PLAN_cross_tier,CONTRACT_DIRECTION,Handoff_State}.md`
- `bridge/.../framework_maintenance/FM-0{1..4}_*.md`
- `bridge/.../TOOLMAKER_BRIEF-{profile_schema_validator,headless_cli_entrypoint}.md`
- `_DECISIONS/_REGISTER.md` + `D-T0-0{1..8}_*.md`

## Tools invoked / mutations

None. No domain tool invoked; no model mutation; no protected path written; no git.

## READINESS VERDICT (explicit deliverable): PROCEED-WITH-FLAGS

The recursive blind spot of prior rounds (architecting from the persona header+ladder without the operative core) is **closed** — the operative core was read first-hand and cross-checked against both repos' real code/schemas/decisions. No previously-unread **governing layer** reshapes the deliverable. The build PLAN is authorable now (and is authored here) as PROPOSAL.

**New layer surfaced (incorporated; strengthens the result):** root governance was **restored since 2026-06-15** — root `docs/{CONTRACT,TYPES,SPEC,DIRECTIVE,PLAN}.md` now exist as **DRAFT pending ratification**. The prompts' Step-A list predates this. It supplies the decisive two-layer precedence rule (`docs/PLAN.md:17`, `docs/CONTRACT.md:9`, K-AGENTS-1 `:123`).

**Corrections to supplier-carried claims (the challenge payoff):**

1. **DEC-041 is NOT missing.** It is canonically defined in piping `execution/_Decomposition/SOFTWARE_DECOMP.md:611` (harness-as-versioned-packages; gated behind D-21 + automation condition; 2026-06-18). app-dev reported it missing because it lives in piping's tree → cross-repo visibility gap, not a missing decision.
2. **The persona's OpenPipeStress Example Binding (`AGENT_DOMAIN_ENGINE.md:709-718`) diverges from reality.** No `project.ops.yaml`; no top-level `states/`/`runs/`/`comparisons/` storage tree; no `Model_Manifest`/`RUN-*`/`CMP-*` artifacts (model/state/run/comparison records live in the engine store). `core/handoff/**` *does* exist — but as engine handoff/export adapters, not the analysis-result tree the persona depicted. Piping is schema-driven + persistence-abstracted (`schemas/*`, `core/*`, SQLite store, on-demand export). → FM-03.
3. **Operation risk-classing + physics-grounding are DESIGN PROPOSALS, not implemented engine truth.** `model_operation.schema.json` has no `risk_class` field; `professional_boundary` is uniform. DEC-043 is a corpus-reliability constraint (routed to piping `AGENTS.md`), not an operation-level gate. The "Invented allowable stress" string is a test fixture (`completeness_checker/src/lib.rs:586`), though the underlying refusal-to-invent behavior is real.

**Caveat:** root canon is itself DRAFT. A confirmatory second cold pass over it is the clean test; recommend running it as part of authoring, not as a blocker.

## Adversarial verification pass (2026-06-21, post-authoring)

A 12-agent adversarial workflow audited this package against source (6 dimensions, each finding independently re-checked refute-by-default). It **refuted 2 false-positive findings** and **upheld 18**, all now fixed:

- **Citation/consistency (fixed):** profile said "six false claim-flags" → corrected to **five** (+`human_review_required`) per `operation_applier/src/lib.rs:1134-1141`; the "no `handoff/` dirs" phrasing → qualified (`core/handoff/**` *does* exist as export adapters; the divergence is the top-level `states/runs/comparisons` tree + `project.ops.yaml`); `PROFILE_STATUS` "(approved)" → "(current, not yet ruled)"; FM-02 count diff now updates subsections (11→12) and clarifies the K-DOMAIN IDs are new **to the root catalog**.
- **Reasoning (fixed):** D-T0-01 now records the **counter-position** (two-layer rule lets app-dev keep the contract local) + SHA-pin sequencing; the ProfileStatus `UNKNOWN`/`INVALID` enum mapping is reframed as **this proposal's interpretation**, not a TYPES.md citation; CONTRACT_DIRECTION §4 adds a **genericness verification** (app-dev's OperationProposal field list is piping-free) closing the circular-provenance risk; the "BLOCKER" citation finding was **corrected** — tier-0's persona citations are lawful (framework-root authoring), and the `_REFERENCES.md` SHA-pin is the *app-dev-side* prerequisite, already surfaced in D-T0-01.
- **Completeness (added):** two TOOLMAKER requirement briefs (profile-schema validator; headless CLI entrypoint); a full **D-T0-08** Fence-3 decision record; `NEXT_INSTANCE_PROMPT.md` sequencing protocol; expanded app-dev tier-1 slice + DEC-041 condition summary in the PLAN; gap-ownership note in CONTRACT_DIRECTION §1c; gate-safe DEFAULT in D-T0-04.

## Blockers / next owner

- 7 decisions in `_DECISIONS/_REGISTER.md` await human ruling (precedence, ProfileStatus, integration-level staging, data-residency, gate sequence, profile-adoption lifecycle, contract versioning).
- 4 canon edits (FM-01..04) are gated framework-maintenance — drafted as diffs, **not applied**.
- After rulings: DOMAIN_ENGINE updates the profile; app-dev and piping each author their own execution slices; CHANGE publishes.
