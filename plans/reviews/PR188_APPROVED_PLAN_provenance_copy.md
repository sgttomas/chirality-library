# PROVENANCE COPY — Approved plan: "Multi-Agent Orchestration and Package-Level WORKING_ITEMS"

**Status: NON-GOVERNING historical provenance record.** This is a verbatim
copy of the owner-approved implementation plan behind PR #188 and D-GOV-12,
preserved solely so the PR #188 review record
(`PR188_multi_agent_review_2026-07-11.md`, whose plan-fidelity lens audited
the PR against this text) remains checkable by future agents. Per the
terminal-artifact rule (docs/governance_harness/PLAN_INDEX.md) and K-AUTH-1,
plans bind nothing; the governing traces of this work are the D-GOV-11/12/13
decision records. Do not select work from this document.

**Source:** Codex plan-mode artifact, extracted 2026-07-11 from the Codex
session rollout log
`~/.codex/sessions/2026/07/11/rollout-2026-07-11T16-21-09-019f5345-2ad0-7631-b5be-70b36695a3a7.jsonl`
(the session that produced branch `codex/agent-governance-redesign`). The
owner approved it in-session ("PLEASE IMPLEMENT THIS PLAN"); it was never
committed as a repo plan document — correctly, per the terminal-artifact rule.

---

# Multi-Agent Orchestration and Package-Level WORKING_ITEMS

## Summary

Extend the Agent 0/1/2 hierarchy with an explicit multi-agent orchestration doctrine supporting both:

1. **Terminal fan-out/fan-in** — a parent dispatches independent children, waits for their terminal returns, validates fan-in, and continues.
2. **Supervised many-to-many agency** — active agents exchange coordination information through their parent during execution, allowing dependencies, findings, blockers, and instructions to propagate between sibling workflows.

These are complementary patterns, not competing architectures. A workflow may also use arbitrary mixtures of sequential and concurrent stages without assigning them another named pattern.

```text
Human ↔ HELP_HUMAN Agent 0
              ↕
    many WORKING_ITEMS Agent 1 instances
              ↕
         many Agent 2 instances
```

The human may:

- prescribe a pattern or execution sequence;
- specify only constraints or priorities;
- leave orchestration selection entirely to Agent 0 or a directly invoked Agent 1.

When unspecified, the responsible manager derives and records an appropriate work graph from current state, dependencies, write ownership, risk, and available evidence.

WORKING_ITEMS becomes a package-level Agent 1 manager. TASK remains Agent 2. `SOFTWARE_DEV` remains deferred while WORKING_ITEMS plus software profiles, skills, and tools are exercised.

## Governance and Instruction Changes

1. Record a new D-GOV decision extending, rather than replacing, D-GOV-11:

   - Terminal fan-out/fan-in and supervised many-to-many agency are both canonical.
   - Sequential and concurrent agent actions may be composed in arbitrary dependency-valid sequences.
   - The hierarchy governs delegation and communication authority; it does not prescribe one universal execution pattern.
   - Humans may prescribe the pattern, partially constrain it, or delegate pattern selection.
   - Agent 0 manages cross-package orchestration.
   - Agent 1 manages intra-package orchestration.
   - Agent 1 may report coordination information upward during execution.
   - Agent 0 may selectively relay information, amend instructions, hold dependants, replan, or escalate.
   - Agent 1 siblings do not communicate through undeclared direct messaging.
   - Agent 2 does not delegate.

2. Add a canonical “Multi-Agent Orchestration” section to root governance:

   - Define terminal fan-out/fan-in.
   - Define supervised many-to-many agency.
   - Explain that mixed work graphs may contain any dependency-valid sequence of individual and concurrent actions.
   - Require the selected or derived orchestration posture to be recorded before dispatch.
   - Permit dynamic replanning when live evidence changes the graph.
   - Require versioned plans and brief amendments rather than silent instruction changes.
   - Preserve failure isolation, context hygiene, validated fan-in, and human authority.

3. Define pattern-selection precedence:

   1. Explicit human direction.
   2. Human-approved constraints, priorities, and gates.
   3. Accepted project/decomposition state and dependencies.
   4. Agent 0 cross-package judgment.
   5. Agent 1 intra-package judgment.

   Manager-selected orchestration inside an approved scope does not require a separate human approval for every child. Scope expansion, consequential risk, authority changes, shared-write conflicts, or acceptance changes return to the human.

