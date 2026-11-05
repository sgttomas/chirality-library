# Bridge Work Loop — standing plan (app-dev ↔ piping tier-0 bridge)

> **Epistemic status: agent-authored plan — not authority.** Written at owner direction
> (Ryan Tufts, K-AUTH-1) on 2026-07-02; protocol reformed 2026-07-02 at owner direction
> (see `LOOP_RECEIPTS.md`, Receipt 0). This plan never authorizes work: owner-adopted
> briefs and owner rulings/directions do. Sources govern on any disagreement. This file
> is a PROTOCOL plus pointer indexes; it carries NO status, NO work history, and NO
> measurements — each loop iteration re-derives state from the live tree, and loop
> closes append a minimal receipt to `_DomainEngines/bridge/LOOP_RECEIPTS.md` (rules
> live at the top of that file). The Loop Log at the bottom is SEALED immutable
> history from Loops 1–2.

## Owner intent (recorded 2026-07-02; goal of record added 2026-07-03)

**The loop's goal** (owner direction of record, quoted verbatim in
`LOOP_RECEIPTS.md` Receipts 1–6): keep the `chirality-app-dev` and
`chirality-piping` project surfaces governably aligned and move this standing
bridge plan forward as far as live authority permits. This section is the
goal's single durable home — the generic launcher (`init/init-prompt.md`) and
`LOOP_INIT.md` deliberately point here instead of restating it.

Execute the most comprehensive amount of bridge work available, as a series of loops,
across sessions. Each iteration discovers state fresh rather than following pre-spelled
direction; implementation proceeds organically as dependencies resolve. Staging is
retained only where the governance structure compels it.

## Why any staging remains (the compelling reasons)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04): deliverable
   tranches require an owner-adopted brief; coordination/control work (decision
   packets, CHANGE preps, design docs) requires owner direction. No agent can
   pre-authorize N tranches; each loop therefore has a gate.
2. **Live binding is gated** — the gate set and its current state are enumerated in
   the ADOPTED profile's open_issues (`_DomainEngines/profiles/open_pipe_stress.yaml`,
   the "Live binding" line) and in the decision registers; re-derive them at Step 0,
   never from this file.
3. **Fences F1–F4** bound what any tranche may touch regardless of ambition.

The loop is therefore comprehensive over the *lawful surface at each iteration* — a
surface that widens as the owner rules. Nothing lawful is deferred by plan design;
work is deferred only by gates.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log since
   the last receipt); read the latest receipt(s) in
   `_DomainEngines/bridge/LOOP_RECEIPTS.md`; check BOTH project decision registers +
   the tier-0 register for rulings newer than the last receipt (new rulings are how
   work unlocks — look every time); harness `status` ×3, `drift --all`, `self-check`
   (`PYTHONDONTWRITEBYTECODE=1` each). Verify any derivative statement — including
   this plan, dated maps, and your own tasking — against the live tree before relying
   on it; on disagreement the live tree wins and the delta goes in the receipt.
   *Conditional, by need:* harness `next` only when selecting deliverable-shaped
   work; the dated readiness assessment
   (`_DomainEngines/bridge/READINESS_2026-07-02_bridge_tranche1.md`) only when
   historical rationale is needed; full harness pytest at discovery only if
   `tools/**` changed since the last receipt (it is always mandatory at closeout —
   step 4).
1. **Select.** The widest lawful tranche(s) now, re-derived. Principles, in order:
   (a) work that discharges a gate prerequisite beats work that doesn't;
   (b) owner-directed items beat agent-inferred ones;
   (c) doc/design-level before any binding;
   (d) match the vehicle to the work type: deliverable work takes a harness brief
       (one brief per deliverable fence — don't split what one brief covers, never
       merge across fences); coordination/control artifacts (decision packets,
       CHANGE preps, design docs, correction records) take explicit owner direction
       and need no brief — the harness brief cannot fence them.
2. **Brief / slate.** For deliverable work: `python3
   tools/practitioner_harness/harness.py brief --project <p> --deliverable <id>` →
   CANDIDATE(s); fill the objective (practitioner-proposed, grounded in cited
   files — K-INVENT-1). For coordination/control work: present the owner a decision
   slate (options + non-binding recommendation + the on-ruling mechanism).
