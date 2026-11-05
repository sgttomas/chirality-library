# PR #188 Review — Feedback for the authoring agent

Reviewed at head `5f20ce750` against `origin/main` (`667a679`). Method: 10-lens
multi-agent review (plan fidelity, decision-record integrity, ontology,
epistemology, axiology, praxeology, paused-run safety, export boundary, code
correctness, validation-claim reproduction), every finding adversarially
verified against primary sources, plus a completeness critic over all 170
changed paths. 73 findings verified (61 main run + 4 hand-verified + 8
continuation-verified), 2 more from the critic, 3 refuted. The full corpus
with evidence and verifier reasoning is in
`PR188_multi_agent_review_2026-07-11.md` (same directory).

## Verdict

**Not ready to merge as-is.** The instruction-layer work is strong — plan
fidelity is high, the mechanical decision-record bindings are sound, all four
validators pass as claimed (33 agent packages 0/0, 43 skills valid, 762 root
tests reproduce), the export manifest is byte-identical to a fresh
regeneration, and the paused concordance runs' evidence folders are untouched
(their loop files are modified — see §A.4).
But the PR currently (a) violates ratified canon it leaves in force, (b)
manufactures authority for two of its own documents, (c) strands both
owner-priority paused runs, (d) ships orchestration machinery whose central
paths are demonstrably non-functional, and (e) contains one false claim in an
immutable validation record. Each is fixable; several need an owner ruling
rather than an edit.

## A. Blocking — fix or obtain an explicit owner ruling before merge

1. **K-AGENTS-1 is violated by the PR's own tree.** Ratified
   `docs/CONTRACT.md:131` mandates that root `AGENTS.md` carry the agent
   matrix; the PR deletes the NORMATIVE/OPERATIVE/EVALUATIVE ×
   GUIDING/APPLYING/JUDGING/REVIEWING matrix without amending K-AGENTS-1 or
   TYPES §9.1–9.2, which still reference it (now dangling). The only surviving
   instantiations are the non-authoritative thesis and a frontend routing
   file. Restore the matrix (or a pointer), or amend K-AGENTS-1 and TYPES §9
   in the same change under a recorded ruling.

2. **D-GOV-13 is an agent disposition presented as an owner ruling.** Its
   HumanRuling cites the approved plan plus "session-wide governance-change
   authority," but the plan contains no requalification content and names none
   of the 14 roles; the record's Ruling SHA is the same agent-authored
   implementation commit that created the record and all 14 frontmatter
   declarations. Under the canon (rulings are owner acts; agent dispositions
   are never human rulings) either the owner explicitly ratifies the D-GOV-13
   table at merge and the record transcribes that act, or the record is
   reframed PROPOSED pending ruling. Also: bind the full 40-char SHA like
   every sibling record.

