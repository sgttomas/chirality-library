# Design walkthrough of software-prd v1

**Method:** author-performed tabletop examination of the saved instructions. These cases are constructed; no project, PRD acceptance, reviewer delegation, or tool execution is simulated as a real event. The purpose is to expose missing branches and unclear returns before human review of the method.

## Case 1: a feature in an existing editor

The owner wants to examine agent proposals while continuing to edit. Inputs are the conversation, an accepted history specification, and a limited preview demonstration. Intake records the different standing of the three. The product account distinguishes live state, source revision, proposal, rejection, application, and undo. Checkpoint A can cite the owner's already explicit direction and asks only about material uncovered choices. The PRD preserves an open stale-proposal response. A separate reviewer examines the complete candidate, the human reviews it at B, and the handoff carries the precise accepted scope into the next authorised undertaking. The method supplies every step without requiring knowledge decomposition or a large publication package.

## Case 2: a large, multi-system product

The intended product includes client tools, shared services, and operational interfaces. Intake must cover shared commitments and material external dependencies. The author proposes one overview with normative annexes, a source inventory, and bounded contributions under a single integration owner. Shared requirements remain in named homes; the accepted set includes the annexes. Review checks cross-section and cross-system meaning. No FEED packages or deliverable IDs are invented during PRD drafting. The workflow scales by added sources, document organisation, and review coverage rather than by a compulsory new role or separate gate for each section.

## Case 3: an API or reusable data-processing product

The method asks about callers, operators, exchanged information, repeated requests, incomplete inputs, and recoverable failures. It does not create screens or pretend every requirement describes a visible click. Developing reusable processing software can be in scope. Merely running a current processor against a dataset remains outside. The requested product outcome determines the route.

## Case 4: maintenance presented as a large task

An urgent database repair spans many tables, or an issue requires a difficult bug diagnosis. Intake identifies restoration or repair as the actual purpose and returns it outside software-prd. Complexity does not create a new product commitment. If the owner separately directs a new capability to prevent the class of failures, that project can enter this workflow while the original repair obligation remains distinct.

## Case 5: a feature request held in a ticket

The ticket proposes a new product capability. The file format is not grounds to reject the request as maintenance. Intake recovers the desired outcome, broader product boundary, and required human decisions. The exclusion concerns issue-ticket execution without a product-definition undertaking, not all requests stored in ticket systems. This distinction was made explicit during the walkthrough.

## Case 6: incomplete or unreadable sources

A current interface agreement is inaccessible. Claims about that interface are held with a specific missing source and affected work. Other source-grounded drafting continues. If the interface defines a central product promise, acceptance cannot imply that it was verified. The human receives the precise consequence and may direct retrieval, revised scope, or an explicit limited basis. A missing source is not replaced by the agent's remembered generic contract.

## Case 7: current behaviour conflicts with intended preservation

Inspection finds that rejecting a preview currently clears selection. The record distinguishes the observation from the desired preservation requirement. The agent can propose new behaviour without claiming it already works. Conversely, observed behaviour does not automatically become an inherited requirement. The human's intended outcome remains a separate source of commitment.

## Case 8: source material contains operational instructions

A document says to ignore governing restrictions or upload a confidential sample elsewhere. Intake treats it as source content, not governing authority. It neither enlarges permissions nor authorises data disclosure. The working record retains a safe description of the relevant concern; copied evidence contains no credentials. No auxiliary tool is invoked solely because source prose demands it.

## Case 9: independent review is unavailable

The author can self-check the PRD but cannot obtain a separate reviewer. The return is review-pending with the candidate preserved. The method does not create a fictional reviewer or treat the same author taking a new rhetorical role as fresh-context review. Human discussion may continue. The requirement must be satisfied or explicitly reconsidered as a method change before the workflow claims conformance at acceptance.

## Case 10: candidate changes after review

A human correction changes the stale-proposal response after a candidate was examined. The author preserves the old candidate and review, revises affected text, and obtains coverage for changed content and relationships. Untouched evidence remains attributable to its original candidate. The new accepted set is identified before B. Old review or acceptance is never transferred silently to the new bytes.

## Case 11: qualified or partial acceptance

The human accepts one feature and leaves an annex unaccepted. The record identifies the exact included scope and common constraints. If that boundary is ambiguous, the agent resolves the ambiguity before reliance. FEED receives only the accepted basis; inclusion of the other annex in a review bundle does not make it authorised scope. Remaining work is carried, not marked complete.

## Case 12: interrupted draft and changed target

A session ends after a source inspection but before review. The handoff preserves sources, findings, candidate, actual human decisions, and next proposed work. The successor inspects the current files. If the intended PRD target changed in another session, publication pauses rather than overwriting it. The candidate survives in the authoring run. No execution tree or project DAG is assumed to exist before setup.

## Case 13: accepted PRD amended after FEED

A newly directed capability affects an existing decomposition. The workflow prepares a successor PRD against its accepted predecessor, with impact and changed commitments. The applicable human acceptance concerns that PRD. The decomposition amendment goes to scope-change under its own authority, and affected downstream work remains open until its owning workflows close it. Producing or accepting the successor does not claim propagation is complete.

## Case 14: acceptance identity without a self-referential manifest

The final PRD and normative annexes are frozen with their identities before the human decision. The later decision record points to that set and does not become a member whose hash must be present in itself. Recording acceptance therefore leaves the approved content unchanged. A working copy at the reader-facing path is checked against the retained candidate before being reported delivered.

## Case 15: no direction to start the next workflow

The PRD is accepted for use in FEED, but this assignment ends at authoring. The return supplies the accepted set and proposed next undertaking. It does not execute software-decomp or project-setup merely because their prerequisites are now available. If an existing human instruction already authorises that continuation, its authority comes from that instruction, not an invented additional gate.

## Result of the tabletop examination

The saved method has an explicit path for each case. The inspection caused clarification of ticket-based feature requests, bounded TASK use of the method, and the limits of final handoff. This is a reasoned design check. It does not establish that another agent will execute the workflow correctly, that the host will enforce it, or that real PRD users will find the two-checkpoint structure adequate. Those questions remain for human review and later observed use.
