# Task Management Federation Survey — Implementation Plan

Status: `IMPLEMENTED, VALIDATED, PUBLISHED, AND EFFECTIVE — COMPLETE`
Date: 2026-08-02
Owning loop: Root governance loop
Supervising role if authorized: `HELP_HUMAN` (Agent 0)
Implementation owner if authorized: `HELPS_HUMANS` (Agent 1)
Subject: invocation-local, read-only survey of all canonical Task Management registers

## 1. Objective and aligned intent

Implement the following behavior:

> Whenever `TASK_MANAGEMENT` is invoked for a registered loop, that instance
> first performs a read-only federation survey of every canonical Task
> Management register. No development loop is required to invoke
> `TASK_MANAGEMENT`.

This is an invocation-local preflight, not a loop-entry binding, scheduled
sweep, workflow gate, daemon, or foreign-write permission. It supplies the
missing receive-side discovery mechanism for cross-loop coordination while
preserving K-TM-1..6.

The planning distinction confirmed by the owner in conversation is:

> Require the survey whenever TASK_MANAGEMENT is already invoked; do not
> require loops to invoke TASK_MANAGEMENT.

This plan originally recorded that design intent for review. The owner's
subsequent explicit direction to implement this plan satisfied H0 for the
bounded candidate tranche. That act did not itself authorize H1 expansion,
publication, or merge; H2 was later supplied and exercised as recorded in
section 17.

## 2. Governing basis

- `docs/governance_harness/_DECISIONS/D-GOV-32_task_management_prd_adoption.md`
- `plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md`, especially
  sections 6.1, 6.2, 8.3, 8.4, 9, 13, and 14
- `docs/CONTRACT.md` K-TM-1..6
- `agents/AGENT_TASK_MANAGEMENT.md`
- `agents/AGENT_HELP_HUMAN.md`
- `agents/AGENT_HELPS_HUMANS.md`
- `agents/AGENT_TASK.md`
- `agents/AGENT_CHANGE.md`
- `AGENTS.md` runtime hierarchy, delegation rules, governance integration
  rules, and agent-index change-notice rule
- `docs/SPEC.md` sections 0.2.1 through 0.2.4
- current Root idle posture at
  `execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md`

The accepted Task Management PRD bytes remain historical adopted product
content and are not edited. A new Root decision/amendment record must carry
the behavioral ruling if execution is authorized.

## 3. Required outcome

At the beginning of every `TASK_MANAGEMENT` invocation:

1. Resolve the invoking loop and its canonical local register.
2. Discover every canonical, tracked Task Management register.
3. Validate every discovered register before relying on its rows.
4. Build a read-only cross-register relationship graph.
5. Surface coordination relevant to the invoking loop and any program-level
   defects visible from the survey.
6. For a Root invocation, surface the complete program-wide view.
7. Continue into the requested Task Management mode only after reporting the
   survey result and its coverage.

The survey may produce observations and proposals. It must never:

- write a foreign register;
- create a receiving row automatically;
- promote, prioritize, elevate, close, or disposition a row;
- treat a notice as a directive;
- create authority, scope, lifecycle, schedule, or approval effects; or
- make any development-loop act depend on invoking `TASK_MANAGEMENT`.

## 4. Scope

### 4.1 In scope

- Invocation semantics in `agents/AGENT_TASK_MANAGEMENT.md`.
- A deterministic federation command in `tools/taskmgmt/taskmgmt.py`.
- Focused unit and live-fixture tests in
  `tools/taskmgmt/test_taskmgmt.py`.
- A Root decision/amendment record for the invocation-local interpretation.
- An instruction-tranche manifest.
- Same-tranche routed notices to the registered App, Piping, and PEC loops.
- Root loop receipt and handoff updates after a lawful, validated tranche.

### 4.2 Out of scope

