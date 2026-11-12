---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: execution/_Decomposition/PROJECT_DECOMP.md
project_scope_refs: [SOW-0011, SOW-0014, SOW-0034]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-003, OBJ-004]
---

# Reflective review of the practice

## Purpose and Objective Traceability

A person and Agent 0 can ask whether the Library's reconciliation, its chosen
local goals and the framing of the work still serve the intended result, and
come out with a reasoned decision to keep or change them that reaches the text
it governs. This deliverable contributes four things to that result: the
accepted decomposition that gives the Library its local goals; the reflective
method and the role and coordination passages that support it; a real
examination carried through to its consequence; and the book *Chirality in
Practice*, which sets out the reasons and experience behind the practice.

Its allocation is the DEL-04-02 card of the
[accepted decomposition](../../_Decomposition/PROJECT_DECOMP.md), with the
formation allocation in that document's §8.1. It serves
[PRD](../../../docs/PRD.md) objectives O1 to O4.

| Scope item | What this deliverable contributes | Objectives | PRD |
|---|---|---|---|
| SOW-0011 | The accepted decomposition of bounded contributions, with its decisions and independent audit | OBJ-001, OBJ-002, OBJ-004 (O1, O2, O4) | R07, §6.2–6.3, A3 |
| SOW-0014 | The examination of goals and framing when a finding calls them into question. DEL-04-01 holds the action and source-reconciliation side | OBJ-002, OBJ-003, OBJ-004 (O2, O3, O4) | R10, R11, A3, A5 |
| SOW-0034 | No output. PRD §3.6 ends the Library's obligation to supply a repository-change evaluation workflow or an application of one | — | R18 as amended |

The decomposition ledger still allocates SOW-0034 here; it has not been
amended to match PRD §3.6, and this scope follows the PRD.

The book serves OBJ-002 and OBJ-003 as one of the maintained publications of
PRD §2.3 and R11. It has no scope item in the ledger.

## Deliverable Definition — Ontology

A **reflective question** asks whether a goal, premise, method or monitoring
arrangement still serves the person's intended result. It starts from a
concrete finding, not from a schedule or a search for things to change.

A finding can show one of four things: a repair needed under existing
commitments; an inadequate explanation; an unsuitable practice; or a purpose
or commitment that needs the human's reconsideration. The examination ends in
one of three results: the route is **retained** with its reason; a method is
**changed** within existing authority; or a **reserved choice** is returned to
the owner with its consequence.

**Reconciliation** compares a result with the commitments as they stand and is
DEL-04-01's. **Reflection** asks whether those commitments, their framing or
the practice still serve. Neither replaces the other.

The **formation set** is the accepted decomposition and what establishes its
acceptance.

- **OUT-001** — The formation set under `execution/_Decomposition/`: the normalised scope, vocabulary and objectives; the package and deliverable design; the owner's decisions; the independent audit; and the accepted snapshots with their manifests. Serves SOW-0011.
- **OUT-002** — Reflective guidance: the method `workflows/reflect-on-work/WORKFLOW.md`; the passages of `agents/AGENT_HELP_HUMAN.md` on intended outcome, changed questions, commitments and continuity; and the coordinated-knowledge-work workflow's passages on testing a premise, diagnosing waiting and when to finish. Together they let a reader notice a changed question, compare local completion with intended use, weigh the cost and warrant of monitoring, and decide to retain a route, revise a method or return a reserved choice. Serves SOW-0014.
- **OUT-003** — A real application: a bounded question examined with the human and Agent 0, the judgment reached with its reason, and its consequence carried into the governing text or an explicit reason for retention. It needs no transcript and no reflection report. Serves SOW-0014 and the reflective side of PRD A3.
- **OUT-004** — The book *Chirality in Practice: Extending Human Capability with Agents*, first edition, at `docs/alignment-manual/Chirality_in_Practice_Edition_1.md` with its generated HTML, and one optional link to it from reflect-on-work. It develops the thesis's relation to practice across the Chirality projects and what experience can warrant keeping or changing in the shared Library. It stands on its own account, with no lineage to an earlier manual, and adds no instructions, required reading or reports.

Definitions and boundary:

