# Chirality Task Management — PRD Authoring Basis

| Field | Value |
|---|---|
| Date | 2026-07-28 |
| Status | `NON_AUTHORITATIVE_AUTHORING_INPUT` |
| Candidate project name | Chirality Task Management |
| Candidate project slug | `projects/chirality-task-management/` |
| Intended next use | Fresh Agent 0 inquiry and PRD candidate authoring |
| Source manifest | `plans/chirality-task-management/SOURCE_MANIFEST.md` |

## 1. Purpose and fence

This record preserves the current product understanding reached between the
owner and Agent 0 so that a later session can author a PRD without reconstructing
the originating conversation.

It is an authoring basis, not a PRD, decomposition, decision, project scaffold,
scope grant, implementation authorization, or acceptance act. Statements below
are labeled to distinguish owner direction from explanatory synthesis and open
questions. A later PRD remains a candidate until separately reviewed and
accepted by the owner.

The three owner-provided Word documents listed in the source manifest are the
professional-framework source corpus for this inquiry. Their original bytes are
retained under `sources/`.

## 2. Owner direction of record for authoring

The following directions were stated by the owner in the 2026-07-28 working
session and govern the next inquiry:

> "I build around the task. Let's explore how to adapt these ideas to
> Chirality."

> "Another perspective to add here is that only certain types of work warrant
> a WORKING_ITEMS manager of TASK agents but among those appropriate
> assignments for TASK agents is completing tasks to resolve action items."

> "And absolutely the nine domains are scanning lenses for agents to
> coordinate their work on, not any kind of sequence or specific workflow."

> "Agent 0 alone or in consultation with the human can make these decisions
> that aren't made at the manager level."

> "And the Task Management service is just code, right? As in no agents. Just
> agents querying it."

> "Task management is all about the nine domains and how those integrate with
> the other systems and governance it's situated in."

> "No the Action Items are not part of the deliverables. They exist outside of
> that, and once they are resolved the results may have updated the
> deliverables documentation, or perhaps it's Root governance, or an App
> improvement, or what have you."

> "Without this, I can't expect that issues that arise during development will
> be dealt with."

These quotations preserve direction. They do not by themselves settle the
open product-design questions in section 10.

## 3. Product thesis

**OWNER-ALIGNED SYNTHESIS**

Chirality Task Management is a non-agentic software service that implements
the Nine Domains of Task Management as a simultaneous scanning framework. It
integrates task-relevant information from the project-management,
project-controls, deliverable-work, planning, approval, checking, decision,
and governance systems in which it is situated.

Its purpose is to ensure that task-relevant issues arising around project work
remain visible across sessions and receive explicit disposition rather than
depending on human memory or accidental rediscovery.

The service does not prescribe a universal task workflow. Tools serve the
professional framework; they do not redefine it.

## 4. The Nine Domains

The nine domains are:

| Domain | Inquiry meaning |
|---|---|
| Action Item | A durable task-management concern requiring attention beyond ordinary unlogged work |
| Assignment | The responsible party, role, or team and the applicable accountability relationship |
| Prioritization | The warranted order or urgency of attention in the situated project |
| Deliverables | The governed outputs or results to which tasks may contribute or relate |
| Work | Actual execution by humans, agents, or deterministic tools |
| Planning | The sequencing, timing, dependencies, and preparation needed for work |
| Approval | Required sign-off, authentication, acceptance, or consensus under the applicable authority |
| Checking | Verification of quality, accuracy, completeness, or conformance |
| Decisions | Recorded choices that materially affect scope, approach, acceptance, schedule, budget, or other work |

The matrix is a mnemonic and diagnostic lens. It is not:

- a nine-step sequence;
- a lifecycle;
- a state machine;
- nine required agents;
- nine queues;
- a replacement for the development loop;
- a source of authority.

Agents and humans use the lenses concurrently to ask what is missing,
unresolved, misaligned, or approaching a HOLD.

## 5. Core ontology

### 5.1 Project, package, deliverable, task, and work

- A project is structured through packages and deliverables.
- A deliverable is a governed result or work product.
- A task is a bounded action undertaken toward a result.
- Work is the actual execution of tasks.
- Not every task warrants durable project-level tracking.
- Ordinary work may remain within a human workflow, an accepted manager
  activation, a work graph, or a bounded TASK-agent brief.

Chirality is therefore **deliverable-structured and task-operated**. Project
truth is organized through governed deliverables; tasks bring the necessary
action, information, judgment, and coordination to those deliverables at the
right time.

### 5.2 Action Items

An Action Item is a native Task Management object. It exists outside the
deliverable folder structure.