4. Rewrite HELP_HUMAN:

   - Inspect current accepted state at each turn.
   - Derive or apply the human-prescribed cross-package work graph.
   - Launch multiple instances of the same or different Agent 1 roles.
   - Select terminal, many-to-many, or mixed execution by stage.
   - Maintain inter-package dependencies and shared-surface ownership.
   - Receive and disposition mid-workflow Agent 1 notices.
   - Relay only minimum sufficient context.
   - Validate terminal and staged fan-in.
   - Replan without disturbing independent work.
   - Return consequential decisions to the human.

5. Rewrite WORKING_ITEMS:

   - One instance owns one activated package, optionally narrowed to selected deliverables.
   - Inventory package deliverables and derive or apply an intra-package work graph.
   - Use terminal fan-out/fan-in for independent bounded deliverable work.
   - Use supervised many-to-many coordination when discoveries or dependencies may affect active siblings.
   - Compose sequential and concurrent stages as required by the work graph.
   - Delegate TASK, ephemeral generalist, or approved dedicated Agent 2 work.
   - Validate returns before using or relaying them.
   - Produce package-level closure evidence and return state.
   - Preserve direct human invocation through a human-parented package activation.
   - Preserve legacy one-deliverable sessions through a compatibility activation.

6. Update project instructions and loop protocols:

   - Standing workplans remain statements of intent, constraints, authority, and gates.
   - Agent 0 or direct Agent 1 derives the current execution graph from live state each turn.
   - Record whether the human prescribed the graph or delegated its selection.
   - Persist the graph actually used, not merely the standing plan.
   - Add package launch, notice, relay, acknowledgment, receipt, resume, and closure rules.
   - Update app-dev and piping project indexes to identify WORKING_ITEMS as package manager.
   - Preserve existing owner gates and CHANGE closeout discipline.

## Orchestration and Runtime Interfaces

### Work graph

Represent orchestration as a dependency graph rather than a fixed list of named patterns.

Each plan records:

- orchestration run and plan version;
- selection authority: `HUMAN | AGENT_0 | AGENT_1`;
- descriptive posture: `TERMINAL_FAN_OUT_IN | SUPERVISED_MANY_TO_MANY | MIXED`;
- agent-instance nodes;
- dependency edges;
- concurrency eligibility;
- accepted basis;
- read scopes and write ownership;
- expected returns and fan-in gates;
- human decision points.

The posture label explains the graph but does not constrain it beyond the actual nodes, edges, permissions, and gates.

### Terminal fan-out/fan-in

Use when child scopes are sufficiently independent and their final returns are adequate for coordination.

1. Parent freezes briefs and fans out eligible children.
2. Children execute without sibling coordination.
3. Parent collects terminal returns.
4. Parent validates completeness, schema, evidence, conflicts, and failures.
5. Parent accepts, reruns, holds, or escalates.
6. Downstream work begins only from accepted fan-in state.

A child may still return an execution failure or critical blocker through its normal parent return channel. That does not convert the run into many-to-many coordination.

### Supervised many-to-many agency

Use when active work can generate information relevant to other active or planned work.

```text
Agent 1 source
  → coordination notice
  → Agent 0 disposition
  → selected Agent 1 recipients
  → acknowledgment or conflict
```

The same pattern applies within a package through Agent 1:

```text
Agent 2 source
  → return/update to parent Agent 1
  → Agent 1 disposition
  → selected Agent 2 recipients or revised downstream briefs
```

Agent 0 brokers Agent 1 coordination. Agent 1 brokers Agent 2 coordination. Children do not bypass their parent.

### Managed tools

- `delegate_agent`
  - Agent 0 → named Agent 1.
  - Agent 1 → TASK, named Agent 2, or allowed ephemeral generalist.
  - Loads actual instructions and sealed context.

- `report_coordination_notice`
  - Child → direct parent.
  - Records a typed notice and wakes the parent when appropriate.

- `send_agent_update`
  - Parent → direct child.
  - Relays information or issues a versioned brief amendment.
  - Delivery occurs at a safe message boundary.

- `ack_agent_update`
  - Child returns `INCORPORATED`, `NO_EFFECT`, `BLOCKED`, `CONFLICT`, or `HUMAN_DECISION_REQUIRED`.

Direct sibling messaging, Agent 1→Agent 1 delegation, Agent 0→Agent 2 delegation, and Agent 2 delegation remain denied.

### Durable records

Persist runtime-managed records under:

```text
{EXECUTION_ROOT}/_Coordination/AgentRuns/<RunID>/
  ORCHESTRATION_PLAN.md
  WORK_GRAPH.json
  instances/<InstanceID>/
    LAUNCH_BRIEF.md
    STATUS.json
    RETURN.md
  notices/<NoticeID>.json
  dispositions/<NoticeID>.json
  updates/<UpdateID>.json
  acknowledgments/<UpdateID>.json
  amendments/<InstanceID>/<Version>.md
  HANDOFF_STATE.md
```