3. **`docs/SOFTWARE_WORKFLOW_PROFILE.md` self-declares RATIFIED via an
   uncommitted plan** — conflating authorization-to-implement with
   acceptance-of-product, which D-GOV-10 itself forbids ("implementation
   artifacts do not acquire authority merely because they were written"). Its
   sibling `WORKFLOW_COMPONENT_STANDARD.md` does this correctly (CANDIDATE
   until accepted). Set CANDIDATE or transcribe a real owner ratification.
   Same fix for `docs/DECOMPOSITION_STANDARD.md`, which claims "this
   specification governs" with no status/provenance block at all, and for the
   CANDIDATE-vs-binding contradiction (DIRECTIVE/AGENTS.md already bind
   WORKFLOW_COMPONENT_STANDARD as governing while its banner says CANDIDATE).

4. **Both paused concordance runs are un-resumable post-merge; no in-flight
   carve-out exists.** New root doctrine ("Multi-agent execution requires the
   managed runtime… defer the multi-agent stage") plus LOOP_INIT §7 clause 6
   in both projects forbid exactly the dispatch mechanism the owner steers
   durably prescribe (four concurrent TASK discovery agents, recorded verbatim
   in app-dev Receipt 18 / piping Receipt 17, resume points in Receipt 22 and
   the resume prompts). `delegate_agent` exists only in the app-dev frontend
   harness, not in the Claude Code loop sessions these runs execute in. Both
   entry paths mandate STOP on material contradiction. Additionally, the
   §7→§8 renumbering of "Session conventions… per-run steer" dangles the
   steers' "overrides LOOP_INIT §7 defaults" reference in both projects, and
   the new `_Coordination/AgentRuns/` record mandate conflicts with the runs'
   pinned authorized write surfaces. Fix: an explicit in-flight carve-out in
   LOOP_INIT §7 (and/or D-GOV-12) — "the two active concordance runs complete
   under their pinned method revision and recorded steers" — plus either
   restored section numbering or a "(formerly §7)" alias.

5. **The exported CI workflow hard-fails the public repo.** The refreshed
   export carries `.github/workflows/harness-premerge.yml`, which triggers on
   public paths (`agents/**`, `AGENTS.md`, …) but runs every step under
   `projects/chirality-app-dev/frontend`, absent from the public tree. Strip
   or gate it in the export profile.

6. **A validation claim in the immutable handoff record is false.**
   `D-GOV-11_IMPLEMENTATION_HANDOFF.md` states "`git diff --check` reported no
   whitespace errors"; against the merge range it exits 2 with 26
   blank-line-at-EOF errors, all in PR-added files (the five software-* skill
   packs and six software_workflow tools). Strip the blank lines and correct
   the record (or have the owner accept the discrepancy explicitly). The other
   validation claims reproduce — say so precisely, because this repo treats
   handoff records as evidence.

## B. The orchestration machinery has non-functional central paths

The PR's core feature partially does not work; none of this is recorded as
deferred:

7. **Managed delegation to all 14 D-GOV-13 dedicated Agent 2 specialists is
   dead.** `assertChildToolPolicy` derives the child allowlist from
   frontmatter `tools:`; none of the 14 files declares one, so
   `parseCommaSeparatedList(undefined)` yields `[]` — any non-empty tools
   request fails, and a zero-tool child cannot do its job. ORCHESTRATOR's own
   frontmatter allowlists PREPARATION/DOMAIN_HYPERGRAPH as managed children.

8. **Instruction-prescribed dispatches are forbidden by the enforced
   allowlists.** ORCHESTRATOR Phase 4.3 says "Spawn AGGREGATION" but its
   `subagents:` omits AGGREGATION; AUDIT_SCOPE_CLOSURE says "dispatched by
   EVALUATION" but EVALUATION's allowlist omits it; WORKING_ITEMS permits
   "approved dedicated Agent 2 roles" while allowlisting only TASK. Two
   just-requalified specialists have no lawful dispatcher. The new validator
   doesn't catch allowlist gaps — add that check.

9. **WAIT-mode children can never report notices or ack updates**
   (`childSessionId` is written to STATUS.json only after the child returns;
   `assertManagedChildSession` requires it mid-run) — the supervised
   many-to-many channel fails closed for every synchronous child, though
   AGENT_TASK ships `report_coordination_notice` in its tools.

10. **Write-disjointness has a TOCTOU** — `assertNoActiveWriteOverlap` runs
    before the instance's own STATUS.json exists, so concurrent `delegate()`
    calls with overlapping writeTargets all launch (reproduced), defeating
    D-GOV-12's "concurrent sibling writes must be disjoint" exactly in the
    concurrent case it exists for; the catch also silently skips siblings with
    corrupt STATUS.json.

11. **First failed `delegate_agent` wedges the parent session** — the handler
    persists `orchestrationRunId`/`executionRoot` before validation; after a
    rejected runId, corrected retries fail "must remain in the parent
    orchestration run" forever.

12. **`validate_change_scope.py` cannot see untracked files** — `git diff
    --name-only` lists only tracked modifications, so out-of-scope file
    *creation* (the most common containment violation) passes the gate the
    software skills bill as the K-WRITE-2 mechanical evidence. Add
    `git ls-files --others --exclude-standard`.

12b. **readOnly sessions can delegate children and write control-plane
    records.** The permission overlay
    (`projects/chirality-app-dev/frontend/src/lib/harness/permission-overlay.ts`)
    admits any 'coordination'-permission descriptor (`delegate_agent`,
    `report_coordination_notice`, `send_agent_update`, `ack_agent_update`) in
    EVERY session mode, deferring wholly to handler-level checks — so a
    readOnly session can launch children and mutate orchestration records.
    Gate the mutating coordination tools on session mode like other write
    surfaces. (Found by the completeness critic in a file no lens had
    covered.)

13. Smaller praxeology breaks: WORKING_ITEMS' minimal brief and the harness
    Launch Brief omit `ScopePath`, the one field TASK hard-requires; software
    skill briefs use `Exclusions` where TASK accepts `EXCLUSIONS`; managed
    TASK children can't satisfy the TASK shell's mandatory run-record write
    under the harness write fence; plan step 9 (route the legacy SDK bridge
    through the managed service) did not land and the adapter remains a
    record-less parallel delegation path — record as deferred if intended.

## C. Value-language drift (axiology) — reconcile or get owner acceptance

14. **K-SEAL-1 was rewritten to drop "gate-approved by a human"** in favor of
    a non-empty, unverified approval-reference string, and the enforcement
    column names ManagedDelegationService although what it verifies is agent
    self-attestation — while D-GOV-11/12 both state no human gate is weakened.
    Restore the human-approval semantics or have the owner rule the change.
    Note: the seven changed files under `projects/chirality-app-dev/docs/`
    (PRD, CONTRACT, SPEC, TYPES, …) replicate this same K-SEAL-1 weakening at
    project level — fix both layers together.

15. **"Every gate" was systematically narrowed to the undefined term
    "consequential gate"** across PROFESSIONAL_ENGINEERING.md, TYPES.md, and
    thesis ch. 06, and D-GOV-12 §9's categorical return-to-human triggers
    appear in the operative doctrine as self-judged "consequential"
    amendments. Define the term against §9's five categorical triggers, or
    restore the categorical wording.

16. Thesis chapters 06/07, appendices A/C still assert the superseded
    human-authority semantics and cite DBM section anchors the rewrite broke —
    the professional-responsibility story is currently inconsistent with the
    architecture the same PR ships.

## D. Cleanups (fix in this PR or a fast follow-up)

- Stale ratified surfaces: `SE_Design_Analysis.md` §4.1 still lists deleted
  SCHEDULING (and nonexistent ESTIMATING) as live writers and WORKING_ITEMS as
  deliverable-local; SPEC §6.5 ConsumerHint still names RECONCILIATION for
  moved semantics; thesis glossary keeps the pre-D-GOV-11 "Type 1 (Manager)"
  entry; Appendix A cites AGENT_HELPS_HUMANS.md as R-series source.
- SCHEDULING (a live Agent 1) was deleted/merged with no decision-record
  anchor — add one line to D-GOV-11 or the handoff naming it.
- `AGENT_DISPOSITION_MATRIX.md` contradicts the handoff's COMPLETE verdict and
  misstates the app-dev pause boundary as W1/W2 (durable record: W2/W3).
- D-GOV-10 supersession notes name directions its record never contained.
- `DECOMPOSITION_STANDARD.md` promotes PKG-XXX/DEL-XXX-YY (3-digit) against
  ratified TYPES §2 PKG-XX/DEL-XX-YY.
- Five deleted agent files remain ACTIVE manifest-backed sources in
  `domains/chirality/_Sources/Source_Manifest.csv` with no staleness
  disposition.
- `agents/AGENT_AUDIT_AGENTS.md` was only partially rebound to the rewritten
  `docs/rubrics/AUDIT_AGENT.md`: Step 2 matches the new
  CONFORMS/PARTIAL/NONCONFORMANT scheme, but other sections still instruct the
  auditor to produce the old rubric's marking artifacts.
- Export: `init/init-prompt.md` (public) points at loop entrypoints absent
  from the public tree; the boundary scan matches only the literal
  `/Users/<owner>/ai-env/projects` prefix, so "Boundary findings: 0" overstates
  the check; the refresh newly publishes TRB briefs, D-GOV-09..13, the
  handoff, and the harness BACKLOG — confirm that is intended, and note
  `human_actors.md` carries owner personal identifiers (pre-existing).
- ClaimStatus VALIDATED/ACCEPTED have no defined asserting authority or
  required acceptance reference; the RELAY claim-status guard is bypassable
  when the parent omits the source noticeId; glossary lets Agent 0 "return
  rulings" and Agent 1 "make manager-level decisions at human gates" —
  tighten the ruling/gate vocabulary.

## E. Additional verified code findings (initially interrupted, since
## confirmed by a continuation verification pass)

All eight of the previously unverified findings survived adversarial
re-verification (empirically reproduced at the cited lines):

- [minor] `dedicated_agent2_approval` enforcement is looser than D-GOV-13's
  stated contract: the field is matched anywhere in the file body (not
  frontmatter — reproduced by moving it into a code block: validator still
  passes 33/0/0), the role check matches any table anywhere in the record,
  and a missing field is WARN + exit 0. Scope to `frontmatter_block()` and
  anchor the role match to the Ruling table.
- [minor] The R-identifier scan (`validate_agent_instructions.py:193`)
  hardcodes the catalog boundary: R6–R17 and all R100–R199 tokens are never
  checked against the catalog (R117 passes silently, R217 is flagged). Use
  the already-loaded `valid_r_ids` for membership instead.
- [minor] The "762 passed" figure depends on an untracked generated staging
  tree; regenerating it breaks whole-repo pytest. Document the required
  generation state next to the claim, or make the suite hermetic.
- [note] Sealed-context read scope has no symlink defense (writes do):
  `tool-path-policy.ts` read containment is purely lexical; a symlink inside
  a granted read root can escape it.
- [note] `delegate_agent`'s BACKGROUND completion handler can raise unhandled
  promise rejections (crash risk for the harness process).
- [note] `run_registered_checks.py` runs registered check commands with no
  subprocess timeout and an unconstrained `--output` path.
- [note] Handoff closure verdict false-closes on unknown instance statuses —
  forward-fragility only (all current writers emit the five known literals);
  fix the status regex inversion.
- [note] The harness's unwired conformance validator
  (`agent-instruction.ts` `ALLOWED_WRITE_SCOPES`) is missing the newly
  ratified `package-level` / `bounded-task-brief` values — latent until
  wired, then it would spuriously warn on WORKING_ITEMS/TASK.

Still unverified (deliberately not re-run — too heavy): the app-dev frontend
suite (682 tests) and the remaining piping suites (Rust/desktop/browser/WASM);
piping's 459 Python tests were re-run and pass. One lens reported the frontend
suite passing but this was not independently reproduced — treat the PR's own
CI evidence as authoritative there.

## What was checked and found sound

Branch is current with main and the sync merge is tree-identical; all four
Ruling SHAs resolve and match content; register rows match records; the
terminal-artifact rule is respected; RECONCILIATION faithfully preserves the
ratified concordance method's guardrails; no paused-run execution artifact is
modified relative to origin/main; K-AUTH-1 human-only approval is intact;
Agent 2 cannot delegate (enforced in code); no path permits self-merge or
lifecycle advancement; export manifest hashes verify against a fresh
regeneration; claimed validator/test counts reproduce (except the
`git diff --check` claim above).

## Suggested disposition path

Two different cures apply, and conflating them would repeat the PR's own
category error (agent-manufactured authority), so keep them separate:

**Requires edits on the branch (no ruling can cure these):**
A1 (restore the matrix or amend K-AGENTS-1 + TYPES §9 together), A4 (in-flight
carve-out for both paused runs + section-numbering fix), A5 (strip/gate the
exported CI workflow), A6 (whitespace + correct the handoff record), all of
§B (the machinery either works or its gaps are recorded as deferred in a
decision record — including 12b), and the §D cleanups.

**Curable by an owner act transcribed at merge (edits optional):**
A2 (ratify or reframe the D-GOV-13 table — one recorded owner sentence
naming the 14 roles suffices), A3 (either ratify SOFTWARE_WORKFLOW_PROFILE /
DECOMPOSITION_STANDARD explicitly or downgrade their status lines to
CANDIDATE), and §C items 14-15 if the owner deliberately accepts the
"consequential gate" narrowing — in which case the term must be defined and
the thesis/PE claims updated to match, rather than left contradicting the
shipped architecture.

**Sequencing suggestion:** land the §A/§B edits and re-run the validators;
then put the owner acts (A2/A3/§C acceptance or rejection) in the merge
ruling itself, so the authority chain for this tranche starts clean. The
review record's finding IDs (C01-C61, H01-H04, V01-V08, CR) in
`PR188_multi_agent_review_2026-07-11.md` carry the evidence for every item
above; cite them in your closure receipts rather than re-deriving.