- Any `LOOP_INIT.md` or standing-workplan reader binding.
- Automatic or scheduled invocation.
- CI wiring.
- A daemon, event bus, message broker, or App runtime route.
- Register-row migration or bulk disposition.
- Foreign-register writes.
- A new register schema or new columns.
- Editing the adopted Task Management PRD bytes.
- General source/evidence staleness implementation beyond cross-register link
  and notice integrity required by this survey.
- Product, decomposition, package, deliverable, dependency, lifecycle,
  release, or professional-reliance changes.

Any finding that the existing schema cannot support deterministic federation
must return as a human decision request. It must not silently expand this
plan into a schema migration.

## 5. Federation contract

### 5.1 Canonical register discovery

The deterministic tool must enumerate tracked files only and accept register
paths only in sanctioned coordination shapes, including:

```text
execution/_Coordination/_TaskManagement/REGISTER.csv
projects/*/execution/_Coordination/_TaskManagement/REGISTER.csv
domains/*/execution/_Coordination/_TaskManagement/REGISTER.csv
_DomainEngines/*/_TaskManagement/REGISTER.csv
```

Archives, exports, fixtures, evaluation copies, generated projections, and
untracked lookalikes are excluded and named in the report. File existence is
not enough: each discovered file must pass the canonical register validator.

### 5.2 Relationship construction

Build a global unique index keyed by `ActionItemID`. Extract cross-register
relationships only from typed or schema-governed fields:

- `ElevatedTo`;
- exact `TM-<LOOP>-<seq>` identifiers in `SourceRef`;
- `NoticeRef` when not `NONE`;
- `Status` and `Disposition` for closure-echo comparison.

Do not infer relationships from `Notes` prose. Use the action-item identifier
as the primary cross-register join key; paths remain evidence references.

Path references are resolved against the owning register's working-root
anchor. If a reference can resolve to more than one plausible surface, report
`AMBIGUOUS_REFERENCE`; do not choose silently.

### 5.3 Finding classes

The derived report must support at least:

| Class | Meaning |
|---|---|
| `INBOUND_ELEVATION` | A foreign row targets the invoking loop or one of its rows |
| `FOREIGN_LINK_TO_LOCAL` | A foreign row cites a local `ActionItemID` |
| `LOCAL_LINK_TO_FOREIGN` | A local row cites a foreign `ActionItemID` |
| `OUTBOUND_AWAITING_ACK` | A local elevated/linked item has no receiving counterpart |
| `REMOTE_CLOSED_LOCAL_OPEN` | A linked remote row is closed while the local row remains non-closed |
| `LOCAL_CLOSED_REMOTE_OPEN` | The local row is closed while the linked remote row remains non-closed |
| `ORPHANED_LINK` | A cited `ActionItemID` does not exist in the surveyed set |
| `DUPLICATE_GLOBAL_ID` | One `ActionItemID` occurs in more than one canonical register |
| `MISSING_NOTICE` | A non-`NONE` `NoticeRef` does not resolve |
| `AMBIGUOUS_REFERENCE` | A path or target has multiple plausible resolutions |
| `INVALID_REGISTER` | A discovered canonical register fails form validation |
| `UNREADABLE_REGISTER` | A canonical register cannot be read |

Findings are observations, not verdicts or directives.

### 5.4 Coverage and failure semantics

- `COMPLETE`: every canonical register was discovered, read, and validated.
- `PARTIAL`: one or more canonical registers were invalid, unreadable, or
  ambiguously identified.

`PARTIAL` must never be summarized as “no cross-loop coordination found.” The
invoked manager may continue local non-dependent work, but it must not rely on
the survey to assert global absence or closure.

An invalid relationship or missing notice is report data, not a tool failure.
Failure to enumerate or read the register set is an operational failure under
D-GOV-02 exit semantics.

### 5.5 Output

The tool writes only a rebuildable, gitignored projection beside the invoking
register, for example:

```text
_TaskManagement/.candidates/federation.json
```