The runtime service owns these append-only control-plane writes. They do not become decomposition or deliverable truth.

### Coordination notices

Each notice records:

- run, notice, sender-instance, and scope IDs;
- notice type;
- `PROVISIONAL | VALIDATED | ACCEPTED | DISPUTED` claim status;
- summary and evidence references;
- affected scopes;
- requested action;
- blocking status;
- human-decision requirement;
- accepted basis reference.

Parent dispositions are:

- `RECORD`
- `RELAY`
- `AMEND`
- `HOLD`
- `REPLAN`
- `ESCALATE`
- `ROUTE`

An informational relay preserves claim status and does not alter the recipient’s brief. Changes to objective, basis, write scope, ownership, risk, or acceptance criteria require a versioned amendment. Consequential amendments require a human ruling reference.

### Write and dependency safety

- Every child declares read scope and write targets.
- Shared reads are allowed.
- Concurrent sibling writes must be disjoint.
- Overlap checks include exact paths and ancestor containment.
- Overlapping writes require serialization against an accepted predecessor.
- Parallel fragments targeting a shared surface are integrated by one declared owner.
- Cross-package shared surfaces receive one Agent 0-assigned owner.
- Failed nodes block only their declared dependants.
- Independent work continues.
- Fan-in refuses missing, invalid, contradictory, or unaccepted returns.

## Software Workflow Capability

Do not create `SOFTWARE_DEV` in this tranche.

Use:

```text
WORKING_ITEMS package manager
+ software activation profile
+ software TASK skills
+ deterministic development tools
```

Initial skills:

- repository reconnaissance;
- bounded software implementation;
- defect diagnosis;
- test and verification planning;
- code and diff review.

Tool support:

- repository and test-surface discovery;
- registered build, test, lint, and typecheck execution;
- changed-path and brief-scope validation;
- affected-test selection;
- normalized test evidence;
- generated-file drift;
- API/schema and migration comparison.

Novel stacks begin with ephemeral generalist Agent 2 instances. Repeated methods graduate into skills. HELPS_HUMANS proposes `SOFTWARE_DEV` only if real app-dev and piping trials demonstrate persistent software-manager semantics that package-level WORKING_ITEMS cannot carry safely.

## Dependency Order and Acceptance

1. Publish the new D-GOV multi-agent orchestration decision.
2. Update root doctrine, standards, schemas, DBM, validators, and disposition records.
3. Rewrite HELP_HUMAN and WORKING_ITEMS.
4. Wait for both concordance worktrees to produce accepted handoffs; rebase.
5. Activate the final deliverable-corpus RECONCILIATION contract.
6. Update app-dev and piping project indexes and loop instructions.
7. Add the software profile, skills, and deterministic tools.
8. Implement managed delegation, work graphs, notices, relays, amendments, and persistence.
9. Route the legacy bridge through the managed service.
10. Run root, app-dev, piping, export, and workflow acceptance tests.

Acceptance scenarios include:

- Human prescribes terminal fan-out/fan-in and the agents follow it.
- Human prescribes many-to-many coordination and notices are relayed during execution.
- Human provides no orchestration pattern; Agent 0 derives and records one.
- A directly invoked WORKING_ITEMS instance derives its intra-package pattern.
- A mixed graph executes sequential and concurrent stages correctly.
- Agent 0 launches multiple WORKING_ITEMS instances with unique package scopes.
- WORKING_ITEMS launches multiple Agent 2 instances over deliverables.
- A validated notice is relayed to selected active Agent 1 recipients and acknowledged.
- A provisional notice remains provisional after relay.
- A consequential amendment blocks for human ruling.
- Direct sibling messaging fails closed.
- Concurrent overlapping writes fail closed.
- Serialized overlapping writes proceed only from accepted predecessor state.
- Local failure leaves independent work running and holds only dependants.
- Restart reconstructs plans, graphs, instances, notices, amendments, and acknowledgments.
- Terminal and staged fan-in reject missing or invalid returns.
- Software packages complete through WORKING_ITEMS plus skills/tools without requiring SOFTWARE_DEV.
- Existing direct Agent 1 entry remains functional.
- All existing root, app-dev, piping, instruction-export, and loop tests pass.

Assumptions:

- TASK is Agent 2.
- Terminal fan-out/fan-in remains fully supported.
- Many-to-many agency is parent-mediated live coordination, not unrestricted sibling messaging.
- Unnamed orchestration sequences are represented by the work graph and need not be individually catalogued.
- Runtime-managed persistence preserves HELP_HUMAN’s lack of project-content write authority.
- No active concordance worktree is modified before its accepted handoff is integrated.
