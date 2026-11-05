# CHANGE Prep — tier-0 profile result-schema hooks + bundled maintenance (2026-07-02)

> **Epistemic status: agent-prepared CHANGE packet — not authority, and not the CHANGE
> itself.** Prepared at owner direction (Ryan Tufts, K-AUTH-1) for owner-action queue
> items 2 and 6 of `_DomainEngines/bridge/WORKPLAN_2026-07-02_bridge_loop.md:168-171,190-195`.
> Every edit below is PROPOSED text only: editing the ADOPTED profile is a tier-0 CHANGE
> and therefore a HUMAN act (K-AUTH-2; D-GOV-04; D-T0-06 lifecycle). This packet adopts
> nothing, rules nothing, and advances no lifecycle. Sources govern on any disagreement;
> every load-bearing claim cites a repo-relative file:line verified against the live tree
> in the preparing session.

**Scope of the owner commit this packet prepares:** close the four result-schema hook
`TBD`s in `_DomainEngines/profiles/open_pipe_stress.yaml` (lines 81, 88, 101, 115) against
the two schemas published by piping DEL-10-03 on 2026-07-02
(`projects/chirality-piping/schemas/operation_outcome.schema.json`,
`projects/chirality-piping/schemas/rule_check_run_result.schema.json` — Loop 1,
`WORKPLAN_2026-07-02_bridge_loop.md:136-141`), plus four independently adoptable
maintenance items (§4). Each §4 item stands alone; declining any of them does not affect §1.

**Quoting convention (GEN-lint care):** where a quoted *before* line contains the removed
DRAFT-suffixed profile filename as a path token, the dead directory prefix is masked as
`<removed-dir>/` so this packet does not itself carry a nonresolving path token. The exact
bytes are at the cited file:line; the cited source governs. Proposed *after* lines use the
basename-only form (no path separator), which is not a path reference.

---

## §1 The CHANGE — four hook fields, one consequential comment

Target file: `_DomainEngines/profiles/open_pipe_stress.yaml` (ADOPTED; `profile_status`
at :25). The four `TBD`s tagged `# DEL-10-03` are the ones this CHANGE closes. The
schema-to-hook mapping below is confirmed by the published schemas' own descriptions:
`operation_outcome.schema.json:5` states it is "cited by the tier-0 profile's
validate_result_schema / apply_result_schema hooks", and
`rule_check_run_result.schema.json:5` states it is "cited by the tier-0 profile's
deterministic_check_result_schema hook". The profile-schema validator accepts any
non-empty string for these fields (`tools/validation/validate_domain_engine_profile.py:328-341`),
so every proposed value below re-validates.

### §1.1 Line 81 — `operation_applier.validate` → `validate_result_schema`

Before (`open_pipe_stress.yaml:81`):

```yaml
      validate_result_schema: "TBD"   # DEL-10-03 (operation_applier OperationOutcome)
```

After (PROPOSED):

```yaml
      validate_result_schema: "projects/chirality-piping/schemas/operation_outcome.schema.json"   # DEL-10-03 published 2026-07-02 (OperationOutcome envelope; mode=validate_only)
```

### §1.2 Line 88 — `operation_applier.apply` → `apply_result_schema`

Before (`open_pipe_stress.yaml:88`):

```yaml
      apply_result_schema: "TBD"      # DEL-10-03 (operation_applier apply OperationOutcome)
```

After (PROPOSED):

```yaml
      apply_result_schema: "projects/chirality-piping/schemas/operation_outcome.schema.json"      # DEL-10-03 published 2026-07-02 (OperationOutcome envelope; mode=apply)
```