- **CLM-001** — Each checkpoint snapshot under `execution/_Decomposition/checkpoint_snapshots/` holds a payload, a `DECISION.md` and an `ACCEPTED_MANIFEST.csv`. The decision, not status wording inside the payload, states the acceptance. The Group 2 decision binds Agent 0's rendering of the structure the owner approved; it does not say the owner inspected those bytes. `_LATEST_ACCEPTED.md` names the accepted decomposition and how to recover its exact reviewed content. `PROJECT_DECOMP.md` is the working decomposition. Accepted snapshots are never rewritten.
- **CLM-002** — Reflection is a method of its own. HELP_HUMAN supplies the posture and coordinated knowledge work organises contributors; neither substitutes for reflect-on-work. HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS may own the method. TASK contributes bounded evidence through its caller.
- **CLM-003** — The reconciliation method and the localities with their needs belong to DEL-04-01. The wider maintenance route, including how a role or workflow is revised, belongs to DEL-02-01. The shared-reference repair belongs to DEL-02-02. Tools and their usage contracts belong to DEL-03-01. Navigation to the book in the README and the manual index belongs to DEL-01-01, and obtaining, compatibility and publication, with the index's edition recovery and render instructions, to DEL-05-01. In `agents/AGENT_HELP_HUMAN.md` and `workflows/coordinated-knowledge-work/WORKFLOW.md` this deliverable's part is the passages named in OUT-002. Which deliverable answers for the rest of the role is undecided, and the step before integration in coordinated-knowledge-work at which the combined result is checked is DEL-04-01's. Who owns that workflow's sections on briefing, shared generated artifacts and shared limits, and the `REVIEW-NOTES.md` beside it, is undecided.
- **CLM-004** — Changes to commitments or acceptance criteria, risk acceptance, explicit holds, protected baselines, acceptance and release belong to the owner. Each consuming project decides its own adoption, policy and release. Publishing an edition of the book is an owner act.

Outside the product: a repository-change evaluation workflow or tool-supported
evaluation; a standing monitoring service; a recursive review hierarchy; an
automatic model loop; scheduled reflection; and any rollout of the practice to
another project.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The formation set shows which decomposition is accepted, by whose decision, and on what independent audit, with each snapshot's files matching its manifest. Reflective guidance does not stand in for it. Source: SOW-0011; PRD R07; decomposition §8.1.
- **REQ-002** — The guidance helps a person and Agent 0 frame a bounded question about framing or practice, connect it to the purpose and accepted goals, tell evidence from uncertainty, weigh monitoring effort against its benefit, and choose retention, an authorised method repair or an owner decision. It keeps human judgment, local ownership and the continuation of unaffected work. It prescribes no meetings, exhaustive audits or successive levels of monitoring. Source: SOW-0014; PRD R10, R11; decomposition card.
- **REQ-003** — An application examines a real question with the human and Agent 0 against intended use, evidence, uncertainty and consequences. A conclusion to retain or change gives its reason; an authorised consequence reaches the governing text; an unresolved warrant stays visible; a reserved choice is returned with its consequence, not decided silently. Source: decomposition card.
- **REQ-004** — For PRD A3 this deliverable supplies the examination of what a finding meant for the goal or framing. The case itself, an actual authorised action on accepted and set-up scope, is defined by DEL-04-01/AC-005. A discussion, a structural pass or the formation set alone does not establish A3. Source: PRD A3; decomposition §8.1, §9.
- **REQ-005** — A revision of reflective guidance is made through the Library's maintenance route and reviewed under the text that preceded it, which stays recoverable until the replacement is verified and adopted. Both the revised passage and the means used to revise it are checked, and proposed text does not authorise itself. A passage that already meets REQ-002 is kept unchanged. A test implements a verification; it does not define or reduce a criterion. Source: PRD R06, A5.
- **REQ-006** — The outputs contain nothing CLM-003 allocates to another deliverable. A finding about another deliverable's product goes to that deliverable's implementation owner; reflection may warrant a change there without making it.
- **REQ-007** — The guidance directs no edit of another contributor's scope or needs, no change to a commitment, criterion, hold, protected baseline or risk disposition, and no acceptance, release or consumer rollout. Those go to the owners in CLM-004.
- **REQ-008** — Published guidance, the book and the formation set hold no credentials or private operational data, keep the identity of their sources, and tell apart actual observation, reused evidence, constructed example and unknown. Source: PRD R17.
- **REQ-009** — The book is a coherent reflective account grounded in identified practice and explanatory sources. It distinguishes the author's commitments, interpretations of documented experience, constructed cases and proposals; states the limits of generalising across projects; and presents learning across the projects as a direction, not an established practice. It uses an impersonal voice and invents no first-person experience. It explains how experience, shared understanding, changed Library means and independent adoption bear on one another, including work after an undertaking is complete, without prescribing another execution system. It replaces no other publication.

