---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-02
package_id: PKG-03
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0035]
package_objective_refs: [OBJ-002, OBJ-003, OBJ-004, OBJ-005]
---

# Inspect repository change and compare its means

## Purpose and Objective Traceability

The Library no longer makes a repository-change evaluator and accepts no work
against one: [PRD](../../../docs/PRD.md) §3.6 ended that obligation when the
evaluator's source left the Library. What this deliverable contributes is what
remains. A reader who meets the former evaluator in the Library's history or
in a reference to it can recover exactly what it was, namely its source and
tests, its paired workflow, the contract it was built to and the account of
its first use, from one identified public revision; and the current Library
works without it.

Its allocation is the DEL-03-02 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md). It serves
PRD objectives O2, O3 and O5.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0035 | No executable capability. The former evaluator's source, contract and evidence stay identified and recoverable, and nothing in the current Library depends on them | OBJ-002, OBJ-003, OBJ-005 (O2, O3, O5) | §2.2, §3.6 (R18 as amended), R15, R17 |

The decomposition ledger and this deliverable's card still describe SOW-0035
as an executable capability to supply. They have not been amended to match
PRD §3.6, and this scope follows the PRD.

## Deliverable Definition — Ontology

The **former evaluator** is `tools/undertaking_evaluation/`, with its
`inspect` and `compare` commands, its guide and its tests, and the paired
workflow `workflows/evaluate-repository-change/`.

The **recovery revision** is commit
`a000e2f40f724dcda9f1158cf3c4c3ed4378884c` of the public Library repository,
the last revision that holds the former evaluator. This locality as it stood
at that revision holds the **original contract**, which is the scope the
evaluator was built to, and the **evidence of first use**, which is the
account of what the first implementation supported and of the private pilot
that exercised it.

Chirality Root holds a private copy of the former evaluator's source as
starting material under Root's own commitments. That copy is outside this
deliverable and outside the Library.

- **OUT-004** — The former evaluator, its original contract and its evidence of first use, recoverable from the public repository at the recovery revision. Serves SOW-0035 and OBJ-003, OBJ-005.
- **OUT-005** — A current Library source that holds no repository-change evaluator and depends on none. Serves SOW-0035 and OBJ-002, OBJ-005.

The original contract numbered its ids from 001 in each kind. Those numbers
keep naming its parts and are not reused; the ids here continue after them.

Boundary:

- **CLM-006** — `workflows/evaluation-protocol/`, `workflows/evaluation-report/` and `tools/evaluation/` are the Library's adherence-evaluation holdings; they stay in the Library and are no part of this deliverable. `workflows/audit-agents/` left the Library in the same removal and is no part of it either. Scaffolding, validators, queries and their usage contracts belong to DEL-03-01. The reflective method belongs to DEL-04-02, which carries no evaluation workflow. Recovery routes for the Library's history in general belong to DEL-05-01.

Outside the product: a new importer, measurement, report, case or trial
comparison, workflow or qualification by actual use; restoring the former
evaluator to the current source; and any route by which a Library user is sent
to Root's copy.

## Completion and Reliance Basis — Epistemology

- **REQ-010** — The recovery revision is reachable from the public repository's `main` branch and holds, as they were, the former evaluator's guide, source and tests, the paired workflow, the original contract and the evidence of first use. Source: PRD §3.6, R15.
- **REQ-011** — The current Library source holds no runnable repository-change evaluator. No instruction, workflow, tool, test, catalog or index in it requires the former evaluator, or a Root checkout, Root's runtime or credentials, or adoption of Root's copy. The current source documents a route to the recovery revision where a Library user meets the former evaluator as a holding, and no mention presents the evaluator as current or Root's copy as a route to it. Source: PRD §2.2, §3.6, R15, R17.
- **REQ-012** — The public repository holds none of the pilot's operational records: no raw session record, message body, session identifier or private path. Source: PRD §2.3, R17.

- **AC-007** — In a fresh clone of the public repository, the recovery revision is an ancestor of `main`, and at that revision `tools/undertaking_evaluation/` holds the guide, the package source and its tests, `workflows/evaluate-repository-change/WORKFLOW.md` exists, and `execution/PKG-03/DEL-03-02/` holds the original contract and the evidence of first use; and the files listed at that revision hold none of the pilot's operational records (no raw session record, message body, session identifier or private path). Verify by VER-007.
- **AC-008** — In the current source no tracked file exists under `tools/undertaking_evaluation/` or `workflows/evaluate-repository-change/`; the workflow catalog and index list no `evaluate-repository-change`; no import, command, registered check or instruction step invokes the former evaluator or names a Root checkout, Root's runtime or credentials, or adoption of Root's copy as something a Library user needs; the tool registry's passage on the former evaluator says it was removed and names the recovery revision, and no tracked mention presents it as current or offers Root's copy as a route; and no tracked file holds a pilot operational record. Verify by VER-008.

## Production and Verification Method — Praxeology

Choices that define the product:

- History is kept by Git at one named revision. Nothing of the former
  evaluator is copied forward into the current source, and this scope does not
  quote the original contract.
- The current source points back to the recovery revision; it never points
  across to Root.

- **VER-007** — Executable check (observes Git objects at the recovery revision in a fresh clone of the public repository) with judgment by a reader who did not write those files (reads them at the revision for the pilot's operational records): run `git merge-base --is-ancestor a000e2f40f724dcda9f1158cf3c4c3ed4378884c origin/main` and `git ls-tree -r --name-only a000e2f40f724dcda9f1158cf3c4c3ed4378884c -- tools/undertaking_evaluation workflows/evaluate-repository-change execution/PKG-03/DEL-03-02`, compare the listed paths with those AC-007 names, and read the listed files at the revision for raw session records, message bodies, session identifiers and private paths.
- **VER-008** — Executable check (observes the tracked files, the workflow catalog and index, and every tracked line that names the former evaluator) with judgment by a reader who did not write those lines (reads each mention for whether it requires the evaluator, presents it as current or offers Root's copy as a route, and reads the tool registry's passage for the removal and the recovery revision), and an executable check (the credential scan, which observes only the patterns it holds): run `git ls-files tools/undertaking_evaluation workflows/evaluate-repository-change`; read `workflows/catalog.yaml` and `workflows/index.json` for the method name; run `git grep -n -e undertaking_evaluation -e evaluate-repository-change` and read each hit; read the passage on the former evaluator in `tools/REGISTRY.md`; search tracked files for session records and private paths; and run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change, stating what the scan does not cover.

## Governing Values and Decisions — Axiology

- **AX-004** — History stays findable without staying alive. Better is fewer steps from any mention of the former evaluator to its exact source and contract: one revision, read with ordinary Git. That may never be gained by restoring the source or its commitments to the current Library, by copying pilot records into the public repository, or by sending a reader to Root's private copy.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-004 | SOW-0035, OBJ-003, OBJ-005 | REQ-010, REQ-012 | AC-007 | VER-007 | What must be recoverable is named by PRD §3.6, and what the public repository may not hold by PRD §2.3 and R17. They are compared with the Git objects of a fresh clone of the public repository, which nothing in the current source writes, and the files at the revision are read by a reader who did not write them. |
| OUT-005 | SOW-0035, OBJ-002, OBJ-005 | REQ-011, REQ-012, CLM-006 | AC-008 | VER-008 | What must be absent and what may not be required come from PRD §2.2, §2.3, §3.6 and R17. That a route to the recovery revision is documented comes from PRD §3.6 and R15. They are compared with the tracked files, the catalog and index and the tool registry, and each mention is judged by a reader who did not write it. The credential scan is the Library's own tool and covers only the patterns it holds. |