The JSON must include:

- invoking loop and register;
- generation command and version;
- authority label (`derived`, `rebuildable`, `never authority`);
- coverage verdict;
- every register path, inferred loop namespace, schema version, row count,
  and validation result;
- deterministic finding records with local/remote IDs and evidence paths;
- declared exclusions;
- unresolved ambiguities and operational errors; and
- an explicit statement that zero register writes occurred.

Console output is a compact summary of the same result.

## 6. Work graph

Execution is serial at instruction/tool integration boundaries and may use
parallel read-only Agent 2 work only where the runtime can preserve sealed
briefs, parentage, scopes, returns, and durable evidence.

| Node | Role | Depends on | Write scope | Required return |
|---|---|---|---|---|
| `A0-ALIGN` | HELP_HUMAN (Agent 0) | owner authorization | runtime control records only | accepted basis, graph v1, gates, sealed Agent 1 briefs |
| `A1-DESIGN` | HELPS_HUMANS (Agent 1) | A0-ALIGN | proposed decision/design records only | frozen component design and exact implementation contract |
| `A2-INVENTORY` | TASK or ephemeral generalist (Agent 2) | A1-DESIGN | read-only managed return | canonical-register and live-link inventory |
| `A2-IMPLEMENT` | TASK generic shell (Agent 2) | A1-DESIGN + A2-INVENTORY | `tools/taskmgmt/taskmgmt.py`, `tools/taskmgmt/test_taskmgmt.py`, run record | tool/test patch and focused test results |
| `A1-INTEGRATE` | HELPS_HUMANS (Agent 1) | A2-IMPLEMENT | agent instruction, decision record, manifest, notices, tool/test integration | coherent candidate tranche and validation manifest |
| `A2-VERIFY` | fresh TASK or ephemeral generalist (Agent 2) | A1-INTEGRATE | read-only managed return | adversarial verification report |
| `A1-VALIDATE` | HELPS_HUMANS (Agent 1) | A2-VERIFY | correction scope limited to candidate tranche | validated manager return and handoff |
| `A1-TM-ACCEPT` | TASK_MANAGEMENT (Agent 1) | A1-VALIDATE | read-only; no register changes | Root and non-Root invocation proof |
| `A0-FANIN` | HELP_HUMAN (Agent 0) | A1-VALIDATE + A1-TM-ACCEPT | runtime control records only | validated cross-manager result and owner decision slate |
| `A1-CHANGE` | CHANGE (Agent 1) | owner publication direction after A0-FANIN | Git/file state only | scoped commit/push/PR readiness; merge only on exact owner direction |

No Agent 2 delegates. Agent 1 managers do not command sibling Agent 1
managers; HELP_HUMAN performs the routing between HELPS_HUMANS,
TASK_MANAGEMENT, and CHANGE.

## 7. Human gates

### Gate H0 — authorize implementation

Before any instruction-surface edit, the owner must approve the exact bounded
tranche or amend this plan. The authorization must confirm:

- invocation-local federation survey is required whenever
  `TASK_MANAGEMENT` runs;
- no loop is required to invoke `TASK_MANAGEMENT`;
- no schema migration or `LOOP_INIT.md` amendment is authorized;
- the in-scope instruction/tool/test/manifest/notice paths may be edited; and
- publication remains a later human-gated act.

### Gate H1 — design expansion

Return to the owner if deterministic implementation would require:

- new register columns;
- a central authoritative register catalog;
- edits to K-TM-1..6;
- edits to the adopted PRD bytes;
- automatic scheduling, CI, daemon, or runtime integration; or
- any foreign write or auto-promotion behavior.

### Gate H2 — publication

After validation, HELP_HUMAN presents the exact candidate HEAD, changed paths,
checks, findings, derivative status, and remaining risks. CHANGE may perform
routine scoped commit/push under its contract. PR merge requires the owner's
exact merge direction and must be recorded in Root closeout evidence.

