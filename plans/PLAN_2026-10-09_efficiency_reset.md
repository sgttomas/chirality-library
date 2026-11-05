# Efficiency reset: implementation plan (revision 3, final)

**Status.** The owner approved the consensus path on 2026-10-09 and directed this plan into `plans/`. The texts in §1 put that consensus into practice; they are not the owner's verbatim wording. Three agents agreed the plan: Agent 1, Agent 2 and Agent 3. Basis: `origin/main` `61f29595c2`. The implementer reconfirms the basis at the start (PR 1 item 0). Counts in this plan are starting evidence, not fixed assumptions.

## 0. Roles and review
| Who | Role |
|---|---|
| **Agent 3** | Implements every PR and repairs its own work |
| **Agent 2** | Reviews PR 1 and the archive; sets Piping's migration point |
| **Agent 1** | Reviews PR 2 and PR 3 by running them; measures |

**Review.** Each PR gets one reviewer, who returns findings only: file:line and the consequence. One pass is a budget preference, not a rule, so material repairs are checked again. Claude reviewers work at moderate effort, with no subagent fan-out.

## 1. Texts

### 1.1 Operating rules (the core of `AGENTS.md`)
1. **The principle.** Agents produce the work and the minimum information needed to review, use or recover it. A record needs a concrete consumer, an acceptance requirement or a recovery need.
2. **Authority.**
   - Previous development procedures are superseded.
   - Current product commitments, explicit holds, reserved decisions and applicable interface contracts remain effective until they are incorporated into their surviving home.
   - The entry points are:
     - this file and the role file;
     - `coordinated-knowledge-work`;
     - the project's `LOOP_INIT.md`;
     - the project's product documents (PRD, `ScopeOfWork.md`, Design);
     - the "Contracts still in force" list.
3. **The PR is the change record.** It says what changed, why, what was checked, and what remains open. A reserved decision is quoted in the owner's words. Naming the verification class is optional.
4. **Decisions edit the current text they govern.** No append registers. Git keeps the history.
5. **The deliverable folder** holds `ScopeOfWork.md`, `Design/` when useful, and `deliverable.yaml`.
   - Do not hand-maintain derived progress or lifecycle state.
   - Maintain current commitments, design and dependency conditions in their source files.
6. **Verify in proportion to consequence.**
   - Routine, reversible changes: inspection or direct exercise.
   - Ordinary implementation: a focused check.
   - Numerical meaning, persistence, permissions and destructive operations: targeted regression tests, plus independent scrutiny by a separate agent.
   - Releases: checks of the actual product.
   - Changing an expected result to silence a failure needs a stated reason.
7. **Reserved for the owner:**
   - changes to commitments or acceptance criteria;
   - releases;
   - risk acceptance;
   - anything an explicit hold names.
8. **Hard boundaries:**
   - each project's fences, stated in its `LOOP_INIT`;
   - nothing private in this public repository;
   - the secret and private-term checks.
9. **Models and effort.** Model and effort choices come from per-session steering; repository instructions carry no model or effort doctrine.
10. **Contracts still in force.**
    - These pointers identify surviving contracts.
    - Agents work from this list and the project documents; they do not need to search the historical documents routinely.
    - Omission does not supersede a current product commitment, applicable interface contract, owner decision or explicit hold.
    - An agent that finds one outside this list adds it here, or moves it into the project document it governs, in the same PR.
    - Keep the list short: it is navigation, not an authority register.

### 1.2 Restated standing Git grant
> For `sgttomas/chirality` only, agents may commit, push, open, update and merge PRs within authorized work. Before merging, verify the change in proportion to its consequences and confirm the required checks pass on the exact head commit. Changes affecting numerical meaning, persistence, permissions, destructive operations or releases also get independent scrutiny from a separate agent. Explicit holds and reserved decisions still apply. The grant does not cover protection bypasses, history rewrites, force pushes, permission changes or releases.

### 1.3 Steer for active sessions (sent by the owner)
> Effective now: stop routine administrative records — run records, receipts, handoff chains, ledgers (including ROOT_RULINGS), notices, MEMORY entries, `_STATUS` updates, and copied source or logs. Keep a record only where it has a concrete consumer, an acceptance requirement or a recovery need. The PR description is the change record. Record a decision by editing the text it governs and give the reason in the PR. Don't move deliverable folders or delete records yet; migrations happen at announced points. Coordinate any instruction edit that overlaps the Root reset. Until that reset merges, an instruction edit still needs a manifest. Verify in proportion to consequence. Keep explicit holds and reserved decisions.

## 2. Work packages

