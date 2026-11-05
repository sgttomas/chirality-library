# Tier-0 CHANGE prep — proven-L2 acknowledgment (STAGED; owner act pending)

**Epistemic status: CHANGE packet, PREPARED ONLY.** Unlike the 2026-07-04
live-binding de-stale CHANGE (owner-delegated execution), this CHANGE is
**not applied**: the proven-L2 acknowledgment is the owner's act (K-AUTH-1;
D-32 rider 4 — "the tier-0 'proven L2' acknowledgment (and any profile
`status:` update) is a separate tier-0 act after the evidence exists").
The evidence now exists (§2); this packet stages the exact edits so the
acknowledgment is a one-line owner act. Register row: `D-T0-10`
(`_DomainEngines/_DECISIONS/_REGISTER.md`), HumanRuling OPEN.

Prepared 2026-07-04 under the owner's in-session direction: "execute the
DEC-064 tranche now, in this session, then stage the L2-acknowledgment
CHANGE and both F3 PROPOSAL packets while the evidence is fresh."

## 1. What "proven L2" means and why it is now satisfiable

`D-T0-08` (RULED 2026-06-21): app-dev F3 opens sequentially — source types,
then domain MCP tools — "not before D-T0-01 (ruled) + a proven L2."
L2 = validated-kernel runs (`D-T0-03` staging; the profile marks
`headless_runner` as the L2 candidate). Until 2026-07-04 the candidate was
lib-only ("TOOLMAKER handoff — entrypoint not yet built").

## 2. The evidence (commit-bound, this PR)

- **Code:** PROVISIONAL thin entrypoint
  `projects/chirality-piping/core/runner/headless/src/bin/headless_preview_runner.rs`
  (DEC-064 / D-32 O-A; TP-RUNNER-014), commit `035e25991`. Zero new
  dependencies; `Cargo.toml` untouched (cargo bin auto-discovery);
  read_only posture preserved.
- **Validated-kernel run:** fixture
  `projects/chirality-piping/fixtures/product_preview/invented_preview_model.json`
  through the entrypoint on a clean head — exit 0, job `Completed`,
  `MECHANICS_SOLVED`, `analysis_status` `[HumanReviewRequired,
  MechanicsSolved, RuleInputsIncomplete]`, 822 result refs including the
  golden `result:stress:pipe-P-120:end-j:torsional-shear`, two SHA-256
  checksums (`runner_request` `3eb2516d…`, `result_envelope` `60cc21fc…`),
  zero runner-result diagnostics (the mechanics envelope carries
  informational/warning domain diagnostics only — none blocking; exit
  status is recorded in the run record). Full captured stdout:
  `projects/chirality-piping/validation/witness/generated/tp_runner_014_headless_entrypoint_preview_run.json`.
- **Run record:** DEL-10-05
  `_run_records/WORKING_ITEMS_RUN_2026-07-04_TP-RUNNER-014.md`.
- **Merge-gate evidence:** the DEC-025 five-surface sweep (5/5 pass) bound
  to the tranche's final code state, committed as the evidence-only
  closeout commit under
  `projects/chirality-piping/validation/evidence/sweeps/`.

## 3. Exact edits the acknowledgment applies

**Target:** `_DomainEngines/profiles/open_pipe_stress.yaml` (ADOPTED;
tier-0 CHANGE only).

**Edit 1 — `headless_runner` impl note (`:106`).** Before:

    impl: "projects/chirality-piping/core/runner/headless (Rust; lib-only — needs a thin CLI entrypoint, lib.rs:655)"

After:

    impl: "projects/chirality-piping/core/runner/headless (Rust; lib + PROVISIONAL thin CLI entrypoint headless_preview_runner — DEC-064/TP-RUNNER-014; final CLI syntax stays TBD)"

**Edit 2 — `headless_runner` status (`:109`).** Before:

    status: "TOOLMAKER handoff — entrypoint not yet built"

After (the acknowledgment itself; owner fills the date):

    status: "L2 PROVEN — validated-kernel run demonstrated 2026-07-04 (DEC-064/TP-RUNNER-014); acknowledged by owner <date> (D-T0-10)"

**Edit 3 — version bump.** `profile_version: "0.3"` → `"0.4"` (`:24`),
per the content-CHANGE precedent. `profile_status` stays ADOPTED.

**NOT changed:** `integration_level: "MANUAL_BRIDGE"` (`:26`) — a proven-L2
demonstration discharges the D-T0-08 precondition; it is not an
integration-level transition (level movement stays risk-graded
per-operation under D-T0-03 and is not claimed here). `mode: read_only`
stays. All other fields byte-identical.

## 4. Owner execution steps (the acknowledgment act)

1. Rule register row `D-T0-10` (fill its HumanRuling cell) — in-session
   words suffice; the agent records them verbatim per K-AUTH-1/D-GOV-04.
2. Apply (or delegate applying) the §3 edits; re-run the validator
   (`tools/validation/validate_domain_engine_profile.py` with
   `--output-report
   _DomainEngines/profiles/_validation/open_pipe_stress.validation.json`);
   expect VALID 0/0 (report regeneration is byte-identical by schema).
3. Same-PR conscious live-pin review: editing the profile does not change
   the live-binding gate line (`:145`), so no severity-pin movement is
   expected; verify with `harness.py self-check` at the final SHA.
4. After the acknowledgment, the D-T0-08 preconditions for F3 step (a) are
   fully met; the staged `D-APP-49` PROPOSAL becomes rulable on its merits.