**Why one schema for both :81 and :88 — and why the n/a split does not change that.**
The published `operation_outcome.schema.json` is a single result *envelope* covering both
run modes: its `mode` property is the enum `["validate_only", "apply"]`
(`operation_outcome.schema.json`, `properties.mode`; Rust source
`projects/chirality-piping/core/model_operations/operation_applier/src/lib.rs`, cited
field-by-field in the schema's description at :5). The profile's validate/apply n/a split
lives on the *other* field of each tool entry — :82 (`apply_result_schema` on the
validate-mode tool, comment `# n/a for validate mode`) and :87 (`validate_result_schema`
on the apply-mode tool, comment `# n/a for apply mode`). Those two are NOT among the four
DEL-10-03 `TBD`s and this CHANGE leaves them byte-identical (an optional tidy is noted in
§1.7). So: both *live* hooks point at the same envelope schema; the mode discriminator
inside the document distinguishes validate outcomes from apply outcomes.

### §1.3 Line 101 — `rule_check_runner` → `validate_result_schema` (owner picks A or B)

Before (`open_pipe_stress.yaml:101`):

```yaml
      validate_result_schema: "TBD"   # n/a (read_only); rule-check result is DEL-10-03
```

**Reasoning.** `rule_check_runner` is `mode: "read_only"` (:98). The profile's own
convention (:74) declares validate/apply hooks "n/a" for read_only tools — these fields
mean "schema of the proposal-validate / proposal-apply outcome", and a read-only checker
produces neither. The tool's actual result shape (the rule-check run result) *is* now
published, but it already has a first-class home: the
`operation_proposal_contract.deterministic_check_result_schema` hook (:115, closed in
§1.4). Binding :101 to the result schema would (i) mislabel a read-only report as a
proposal-validate outcome, (ii) make `rule_check_runner` inconsistent with the other two
read_only tools (`completeness_checker` :94-95, `headless_runner` :108-109, both staying
n/a), and (iii) duplicate the :115 binding.

**Disposition A (RECOMMENDED): labeled n/a, comment updated to point at the published shape.**

```yaml
      validate_result_schema: "n/a"   # read_only — no proposal-validate outcome; rule-check result shape published (DEL-10-03, 2026-07-02): projects/chirality-piping/schemas/rule_check_run_result.schema.json, carried by operation_proposal_contract.deterministic_check_result_schema
```

This closes the `TBD` (the field is no longer "to be determined" — it is determined to be
n/a), keeps the read_only convention coherent, and leaves the reader a pointer to the
published schema. The validator accepts `"n/a"` (any non-empty string;
`validate_domain_engine_profile.py:328-341`).

**Disposition B (ALTERNATIVE, if the owner prefers every emitting tool to carry its
result schema directly):**

```yaml
      validate_result_schema: "projects/chirality-piping/schemas/rule_check_run_result.schema.json"   # read_only result shape (DEL-10-03, 2026-07-02) — NOT a proposal-validate outcome; duplicate of the :115 binding
```

If B is chosen, the owner should consider the same treatment for `completeness_checker`
and `headless_runner` for consistency (out of this packet's scope — their shapes are not
published). The owner picks; A is recommended.

### §1.4 Line 115 — `operation_proposal_contract.deterministic_check_result_schema`

Before (`open_pipe_stress.yaml:115`):

```yaml
    deterministic_check_result_schema: "TBD"   # DEL-10-03 (rule_check_runner result shape)
```

After (PROPOSED):

```yaml
    deterministic_check_result_schema: "projects/chirality-piping/schemas/rule_check_run_result.schema.json"   # DEL-10-03 published 2026-07-02 (RuleCheckRunResult; document_kind openpipestress.rule_check.run)
```

### §1.5 Consequential comment edit — the `deterministic_tools` header block (:72-74)

Once the hooks bind, the header comment's "not yet published as standalone schemas"
clause is false and must not survive the CHANGE.

Before (`open_pipe_stress.yaml:72-74`):

```yaml
  # Recorded TBD pending the piping DEL-10-03 result-schema declaration (operation_applier /
  # rule_check_runner result shapes exist in Rust but are not yet published as standalone
  # schemas); for read_only tools, validate/apply are n/a (recorded TBD).
```

After (PROPOSED):

```yaml
  # DEL-10-03 result-schema declaration published 2026-07-02: the operation_applier and
  # rule_check_runner result shapes are standalone schemas under
  # projects/chirality-piping/schemas/ (operation_outcome.schema.json,
  # rule_check_run_result.schema.json); the Rust sources govern on disagreement.
  # For read_only tools, validate/apply remain n/a.
```

### §1.6 The open_issues line at :143 — VERIFIED: no edit required

The preparing brief anticipated a "result-schema TBDs x4" clause at :143. Checked against
the live tree (K-INVENT-1: the tree governs over the tasking), line 143 reads:

```yaml
    - "Live binding (L2-L3) gated x4: tier-0 adoption, app-dev F3, piping D-21, DEC-041 automation condition (residency is NOT a blocker post D-T0-04)."
```

Its "gated x4" clause names the four *live-binding gates*, not the four result-schema
`TBD`s — and none of those gates is cleared by publishing schemas or closing hook fields
(app-dev F3 needs the D-T0-08 sequence; piping D-21 adoption is held; DEC-041's
automation condition needs a consumable package —
`WORKPLAN_2026-07-02_bridge_loop.md:22-25`). **Recommendation: leave :143 byte-identical.**
No `open_issues` entry (:139-145) names the result-schema `TBD`s; the prose that actually
goes stale is the :72-74 header comment, handled in §1.5. Editing :143 to mention this
CHANGE would *add* an inaccuracy, not remove one.

### §1.7 Optional owner tidy-ups inside the same file (not part of the tasked four)

- **:82 and :87** — the n/a halves still carry the literal value `"TBD"` with n/a
  comments. The owner MAY relabel both values to `"n/a"` (validator-safe) so that, after
  this CHANGE, a grep for `"TBD"` in `deterministic_tools` returns only the genuinely
  undetermined read_only fields (:94-95, :102, :108-109). Default: leave as-is (no
  harness finding tracks them; see §3).
- **profile_version bump** — see §3, second bullet (owner option).

---

## §2 Owner execution steps (K-AUTH-2 — every step below is the owner's act)

1. **Branch first.** Do not commit to `main` directly (house git hygiene,
   `_DomainEngines/CHANGE_HANDOFF.md:12`). Suggested branch:
   `change/tier0-profile-result-schema-hooks`.
2. **Apply the §1 edits** to `_DomainEngines/profiles/open_pipe_stress.yaml`: §1.1, §1.2,
   §1.4, §1.5 as written; §1.3 per the disposition you pick (A recommended); optionally
   §1.7 and the §3 version bump. This file is agent-unwritable by standing constraint
   (`WORKPLAN_2026-07-02_bridge_loop.md:75-76`) — the edit itself is what makes this a
   tier-0 CHANGE.
3. **Re-validate the profile** (D-T0-06 cadence precedent: the 2026-07-01 rename CHANGE
   re-ran the validator and regenerated the report —
   `docs/governance_harness/_DECISIONS/_REGISTER.md:38-39`):

   ```
   python3 tools/validation/validate_domain_engine_profile.py \
     _DomainEngines/profiles/open_pipe_stress.yaml \
     --output-report _DomainEngines/profiles/_validation/open_pipe_stress.validation.json
   ```

   Expect `result: VALID`, 0 errors / 0 warnings (current record:
   `_DomainEngines/profiles/_validation/open_pipe_stress.validation.json`). Note: the
   regenerated report may embed a machine-absolute `profile_path`, as the current one
   does — that is an evidence artifact, permitted (the harness notes it as INFO
   `ABS_PATH_IN_EVIDENCE`, SPEC §0.2.4).
4. **Run the harness** and compare against §3:
   `python3 tools/practitioner_harness/harness.py status --domain-engines` (expect: no
   severities, as today) and `python3 tools/practitioner_harness/harness.py self-check`
   (expect the §3 totals). Use `PYTHONDONTWRITEBYTECODE=1`.
5. **Optionally fold in §4 items** — each is independently adoptable, in this commit or
   separately.
6. **Commit with the SHA-binding note.** The CHANGE binds at its publication commit
   (K-AUTH-2; same convention D-GOV-07 records for gate acceptances — content plus commit
   SHA, `docs/governance_harness/_DECISIONS/D-GOV-07_domain_gate_sha_binding.md:15-17`).
   Suggested message (PROPOSAL):

   ```
   tier-0 CHANGE: bind the ADOPTED profile's four result-schema hooks to the
   published DEL-10-03 schemas (owner act, K-AUTH-2)

   open_pipe_stress.yaml :81/:88 -> schemas/operation_outcome.schema.json,
   :115 -> schemas/rule_check_run_result.schema.json, :101 resolved n/a
   (read_only; disposition A), deterministic_tools header comment updated.
   Validator re-run: VALID. Prepared (proposal only) in
   _DomainEngines/bridge/CHANGE_PREP_2026-07-02_profile_result_schema_hooks.md.
   ```
7. **Status surfaces.** There is no live top-level `PROFILE_STATUS.md` — the only file of
   that name is the immutable 2026-06-21 prep-snapshot copy
   (`_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/PROFILE_STATUS.md`; see §4(b)).
   The authoritative status surface is the profile itself (`open_pipe_stress.yaml:25`),
   and `profile_status: "ADOPTED"` does NOT change — a hook-value CHANGE is not a
   lifecycle transition (D-T0-06 gates cover DRAFT→VALIDATED→ADOPTED; nothing here moves
   status). The D-T0-06 cadence therefore requires no status-file update beyond the
   optional §4(b). Queue item 2 gets marked done in the next Loop Log append
   (`WORKPLAN_2026-07-02_bridge_loop.md:197` — append-only; an agent may do that next loop).

---

## §3 Verification plan — what the harness should show after

Baseline (verified in the preparing worktree, harness at the same commit):
`self-check` exit 0 with **INFO=9, NOT_APPLICABLE=1, REVIEW=23, WARN=3**;
`status --domain-engines` "Finding severities: none" (contradiction pointer count 5).

- **§1 alone is finding-neutral: expect identical totals.** No current finding tracks the
  yaml hook fields — GEN-5 (unresolved refs) walks `.md` control files only
  (`tools/practitioner_harness/cmd_self_check.py:537-543`), and the DE checks emit
  nothing on the profile today (baseline above). The §1 verification is therefore the
  validator re-run (VALID) plus human diff review, not a harness delta.
- **VERSION_STRING_DRAFT_AMBIGUITY (INFO) — owner option to also bump `profile_version`.**
  Self-check currently reports INFO on `open_pipe_stress.yaml` because
  `profile_version: "0.1-DRAFT"` (:24) carries a `-DRAFT` suffix while `profile_status`
  is ADOPTED (explicitly not a status conflict — labeling ambiguity only). This CHANGE is
  the first content change to the ADOPTED profile, which is a natural point to make the
  version string honest: bumping to e.g. `"0.2"` clears the INFO (9→8) and makes the
  hook-binding version-visible. Owner option, not required; the validator accepts either.
- **If §4(a) is adopted:** WARN 3→2 (`_DomainEngines/CHANGE_HANDOFF.md:27` clears).
- **If §4(b) is adopted:** no count change — the bridge prep snapshot is outside GEN-5's
  v1 scope (`cmd_self_check.py:541-543`); the fix is reader-accuracy only.
- **If §4(c) stays at its default (leave as-is):** WARN count unchanged — the D-T0-06:7
  WARN remains one of the three known, accepted UNRESOLVED_SOURCE_REFs.
- **If §4(d) stays at its default (leave as-is):** ditto for D-GOV-07:26.
- **Environment caveat for anyone re-measuring in a fresh checkout:** the WARN=3 baseline
  depends on two *untracked* working-copy artifacts present in the owner's checkout — the
  gitignored `_harness_generated/briefs/` files (cited by the two committed briefs at
  `docs/governance_harness/briefs/TRB-chirality-app-dev-DEL-10-01-2026-07-02.md:79-80`
  and `docs/governance_harness/briefs/TRB-chirality-app-dev-DEL-10-03-2026-07-02.md:81-82`)
  and the empty `_DomainEngines/proposals/open_pipe_stress/` directory (cited at
  `_DomainEngines/CHANGE_HANDOFF.md:41`; git does not track empty directories). A fresh
  clone shows WARN=8 (+4 brief refs, +1 proposals-dir ref) until those exist. This
  packet's cleanliness was proven in a fresh worktree with both artifacts replicated:
  totals matched the main baseline exactly, before and after adding this file. If the
  owner wants the proposals-dir WARN clone-stable, a `.gitkeep` under
  `_DomainEngines/proposals/open_pipe_stress/` would do it (observation only — not one of
  the tasked proposals).

---

## §4 Bundled maintenance proposals (queue item 6 — each independently adoptable)

### (a) `_DomainEngines/CHANGE_HANDOFF.md:27` — dead path token for the removed DRAFT filename

The line already carries the correct historical annotation; only the *path token* is dead
(the file was renamed 2026-07-01 per D-GOV-06), which is what WARNs
(`UNRESOLVED_SOURCE_REF`, K-PROV-1). Fix: demote the token to basename-only (no path
separator → no longer parsed as a path reference), preserving every word of history.

Before (`_DomainEngines/CHANGE_HANDOFF.md:27`; dead prefix masked per the quoting
convention above — exact bytes at the cited line):

```md
- `<removed-dir>/open_pipe_stress.DRAFT.yaml` — *historical: as committed 2026-06-21; since VALIDATED → ADOPTED (owner Gate 2, D-T0-06) and renamed to `profiles/open_pipe_stress.yaml` 2026-07-01 per D-GOV-06*
```

After (PROPOSED — basename-only, no separator):

```md
- `open_pipe_stress.DRAFT.yaml` (historical filename, since removed from the profiles directory) — *historical: as committed 2026-06-21; since VALIDATED → ADOPTED (owner Gate 2, D-T0-06) and renamed to `profiles/open_pipe_stress.yaml` 2026-07-01 per D-GOV-06*
```

Expected effect: WARN 3→2. `CHANGE_HANDOFF.md` is a mutable control-area pointer file
(self-classified, `_DomainEngines/CHANGE_HANDOFF.md:19-24`), so an in-place fix carries
no immutability concern. **Recommended: adopt.**

### (b) Prep-snapshot `PROFILE_STATUS.md:5` — stale DRAFT filename

File: `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/PROFILE_STATUS.md` (the only
`PROFILE_STATUS.md` in the tree — there is no live top-level copy). Its "Active profile"
row still names the DRAFT-suffixed file. Two tensions: the row is *historically true* (it
was the active filename on 2026-06-21), and the file sits inside the directory
`CHANGE_HANDOFF.md:33` labels an "immutable run record". It produces NO harness finding
(outside GEN-5 v1 scope), so this is purely reader-accuracy. The D-GOV-06 cleanup
precedent is annotation-not-rewrite (`docs/governance_harness/_DECISIONS/_REGISTER.md:39-40`:
"D-T0-06's stale HumanRuling line annotated").

Before (`_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/PROFILE_STATUS.md:5`; dead
prefix masked — exact bytes at the cited line):

```md
| Active profile | `<removed-dir>/open_pipe_stress.DRAFT.yaml` |
```

After (PROPOSED — keep the historical fact, annotate forward, basename-only):

```md
| Active profile | `open_pipe_stress.DRAFT.yaml` (as of this 2026-06-21 snapshot; renamed to `_DomainEngines/profiles/open_pipe_stress.yaml` 2026-07-01 per D-GOV-06) |
```

**Recommended: adopt** (annotation preserves the run record's historical claim while
routing readers to current truth). Reasonable alternative: leave the snapshot untouched
on strict immutability grounds — the WORKPLAN's queue item 6 already serves as the
forward note.

### (c) `_DomainEngines/_DECISIONS/D-T0-06_profile_adoption_lifecycle.md:7` — CAUTION: fixture-adjacent. DEFAULT: leave as-is.

Line 7 ("Verified facts") cites the DRAFT-suffixed filename and WARNs. **But this file's
title line (:1) — which still carries the PROPOSAL tag with an unset HumanRuling (quoted
here only by description, so this packet does not reproduce the fixture pattern the
harness hunts) — is one of the three owner-retained self-check fixtures** — surfaces the owner ruled (2026-07-01) must stay **byte-identical**
as live test material (`docs/governance_harness/_DECISIONS/_REGISTER.md:41-53`; full
fixture list in §5). Line 7 is not itself the fixture line, but any edit to this file
sits one line-drift away from fixture bytes and from the pinned finding expectations
(STALE_RULING_ANNOTATION=2, TITLE_CONTRADICTS_RULING=1, STALE_DRAFT_DIRECTIVE=1 —
register :52-53).

**Default recommendation: LEAVE AS-IS.** The :7 WARN is one of the three known,
enumerated, accepted UNRESOLVED_SOURCE_REFs (`WORKPLAN_2026-07-02_bridge_loop.md:190-193`);
the WARN=3 baseline *is* the pinned normal. If the owner nonetheless wants it cleaned:
first re-check the owner-retained fixture list at the register lines above, confirm the
title line (:1) stays byte-identical, use the annotation style already present in this
record (the bracketed italic note at :14), keep the historical sentence intact, and
re-run `self-check` to confirm the pinned REVIEW counts are unmoved and WARN drops by
exactly one. For completeness, an annotation-style edit that satisfies those constraints
(ALTERNATIVE ONLY — the default stands):

```md
**Verified facts:** `VALIDATED` requires a deterministic profile-schema validator — **not built** (TOOLMAKER handoff). Current profile is DRAFT (`open_pipe_stress.DRAFT.yaml`, the then-current filename under the tier-0 profiles directory; renamed 2026-07-01 per D-GOV-06). *[Facts as verified 2026-06-21; validator since built and profile ADOPTED — see the HumanRuling and Progress notes below.]*
```

### (d) `docs/governance_harness/_DECISIONS/D-GOV-07_domain_gate_sha_binding.md:26` — decision-record immutability. DEFAULT: leave the record; forward note instead.

Line 26 (inside the RULED record's coverage note) cites the pointer-file form
`gate_snapshots` + `/_LATEST_GATE6.md`, which resolves neither repo-root-relative nor
file-relative — the live instances are per-domain, e.g.
`domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE6.md` (also under
`domains/chirality-piping/` and `domains/chirality-app-dev/`). The citation is
*semantically correct* (it describes a per-domain file class, deliberately not one path);
the WARN is a parser-precision artifact.

Before (`D-GOV-07_domain_gate_sha_binding.md:26`, exact):

```md
via lighter `gate_snapshots/_LATEST_GATE6.md` pointer files without a
```

**Default recommendation: LEAVE THE RECORD UNTOUCHED.** D-GOV-07 is a RULED decision
record (Status/Ruling at :3-5); rewording ruled prose — even a citation — erodes the
record-immutability norm this repo runs on (the same norm behind "never edit DEC-041
prose"). Note the resolution *forward* instead: when the owner next touches the
governance register (`docs/governance_harness/_DECISIONS/_REGISTER.md`) or when D-GOV-03
domain-shape verifier work resumes (D-GOV-07:18-19 names it the dependent), add a note
that the :26 reference is a per-domain file-class citation whose live instances are the
three `domains/*/_Decomposition/gate_snapshots/_LATEST_GATE6.md` files, and that the WARN
is accepted. The WARN stays in the baseline (3 total, or 2/1 as §4(a)/(c) land).
If the owner instead rules an in-place fix, the minimal edit that clears the parser while
preserving meaning is (ALTERNATIVE ONLY):

```md
via lighter `domains/<domain>/_Decomposition/gate_snapshots/_LATEST_GATE6.md` pointer files without a
```

(the `<domain>` placeholder is skipped by the reference parser, and the generic form is
arguably what the record always meant).

---

## §5 Explicitly out of scope for this packet and the owner commit it prepares

1. **The three owner-retained self-check fixtures** (ruled 2026-07-01 as live test
   material, must stay byte-identical; `docs/governance_harness/_DECISIONS/_REGISTER.md:41-53`).
   Named, so no §1/§4 edit can be mistaken for touching them:
   - `_DomainEngines/DOMAIN_ENGINE_INDEX.md:34` — the layout-tree annotation tagging the
     decision register as a PROPOSAL with an unset HumanRuling (described, not quoted —
     reproducing the tag verbatim would itself trip the detector this fixture feeds);
   - `_DomainEngines/_DECISIONS/D-T0-06_profile_adoption_lifecycle.md:1` — the title line
     carrying the same tag (why §4(c)'s default is leave-as-is);
   - `_DomainEngines/RULINGS_PUBLISHED.md:20` — the action-flow line "Update the DRAFT
     profile per rulings."
   Pinned expectations that must survive any adopted item: STALE_RULING_ANNOTATION=2,
   TITLE_CONTRADICTS_RULING=1, STALE_DRAFT_DIRECTIVE=1 (register :52-53).
2. **DEC-041 / DEC-051 prose** — immutable history (standing constraint,
   `WORKPLAN_2026-07-02_bridge_loop.md:76-78`).
3. **The readiness assessment**
   (`_DomainEngines/bridge/READINESS_2026-07-02_bridge_tranche1.md`) — deltas go in Loop
   Log entries, never in the record.
4. **Anything requiring a ruling:** D-APP-45 / D-APP-46 (AWAITING_RULING), D-21 adoption
   (held), any lifecycle advance, root `docs/CONTRACT.md` ratification. This packet
   proposes text; it adopts, rules, and promotes nothing.
5. **The ADOPTED profile itself** — this packet does not edit it; §1 is the owner's edit
   to make (K-AUTH-2).

---

*Prepared 2026-07-02 in a clean worktree off `main`. Cleanliness proof: harness
`self-check` run against the worktree before and after authoring this file — totals
identical to the main baseline (INFO=9, NOT_APPLICABLE=1, REVIEW=23, WARN=3; the WARN set
is exactly the three known UNRESOLVED_SOURCE_REFs discussed in §4(a)/(c)/(d)); this file
adds zero findings.*