### Phase 0: steer and baseline
- **The owner sends §1.3,** and decides whether the Piping T3 session pauses until Phase 4 or finishes only I4.
- **Per-PR baseline, 2026-09-25 to 10-09 (taken by Agent 1):**
  - 322 merged PRs;
  - about $17 of Claude spend per PR at list price;
  - 86% of October commits touched no code or tests;
  - 57 record lines per line of code and tests (1.9:1 for prose alone);
  - Claude output tokens: 23% on records against 1.4% on code;
  - $728 of subagent cache rebuilds after waits;
  - 2.4% of Claude cost spent on turns that only check state or poll.
- **Codex per PR:** these are period totals divided by merged PRs: about 0.41M uncached input, 22M cached input and 50K output tokens per PR. Threads in sibling folders are excluded, which may undercount Piping.
- **Per-slice baseline (Agent 1):** attribute tokens and active agent time to **completed slices** within App v4 Group B, Group C and Piping T3, and state the uncertainty. This runs in parallel and does not gate PR 1.

### PR 1: Root reset (Agent 3 implements; Agent 2 reviews)
This is one PR made of small commits, each retiring a duty together with the check that enforces it.

**0. Reconfirm the basis.**
- Check branch protection and rulesets. As observed on 2026-10-09: one required check, `harness`, `strict` false, no rulesets.
- Check the repository state and the actual migration inventory.

**1. `AGENTS.md`.**
- Add §1.1 and §1.2.
- Add `coordinated-knowledge-work` to the central workflow table.
- Repair the dangling "requirement below" sentence.
- Build the contracts list (rule 10) by reading DIRECTIVE, CONTRACT, SPEC, TYPES, AGENT_WORKFLOW_RUNTIME and the standards for their actual standing. Where a product contract belongs in a project PRD, move it there. Keep the list short; omission supersedes nothing.

**2. Headers on old documents.**
- A document now wholly historical gets: *"Reference and history; not binding. See AGENTS.md."*
- A document mixing retired procedure with live contracts gets: *"Development procedures in this document are superseded by AGENTS.md (2026-10-xx). Current product contracts remain in force; see the list in AGENTS.md."*
- Replace the stacked status banners with these headers. Repair nothing else inside the documents.

**3. The Git grant.** `.agents/skills/chirality-change/SKILL.md` and `docs/PRD_ROOT.md` §5.3.1 point to §1.2, and the stale wording goes. Branch-prefix defaults are unchanged.

**4. Retire these by name, together with their callers.**
- **Guards and state:**
  - G0 `validate_root_materialization_fence.py`
  - G1 `validate_root_harness_adapter.py`
  - G2 `validate_root_surface_ownership.py`
  - G3 `validate_root_work_graph_dispatch.py`, with `execution/_harness/*.yaml` and `root_governance_state.py`
  - G4 `validate_instruction_tranche_manifest.py`
- **Receipt and status tooling:**
  - `validate_{app_dev,pec,piping}_loop_receipts.py`
  - `loop_receipt_contract.py`
  - `root_historical_status.py`
- **Hold-register preflights:** those in the App v3 and PEC loops.
- **Tests:** the test suites of everything above.
- **Callers to change in the same PR:**
  - `adapter_loader.py` and `adapter_project.py`;
  - `cmd_self_check.py`;
  - `root_runtime_successors.py`;
  - `tools/REGISTRY.md`;
  - `tools/scaffolding/apply_root_retirement.py`;
  - `tools/practitioner_harness/test_agent_runs_archive.py`;
  - the root-command refusal messages in `harness.py` that reference `execution/_harness/adapter.yaml`.

The scope is obsolete development administration only. Product persistence, input-validation and security checks are untouched.

**5. Keep the `harness` job in `governance-harness.yml`.** It produces the only required check, so it must keep running. Its contents shrink to:
- the conflict-marker check;
- the run-record leak check, re-scoped to what is still committed;
- the private-term check;
- the test suites of tools that remain.

Branch protection changes only in PR 3.

**6. Workflows.** `construct-local-work-graph` and `bounded-reconciliation` lose their compulsory closeout, RECEIPT and MEMORY steps. A work graph becomes optional and generated.

**7. Loop entry and init prompts.**
- Root `execution/_Coordination/LOOP_INIT.md` is cut to a few lines.
- The App v4 and Piping `loop/LOOP_INIT.md` files become terse:
  - location;
  - entry points;
  - the tool, once PR 2 lands;
  - hard boundaries;
  - the objective, which comes from the init prompt.
- `init/dev-loop-init-prompt.md` and the other live init prompts get correct entries, after checking their actual entry points.
- The dormant header goes only where inspection confirms dormancy.