An Action Item may reference:

- one or more deliverables;
- a package;
- a project or project loop;
- Root governance;
- Chirality App;
- PEC;
- Piping or another domain application;
- another program service;
- an external party;
- a concern whose final owning surface is not yet known.

Association with a deliverable does not place the Action Item inside the
deliverable or make it deliverable scope.

Resolving an Action Item may result in:

- changed deliverable documentation or implementation;
- a Root governance act;
- an App, PEC, Piping, or other product improvement;
- a decision or approval;
- a scope-change request;
- new checking or evidence;
- receipt of missing information;
- no artifact change, where the resolution is informational or no action is
  warranted.

The Action Item closes by citing the resulting evidence or explicit
disposition. It never grants scope, authority, approval, or lifecycle effect
merely by existing.

### 5.3 Observations and promotion

A development agent may observe a potentially meritorious concern outside its
current brief. The agent acts only inside its brief and returns the observation
to its parent manager with evidence and the reason it is outside the current
assignment.

The observation is not automatically an Action Item. A later nine-domain scan
and the applicable Agent 1, Agent 0, or human judgment determine whether it is:

- ordinary work inside accepted scope;
- a durable Action Item;
- a decision or approval need;
- a scope-change candidate;
- a planning or checking matter;
- a valid deferral with a trigger;
- evidence only;
- a duplicate;
- rejected or already resolved.

The PRD must define the minimum useful capture and promotion contract without
turning every agent observation into backlog.

## 6. Agent and service boundary

### 6.1 The service is code

Task Management is software. It contains no embedded Agent 0, Agent 1, Agent 2,
LLM, autonomous judgment, or second execution loop.

It may provide:

- parsers and integrations;
- a task-management information model;
- Action Item records and views;
- deterministic query operations;
- an App-facing module or sidecar interface;
- cited joins across the nine domains;
- deterministic validations and completeness checks;
- explicitly authorized mutation operations, if the PRD later includes them.

The exact persistence and mutation design is an open PRD question.

### 6.2 Existing agents retain their roles

- Development agents look primarily to the applicable development-loop
  instructions.
- Where the work warrants managed package production, `WORKING_ITEMS` manages
  bounded TASK agents working in accepted deliverables.
- Not every task or Action Item warrants a `WORKING_ITEMS` activation.
- TASK agents perform only their bounded assignments and return out-of-brief
  observations upward.
- Agent 1 makes judgments inside its accepted manager scope and latitude.
- Agent 0 makes cross-manager and cross-package judgments within its accepted
  latitude, alone or in consultation with the human.
- The human performs reserved authority and judgment acts where the applicable
  latitude ends.

Task Management informs these actors. It does not dispatch them or replace
their instruction packages.

### 6.3 Decision distinction

The PRD must preserve the distinction between:

- ordinary execution judgment;
- Agent 1 operational or package judgment;
- Agent 0 cross-manager or program judgment;
- owner ruling, adoption, acceptance, or other reserved human act.

A Task Management view must not mislabel every unresolved matter as waiting on
the owner.

## 7. Integration without subsumption

Task Management integrates the nine domains with the systems that already own
their authoritative state:

| Domain | Principal integration source or owner |
|---|---|
| Action Item | Task Management |
| Assignment | Task Management plus applicable responsibility structures, activations, and briefs |
| Prioritization | Project-management judgment, owner direction, dependencies, and project controls |
| Deliverables | Accepted decomposition and deliverable state |
| Work | Human work and governed agent workflows |
| Planning | Workplans, dependencies, schedules, and project controls |
| Approval | Applicable human and professional approval instruments |
| Checking | Validators, reviewers, and assurance processes |
| Decisions | Governed decision records and registers |

Task Management must not silently become:

- the general coordination plane;
- an agent-orchestration service;
- a runtime or session-presence service;
- a lock manager;
- the authoritative dependency graph;
- the deliverable lifecycle authority;
- the project-controls or resource-governance service;
- a substitute for project governance;
- a universal issue dump;
- a mandatory workflow imposed on every act of work.

Externally owned facts may be displayed when they are relevant to a
nine-domain scan, but their authority remains with their owning systems.

## 8. Four-way concordance

The PRD should test every proposed capability against four questions:

1. **Ontology — what kind of thing is it?**
2. **Epistemology — what may be known, and from what evidence?**
3. **Praxeology — who may act, through which workflow and authority?**
4. **Axiology — what values govern judgment where facts do not determine one
   answer?**

Current owner-aligned posture:

| Dimension | Task Management posture |
|---|---|
| Ontology | Tasks are bounded actions; Action Items are external task-management objects; deliverables remain governed work products; the service is code; agents are distinct actors |
| Epistemology | The service integrates cited state from owning systems and must distinguish authoritative, observed, derived, proposed, unknown, and stale information |
| Praxeology | Agents and humans apply the nine-domain lenses; existing managers and workflows execute and govern work; the service does not manufacture authority |
| Axiology | Preserve professional accountability, keep workers focused, prevent avoidable HOLDs, reduce human memory burden, avoid bureaucracy, prefer simple open tools, and keep the framework prior to its implementation |

## 9. Desired product outcomes

The PRD should refine and test at least these candidate outcomes:

1. A task-relevant issue observed during project work can survive the session
   that observed it without becoming unauthorized scope.
2. A nine-domain scan can determine what information or judgment is missing
   before a warranted Action Item is actionable.
3. Every Action Item has an explicit disposition path and cannot disappear
   silently between sessions.
4. Action Items remain distinct from deliverable scope while retaining
   traceability to any affected deliverables and resulting changes.
5. Agents can query task-management state without Task Management becoming an
   agent or orchestrator.
6. Agent 1, Agent 0, and human decision latitude remain visible and are not
   collapsed into one approval queue.
7. Task Management integrates with surrounding project systems without
   duplicating or superseding their authority.
8. The nine-domain framework reduces coordination failure and cognitive load
   without requiring every task to be logged.
9. The implementation remains subordinate to the professional framework and
   does not impose an incompatible workflow.

## 10. Open PRD questions

The PRD inquiry must investigate, decide, or explicitly defer:

1. Who are the initial users: the owner, Agent 0, Agent 1 managers, other
   agents, human project participants, or some staged subset?
2. What is the authoritative persistence form for Action Items?
3. Does the service own file-native Action Item records, a service-managed
   store, or a combination with explicit authority and recovery semantics?
4. What is the exact distinction among task, Action Item, observation, issue,
   risk, HOLD, dependency, and Remaining work?
5. What warrants promotion of an observation or task into an Action Item?
6. What is the minimum Action Item lifecycle and schema?
7. At which levels may Action Items be viewed or associated: program, loop,
   project, package, deliverable, discipline, external party?
8. Which Action Item operations are deterministic service operations, and
   which require Agent 1, Agent 0, or human judgment?
9. How are assignments represented without confusing agent execution with
   professional accountability?
10. How is prioritization represented without falsely converting situated
    value judgment into an automatic score?
11. How are decisions, approvals, changes, checking, and closure evidence
    linked without copying their authoritative state?
12. What does the initial Chirality App Tasks module contain?
13. What interfaces may domain applications or project adapters use?
14. What is the smallest useful first release?
15. What open-data, export, recovery, and migration requirements preserve the
    rule that tools serve the framework?
16. What remains usable if the service is unavailable?
17. How does Resource Governance consume or enrich task information without
    entering Task Management scope?
18. How are the ordinary word “task,” the Task Management product, and the
    existing `TASK` Agent 2 shell kept semantically distinct?
19. What measurements demonstrate reduced coordination failure rather than
    increased tracking burden?
20. What falsifies the product thesis?

## 11. Adjacent Root architecture question

The owner separately expressed the desire to eliminate required handoff-state
artifacts so that later sessions re-derive current state from immediate
authoritative sources, with work-scope information residing in deliverable
folders and Action Items residing in Task Management.

This is an adjacent Root architecture question, not a Task Management feature
or an amendment made by this authoring basis. A Task Management product may
make that future change more feasible by giving Action Items a proper home,
but its PRD must not silently amend Root workflow doctrine or claim that
handoff-state elimination has been accepted.

## 12. Recommended next sequence

1. Start a fresh `HELP_HUMAN` / Agent 0 inquiry session from this authoring
   basis and the retained source corpus.
2. Inspect current Root, App, PEC, Piping, runtime, agent, workflow, and
   project-controls boundaries only as needed to establish concordance and
   avoid duplicated ownership.
3. Author a complete Chirality Task Management PRD candidate with explicit
   provenance labels and falsification criteria.
4. Iterate with the owner and adopt no bytes without a separate owner act.
5. After PRD adoption, invoke `SOFTWARE_DECOMP` to derive packages and
   deliverables through its governed gates.
6. After decomposition acceptance, invoke `PROJECT_SETUP` to materialize the
   new project and its development loop.
7. Route any App Tasks module change through the App project's own later
   scope-change process against the accepted Task Management boundary.

No project execution tree, package, deliverable, App amendment, or
implementation is created by this record.
