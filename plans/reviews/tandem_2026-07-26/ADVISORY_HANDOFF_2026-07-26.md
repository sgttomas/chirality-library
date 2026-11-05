# Advisory-Session Handoff — Chirality Architecture Remediation

Written 2026-07-26 by the second meta-reviewer / advisory session (Claude Fable 5).
Non-governing. Role: independent read-only verification of each implementation gate
before owner approval. Prior participation: supervised the excluded fourth tandem
pass; authored independent_meta_2 (both disclosed in ENGINE_IDENTITY_REGISTER.csv).

## Plan state (approved remediation plan, executed by codex agent in another session)

DONE (all independently verified by this session):
- Step 0: safety tar `/Users/<owner>/dev/chirality-review-safety-2026-07-26-DA31C19.tar` (+.sha256)
- Step 1: evidence package PR #360, merge 918bb48b8; OD-0 .pyc exception applied additively
- Sitting rulings: APP-HOLD-1 (OD-1), Option A (OD-2), bounded severity convention (OD-3)
- Step 3: APP-HOLD-1 applied — PR #363 (commit 4cdf469cf); D-APP-75; register
  entry_path_scope=ANY; no runtime exception mechanism (stricter than plan, accepted);
  one ruled deviation: live test corrected for placement-dependent assertion,
  corrected SHA 2d8d846b9aa9db7b47023a8f6af76649530e0a3c308fad7367c065a8f0bdcd2b,
  recorded in D-APP-75
- Step 5A: D-GOV-28 candidate PR #362 (f78a8362); adoption ruled "APPROVE: D-GOV-28
  Option O-A"; publication PR #364, merge fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb;
  adopted PRD_ROOT.md byte-equals candidate 0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d
  (verified). O-11 adopted. Design note: plan's O-11/O-12 became TRANSCRIBED block +
  single PROPOSED O-11 (accepted knowingly)
- SCA-001 Gate 1 CONFIRMED; Gate 2 open once D-GOV-28 EffectiveSHA backfill closes
- LAST INSTRUCTION to implementing agent: backfill D-GOV-28 EffectiveSHA to
  fb0b3d247d32..., then WAIT

REMAINING: Root SCA-001 Gates 2–5 (step 6) · App SCOPE_CHANGE §13 correction (step 7)
· App repair lanes + one population repin + APP-HOLD-1 clearance (step 8) ·
D-APP-48/49 evidence tranche (step 8) · bounded maintenance incl. PEC-K-03/K-11
annotation + RB-PEC-ADAPTER notice + README C-4 with correcting receipt (step 9) ·
later reforms (step 10) · Option A closure criteria audit.

## Standing verification facts (frozen, load-bearing)

- Six held contracts (scan-authoritative, census-confirmed): DEL-02-01, DEL-02-02,
  DEL-02-04, DEL-05-04, DEL-08-02, DEL-08-03 — dead object 416b29033bbacb0bc3648d84033272b7ab4e6e11
- D-GOV-20 core sentence (verbatim check anchor): "One opt-in per-user headless
  daemon exclusively owns runtime engines, credentials, sessions, delegation, tools,
  turn locks, interruption, and local-model residency."
- Evidence package: execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/
  (111-entry hash list eeae332d16847818f6be6cf69cb601929d33ac1bda4da33b26f2b7bb9b1c7f29)
- Verified code facts for upcoming SCAs: engine impls still under App
  frontend/src/lib/harness (imported by electron/runtime-host.ts via LegacyAgentEngineAdapter);
  daemon body<T>() casts without runtime schema validation (runtime-daemon.ts ~354)

## Carry-forward review conditions (attach at the named gate)

1. App SCA (step 7): remove §13 semantic-ownership claim WITHOUT asserting
   implementation has fully rehomed — App hosts residual carriers as client under a
   tracked migration obligation; the word "tracked" requires an actual register row.
   Quote adopted Root boundary verbatim. Credential seam: Electron is daemon host/
   storage substrate, never credential owner (D-GOV-20 exclusive-daemon-ownership).
2. Root SCA Gates 2–5: topology derived from adopted PRD only; stewardship
   deliverable should define routine change classes (avoid approval-funnel);
   SOW-104 reserved-not-allocated.
3. Repin (step 8): population-wide, once, only after corrected App decomposition
   accepted; never per-contract; APP-HOLD-1 cleared only after revalidation.
4. Method-lane candidates (step 10): review stopping rule (novel fact or concrete
   defect required; two null passes terminate); run candidate acceptance tests at
   live placement; deterministic hold enforcement.
5. Watch: governance saturation — steps 8–10 should get leaner, not richer.

## Verification method used at each gate

Re-hash every claimed artifact; rerun scans/tests/validators independently
(from repo root — manifests are repo-root-relative); diff copies against live
originals; check git tranche file lists against authorized enumerations; confirm
narrative artifacts never edited post-admission (corrections additive only).