**7a. Piping boundaries.** Before `PROJECT_GUIDANCE.md` becomes historical:
- copy F-PIP-1..4 byte for byte into Piping's `LOOP_INIT`. Their definitions are in `loop/WORKPLAN_2026-07-18b_piping_loop.md`, and DEC-081 forbids editing F-PIP-2's text;
- copy DEC-043 into the same file;
- verify both against the current basis.

**8. The overlay fix.**
- Remove `agentsOverlay` from `projects/{chirality-app-dev,chirality-runtime,pec}/chirality.project.json`.
- Update the protected path in `_DomainEngines/profiles/pec.yaml`.

**PR 1 is accepted when:**
- the required `harness` check is reported and passes;
- no maintained executable path or live document depends on a removed module (historical records are not rewritten just because they mention a retired command);
- a search for remaining recording duties has been reviewed (the search is a discovery aid, not a gate);
- the review is clean.

### PR 2: App v4 pilot (Agent 3 implements; Agent 1 reviews)
**Timing:** after Group C's next quiet boundary. The pointers Group C needs are updated in the same PR.

**1. Flatten the folders,** for example `execution/PKG-07/DEL-07-02/`, with long names in the scope of work and the YAML. Naming is the implementer's call. Fix the references the move breaks.

**2. Migrate dependencies by meaning** (`tools/deliverables/migrate_dependencies.py`, reused for Piping).
- **Inputs:**
  - the 567 active EXECUTION rows; the 7 retired rows are excluded unless restored;
  - declarations found only in `_DEPENDENCIES.md`, which are flagged rather than imported as narrative.
- **Rules:**
  - The consumer's UPSTREAM text is the need.
  - DOWNSTREAM rows that add timing, scope or a restriction fold into the need's condition.
  - Contradictions are flagged.
  - Local pairs with only a DOWNSTREAM row are inverted into the consumer's need.
  - Distinct conditions on one pair stay distinct needs (145 pairs have them).
  - Needs are consolidated only when demonstrably equivalent.
  - Timing and restrictions held outside `Statement` are carried over.
  - Targets that aren't deliverables (151 external, 26 documents, 17 packages, 14 unknown) are typed. Nothing is written outside the project.
  - Relationships that DAG-004 holds as non-gating stay `gating: false`.

  ```yaml
  id: DEL-07-02
  name: Connector recovery
  code_paths: [app/src-tauri/src/recovery/**]
  needs:
    - from: DEL-04-01            # or external:<name> | doc:<path> | package:<id> | unknown
      condition: "PEC connector definition input available with its failure behaviour"
      when: "before qualification"
      gating: true
      evidence: app/src-tauri/tests/recovery.rs::connector_failure
  checks: [app/src-tauri/tests/recovery_*.rs]
  ```

**3. Accounting** (printed to the console and summarized in the PR).
- Every active input is accounted for as preserved, consolidated with a named partner, or excluded with a reason.
- **Focused cases:**
  - distinct conditions on one pair;
  - DOWNSTREAM inversion;
  - each type of non-deliverable target;
  - unresolved inputs;
  - retired rows;
  - declarations found only in `_DEPENDENCIES.md`.
- Running the migration a second time changes nothing.

**4. Compare with DAG-004 by meaning.** The 212 active pairs are compared against DAG-004's 129 admitted arcs and 83 held, non-gating candidates, using its own build rule. Every difference is explained, and no non-gating relationship becomes a blocker.

**5. Per-deliverable administrative files.**
- **Relocate first:** useful `_REFERENCES` sources, `_CONTEXT` identity and scope facts, and notes that encode a condition.
- **Then remove:** `Dependencies.csv`, `_DEPENDENCIES.md`, `_STATUS.md`, `MEMORY.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_SEMANTIC*` and `_run_records`.

**6. Seed `code_paths`.** Unmapped paths are allowed.

**7. CLI v0 in `tools/deliverables/`.**
- Commands: `neighborhood`, `impact`, `touches`, `dag-diff` and `check`.
- It reuses suitable graph functions, without the old lifecycle or approval machinery.
- Its JSON names the revision read and any working-tree changes it saw.
- `check` treats malformed identities or syntax as errors. Well-formed unresolved needs and cycles are reported with their source locations and never fail.
- Partial results carry "unknown" where data is missing.

**8. Baseline tag.** After merge, create `app-v4/deps-baseline-1` citing DAG-004's existing acceptance and the migration PR.
- Owner words are needed only for **substantive** differences listed in PR 2.
- A difference is substantive if it changes the gating edge set or what a need's condition means.
- Differences that are only representational, or explained by DAG-004's own build rule, are not.
- The tag must not imply that the owner reviewed the generated YAML.

**9. Legacy readers.**
- The App v4 path is isolated or adapted.
- Legacy dependency readers retire once their remaining consumers, including dormant product code, are accounted for.
- The current accepted `_DAG` stays until Phase 5.

