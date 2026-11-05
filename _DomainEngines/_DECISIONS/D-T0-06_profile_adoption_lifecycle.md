# D-T0-06 — Profile adoption lifecycle + sub-gates  (PROPOSAL; HumanRuling: TBD)

**Decision:** Adopt the `DRAFT→VALIDATED→ADOPTED` lifecycle and the protected-write / mutating-tool / proposal-application / external-prover / reliance sub-gates.

**Why the owner's:** adoption and each consequential transition are human gates (persona Gates 2–5; QA contract).

**Verified facts:** `VALIDATED` requires a deterministic profile-schema validator — **not built** (TOOLMAKER handoff). Current profile is DRAFT (`profiles/open_pipe_stress.DRAFT.yaml`).

**Recommendation:** adopt the persona cadence; commission the profile-schema validator via a TOOLMAKER requirement brief before any `VALIDATED` claim. Keep `operation_applier.apply` human-confirmed (K-DOMAIN-3).

**Unblocks:** moving the profile off DRAFT. **Forecloses:** "adopted" without a validator.

---
**HumanRuling:** **Persona cadence** `DRAFT→VALIDATED→ADOPTED`; `VALIDATED` gated on the **TOOLMAKER profile-schema validator** (briefed, not built — see `TOOLMAKER_BRIEF-profile_schema_validator.md`). Profile stays DRAFT until the validator exists. *[Condition met 2026-06-21: validator built, profile **VALIDATED → ADOPTED** per the Progress note below; contradiction cleanup directed by D-GOV-06, ruled 2026-07-01.]*   **RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21

**Progress (2026-06-21):** validator built (`tools/validation/validate_domain_engine_profile.py`, 8/8 tests) and the profile **passed** (report `_DomainEngines/profiles/_validation/open_pipe_stress.validation.json`) → `DRAFT → VALIDATED`. **Human Gate 2 (`VALIDATED → ADOPTED`) ruled by the owner 2026-06-21** → ProfileStatus **ADOPTED**; the OpenPipeStress integration boundary is governed-authoritative. Lifecycle complete.