## 8. Agent 0 execution instructions — HELP_HUMAN

When H0 is satisfied:

1. Enter through `execution/_Coordination/LOOP_INIT.md` and run the idle
   workplan's live-state checks. Treat this as a separately authorized bounded
   lane, not a successor Root production phase unless the owner rules
   otherwise.
2. Resolve current branch/worktree/HEAD, upstream divergence, dirty state,
   current Root receipt, and applicable App/Piping/PEC receipts.
3. Create a real managed run under
   `execution/_Coordination/AgentRuns/<RunID>/`; do not create placeholder
   children.
4. Freeze `ORCHESTRATION_PLAN.md` and `WORK_GRAPH.json` before dispatch.
5. Dispatch `HELPS_HUMANS` with ownership of component design, implementation
   fan-out, instruction/tool integration, validation, manifest, and notices.
6. Require HELPS_HUMANS to freeze the component design before any Agent 2
   write-capable dispatch.
7. Relay only typed, evidence-bound notices. Any scope or schema expansion
   returns to H1.
8. After HELPS_HUMANS returns, invoke `TASK_MANAGEMENT` read-only for
   acceptance proof from Root and at least one non-Root loop context.
9. Validate both Agent 1 returns. Refuse fan-in if any expected artifact,
   coverage result, write-containment proof, or check result is missing.
10. Present the exact publication decision to the owner. Route to CHANGE only
    after candidate readiness is established.
11. Close with accepted upstream basis, derivative status, closure verdict,
    rerun requirements, remaining blockers, and next owner.

## 9. Agent 1 execution instructions — HELPS_HUMANS

### 9.1 Design phase

1. Re-read the governing basis and all live Task Management callers,
   validators, register instances, and adoption decisions.
2. Produce a component design record using the required HELPS_HUMANS
   structure.
3. Confirm classification:
   - persistent invocation semantics belong in `AGENT_TASK_MANAGEMENT.md`;
   - deterministic federation belongs in `tools/taskmgmt/taskmgmt.py`;
   - run-specific inventory and verification belong in sealed Agent 2 briefs;
   - no new skill or dedicated Agent 2 package is justified.
4. Freeze discovery patterns, join grammar, finding classes, coverage
   semantics, output contract, and compatibility requirements.
5. Dispatch `A2-INVENTORY`. Validate its return before authorizing tool edits.

### 9.2 Implementation phase

1. Dispatch `A2-IMPLEMENT` with exact write targets limited to the two
   Task Management tool/test files and its run record.
2. Independently amend `agents/AGENT_TASK_MANAGEMENT.md` to:
   - add federation preflight before all modes;
   - state Root versus non-Root presentation behavior;
   - preserve local-only register writes and human dispositions;
   - distinguish invocation-local survey from a standing sweep obligation;
   - define `PARTIAL` behavior and prohibit false absence claims; and
   - require a manual read-only equivalent if the deterministic helper is
     unavailable.
3. Draft the Root decision/amendment record without rewriting D-GOV-32 or the
   adopted PRD bytes.
4. Draft the G4 instruction-tranche manifest.
5. Draft same-tranche notices for App, Piping, and PEC. Notices state the
   changed shared instruction/tool behavior and require no project-local
   adoption, register edit, or loop-entry change unless an owning loop later
   rules otherwise.
6. Fan in A2-IMPLEMENT, inspect its diff and tests, and integrate only after
   confirming write containment.

### 9.3 Verification and handoff

1. Dispatch a fresh `A2-VERIFY` against the complete candidate diff.
2. Reproduce all required checks independently; correct only candidate-scope
   defects.
3. Record live-survey observations separately from implementation acceptance.
   Do not auto-repair any register or notice finding discovered by the new
   survey.