- **AC-001** — `_LATEST_ACCEPTED.md` names the accepted decomposition and how to recover its exact reviewed content, and that recovery succeeds. Every file listed in each snapshot's manifest matches its recorded hash. The working decomposition gives every scope item one package, every in-scope item at least one deliverable, and every deliverable a goal, scope items, objectives, anticipated outputs, evaluation and boundary. The independent audit is present with its findings and limits. Verified by VER-001.
- **AC-002** — From the guidance in OUT-002 a reader with a concrete finding can identify the changed question, compare local completion with intended use, weigh the cost and warrant of monitoring, and tell the retain, authorised-revision and reserved-choice routes apart. The passages work together and require no ceremony, schedule, report or further layer of oversight. Verified by VER-002.
- **AC-003** — One real examination with the human and Agent 0 shows its question, the judgment reached and its reason, what stayed uncertain, and either the governing text that changed as a result or the explicit reason the route was retained. A reserved choice that was returned is distinguishable from one that was decided. Verified by VER-003.
- **AC-004** — For the A3 case that DEL-04-01 identifies, the examination with the human of what its finding meant for the goal or framing is shown: the judgment, its reason and its consequence in the governing text. Verified by VER-004. The case DEL-04-01 identified is F-02: the repair of DEL-02-02's reference-applicability reading after independent examination found current callers of the rules it had treated as legacy. DEL-04-01's identification and assessment of it are in its [formation and reconciliation basis](https://github.com/sgttomas/chirality-library/blob/1d536c58b787db14d544783667e0fbe4d8c44cbd/execution/PKG-04/DEL-04-01/Work/FormationAndReconciliation.md#agent-0-assessment-of-the-actual-f-02-case), and the examination with the human is in this deliverable's [reflective basis](https://github.com/sgttomas/chirality-library/blob/1d536c58b787db14d544783667e0fbe4d8c44cbd/execution/PKG-04/DEL-04-02/Work/ReflectiveBasis.md#agent-0-assessment-of-the-real-framing-question), which also holds the examination AC-003 refers to. Both files are at revision `1d536c58b787db14d544783667e0fbe4d8c44cbd` and no longer in the tree. Naming the case says where it is recorded; it states no result.
- **AC-005** — Each revision of the guidance in OUT-002 was reviewed under the preceding text, with checks of both the revised passage and the means used to make it. That text is recoverable from Git, and the adoption names the authority that adopted it. An unrevised passage meets REQ-002 when read by someone who did not write it, and a review that weighed changing it and kept it says why in its pull request or return. Verified by VER-005.
- **AC-006** — Across the outputs, reserved choices go to their owners, nothing allocated to a sibling deliverable appears, no formation, structural or discussion-only evidence is presented as fulfilment, compatibility, release or adoption, and the public text passes the credential scan. Verified by VER-006.
- **AC-007** — The book reads as a reflective account throughout, and the manual index, the README and the link from reflect-on-work present it that way. Each case claim resolves to its source and states its limit, and the link from reflect-on-work resolves to an exact book source. The HTML is the renderer's output for the committed Markdown. No other publication is changed by it, and nothing in it creates an obligation, adoption or approval. Verified by VER-007.

## Production and Verification Method — Praxeology

Choices that define the product:

- Reflection starts from a concrete finding and the person's intended result.
  It frames the smallest question that could change a useful decision.
- Its result is carried into the governing text by that text's owner. Ordinary
  disagreement between a result and a scope goes to bounded reconciliation; a
  method change goes through `workflows/create-workflow/WORKFLOW.md`.
- The method needs no tool, resource file, matrix, score or report.
- The book's Markdown is its source. The HTML is generated from a committed
  source revision by `docs/alignment-manual/render_manual.py` and is never
  edited by hand.
- A change to the decomposition's allocation goes through the scope-change
  route and a new accepted basis. A snapshot is never edited.

- **VER-001** — Open `_LATEST_ACCEPTED.md` and follow its recovery route. For each snapshot, compute the SHA-256 of every file its `ACCEPTED_MANIFEST.csv` lists and compare. Read the working decomposition's ledger and cards for the coverage AC-001 names, and read the audit's findings and limits.
- **VER-002** — A reader who did not write the guidance takes a bounded finding through reflect-on-work and the named passages, and records where each step in AC-002 is found and any ceremony, schedule or report the text requires. Reading the text establishes usability, not that a real application took place.
- **VER-003** — With the human and Agent 0, trace the selected examination from its question to the governing edit or the reason for retention, using the pull request and the changed text. Require no transcript.
- **VER-004** — Read the case DEL-04-01 identifies, named in AC-004, and locate the reflective judgment about its finding and that judgment's consequence. Mark missing evidence as unverified; a labelled or synthetic case is rejected.
- **VER-005** — Comparison with a named reference (the preceding text in Git) and judgment by a reader who did not write the passage: For each revision, compare the diff with the preceding text, confirm the maintenance route was followed and the checks of the means used are identifiable, confirm the old text is recoverable, and identify who adopted it. For a retained passage, read the passage itself against REQ-002.
- **VER-006** — Read the outputs against REQ-006, REQ-007 and REQ-008, naming each reserved choice and where the text sends it. Run `python3 tools/validation/validate_run_record_leaks.py --base <base> --head <head>` on the change and state what the scan does not cover.
- **VER-007** — Read the whole book, not only its introduction, against REQ-009, with scrutiny by someone other than its drafter. Follow each case claim and the reflect-on-work link to its source as a reader of the public Library would, without private access. Run `python3 docs/alignment-manual/render_manual.py --source <book.md> --output <book.html> --basis-date <date> --basis-revision <commit> --edition-label 'Chirality in Practice · First edition' --metadata-at-end --check`. Read the index and README entries. The author reviews title, interpretation and content; publication is a separate act.

## Governing Values and Decisions — Axiology

- **AX-001** — Local completion is judged by the human's intended result. Better is more reflective questions that end in a decision reaching its governing text, or a stated reason to retain, for less interruption of the work. That may never be gained by adding reports, agents or monitoring layers, or by taking a decision on purpose or commitments away from the human.
- **AX-002** — Commitments and historical evidence are preserved. An adverse finding may show missing behaviour, a stale description, missing evidence or an unsuitable framing; better is naming which. No finding licenses weakening a criterion to obtain a pass, and a substantive ambiguity is stated with its consequence while unaffected work continues.
- **AX-004** — The book's claims are no stronger than their grounds. Better is more of its claims traced to an identified source with the limit stated. That may never be gained by turning the book into instructions or by reporting as established what is a proposal or a constructed case.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-001, OBJ-002, OBJ-004 | REQ-001, CLM-001 | AC-001 | VER-001 | Acceptance is read from each snapshot's `DECISION.md`, and the audit is by a reviewer who did not author the decomposition. The manifests are the formation set's own earlier output and only guard against change. Coverage is read against PRD R07 and §6.2. |
| OUT-002 | OBJ-002, OBJ-003, OBJ-004 | REQ-002, CLM-002 | AC-002 | VER-002 | What the guidance must support comes from the decomposition card and PRD R10 and R11. Whether the text delivers it is judged by a reader who did not write it. |
| OUT-003 | OBJ-002, OBJ-003, OBJ-004 | REQ-003, CLM-004 | AC-003 | VER-003 | What an application must show comes from the decomposition card. The case is a real examination; the human who took part confirms the judgment and its consequence. |
| OUT-003 | OBJ-002, OBJ-003, OBJ-004 | REQ-004 | AC-004 | VER-004 | What the case must show comes from PRD A3, and the case from DEL-04-01. The human confirms the reflective judgment. |
| OUT-002 | OBJ-002, OBJ-003, OBJ-004 | REQ-005, CLM-004 | AC-005 | VER-005 | The rule comes from PRD R06 and A5. The preceding text comes from Git history. |
| OUT-002 | OBJ-002, OBJ-003, OBJ-004 | REQ-006, REQ-007, REQ-008, CLM-003, CLM-004 | AC-006 | VER-006 | Reserved choices come from PRD §5 and R10 and the sibling allocation from decomposition §9. The credential scan is the Library's own tool and covers only the patterns it holds. |
| OUT-004 | OBJ-002, OBJ-003 | REQ-009, REQ-008 | AC-007 | VER-007 | Whether the book has the character REQ-009 states is judged by a reader other than its drafter. Case claims are checked against their cited sources, which lie outside the book. The render check compares the HTML with the renderer's own output and only guards against change. |