**PR 2 is accepted when:**
- the accounting shows no unexplained loss;
- the focused cases pass and the migration is idempotent;
- Agent 1 has checked 3–5 deliverables for meaning;
- every DAG-004 difference is explained;
- App v4 builds and tests are unaffected.

### PR 3: checks and CI (Agent 3 implements; Agent 1 reviews)
1. **A coverage map in the PR description,** at suite or behaviour level, with these columns:
   - the consequential failure the suite detects;
   - what it overlaps with;
   - where and when it runs;
   - its cost;
   - the last consequential failure observed, as evidence where available. A suite that has caught nothing recently is not retired for that reason alone.
2. **Exercise selection before removing the old machinery:**
   - a relevant change selects the check;
   - an irrelevant change doesn't;
   - a selected check that fails makes the result fail.

   Keep the three states "passed", "not selected" and "never ran". Don't assume a documentation change is irrelevant.
3. **A required set per project, chosen by consequence.**
   - Narrow end-to-end connection tests stay where they're warranted.
   - Broad matrices run on a schedule or on demand.
4. **Remove unnecessary selection and evidence machinery while keeping trustworthy selection and result reporting:**
   - the coverage-planning plumbing;
   - the stale-base demand where no relevant input changed;
   - duplicate test lanes on PRs.
5. **Route App v4 code to its own tests,** removing the fallback to the full v3 App and PEC suites.
6. **DEC-025.**
   - It retires once its useful coverage has a hosted home.
   - Piping's `LOOP_INIT` states its assurance rule.
   - `run_evidence_sweep.py` remains only for macOS release candidates.
7. **Branch protection.** The implementer proposes the configuration and the owner applies it. This step is done only when the configuration is applied and shown working on one PR per project.

### Phase 4: Piping (Agent 2 sets the point; Agent 3 executes; Agent 1 reviews)
- **Agent 2** establishes the work actually outstanding on `codex/piping-numerical-integrity-20260926`: its product diff against `main`, its open PRs and its active writes, not its commit count. It proposes the migration point.
- **Agent 3**:
  - moves the remaining product decisions into the files they govern (for example #1168's retirement of the legacy pressure contract);
  - then runs the migration and accounting on Piping's deliverables.

  The fences and DEC-043 moved in PR 1.

### Phase 5: archive (Agent 3 executes; Agent 2 reviews)
- For each batch, tag the commit before removal with a unique tag (`archive/<scope>-2026-10-xx`). There is no history rewrite.
- **No dangling live references.** Before removal, relocate or repoint content still needed, and adapt the tools that read these paths. Historical references resolve through the archive tag.
- **Remove from the working tree:**
  - AgentRuns and `_run_records`;
  - `_Reconciliation` and `_Evaluation`;
  - ScopeChange before-and-after copies;
  - superseded `_DAG` snapshots;
  - closed ledgers;
  - notices, steers and workplans;
  - `plans/evidence`;
  - superseded manual editions;
  - governance-harness proposals, manifests and D-GOV files;
  - records of dormant projects.
- Archiving doesn't retire a dormant project's product source or its current contracts.

### Phase 6: evaluate (Agent 1 measures; then the owner decides)
- **Primary measure:** attributable effort (tokens and active agent time) per completed slice or undertaking.
- **Secondary:**
  - per-PR ratios;
  - record lines per line of code;
  - subagent cache-rebuild cost;
  - escaped defects (fix PRs and reverts);
  - integration latency, optional.
- **Recovery exercise:** a fresh App v4 session with only `AGENTS.md`, `LOOP_INIT` and the CLI picks up the next piece of work.
- One-off measurement scripts stay outside the repository, and raw session logs stay private.
- The owner then decides PEC's future and whether any further consolidation is worth doing.

## 3. Owner acts
1. Send §1.3, and decide on the Piping T3 session.
2. Answer only the substantive dependency differences PR 2 lists.
3. Apply the branch protection proposed in PR 3.
4. Answer the ambiguities flagged by PR 2 and Phase 4.

## 4. Risks and guards
| Risk | Guard |
|---|---|
| Meaning lost in migration | Migration by meaning, full accounting, focused cases, idempotency, DAG-004 comparison, ambiguities sent to the owner |
| A required check stranded | `harness` job kept through PR 1; protection changed only once the replacement is shown working |
| Broken callers | Each caller retired or adapted alongside its module; legacy readers kept until their consumers are accounted for |
| Conflicts with work in flight | The steer, quiet points, Group C pointers updated in PR 2, a chosen migration point for Piping |
| The old burden growing back | Reviewers reject registers, stored status, blanket gates, and records without a consumer |
| Defects missed after cuts | A required set chosen by consequence, selection exercised, first review at three weeks against existing CI history |
