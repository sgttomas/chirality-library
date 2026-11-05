# Tier-0 CHANGE prep — de-stale the ADOPTED profile's live-binding gate line

**Epistemic status: CHANGE packet, executed same-session under explicit owner
delegation.** The ADOPTED profile is never agent-edited except by tier-0
CHANGE — owner act or explicit owner-delegated execution (workplan standing
constraints; K-AUTH-2). The delegation for this CHANGE is the owner's
in-session direction of 2026-07-04 (Ryan Tufts), verbatim:

> First merge PR #38 then complete the recommended changes and then proceed
> as recommended through the "Decision slate" including #6 for the tier-0
> CHANGE to de-stale. All of this should land as just one PR at the end.

Slate item 6 of the six-item decision slate presented in-session at the
assessment close (enumerated in Receipt 20; Receipt 19 records the
assessment run itself): "a tier-0 CHANGE to de-stale profile line 145's
gate enumeration." Precedent: the 2026-07-02 CHANGE
(`CHANGE_PREP_2026-07-02_profile_result_schema_hooks.md`, applied in PR #17
at `d70d8df92` with owner ruling R2).

## 1. Exact edits

**Target:** `_DomainEngines/profiles/open_pipe_stress.yaml` (ADOPTED).

**Edit 1 — the live-binding line (`:145`).** The line still enumerates four
gates, of which three are now cleared: tier-0 adoption (ADOPTED 2026-06-21,
D-T0-06), piping D-21 (RULED 2026-07-02, `DEC-056`), and the DEC-041
automation condition (declared met 2026-07-04, `DEC-063`/piping register row
`D-31`). The self-check `STALE_LIVE_BINDING_GATE` REVIEW finding fires on the
first two today. Before:

    - "Live binding (L2-L3) gated x4: tier-0 adoption, app-dev F3, piping D-21, DEC-041 automation condition (residency is NOT a blocker post D-T0-04)."

After:

    - "Live binding (L2-L3) gated x1: app-dev F3 (D-T0-08 sequence — proven L2 then source types then MCP tools, proven-L2 scoping at piping D-32; cleared: tier-0 adoption 2026-06-21 per D-T0-06, piping D-21 2026-07-02 per DEC-056, DEC-041 automation condition 2026-07-04 per DEC-063/D-31; residency is NOT a blocker post D-T0-04)."

The rewrite keeps the "Live binding … gated" detection phrase, moves every
cleared gate into the single trailing parenthetical (which the harness gate
tokenizer strips before token resolution), and leaves exactly one live gate
token, `app-dev F3`. Expected mechanical effect: `STALE_LIVE_BINDING_GATE`
clears; self-check REVIEW total 29 → 28; `bridge-status`
`live_binding_gate_rows` 4 → 1.

**Edit 2 — version bump.** `profile_version: "0.2"` → `"0.3"` (`:24`),
following the PR #17 precedent that a content CHANGE bumps the profile
version. `profile_status` does NOT change — a content CHANGE is not a
lifecycle transition (D-T0-06).

## 2. Execution steps

1. Branch-first (this CHANGE rides `claude/loop-slate-execution`, the
   owner-directed single PR).
2. Apply the §1 edits.
3. Re-validate and regenerate the report from the canonical checkout path
   (PR #17 live-pin lesson — never from a transient worktree path):
   `python3 tools/validation/validate_domain_engine_profile.py
   _DomainEngines/profiles/open_pipe_stress.yaml --output-report
   _DomainEngines/profiles/_validation/open_pipe_stress.validation.json`
   — expect `result: VALID`, 0 errors / 0 warnings. The report lawfully
   embeds a machine-absolute `profile_path` (evidence artifact, SPEC §0.2.4
   INFO `ABS_PATH_IN_EVIDENCE`); its schema carries no `profile_version`
   field, so a green regeneration is byte-identical — zero diff is the
   expected outcome, and the VALID result was confirmed live at 0.3.
4. Conscious live-pin update in the same PR: self-check severity-totals
   REVIEW 29 → 28 (`tools/practitioner_harness/test_live_baseline.py`).
5. Closeout checks at the final SHA per the amended workplan step 4.

## 3. Verification plan

- Validator VALID, 0/0.
- `harness.py self-check`: exit 0; `STALE_LIVE_BINDING_GATE` absent; totals
  INFO=14 / NOT_APPLICABLE=1 / REVIEW=28 / WARN=2 (after the pin update).
- `harness.py status --domain-engines`: no severities.
- `harness.py bridge-status`: no findings; the owner-act gate row derives
  x1 from the rewritten line.
- Full practitioner-harness pytest green at the final SHA.

## 4. Not changed

`profile_status` (stays ADOPTED); `open_issues` entries `:142-144`, `:146`
(byte-identical); the `headless_runner` block `:105-111` (its
"entrypoint not yet built" status stays true until the D-32-ruled tranche
lands and a subsequent tier-0 act updates it); the three owner-retained
self-check fixtures; `agent_writable_paths`; every other profile field.