4. Return to HELP_HUMAN with:
   - component design;
   - exact changed paths;
   - Agent 2 returns and fan-in disposition;
   - tool output and coverage for all live registers;
   - validation results;
   - compatibility and derivative status;
   - unresolved findings and H1 decisions, if any; and
   - a closure verdict of `READY`, `CONDITIONAL`, or `BLOCKED`.

## 10. Agent 2 sealed execution instructions

### 10.1 A2-INVENTORY — read-only current-state audit

Construction form: sealed ephemeral generalist or generic `TASK`; no skill.

```text
PURPOSE: Inventory the live canonical Task Management federation before implementation.
RequestedBy: HELPS_HUMANS
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/<RunID>/instances/A2-INVENTORY
ApplyEdits: false
Tasks:
  - Identify every canonical live Task Management register and its loop namespace.
  - Validate all registers with the existing validator.
  - Inventory exact current uses of ActionItemID, SourceRef, NoticeRef, ElevatedTo, Status, and Disposition.
  - Identify cross-register links, missing notices, ambiguous references, duplicate IDs, and unsupported shapes.
  - Propose deterministic fixtures and expected classifications without changing files.
ExpectedOutputs:
  - Structured inventory with authoritative/candidate claim labels.
  - Compatibility risks and any H1 decision request.
  - Exact fixture matrix for A2-IMPLEMENT.
EXCLUSIONS:
  - No file writes beyond runtime-managed return records.
  - No register mutation or semantic disposition.
CustomInstructions:
  - Use read-only filesystem, Git-inspection, and validation operations only.
```

Acceptance: 100% of discovered canonical registers accounted for; every
assertion cites a path/row; no unsupported form silently omitted.

### 10.2 A2-IMPLEMENT — deterministic tool and tests

Construction form: generic `TASK`; no skill.

```text
PURPOSE: Implement the frozen Task Management federation-survey tool contract and focused tests.
RequestedBy: HELPS_HUMANS
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/<RunID>/instances/A2-IMPLEMENT
ApplyEdits: true
AllowedWriteTargets:
  - {REPO_ROOT}/tools/taskmgmt/taskmgmt.py
  - {REPO_ROOT}/tools/taskmgmt/test_taskmgmt.py
  - {REPO_ROOT}/execution/_Coordination/AgentRuns/<RunID>/instances/A2-IMPLEMENT/_run_records/
Tasks:
  - Add the federation command and deterministic output contract exactly as frozen.
  - Preserve existing validate and candidate-scan behavior and CLI compatibility.
  - Add focused unit tests for discovery, linking, coverage, failure semantics, determinism, and zero register writes.
  - Run focused tests and report exact results.
ExpectedOutputs:
  - Bounded patch to the two authorized files.
  - Passing focused tests or a precise FAILED return.
  - Applied-change list and write-containment proof.
EXCLUSIONS:
  - No agent, governance, manifest, notice, register, loop, CI, or schema edits.
CustomInstructions:
  - Use only tools needed to edit the two authorized implementation files and run their focused tests.
```

Acceptance: existing tests remain green; new tests cover every required
finding class and coverage state; before/after hashes prove registers were not
modified.

### 10.3 A2-VERIFY — fresh adversarial verification

Construction form: fresh sealed ephemeral generalist or generic `TASK`; no
skill; read-only.

```text
PURPOSE: Adversarially verify the complete federation-survey candidate tranche.
RequestedBy: HELPS_HUMANS
WorkingRoot: {REPO_ROOT}
ScopePath: {REPO_ROOT}/execution/_Coordination/AgentRuns/<RunID>/instances/A2-VERIFY
ApplyEdits: false
Tasks:
  - Verify the implementation against this plan, the frozen component design, K-TM-1..6, and AGENT_TASK_MANAGEMENT.
  - Reproduce focused tests and run the command against all live registers.
  - Verify Root global presentation and non-Root relevance filtering.
  - Hash every register before and after execution and prove zero modification.
  - Test malformed, missing, ambiguous, duplicate, orphaned, and partial-coverage fixtures.
  - Inspect for hidden loop-entry, CI, scheduling, schema, authority, or foreign-write effects.
ExpectedOutputs:
  - PASS/FAIL matrix for every acceptance criterion.
  - Findings with severity, evidence, and bounded remediation recommendation.
  - Final verdict READY, CONDITIONAL, or BLOCKED.
EXCLUSIONS:
  - No edits or register dispositions.
CustomInstructions:
  - Use read-only filesystem/Git inspection and non-mutating test execution only.
```

