# Course 02: Document and Configuration Control

[Series](../index.html) · [Case](../case-study.html) · [Glossary](../glossary.html) · [References](../references.html)

People need to know which information governs their work and whether that information describes the actual product. Document control and configuration control establish these relationships.

This course teaches a practical control method for a small project, in a team where people work with AI agents. You will identify records, establish their permitted use, distribute changes, and trace effects. You will preserve earlier information so another person can understand a decision's basis.

## Prerequisites and outcomes

Complete Course 01 and read Northbank Packet A. Keep your appointment response available.

### How this course is built

The series index explains [how the series is built](../index.html#how-the-series-is-built). The classical method was examined here in a working arrangement where preparing and checking each record takes people's time to write, copy, and distribute; with agents, records are cheap, so teams now risk keeping too many, and each surplus record takes the attention of the people who must read and maintain it. Controllers therefore need restraint about which records to keep, and they must govern which basis, by identity, revision, and status, each agent reads. Lesson 5 treats that as an arrangement to design.

### The teaching arrangement

Use the case's [arrangement for working with agents](../case-study.html#working-with-agents-in-the-case). In this course, agents prepare and copy records only as working material; issuing a controlled revision stays with the people who hold that authority.

### Outcomes

By the end, you can:

- Assign stable identities to project information.
- Distinguish revision, status, and authorized use.
- Establish a baseline for a stated purpose.
- Trace a change to its affected users and work.
- Identify differences between defining records and the actual configuration.
- Issue a controlled basis to an agent, and check which basis its output used.
- Decide which records a project needs, and keep the rest out of the controlled set.

## Lesson 1: Give information a stable identity

### The classical method

A filename helps you find a document, but it may not identify the document reliably. People copy files, rename them, and attach extracts to messages; similar filenames can contain different revisions.

Use a stable identity that survives those movements. Northbank uses A02 for the project basis; Rev 0 and Rev 1 are different revisions of that identified document. A reference to “the basis file” leaves the reader uncertain.

Record enough information to retrieve the exact item. Useful fields include identity, title, revision, status, origin, location, and issue date; add subject and use limits where they matter. An attachment copied into another folder should keep its identity and revision.

An extract also needs identity, so state its parent source and the extent of the extract. A table copied without its source note can change how the reader understands it. At Northbank, the planning-estimate note on the legacy schedule is essential to its value as evidence.

Use one authoritative location for a controlled item when the working system allows it; other copies should identify their origin and controlled status. Arrange access so the people doing the work can retrieve the required revision.

Apply this identification method:

1. Assign the item a stable identity.
2. Record its revision and title.
3. Identify its origin and retrievable location.
4. Record its status and permitted use.
5. Identify any parent source or attached evidence.
6. Check that the intended user can retrieve it.

Preserve earlier revisions according to the actual retention requirements: they help reconstruct a decision and explain a later change. Control access to sensitive information under the applicable arrangements.

### What it assumes

The 'What it assumes' passages in this course describe working arrangements for comparison. They are not universal facts about human practice; examine whether they hold in the task at hand.

The classical method assumes that copies and extracts multiply at the pace of people's work. It also assumes that a person reading a document brings some context: a draft watermark, an unfamiliar date, or a colleague's remark can make them pause before they use the wrong file.

### What changes with agents

Agents copy, extract, summarize, and re-save at machine pace, and each derivative is a new item that can lose its identity. An agent's summary of A03 that omits the planning-estimate note is the classical extract problem, produced in seconds and possibly many times.

Agents read what they are given or can reach. An agent given access to Northbank's shared folder meets A02 Rev 0 and Rev 1 under similar filenames, as A07 reports, and it has no institutional memory to tell it which one the team uses. Unless its brief or the record's own fields say which revision governs, it may use either one.

Agents are also intended users now. Step 6 asks whether the intended user can retrieve the item; when an agent works from the record, that includes the agent.

### The extended method

Require identity on every agent derivative. An agent's extract, summary, or table states its parent source, revision, and extent, just as a person's extract must. Prefer links to the authoritative location over agent-made copies, because cheap copies multiply the items whose identity someone must keep.

Brief agents with exact identities and revisions, not folder paths or descriptions such as “the basis file.” Ask the agent to report the identity and revision of each source it used, and check that report against the identified basis.

| Choice | Gain | Cost |
| --- | --- | --- |
| Give the agent the whole shared folder | It can find a relevant item you did not name | It may read a draft or superseded revision, such as A02 Rev 0 |
| Give the agent an identified set of records | It works from the controlled basis | It misses any relevant item left out of the set; A07 shows that the library index omits A04 |

## Lesson 2: Distinguish revision, status, and purpose

### The classical method

A revision identifies a version, status describes its condition under the control process, and purpose describes what the item was issued for. These three fields answer different questions.

The highest revision may be a draft; an older revision may remain the approved basis for a particular activity. A document issued for review may support comments but not be authorized for purchase or construction.

Approval also has scope. A02 Rev 1 is approved for project development and states unresolved inputs; its approval does not establish that equipment selection is complete. A04 is a checked observation with explicit limits.

Create a baseline when a group of identified information must serve as a controlled reference. State its purpose and change process, and include the relevant revisions, decisions, and unresolved conditions. A baseline can contain open matters if their treatment is explicit and suitable for its purpose.

Before you rely on an item, ask:

- Is this the identified revision needed for the activity?
- Does its status permit this use?
- Does its approval cover this content and scope?
- Are its unresolved conditions compatible with the activity?
- Has a later decision changed its permitted use?

Use an issue check:

1. Identify the receiving activity.
2. State the permitted use.
3. Check the required review and approval evidence.
4. List unresolved conditions that affect the use.
5. Identify the issued revisions.
6. Notify the intended recipients.

Do not use a “current” label without defining what purpose it is current for. When several activities use different baselines, make their relationships explicit; otherwise, people can combine individually valid information into an inconsistent result.

### What it assumes

The classical method assumes that the people who receive an issue read its status and purpose, and that a person who uses the wrong revision does so in one piece of work at a time. Someone usually notices before the error has travelled far.

### What changes with agents

An agent reads status only if the status is in the material it receives and the brief makes it matter. Without that, it can treat the newest-looking file as current, or a proposal as basis.

A superseded or draft revision used by an agent can spread faster. One designer who opened A02 Rev 0 affects the work that designer touched. An agent briefed with Rev 0 can carry 15 litres per second into every draft, calculation, and list it prepares, and other agents may then read those outputs as inputs.

So the brief becomes an issue. Every agent assignment receives information for a purpose, which is exactly what the issue check governs.

### The extended method

Treat each agent brief as an issue of controlled information, and apply the issue check to it. State the receiving activity and its permitted use, identify the issued revisions with their status, and list the unresolved conditions that affect the work. For Northbank project development, that means A02 Rev 1 as approved for project development, with its unresolved operating conditions, and A05 Rev 0 marked as a proposal.

When the basis changes, include agent work in progress among the recipients. An agent assignment briefed before the change is still working from the earlier basis until someone stops it or re-briefs it.

## Lesson 3: Control a change through its consequences

### The classical method

A changed document can affect work already completed, and it can also change inputs that another person is using. Revision control preserves the versions; change control deals with these consequences.

Start with the proposed departure from the approved basis. Identify its reason, the requirements it affects, its technical and resource effects, and who has authority to decide it. Seek the necessary decision before you implement a reserved change.

After approval, update the defining information and notify the affected people. Ask each receiving owner to examine the effect on their work. A sent message is evidence of distribution, but it does not establish that the recipient applied the change correctly.

Different owners may need different actions. A flow change can affect pump selection, piping, electrical loads, controls, supports, tests, and operating information, but the exact effects require competent examination. Do not assume the list is complete just because it is long.

Keep the original proposal and decision basis available, identify which revisions the new decision changes, and record any conditions on implementation. That lets a successor tell an authorized change apart from an unexplained document difference.

Apply a controlled-change method:

1. State the proposed departure.
2. Identify the affected baseline.
3. Assess the effects with the affected owners.
4. Obtain the required decision.
5. Revise the defining information.
6. Distribute the identified revision.
7. Check adoption in affected work.
8. Preserve the decision and earlier basis.

Where an input defect is found, correct its distribution promptly and assess the work that already used it. Preserve the defect and repair evidence when later examination needs them; a silent file replacement prevents that examination.

### What it assumes

The classical method assumes that revising and distributing documents takes people's time, so changes move slowly. That slowness limits how far an error travels before someone notices it. Preparing an impact list also takes effort, so the list reflects someone's thought about each entry.

### What changes with agents

Agents make several steps fast. An agent can draft an impact list for a flow change quickly, and the list may be long. The classical warning matters more: a long list is not a complete one, and a list an agent produced cheaply does not show that anyone examined each entry.

An agent can revise defining information across many documents quickly, and it can carry a wrong value as quickly as a right one. Course 08 develops this for [propagating dispositions](08-project-execution.html#lesson-4-connect-purchasing-risk-and-change).

Agents can check adoption at the level of text. An agent can search every output for 15 litres per second and report each place it appears. That search is useful for the impact enquiry, but it finds the value only where it is written. A pump duty or pipe size that someone derived from 15 litres per second does not contain the number, and finding it needs the owner's examination.

Agents can also overwrite files. An agent that corrects a document by replacing it in place performs the silent file replacement that the classical method forbids, and it can do so many times before anyone notices.

### The extended method

Use the same eight steps. Agents can draft Step 3's impact list, perform the mechanical revisions of Step 5, distribute in Step 6, and run text searches that support Step 7. They do not decide in Step 4, and they do not establish technical adoption in Step 7: each affected owner examines whether their work actually adopted the change.

Before any agent revises a document, confirm that the decision exists and identify its scope. Arrange for agents to create a new revision instead of overwriting the controlled one, so the defect and the repair both remain available.

## Lesson 4: Connect the records to the product

### The classical method

Configuration means the arrangement and characteristics of the product or system. Its defining information can include drawings, specifications, software versions, equipment lists, settings, and selected vendor data.

Document control alone cannot show what was installed: a revised drawing may be approved but not applied, a field change may exist without an updated drawing, and a test may cover a configuration different from the delivered one.

Configuration control connects the product, its defining records, authorized changes, and examination evidence. For each important item, identify the actual configuration and the records that define it, and match observations to that configuration.

In early Northbank development, the project has no selected pump configuration, and the product-family brochure cannot fill that gap. It may support investigation, but it does not identify a selected motor, curve, materials, or control arrangement.

Use a configuration comparison at a meaningful transition:

1. Identify the product or system under examination.
2. List the records that define its relevant characteristics.
3. Identify the actual configuration from suitable observations.
4. Compare the defining records with those observations.
5. Record discrepancies and affected evidence.
6. Assign each discrepancy a required response.

Use detail that serves a decision, dependency, examination, or recovery need. A small project can use a simple list, but complex products may need specialized systems. The control must make the relationship understandable to the people who rely on it.

### What it assumes

The classical method assumes that records are costly to make, so a small project keeps few of them and each one has a reason. It also assumes that whoever writes a configuration record has some knowledge of the product it describes.

### What changes with agents

Agents can produce configuration records cheaply and in volume. They can also produce a plausible configuration description from what they have: given the Northbank brochure, an agent can write an equipment list with a motor, a curve, and materials that reads like a selection. The classical rule that the brochure cannot fill the gap becomes more important, because the filled gap now looks like a record.

Agents work on records, not on the product. Step 3 identifies the actual configuration from suitable observations, and those observations still come from people and instruments on site. An agent can compare the records with observations that someone supplies, but it cannot supply the observation.

The classical rule about detail now does more work. Each record an agent adds has to be read, examined, and kept current by someone, and a stale record is one that a later agent may read as current.

### The extended method

Keep a record only when a concrete consumer needs it to decide, act, examine, or recover, or when an acceptance requirement calls for it. Prefer a link or a query to another maintained copy. Brief agents to mark any configuration entry that lacks a selection or an observation behind it, instead of filling it.

| Choice | Gain | Cost |
| --- | --- | --- |
| Record everything agents can produce | A complete trail and easy recovery | Each record uses attention; signal is buried; more stale copies for agents to read |
| Keep only records with a named consumer | Less to read and keep current | A consumer you did not anticipate may lack a record they needed |
| Link to the authoritative source instead of copying | One place to keep current | The reader must be able to reach the source |

## Lesson 5: Govern what agents read and write

In a human team, which information people work from is governed partly by distribution and partly by habit. People know where the approved files are, ask a colleague when unsure, and rarely open a folder they have no reason to open. With agents, the information an agent works from is its brief and whatever it can reach. That is a design you choose, so the control arrangement must make it explicit.

Design the arrangement from its required function: every agent works from an identified basis, and no agent output enters that basis without examination.

**Control what agents read.** Give each agent the identified records with revision and status, and the unresolved conditions that affect its work. Where an agent has broader access, state which revisions govern and which items are drafts, proposals, or archived references, such as A02 Rev 0, A05 Rev 0, and A03 Rev 0.

**Control what agents write.** Agent outputs are working material until someone examines them. Keep them apart from the controlled set, identify them as agent work with the basis they used, and admit them to the controlled set only through the issue check. Arrange for agents to create revisions, not overwrite controlled items.

**Check the basis each output used.** Ask each return to list its sources by identity and revision, and compare that list with the brief. An output built on the wrong revision can be well formed and wrong throughout.

**Practise restraint.** Agents make records cheap, but the attention of the people who read them is not. Ask of each record: who will use it, and for what question? Remove or link any record without an answer.

**Design against the known failure modes:**

- A superseded or draft revision used as current, and its values carried into many outputs.
- An extract or summary that lost its parent identity or its source note.
- An agent output read by another agent as if it were controlled basis.
- A silent replacement that erases the defect and the evidence of repair.
- A text search for a changed value taken as proof that no derived work used it.
- Records produced because they are cheap, not because anyone needs them.

Part of the classical discipline answered the cost of making and copying records by hand, and that part loses force when agents produce them. The parts that govern identity, status, approval scope, and the link between records and product keep their reasons, and agents make them more important, because more work now rests on whichever basis an agent was given.

This is an argument from how the costs have changed, not a measured result. Agent capability and cost vary with the task and the system, so test the premise against your own work. Course 08 extends this view to [the whole working arrangement](08-project-execution.html#lesson-6-engineer-the-arrangement-that-does-the-work).

## Northbank worked example: Two basis revisions

The responsibility brief depends on a clear working basis. Here, the task is to recover that basis and identify work affected by use of the wrong revision.

A07 reports that the shared folder contains A02 Rev 0 and Rev 1 under similar filenames. A designer has opened Rev 0, whose draft flow is 15 litres per second.

The document controller identifies A02 Rev 1 and its approval record. That revision's required flow is 18 litres per second. The controller preserves Rev 0 as an earlier draft and removes the ambiguity about whether it is the working basis.

The project engineer then examines the affected work. The controller cannot determine technical impact just by relabeling the file. The designer must identify the calculations, sketches, and selection notes that used Rev 0.

| Item | Control response | Further examination |
| --- | --- | --- |
| A02 Rev 0 | Identify as an earlier draft; preserve its history. | Find work that used its 15 litres per second value. |
| A02 Rev 1 | Identify as approved for project development. | Preserve its unresolved operating conditions. |
| A03 Rev 0 | Preserve the archived status and planning-estimate note. | Examine any design conclusion that treated it as a site survey. |
| A04 Rev 1 | Add its checked observation and location to the working index. | Keep capacity, protection, and compatibility unresolved. |
| A05 Rev 0 | Retain as a proposal. | Prepare the sponsor's requested impact assessment. |

The correction does not create a new scope decision; it puts the already approved A02 Rev 1 back into working use. Any affected technical work still needs examination and repair.

### The same work with agents

This account is a teaching assumption, not a Northbank record: the records do not say how any of the work was produced.

The document controller briefs an agent to draft the source-control list and to search the project's working outputs for the values 15 litres per second and 480 V. The brief identifies A02 to A07 with their revisions and status, states that A02 Rev 1 holds the approval record, and asks the agent to list each source it used by identity and revision.

The controller does not accept the list because it is complete in form. The controller checks that Rev 1 is identified by its approval record, not by its filename; that A03 keeps its archived status and planning-estimate note; that A04 appears even though A07 reports that the library index omits it; and that A05 stays a proposal.

The search results are leads for the impact enquiry, not its conclusion. A hit shows where a value is written. The absence of a hit does not show that no work used Rev 0, because a value derived from 15 litres per second need not contain the number. The designer and the project engineer still examine the affected work.

If agents had been working from the shared folder while both revisions sat there, the enquiry would also cover their outputs.

The control and technical responses are the same as in the classical account. Agents change who drafts the list and runs the search, and what the controller and the owners must check.

## Transfer example: A manufactured product drawing

A workshop holds Drawing D17 Rev 2, issued for manufacture. Engineering later creates Rev 3 as a review draft, and a technician finds Rev 3 in a message.

The revision number alone does not authorize manufacture to Rev 3, so the technician checks the purpose it was issued for and its approval. If a physical part already follows Rev 3, the team examines that discrepancy before describing the part as conforming.

Preserve the draft and the identity of the manufactured part. The technical owner determines the consequence, and document control supports that determination through reliable records.

An agent preparing machining instructions from the drawing folder meets the same choice as the technician. If its brief names D17 Rev 2 as issued for manufacture, it can work from the right revision; if it does not, it may take Rev 3 because it is newer.

## Practice: Recover a controlled working basis

Use A02 to A07 and Portfolio 01. The supplied condition is the folder discrepancy reported in A07, and no additional approval or technical result is available.

First prepare source-control entries for A01, A06, and A07 yourself, without an agent: identity, revision, status, permitted use, and limits. The worked example does not cover these records, so the entries are your own baseline for judging what an agent's list should contain. Work with an agent for the outputs that follow.

Supply these outputs:

1. A source-control list with identity, revision, status, permitted use, and limits.
2. A short issue note identifying the project-development basis.
3. A distribution list based on affected activities.
4. An impact enquiry for work that may have used A02 Rev 0 or A03.
5. A comparison checklist for a future selected equipment configuration.

State which entries come from Packet A, and identify any missing location or distribution information. Do not invent a completed impact assessment. Ask a partner to retrieve the basis using your list.

For each agent-assisted output, keep the brief you gave the agent and a short note of what you checked in its return, what you found, and what you changed.

Then complete three further exercises:

1. **Issue a basis to an agent.** Write the brief for an agent that will draft the impact enquiry. Apply the issue check from Lesson 2 to the brief itself: receiving activity, permitted use, issued revisions with status, and unresolved conditions.
2. **Check the basis used.** Compare the sources that the agent reports using with the revisions you issued. Record any difference, or record that there was none and what the comparison would have caught.
3. **Practise restraint.** For each record you produced in this practice, including agent outputs, name its consumer and the question it answers. Remove or replace with a link any record without an answer, and explain one removal or one record you kept.

## Knowledge check

1. How does a stable document identity differ from a filename?
2. Why can the highest revision be unsuitable for an activity?
3. What does the approval of A02 Rev 1 permit and leave unresolved?
4. Why does sending a revised document not establish adoption?
5. What distinguishes document control from configuration control?
6. What response is needed after work used the wrong basis revision?
7. Why can an agent's use of A02 Rev 0 cause more damage than one designer's use of it?
8. What does it mean to treat an agent brief as an issue of controlled information?
9. Agents make records cheap. Why can a surplus record still be a cost, and what test decides whether a record should exist?
10. An agent searches the project outputs and finds no remaining use of 15 litres per second. What does that establish, and what does it not establish?
11. Name one document-control practice whose reason weakens when agents produce records, and one that becomes more important. Explain each from the cost it was answering.

## Assessed assignment: Issue a controlled basis

Prepare a controlled-basis package for Northbank project development, working with agents. Use Packet A only, and include a revision list, an issue note, an affected-work enquiry, and a change method. Add a short account of how you arranged what the agents read and wrote, with the briefs you used and your examination record.

Then defend the package to your instructor. Explain its main conclusions and what you checked, and reason through changed premises such as an agent that overwrote a revision, a recorded amendment to A05, or a further omission from the library index. Your instructor rates the defense as the [teaching guide](../instructor-guide.html#assess-agent-assisted-work) describes; in text-only study it is rated on changed-premise reasoning with the medium recorded.

An instructor assesses nine observable criteria:

| Criterion | Evidence required |
| --- | --- |
| Identity and retrieval | Each relevant item has an exact identity, revision, and retrievable source reference. Agent-made extracts and summaries identify their parent source and revision. |
| Status and use | The package distinguishes drafts, approved development information, observations, proposals, and open inquiries. |
| History | Earlier information remains identifiable without ambiguity about its permitted use. |
| Change consequences | The method assigns impact examination, decision, distribution, and adoption checks. It does not treat an agent's text search or distribution as evidence of technical adoption. |
| Configuration relationship | The package identifies missing product definition and limits the proposed comparison accordingly. |
| Control of what agents read and write | Each brief issues an identified basis with revisions and status, and agent outputs stay separate from the controlled set until examined. |
| Record restraint | Each record kept names its consumer and the question it answers. |
| Examination record | The record shows which basis each agent output actually used, what you checked, what you found, and what you changed. |
| Defense | You explain the package's main conclusions and their grounds, and reason correctly through the changed premises your instructor poses. |

Demonstrate retrieval to a reviewer and explain one impact enquiry. Repair any ambiguous basis or unsupported configuration claim. Acceptance in training grants no authority to release a real purchase or construction package.

## Portfolio continuation and references

Keep the package as Portfolio 02 and link it to Portfolio 01. Course 03 will improve its subject index and assess the evidence behind selected claims.

The [management manual (Edition 9)](../../alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v9.html), sections 6.3 and 6.6, explains why a record needs a concrete purpose and why reliance needs an identified edition.

For optional study, compare your organization’s actual document and configuration procedures with the [series glossary](../glossary.html). Use the [reference guide](../references.html) to distinguish each source's purpose and authority.