3. **Gate.** STOP; adoption/ruling/direction is the owner's act (K-AUTH-1; D-GOV-04).
   Briefs: owner edits `state:` → HUMAN_ADOPTED, fills `adopted_by:`/`adopted_on:`
   (per `docs/governance_harness/human_actors.md`), moves the file to a governed
   path OUTSIDE `_harness_generated/`, commits; agent confirms with
   `brief --verify-adoption <path>`. Directions/rulings given in-session are quoted
   verbatim in the receipt and recorded in their governed artifact (packet §7,
   ruling record, register row) as part of execution. Record every gate outcome in
   the receipt — including no-ops and their reason.
4. **Execute + check (by work type).** Branch-first + PR unless the owner directs
   main-direct; mutually exclusive write scopes when parallel; inside fences +
   standing constraints below. Prefer independent branches or one batched PR over
   stacked dependent PRs — deep stacks impose a rigid owner merge order (the
   six-deep #21–#26 stack, merged reverse-order in Receipt 7, is the cautionary
   precedent).
   - Adopted deliverable tranches: `run-validations`, `scope-check` (PR diff range
     vs fence), `evidence-check`, `closeout-digest`.
   - Coordination/control artifacts: adversarial review (citation integrity,
     convention fidelity against the named precedent, register consistency) +
     git-diff scope containment.
   - ALL work at closeout: `self-check`, `drift --all`, and the FULL harness pytest
     including the live-baseline suite — non-`tools/**` changes that alter measured
     reality are exactly what the live pins catch (both 2026-07-02 CI failures were
     this); a legitimate change that moves a pinned measurement carries its
     conscious pin update in the same PR. Closeout checks bind to the exact
     final commit: any edit after a check run — however small — invalidates
     that run; re-run the closeout set at the final SHA before recording
     results in a receipt (the Receipt 19 D-05b delta is the precedent).
   - CI (governance-harness workflow) green; owner merges — never self-merge.
5. **Receipt.** Append a minimal receipt to `_DomainEngines/bridge/LOOP_RECEIPTS.md`
   per its local rules — pointers, verbatim owner directions, gate outcomes,
   check pass/fail. No narrative here or anywhere else. Next iteration starts at 0.

## Standing constraints (all iterations)

- No F1/F2/F3/F4 crossing without the gating ruling: no DomainEngineProfile /
  OperationProposal source types in `frontend/src`, no domain MCP tools, no
  CHECKING→ISSUED (lifecycle advances are human-only), no release/publish, no
  provider/egress changes.
- No writes under `projects/chirality-piping/core/**`, `schemas/**`,
  `core/handoff/**`. Tier-0 control-root writes only under
  `_DomainEngines/proposals/open_pipe_stress/**` or `_DomainEngines/bridge/**`
  (profile `agent_writable_paths`).
- Never edit: the ADOPTED profile (tier-0 CHANGE only — owner act or explicit
  owner-delegated execution); the three owner-retained self-check fixtures
  (governance register item 3); DEC-041 prose / DEC-051's "staged for CHANGE"
  wording (immutable history); the readiness assessment and the sealed Loop Log
  (deltas go in loop receipts, not the record).
- Cross-reference, never invent (K-INVENT-1). Two deliverables share the id
  DEL-10-03 (app-dev "OperationProposal Record and Human Gate Workflow" vs piping
  "Local FEA handoff data contract") — always name the repo; never merge their rows.

## Where live work is re-derived (pointer index — never a status surface)

Work history and completion state live in git, PRs, decision records, and
deliverable-local files. This index only says WHERE to look at Step 0:

- **Decision registers** (open rows are the owner-gated surface):
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` ·
  `projects/chirality-piping/execution/_Coordination/_DECISIONS/_REGISTER.md` ·
  `_DomainEngines/_DECISIONS/_REGISTER.md`.
- **Gates**: the ADOPTED profile's open_issues "Live binding" line
  (`_DomainEngines/profiles/open_pipe_stress.yaml`) + D-T0-08's sequence.
- **Deliverable-shaped work**: harness `next` pick-lists + the briefs under
  `docs/governance_harness/briefs/`.
- **Piping's own track**: `projects/chirality-piping/docs/PLAN.md` (Phase/R rows)
  and `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md` §12.
- **App-dev's own track**: `projects/chirality-app-dev/docs/PLAN.md` (strategic
  roadmap; tactical/sequencing state routes to its `execution/_Coordination`
  artifacts, whose register rows are already indexed above).
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `_DomainEngines/bridge/LOOP_RECEIPTS.md`.
- **Shared-id hazard** (standing): two deliverables share the id DEL-10-03
  (app-dev vs piping) — always name the repo.

## Generated owner-action view (HB-2)

The hand-maintained owner-action pointer index was transitional and is replaced
by a generated view. At Step 0, run:

`PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py bridge-status`

The view is generated output, not authority. It reads the decision registers,
the ADOPTED profile's live-binding line, governed brief lifecycle records, and
the latest loop receipt; it reports sourced owner-shaped act rows and never
selects work. This workplan section intentionally carries no hand-maintained
owner-action state. Remaining harness development candidates live in
`tools/practitioner_harness/BACKLOG.md`.

## Loop Log (SEALED 2026-07-02 — immutable history, no further entries)

> Sealed at owner direction during the 2026-07-02 loop-protocol reform
> (Receipt 0 in `_DomainEngines/bridge/LOOP_RECEIPTS.md`). The narrative
> entries below are the historical record of Loops 1–2 and are never edited.
> Loop closes now append a minimal receipt to `LOOP_RECEIPTS.md` instead;
> the narrative pattern below is retired — do not imitate it.

- **2026-07-02 — Loop 1** (session of record for this plan). Discover: main
  `78a592fbf` clean; drift 92/154 all piping, flat vs recorded 92/101; self-check
  exit 0, REVIEW pins exact (2/1/0/1, DRAFT_BASIS_RULED_CLOSED=7 INFO, GEN-8=19
  files), WARN=3 UNRESOLVED_SOURCE_REF (pre-existing, un-enumerated by prior
  baseline); pytest 236 passed (+1 vs baseline = PR #12's new
  `test_adapter_domain_engines.py` test). Spot-verify: 7-agent sweep, zero refuted;
  deltas: DEC-042 item 3 already built (DEC-043), D-APP-44 is RULED Option A (not
  open), no new rulings since the 2026-07-02 assessment; D-28's 43-count verified at
  source (`event-schema.ts`). Select+Brief: CANDIDATE briefs generated with
  practitioner objectives for app-dev DEL-10-03 and DEL-10-01
  (`_harness_generated/briefs/TRB-chirality-app-dev-DEL-10-0{3,1}-2026-07-02.md`).
  Gate: STOPPED awaiting owner adoption. No governed files changed except this plan
  file (bridge/** lane, owner-directed).
  Gate outcome (same day): owner adopted BOTH briefs in-session, directed this plan to
  ride main, granted repo-wide write scope for this loop, and pulled the piping-lane
  backlog into the loop "as appropriate" — execution proceeds in Loop 1; results
  appended below on close.
  Execution (same day, main-direct at owner direction): adoption recorded and both
  fences verified ACTIVE at `abafd4d24` (first adopted briefs in this repo's
  history). Piping lane at `a0c50e5aa`: published
  `schemas/operation_outcome.schema.json` + `schemas/rule_check_run_result.schema.json`
  (derived field-by-field from the operation_applier / rule_check_runner Rust sources,
  which govern) + stdlib contract tests; appended `DEC-055` to SOFTWARE_DECOMP.md §12
  per the D-28 packet §8 mechanism (DEC-041 untouched) and pointed the D-28 register
  note at it. App-dev DEL-10-03 tranche at `4968ed485`: result-schema TBDs closed by
  cross-reference, adapter/record TBDs narrowed with residuals explicit, INSP-03
  status-wording repaired as a MEMORY forward-correction (`_STATUS.md` needed no
  change — already qualified). App-dev DEL-10-01 tranche at `9a29c0372`:
  Guidance cross-reference note, `_DEPENDENCIES.md` annotate-only satisfaction
  evidence for the three anchors (CSV untouched). Bridge lane (this commit):
  PLAN_cross_tier.md rows 40–41 reconciled (tier-1 DONE markers; entrypoint
  unbundled from the DEC-042 lane). Checks: scope-check clean both tranches
  (5/5 and 3/3 in-fence, 0 prohibited); run-validations + evidence-check 3/3 both
  briefs; closeout digests produced; piping pytest full suite passed; harness
  pytest 236 passed; drift 92/154 flat; self-check exit 0 after deleting the
  scratch evidence records (rebuildable; D-GOV-01). New harness defects surfaced
  and queued (owner-action queue items 5–6). Deferred to next loop: DEC-042
  items 1–2 design docs; D-21 packet prep (pending owner direction on lane).

- **2026-07-02 — Loop 2.** Discover: main `054f9f4db` clean, five commits past the
  Loop 1 close (`d0b53d851`) — owner-merged PR #13 harness fix (`7da70fbf5`) plus
  three owner LOOP_INIT.md bridge commits; full-diff confirms NO register,
  decision, profile, or governed-record changes in that range, so no new rulings
  landed. Measurements: status ×3 no severities (app-dev 53 / piping 101 status
  files; tier-0 contradiction pointer 5); drift 92/154 flat vs recorded 92/101;
  self-check exit 0 with REVIEW=23 (pins exact vs Loop 1: 2/1/0/1 + GEN-8 19
  files), INFO=9, WARN=3 — the 8 brief-format GEN-5 WARNs are gone and evidence
  records self-label for GEN-3, i.e. queue item 5 is discharged by PR #13
  (verified at `evidence_records.py:150` / `cmd_self_check.py:492`); pytest 239
  passed (+3 = PR #13's regression tests); `next`: app-dev 53 CHECKING, piping
  8 CHECKING / 92 IN_PROGRESS / 1 ISSUED. Spot-verify: 7-agent sweep (registers,
  Loop 1 outputs, adopted-fence residuals, DEC-042 lane, D-21 packet scope,
  readiness §1, completeness critic) — zero substantive refutations; both briefs
  still HUMAN_ADOPTED (owner review→CLOSED pending); profile hook fields still
  TBD ×4 (queue item 2 open); D-APP-45/46 AWAITING_RULING (app-dev register
  :56-57); D-21 NOT_PREPARED (held) (piping register :45). Deltas vs the maps
  (recorded here, maps never edited): (1) readiness §7 "9 RULED tier-0 register
  rows" is a MISCOUNT — the live register has exactly 8 (D-T0-01..08 at
  `_DomainEngines/_DECISIONS/_REGISTER.md:7-14`); the ninth "RULED" match is the
  register's title line. (2) readiness §1.1 cites the FM-04 record under
  `_DomainEngines/proposals/open_pipe_stress/` — that directory is empty; the live
  FM records sit under `bridge/BRIDGE_2026-06-21_tier0-prep/framework_maintenance/`.
  (3) PLAN_cross_tier who-does-what rows drifted to :47-48 (map cites :40-41);
  substance of the Loop 1 reconciliation holds. (4) readiness §1.3's "DEC-055
  still pending" is cleared (Loop 1 appended it; live at SOFTWARE_DECOMP.md:625).
  (5) piping DEL-10-03 header/history mismatch unchanged (IN_PROGRESS `_STATUS.md:3`
  vs CHECKING history :15 — known drift-92 class, K-CONFLICT-1 human call).
  Select: NO lawful agent tranche exists outside the owner gates this iteration —
  the two adopted fences are fully discharged (every remaining residual is
  human-shaped or gate-blocked: ResponsibleParty, issuance basis/INSP-04,
  _SEMANTIC_LENSING HumanRuling=TBD rows, SatisfactionStatus judgments, profile
  hook fields in a prohibited path), the tier-0 proposals lane is empty by design,
  and both open backlog items are piping-lane pending queue-item-4 direction.
  Loop 2 instead sharpened the gate: D-21 packet prep is execution-ready (one new
  file `execution/_Coordination/_DECISIONS/D-21_prd_scope_change_v0_2_milestone_set.md`
  on the D-28 packet skeleton — PROPOSAL disclaimer; §2 verified-facts checked
  cold; §4 options adopt-v0.2-set / decline-terminate-at-R5 / adopt-delta; §7
  Human Ruling left OPEN; §8 mechanism DEC append + register row NOT_PREPARED→
  AWAITING_RULING; content = v0.2 scope delta (R6/R7 + inserted R3 from
  `docs/_ScopeChange/OpenPipeStress_PRD_v0.2.md`) + the mandatory
  traceability-breaking FR crosswalk (flat FR-001..025 → FR-MOD/KNOW/GUI/SOL/RULE/
  CMP/HAND/AGENT/REP per `plans/PLAN_2026-06-17_prd_completion.md:263`); prerequisite
  D-27 RULED; adoption hold intact); DEC-042 items 1–2 have NO owning deliverable
  (no PKG-16 Spec scopes them; no design artifact exists; DEL-16-05 slot free) —
  owner scoping act required on top of lane direction. Gate: STOPPED — no piping-lane
  writes, no briefs generated (nothing deliverable-shaped exists to fence: the D-21
  packet is coordination-level; DEC-042 items lack a deliverable). Work done this
  iteration (bridge lane, this commit): backlog rows executed in Loop 1 marked
  DONE; queue item 5 marked DONE (PR #13); queue item 4 sharpened with the
  execution-ready D-21 scope and the DEC-042 scoping sub-decision. Owner-action
  queue after this loop: items 1–4 and 6 open. Next iteration unlocks on any of:
  item 4 direction (D-21 packet prep executes immediately; DEC-042 items 1–2 once
  scoped), item 2 tier-0 CHANGE (closes the profile's four hook TBDs against the
  published schemas), D-APP-45/46 rulings (keystone: F3 sequence + DEC-041
  automation), or brief review→CLOSED (item 1 lifecycle completion).
  Gate outcome (same day): owner directed in-session — "Consider the dependencies
  and plan to execute all items, working in parallel when write scopes are
  mutually exclusive." Read as: queue-item-4 lane direction granted (piping-lane
  backlog runs in this loop); all agent-executable items proceed; owner-only acts
  (rulings, adoption, CHANGE application, brief CLOSED) stay owner-side as
  prepared packets.
  Execution (same day, branch-first + PR per protocol step 4 — Loop 1's
  main-direct grant was not assumed to extend): three parallel worktree branches
  with mutually exclusive write scopes, each implement→adversarial-review(→fix)
  verified, all three clean with zero BLOCKER/MAJOR findings (~115 citations
  cold-checked by independent reviewers). (1) PR #14 `loop2/d21-packet-prep`
  (`3b03430cb`): D-21 SCOPE_CHANGE packet on the D-28 skeleton — §7 Human Ruling
  literally OPEN, adoption hold intact; Annex A complete FR crosswalk, all 25 flat
  v0.1 FRs → v0.2 successors with dual citations (12 DIRECT / 7 SPLIT / 2 MERGE /
  2 NARROWED / 3 UNMAPPED, explained); register row 45 → AWAITING_RULING (adoption
  held) per the register's own precedented vocabulary (D-28 pre-ruling row doesn't
  exist in history — it landed RULED — so precedent taken from rows D-15..D-26 and
  D-28 §8's own token usage); piping pytest 369 passed in-worktree. Packet §2
  records the owner direction as superseding DEC-042's "no packet is prepared
  while held" clause for PREPARATION only — flagged for confirmation at ruling.
  (2) PR #15 `loop2/dec042-design-docs` (`adfebfcff`): DEC-042 items 1–2 design
  docs in piping `plans/` under the fence-free prep sanction; substantive
  discovery recorded in doc 1: the app-dev harness has NO formal Plan/step type
  today, so the OperationSet→Plan extension is a piping-side envelope with the
  app-dev half labeled OPEN; both docs state the three live gates and leave the
  landing spot (decomposition vs DEL-16-01 amendment) to the owner. (3) PR #16
  `loop2/tier0-change-prep` (`dd6dfb951`): tier-0 CHANGE packet for queue item 2 —
  exact before/after for :81/:88 → operation_outcome.schema.json, :115 →
  rule_check_run_result.schema.json, :101 as a reasoned owner choice, plus the
  :72-74 header-comment edit; ADOPTED profile byte-identical on the branch.
  Tasking correction caught in-execution (K-INVENT-1, tree governs): profile :143
  is the live-binding gate line, NOT a schema-TBD line — no :143 edit proposed;
  this entry corrects the Select paragraph's ":143 open_issues" framing above.
  New environment fact: fresh worktrees measure self-check WARN=8 (not 3) —
  four committed-brief refs point at gitignored `_harness_generated/` paths and
  CHANGE_HANDOFF.md:41 cites the untracked empty proposals dir; all three
  branches verified finding-neutral against a same-environment baseline (byte-
  identical finding sets), and the WARN=3 main-checkout baseline still holds.
  Checks: per-worktree harness self-check exit 0 ×3 (finding-neutral); piping
  pytest 369 passed (PR #14 worktree); CI governance-harness workflow green on
  all three PRs; scope containment re-verified by reviewers AND by the main loop
  (diffs: exactly 2 + 2 + 1 files, no overlaps). Owner queue after execution:
  item 1 (brief review→CLOSED), item 2 (apply PR #16's CHANGE after merge),
  item 3 (D-APP-45/46), item 4 residue (merge PRs #14/#15/#16; confirm the
  prep-supersession read at D-21 ruling; choose the DEC-042 design landing spot),
  item 6 (PR #16 §4 proposals; fresh-clone WARN=8 note). Owner merges — never
  self-merge (protocol step 5); this close-out commit rides main in the bridge
  lane like Loop 1's and c0934ca61 before it.
  Rulings round (same day, owner in-session): owner directed push→merge→rule;
  main pushed (`054f9f4db..7eabe0ff2`), PRs #14/#15/#16 owner-merged
  (`4f6846565`/`6d893e9eb`/`3e965f021`), merged tree self-check clean at the
  exact WARN=3 baseline. Owner then ruled the full slate: R1 D-21 = O-A with
  the §5 rider + sub-confirmation (i), §7 fill confirmed; R2 tier-0 CHANGE
  approved with :101 Option A + version bump, execution explicitly delegated;
  R3 DEC-042 designs stay in plans/ until R7 has weight; R4 briefs signed off;
  R5 D-APP-46 Option A + D-APP-45 recommendation approved; R6 (a)(b) adopted,
  (c)(d) defaults, (e) optional taken, (f) ruled "all shall be IN_PROGRESS"
  class-wide. Executed across five mutually-exclusive-scope branches (every
  one implement→adversarial-review clean, zero BLOCKER/MAJOR): PR #17
  `loop2/tier0-change-apply` (profile hooks bound ×4, :101 Option A,
  profile_version 0.1-DRAFT→0.2, validator VALID; CHANGE_HANDOFF:27 +
  PROFILE_STATUS + .gitkeep maintenance; D-T0-06/D-GOV-07 byte-untouched per
  defaults; live-pin fix `ca071b64f` after CI caught the regenerated
  validation report's transient worktree path — re-validated from the
  canonical checkout path, pin exactly-one ABS_PATH_IN_EVIDENCE holds). PR #18
  `loop2/rulings-record` (briefs CLOSED ×2, verify-adoption terminal posture
  confirmed; D-APP-46 + D-APP-45 RULED per the D-APP-44 pattern, Ruling SHAs
  TBD-until-merge). PR #19 `loop2/d21-ruled` (§7 filled per D-28 post-ruling
  precedent; DEC-056 appended at SOFTWARE_DECOMP.md:626; register row 45
  RULED; SCA propagation authorized NOT executed). PR #20
  `loop2/status-class-correction` (the R6(f) class ruling executed: 92
  reversal history entries authored — parser-verified as IN_PROGRESS
  assertions — Decision_Log at LIFECYCLE_CORRECTION_2026-07-02_2050 mirroring
  the 2026-05-11 precedent, _LATEST repointed, adapter baseline re-measured
  0/101; drift 92→0 over 154 files, reviewer re-derived the mismatch set
  byte-identical; conscious live-pin update 92/101→0/101 +
  prose_bullet_v1/README refresh in the same PR so CI is self-consistent).
  D-GOV-07:26 forward note per R6(d) default: the WARN stands as
  accepted-known; the decision record is not edited — this Loop Log entry is
  the forward note. Gate posture after this round: live-binding ×4 → piping
  D-21 CLEARED (DEC-056); tier-0 adoption already cleared; remaining two —
  app-dev F3 and DEC-041 automation — both route through the now-greenlit
  package extraction (D-APP-46 Option A). Owner acts remaining: merge
  PRs #17–#20 + fill the two Ruling SHAs (queue item 0); direct the SCA
  propagation and the extraction tranche when ready.