Acceptance: independent reproduction, exact evidence, zero open critical/high
findings, and no reliance on the implementing child's assertions alone.

## 11. Agent 1 acceptance instructions — TASK_MANAGEMENT

After HELPS_HUMANS declares the candidate validated, HELP_HUMAN invokes
TASK_MANAGEMENT read-only in at least two contexts:

1. Root register context: federation preflight must report all registers and
   the complete program view.
2. One non-Root context: federation preflight must read the same canonical set
   while emphasizing relationships involving the invoking loop.

TASK_MANAGEMENT must:

- report survey coverage before its normal mode output;
- cite foreign rows without writing them;
- refuse to infer human dispositions;
- report any live missing notice or closure echo as an observation;
- perform no register write during acceptance; and
- return whether the invocation semantics are usable and faithful to the
  aligned intent.

This acceptance run is behavioral evidence, not semantic approval.

## 12. Agent 1 closeout instructions — CHANGE

CHANGE enters only after HELP_HUMAN validates fan-in and the owner reaches the
publication gate.

1. Inspect branch/worktree/HEAD/upstream and unrelated dirty state.
2. Confirm the changed-path inventory matches the authorized tranche.
3. Confirm the instruction-tranche manifest names every instruction-surface
   path and the three routed notices.
4. Confirm HELPS_HUMANS and TASK_MANAGEMENT returns, A2 verification, check
   results, handoff state, derivative status, and blockers are present.
5. Stage only tranche paths; commit and push under routine closeout rules when
   their conditions hold.
6. Produce an Integration Readiness Report for the exact candidate HEAD.
7. Open/present the human-gated PR if authorized by the owning workflow.
8. Do not merge without the owner's exact merge direction. Before merge,
   verify the source HEAD and completed check verdicts; stop on drift or
   conflict.
9. Record approved source HEAD, owner direction, effective merge SHA, and
   resulting branch state in ordinary Root closeout evidence.

## 13. Expected changed paths

Required candidate paths:

```text
agents/AGENT_TASK_MANAGEMENT.md
.gitignore
tools/taskmgmt/taskmgmt.py
tools/taskmgmt/test_taskmgmt.py
docs/governance_harness/_DECISIONS/<new federation-survey decision record>.md
docs/governance_harness/_DECISIONS/_REGISTER.md
docs/governance_harness/tranche_manifests/<new federation-survey manifest>.yaml
projects/chirality-app-dev/execution/_Coordination/<routed notice>.md
projects/chirality-piping/execution/_Coordination/<routed notice>.md
projects/pec/execution/_Coordination/<routed notice>.md
execution/_Coordination/LOOP_RECEIPTS.md
execution/_Coordination/HANDOFF_STATE.md
```

Managed runtime records under
`execution/_Coordination/AgentRuns/<RunID>/` are additional execution evidence.
The `.gitignore` change is limited to the canonical derived projection beneath
any registered `_TaskManagement/.candidates/` directory; it grants no new
runtime authority or register scope.
Do not add `AGENTS.md`, `LOOP_INIT.md`, register CSVs, the adopted PRD, or
`docs/CONTRACT.md` to the tranche without an H1 ruling.

## 14. Validation matrix

At minimum:

```text
python3 -m pytest tools/taskmgmt/test_taskmgmt.py
python3 tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv
python3 tools/taskmgmt/taskmgmt.py validate --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv
python3 tools/taskmgmt/taskmgmt.py validate --register projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv
python3 tools/taskmgmt/taskmgmt.py validate --register _DomainEngines/pec/_TaskManagement/REGISTER.csv
python3 tools/validation/validate_agent_instructions.py
python3 tools/validation/validate_instruction_tranche_manifest.py
python3 tools/validation/validate_path_anchors.py
git diff --check
```

Also run:

- the new federation command once for each live register;
- before/after content hashes of all registers;
- the full practitioner-harness test suite;
- instruction-entrypoint and claims-language validation used by the current
  governance-harness tranche baseline; and
- any additional checks named by the live Root workplan or manifest validator.

Check output must distinguish structural PASS from semantic acceptance.

## 15. Acceptance criteria

The tranche is `READY` only when:

1. Every `TASK_MANAGEMENT` invocation is contractually required to perform the
   federation preflight.
2. No loop is required to invoke `TASK_MANAGEMENT`.
3. All canonical live registers are discovered and reported.
4. Root receives a global view; non-Root invocation receives relevant
   cross-loop findings without losing coverage disclosure.
5. Existing linked rows are classified without schema migration.
6. Missing/invalid/unreadable inputs produce explicit `PARTIAL` or operational
   results, never false absence.
7. Tool output is deterministic, derived, rebuildable, and gitignored.
8. All register hashes are unchanged after every survey and acceptance run.
9. No human disposition, authority effect, foreign write, loop binding,
   schedule, CI, daemon, or runtime integration is introduced.
10. Focused, full, manifest, agent, path, and whitespace checks pass.
11. App, Piping, and PEC notices are routed in the same tranche.
12. HELP_HUMAN validates all manager returns and presents the exact candidate
    to the owner before publication.

## 16. Stop, recovery, and handoff

Stop and return to the owner when:

- the live basis contradicts this plan;
- the current checkout contains overlapping unrelated edits on candidate
  paths;
- schema change or central authoritative registry becomes necessary;
- a foreign write appears necessary;
- an Agent 2 exceeds its brief or write target;
- any critical/high verification finding remains open;
- validation cannot be reproduced; or
- the candidate HEAD changes after publication approval.

On failure, preserve completed returns, mark dependants held, and keep
independent read-only evidence valid. Do not partially publish an agent change
without its tool/tests/manifest/notices, and do not silently downgrade survey
coverage.

Final handoff must state:

- accepted upstream basis;
- candidate commit/HEAD and changed paths;
- derivative-package currency;
- Agent 2 and Agent 1 validation status;
- federation coverage and live findings;
- closure verdict;
- exact rerun requirements;
- remaining blockers; and
- next owner/gate.

## 17. Authorization boundary

The owner subsequently directed implementation of this plan. H0 is therefore
satisfied for the bounded candidate tranche, and HELP_HUMAN instantiated and
closed the work graph. H1 was not required. On 2026-08-02 the owner directed,
verbatim, "Merge via PR." H2 is therefore satisfied for the exact checked PR
publication and merge of this bounded tranche; direct-main push and check
bypass remain unauthorized.

CHANGE completed H2 through
[PR #478](https://github.com/sgttomas/chirality/pull/478). The validated
implementation commit was `bb44d71c93cc5431d5fc8a902e716cc88966ea9f`;
the exact approved source HEAD was
`08ed85ae1a1ae2be9eba971e6567fad2bb202b56` against final base
`4d55dea0f375034b66949723a7b849a2c962d8a3`. `Harness pre-merge`,
`harness`, and `pec` all returned `SUCCESS`. GitHub merged the PR as
`2c25bd2c47c4b2f4190275ad39579a983f8786aa`, by `sgttomas`, at
`2026-08-02T22:13:19Z`; the closeout comment is
[here](https://github.com/sgttomas/chirality/pull/478#issuecomment-5160591595).
The plan graph is closed with no remaining H2 action for PR #478.
