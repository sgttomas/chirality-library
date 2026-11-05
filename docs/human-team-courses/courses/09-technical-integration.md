# Course 09: Project Engineering and Technical Integration

[Series](../index.html) · [Northbank case](../case-study.html) · [Glossary](../glossary.html) · [References](../references.html)

## Purpose and preparation

Project engineering coordinates the technical whole. Discipline engineers produce competent contributions, and the project engineer establishes how those contributions fit together and satisfy the project basis.

A sound component can become unsuitable in combination: a motor can match its supplier's data while mismatching the site supply, and an accessible pump can become inaccessible after the piping is installed.

This course teaches you how to coordinate that technical whole in a team where people work with AI agents. Complete Courses 01 to 08 before this course. Bring your project basis, source index, requirements, and execution package. Read Northbank Packets A, B, and C.

### How this course is built

The series index explains [how the series is built](../index.html#how-the-series-is-built). In this course the shifted constraint is the cost of examining how contributions fit together: agents can cross-check interface lists, supplier data, and discipline inputs cheaply and often, but they can also carry a change or an error through connected work at the same speed, while interface ownership stays with people. Lessons 1 to 5 each follow the series' four steps, and Lesson 5 treats the integration arrangement; for the general design of a human-agent arrangement, see [Course 08, Lesson 6](08-project-execution.html#lesson-6-engineer-the-arrangement-that-does-the-work).

### The teaching arrangement

Use the case's [arrangement for working with agents](../case-study.html#working-with-agents-in-the-case). The records do not say how any Northbank contribution, including B01, was prepared, so this course labels any supposition that an agent prepared one as a teaching assumption.

### Outcomes

After this course, you can:

- Maintain a usable design basis across disciplines.
- Assign technical interface responsibilities.
- Examine supplier information against the project configuration.
- Coordinate construction, operation, and maintenance needs.
- Review the integrated result and propagate technical changes.
- Arrange agent cross-checks of interfaces, supplier data, and discipline inputs, and decide how often to run them.
- Distinguish consistency among contributions from correctness of the integrated result, and keep configuration control in step with agent-speed change.
- Direct, examine, and accept agent contributions, and show which judgments are your own.

## Lesson 1: Establish the technical basis

### The classical method

A design basis translates intended use into the conditions needed for technical development. It identifies requirements, operating cases, physical conditions, constraints, adopted decisions, and unresolved inputs.

Keep requirements distinct from assumptions and solutions. Northbank requires 18 litres per second at the distribution header under conditions the project must establish. A particular pump model is a possible solution.

The flow value alone cannot establish pump selection: the mechanical engineer needs suction conditions, required pressure, water properties, and relevant operating cases. Other disciplines need different parts of that same basis.

Identify the source and standing of each input. A checked observation establishes what the observer recorded within the survey's limits; a project approval establishes a commitment within the approver's authority.

A04 establishes a checked observation of the existing connection: 600 V, three phase, 60 Hz. It does not establish spare capacity or protection coordination, so keep those limitations with the value.

Manage open inputs at their point of need. State the decision they block, the owner, the required investigation, and the expected resolution. A permitted assumption stays unconfirmed until evidence resolves it.

Use this basis method:

1. Identify the technical decision to be made.
2. List its required conditions and requirements.
3. Locate the applicable sources.
4. Record each source's limitations.
5. Identify unresolved or conflicting inputs.
6. Define the work that can proceed on that basis.

Do not copy an attractive value from an unrelated project, because similar equipment or familiar practice cannot establish the missing conditions.

### What it assumes

The 'What it assumes' passages in this course describe working arrangements for comparison. They are not universal facts about human practice; examine whether they hold in the task at hand.

The classical method assumes that the people who use a basis value have read, or can ask about, its source, so the value's limits travel with it in their understanding. It also assumes that tracing every value to its source and standing is laborious, so projects check provenance when something looks wrong rather than routinely. Northbank shows that the assumption already fails at times: A07 records a design note that cites the legacy schedule without its source note.

### What changes with agents

**Agents use what they are given, as they are given it.** An agent that receives 600 V in a table, without A04's statement that it does not establish spare capacity, protection coordination, or equipment compatibility, can treat the value as settling more than it does. An agent can only use the records it can reach: A07's library index lists the brochure but omits the electrical survey, so an agent that works from that index may not find A04 at all.

**Agents can fill gaps with plausible values.** Asked to proceed with a selection while A02's suction conditions, pressure, and water properties are unresolved, an agent may supply typical values from general knowledge. That is the classical error of copying an attractive value from an unrelated project, made quickly and presented with the same confidence as a sourced value.

**Provenance tracing becomes cheap.** An agent can trace each value in a document to its source and record that source's standing and limits, and it can repeat the trace at every issue. For example, it can trace B01's 480 V to A03, and A03's 480 V to an earlier planning estimate with no field survey reference. A team can therefore check provenance routinely, not only when a value looks wrong. The trace reports where a value came from; whether the source is adequate for the decision remains a judgment for the responsible engineer.

What does not change: agents cannot resolve an open input. The suction conditions, required pressure, water properties, and operating cases that A02 lists still need investigation and the owners who establish them.

### The extended method

Use the same six steps, and keep the basis as a table in which each value carries its source, revision, standing, and limits. Give agents that table as their basis, and require every value in an agent's output to cite its basis entry. Instruct agents to mark a needed value that has no basis entry as unresolved, and not to supply one.

Use agents to trace provenance whenever a basis entry or a dependent document is issued, and have the engineer responsible for the value examine the findings. An agent can list which decisions each open input blocks; the project assigns the owner and the investigation.

The choice of what agents read is a real tradeoff:

| Agents read | Gain | Cost |
| --- | --- | --- |
| The basis table only | Each value arrives with its standing and limits; agents work from one identified reference | An error in the table passes to every consumer, and no agent is placed to notice it |
| The full source records | Agents can check the table against its sources and find errors in it | Agents can pick up an archived or superseded record, such as A03 or A02 Rev 0 under its similar filename |
| The table for production, the sources for a separate cross-check | Production stays consistent, and a differently briefed check can find table errors | Two assignments to brief and examine, and a person to decide between them when they disagree |

## Lesson 2: Allocate ownership across interfaces

### The classical method

An interface is a boundary where contributions interact, and it can involve geometry, loads, power, signals, data, operating behavior, or responsibility.

A named discipline boundary does not define the contribution exchanged across it. “Mechanical to electrical” is too vague, but “Selected motor rating and starting requirements” states something the consumer can use.

Give each interface a supplying owner and a receiving owner. Identify the contribution, its conditions, its point of need, and the examination it needs. Name the integration owner who resolves relationships across the whole result.

| Interface contribution | Supplying responsibility | Receiving responsibility | Needed examination |
| --- | --- | --- | --- |
| Operating cases and changeover definition | Operations with project engineering coordination | Mechanical and controls | Confirm behavior and basis for design |
| Motor conditions and selected configuration | Mechanical and supplier technical contribution | Electrical | Check compatibility, capacity, and protection basis |
| Equipment loads, dimensions, and access | Mechanical and supplier technical contribution | Civil | Check support, foundation, and access implications |
| Isolation and restart arrangements | Relevant disciplines | Operations and maintenance | Examine the connected operating activity |

This is a proposed allocation for the teaching exercise. B03 supplies no accepted owners or required dates, so the project must establish those assignments.

The supplying owner checks the contribution before issuing it. The receiving owner examines whether it meets the stated need. A document's arrival does not establish that the interface is satisfied.

Some design relationships are coupled: motor selection affects the electrical design, and the electrical conditions constrain motor selection. Manage the coupled decision as coordinated work.

Exchange bounded preliminary information when it can support authorized development. Mark its status, uncertainty, permitted use, and what would trigger its revision. Do not let preliminary dimensions quietly become construction dimensions.

The project engineer coordinates resolution, but discipline responsibility stays with the appropriate engineer. Coordination does not grant competence or authority in every technical field.

### What it assumes

The classical method assumes that people sit on both sides of every interface. Each person examines what they send and what they receive, and a vague definition such as “mechanical to electrical” often works in practice because the two engineers fill in its meaning in conversation. It also assumes that keeping an interface schedule current costs a coordinator's time and the participants' meeting time, so the schedule is reviewed at intervals.

### What changes with agents

**Cross-checking an interface list becomes cheap and repeatable.** An agent can compare B03 with each discipline's stated needs and with A01's responsibilities, and report that the list names no owners or required dates. It can also report that the list's needs are coupled: the mechanical team needs the electrical motor conditions, and the electrical team needs the selected motor and starting method. A team can run such a check whenever a contribution changes, not only at a scheduled interface review.

**Ownership does not move.** A01 keeps responsibility for technical contributions with the discipline engineers and gives the project engineer the coordination of interfaces. An agent holds no appointment, so it cannot be a supplying, receiving, or integration owner. An agent's cross-check can report that owners are missing and can draft a proposed allocation, but the project makes the assignment.

**Agent-to-agent exchange removes the informal check.** Suppose, as a teaching assumption, that agents draft both the mechanical contribution and the electrical design that consumes it. Preliminary information can then pass from one agent's output into another agent's input with neither owner examining it, and the conversation that used to fill in a vague definition no longer happens. So a precise statement of the contribution, its status, and its permitted use becomes more important, not less. Preliminary dimensions can become construction dimensions faster, and nobody may notice.

### The extended method

Name people as the supplying, receiving, and integration owners of each interface. Treat agent work on either side as part of the owner's contribution: the supplying owner examines it before issue, and the receiving owner examines it against the stated need.

Put each preliminary contribution's status, uncertainty, permitted use, and revision trigger in every brief that uses it, and check that the agent's output kept them. Route agent outputs across an interface through the owners, unless the owners have agreed a bounded exchange and how they will examine it.

Choose how often to cross-check each interface by how fast its contributions change and what an undetected mismatch would cost:

| Cross-check frequency | Gain | Cost |
| --- | --- | --- |
| At planned interface reviews | Owners examine findings together, with full context | Mismatches spread into dependent work between reviews |
| At each issue of a contributing document | Mismatches are found before dependent work uses them | More findings for owners to examine, many of them minor |
| Continuously, as agent outputs change | Earliest detection | Findings can arrive faster than owners can examine them, and the volume can hide the finding that matters |

Cheap cross-checks change how often you can look. They do not change who decides whether the contributions fit.

## Lesson 3: Review supplier information as project information

### The classical method

A brochure describes a product family. It may leave out the selected model, accessories, ratings, materials, software, and operating cases, and those gaps matter when dependent work needs the actual configuration.

Start the review with the purchase requirements and the identified submission. Compare the submission with the governing basis and the required interfaces, and identify evidence that is absent, conflicting, or insufficient.

Check the submission's provenance, because a supplier may have copied an outdated input. Repair the source relationship as well as the visible value.

Northbank B01 offers 480 V motors copied from A03, which is an archived reference without a field survey basis. A04 records the checked 600 V connection.

This discrepancy rules out an unsupported conclusion about compatibility. The electrical engineer must assess the proposed configuration and the relevant system conditions; neither the project manager nor procurement can declare the mismatch resolved.

Supplier review outcomes need clear meaning. For example, a project can distinguish accepted for a stated purpose, revise and resubmit, and information only. Use the actual organization's definitions.

A review disposition should identify the configuration, the scope reviewed, the findings, the conditions, and the dependent release, because an acceptance stamp without those relationships invites incorrect reliance.

Do not waive technical evidence to keep a delivery slot. Explain the effect on the schedule and seek the appropriate decisions, and continue the supplier questions and independent package preparation within authority.

C03 forecasts a corrected package and delivery timing, but it supplies no corrected technical submission, so the forecast cannot serve as the missing pump curve or configuration list.

### What it assumes

The classical method assumes that people at the supplier prepared the submission, so its completeness and care roughly indicate the effort and checking behind it. It also assumes that a line-by-line comparison of a submission with the basis takes a reviewer's time, so reviewers concentrate on the items they judge critical and read the rest more lightly.

### What changes with agents

**A submission's form stops indicating its checking.** [Course 08](08-project-execution.html#lesson-4-connect-purchasing-risk-and-change) noted that suppliers may use agents too, and used B01's copied voltage to show the kind of error they can make faster. As a teaching assumption, suppose a supplier's agent assembled a submission. Every field can be filled, every table can be formatted, and the submission can still carry a value copied from an unsupported source. A complete-looking submission is not evidence that anyone examined it.

**The team's comparison becomes cheap and complete.** An agent can compare every value in a submission with the purchase requirements, the basis table, and the interface needs, and it can trace each value's provenance. Given B01, A02, A03, A04, and B03, such a comparison can report the voltage discrepancy with the provenance trace that Lesson 1 described, and report that the selected pump curve, declared operating cases, and complete configuration list are absent. The reviewer no longer has to choose which items to read closely in order to save time.

**Comparison is not review.** An agent's comparison establishes whether the submission agrees with the records the agent was given. It cannot establish whether the offered configuration suits the site supply and system conditions; that is the electrical engineer's determination, which A04 leaves open. An agent asked to "complete" a review can also fill a gap, for example by reading curve data from the product family brochure that B01 contains, although a family description does not identify the selected configuration.

### The extended method

Have agents compare and trace the whole submission, and give the reviewer the findings with the records each finding rests on. The reviewer examines the findings and then the questions a comparison cannot reach: suitability for the identified configuration and system conditions, and whether the operating cases the submission must answer are themselves established.

Have the competent person issue the disposition, and state in it what the agent comparison covered and what the reviewer examined. Agents can help draft supplier questions and the deficiency reply; [Course 08, Lesson 4](08-project-execution.html#lesson-4-connect-purchasing-risk-and-change) explains why that reply cannot be an approval. The questions must still name the project's own required contribution.

## Lesson 4: Coordinate the whole life of the result

### The classical method

The installation must support construction, operation, and maintenance, and each of these activities can reveal requirements that component calculations miss.

Construction participants can identify access, lifting, sequencing, connection, and temporary-condition concerns. Operators can identify start, stop, changeover, alarm, and recovery needs. Maintainers can identify inspection, isolation, removal, and spare-part needs.

Invite those participants while change is still practicable. Give them the current basis and a concrete activity to examine, because a general request to “review the design” often produces uneven coverage.

Use activity-based questions:

- How will the equipment reach its installed position?
- What must be available before connection work starts?
- How will an operator recognize the relevant abnormal condition?
- What information supports isolation and restart?
- Can the identified component be removed for maintenance?

Record the observation and the affected requirement or interface, assign its resolution, and confirm the repair with the participant whose need it affects.

Control the relationship between the design and the installed configuration. Identify the equipment, drawings, settings, software, and other items that define the result, and retain authorized changes and examination evidence.

A site substitution can affect several disciplines: a revised motor can change power requirements, controls, dimensions, and protection checks. Handle the substitution through the technical and commercial change arrangements before dependent work uses it.

Avoid duplicate configuration lists with different owners and values. Use an authoritative record with usable references. Document control distributes the right revision, but technical owners establish its content and applicability.

### What it assumes

The classical method assumes that preparing a concrete activity for review costs the project team's time, and that the participants' time is scarce, so whole-life reviews happen at one or two points in the design. It also assumes that configuration lists are kept by people, so a duplicate list with different values appears only when someone takes the trouble to make one.

### What changes with agents

**Preparation becomes cheap, so participants' time can go further.** An agent can prepare an activity walk-through for each construction, operating, and maintenance activity against the current basis, draft the activity-based questions, and pre-check the gaps that the records already show, such as B03's operations need for access, isolation, maintenance, and restart arrangements with no owner. The operators' and maintainers' time can then go to the questions only they can answer.

**The participants cannot be simulated.** An agent can describe how operators typically recognize an abnormal condition. It does not know how Northbank's operators work, what they can see from their usual position, or what has gone wrong at this site before. A01 gives operations the duty to provide operating conditions and the operations lead the acceptance of operating information. An agent's simulated operator review is preparation for operations' review, not a substitute for it. Whole-life coordination remains a relationship among people, and it continues after handover, as Course 10 shows.

**Duplicate configuration lists become cheap.** Each agent assignment that touches the equipment can produce its own configuration list, and the lists can disagree without anyone deciding to make a second record. One authoritative configuration record becomes more important.

**A substitution's effects can be traced fast, and so can its errors.** An agent can list the power, controls, dimension, and protection items that a proposed motor substitution affects; the protection and compatibility determinations remain the electrical engineer's. It can carry the substitution into dependent documents just as fast, whether or not the change arrangements have decided it.

### The extended method

Have agents prepare the activity walk-throughs and questions, and have the construction, operations, and maintenance participants examine them. Invite participants while change is still practicable, as before; cheaper preparation lets you invite them earlier and more often, but each invitation still uses their time, so bring each one a concrete activity and the questions that need their knowledge.

Keep one authoritative configuration record, owned by the technical owners. Give agents that record as a read-only reference, and require any agent output that contains configuration information to cite the record's revision rather than restate a list of its own.

Let agents trace a substitution's effects as soon as it is proposed, and label the trace as an assessment of a proposal. Dependent work adopts the substitution only after the technical and commercial change arrangements decide it.

## Lesson 5: Examine integration and repair connected work

### The classical method

An integrated review examines relationships as well as parts. Start with the approved purpose, current configuration, and identified operating cases. Trace each required interaction across the relevant contributions.

Work in both directions: trace each requirement to its implementation and examination, and trace each implemented feature to an authorized need or decision. This can reveal missing scope and unintended additions.

For Northbank, trace standby behavior from operations' definition through equipment, controls, power, instructions, and planned examination. A complete mechanical drawing alone cannot establish that behavior.

Set the review purpose and competence before the session. Include independent examination where the project or the consequences require it. Identify the exact revisions of the candidate and the sources.

State findings as observations or conclusions, with the grounds that support them, and keep an observed discrepancy separate from its interpretation. State the affected claim, evidence, consequence, owner, and closure evidence. “Please coordinate” does not identify a repairable defect.

After a change, inspect the affected dependencies. Update the technical basis where the meaning changes. Notify consumers through the controlled issue process, and confirm adoption in their actual work.

Re-examine the changed behavior and connected evidence. Preserve valid earlier checks where their basis remains unchanged. Do not repeat every check solely because a document received a new revision.

The integration owner closes a finding based on evidence or on a decision within the decision owner's authority. State whether the response corrects the result, changes the requirement, or limits the proposed reliance.

A disposition does not establish unexamined behavior, and it cannot waive an obligation outside that authority. Moving a finding to another list does not satisfy the requirement.

### What it assumes

The classical method assumes that tracing in both directions across every contribution is laborious, so a project holds integrated reviews at planned points and samples the relationships between them. It assumes that between reviews, errors spread only as fast as people revise documents. It also assumes that when the integrated review finds the contributions consistent, the people who prepared them worked from their own understanding of the sources, so their agreement carries some independent weight.

### What changes with agents

**Tracing becomes cheap and repeatable.** Agents can trace requirements to implementation and back across the contributions whenever any of them changes. How often the project examines integration stops being fixed by the cost of tracing and becomes a design choice.

**Agreement among agent outputs is consistency, not correctness.** Suppose, as a teaching assumption, that agents drafted the mechanical, electrical, and controls contributions from one brief and one basis. An agent cross-check that finds them consistent shows that they agree with each other and with that basis. It does not show that the basis is right. If the shared basis carried A03's 480 V, every contribution would agree on 480 V, and the cross-check would pass. The classical integrated review drew some independence from the separate understanding of each discipline engineer; outputs drafted by agents from a shared brief may not have it.

**Changes ripple at agent speed.** An agent can carry a change through every dependent output quickly. If the controlled issue and the confirmation of adoption still move at the classical pace, dependent outputs on different revisions of the basis can exist side by side, and an output can adopt a proposal before anyone has decided it. Configuration control and the identified basis must keep pace with the agents, or the speed produces inconsistency faster than review can find it.

**Findings are easy to close on paper.** An agent can reword a finding, merge it into another, or mark it addressed in a revised document. None of these closes it. The integration owner still closes a finding on evidence or an authorized decision.

What does not change: the integrated review still needs competent people, the exact revisions of candidate and sources, and the operating cases. Evidence reuse follows the same rule as before: preserve valid checks whose basis is unchanged.

### The extended method

Use agents for frequent consistency tracing, and use the integrated review by people for what consistency cannot establish: whether the shared basis matches the sources and the site, whether the coupled decisions are sound, and whether the connected behavior, such as standby changeover, is defined and examined across the operating cases.

Make every agent output identify the basis revision it used. When a change is decided, issue it as one identified revision, have agents propagate it, and check each affected output against that revision. Sending the instruction does not show that each output adopted it, as Course 08 Lesson 4 noted.

Where agents drafted contributions on both sides of an interface, give the integration check a different basis from the production: brief the checking agent from the source records rather than the production brief, or have a discipline engineer examine the shared basis directly. Where the consequence warrants it, the examiner is a competent person.

Treat the integration cross-checks as a monitoring system. Like an alarm system, it needs a stated purpose, a sensitivity set by consequence, and a person who acts on each alarm. Findings that arrive faster than owners can examine them become a queue, which Course 08 called verification debt, and the important finding can be lost in it.

| Arrangement choice | Gain | Cost |
| --- | --- | --- |
| Frequent agent consistency tracing | Inconsistencies found before dependent work uses them | Findings queue for owners, and consistency can be mistaken for correctness |
| Integrated reviews by people at planned points | Examination of basis, coupling, and behavior with full competence | Errors can spread between reviews when agents change work quickly |
| Checks briefed from source records, not the production brief | Can find an error that the production shares | A second assignment to brief, examine, and reconcile |
| Agents propagate decided changes | Fast, complete adoption of a decision | A proposal or an error propagates just as fast unless the basis is identified first |

Choose the combination that keeps examined integration in step with the rate of change, not the one that runs the most checks.

## Worked Northbank example

The execution plan depends on technical release conditions. Here, the familiar source discrepancies become specific contributions and interfaces that the project engineer must coordinate.

The project engineer prepares a technical release account using A02 Rev 1, A04 Rev 1, B01 Rev 0, and B03 Rev 0.

| Matter | Supported position | Next contribution |
| --- | --- | --- |
| Flow | A02 requires 18 litres per second under unresolved operating conditions | Mechanical and operations establish the hydraulic cases |
| Future increase | A05 proposes 22 litres per second | Impact assessment and sponsor scope decision |
| Supply | A04 observes 600 V, three phase, 60 Hz | Electrical capacity, protection, and compatibility assessment |
| Supplier offer | B01 offers 480 V motors and incomplete selection data | Corrected, identified submission for technical review |
| Changeover | A02 requires confirmation with operations | Define the required behavior; assess A05 separately |
| Civil and maintenance interfaces | B03 identifies needs without owners or dates | Establish interface assignments and points of need |

The account does not conclude that the selected equipment is suitable, because no complete selected configuration exists in the supplied packet. A06 also leaves legal applicability open.

The team can prepare review criteria, an interface schedule, and supplier questions, and it can arrange the missing investigations. Final selection-dependent release, however, needs the required evidence and decisions.

Suppose a colleague says, “The corrected forecast solves the voltage problem.” The project engineer points to C03's status and content: it forecasts package timing and cost, but it does not identify an accepted electrical configuration.

The resulting technical issue stays open, but its owner and point of need become explicit. The schedule receives the real release condition instead of an assumed technical approval.

### The same work with agents

The project engineer briefs one agent to cross-check B01 against A02 Rev 1, A03 Rev 0, A04 Rev 1, and B03 Rev 0, and a second agent to cross-check B03 against each discipline's needs and A01's responsibilities. Each brief identifies the records with their revisions and status, states that B01 is submitted for technical review and not accepted, states that A03 is an archived reference, and asks the agent to cite the record behind every finding and to propose no technical resolution.

The first return reports the 480 V against A04's 600 V, traces the 480 V to A03 and its planning-estimate source note, and lists the absent pump curve, operating cases, and configuration list. The second reports that B03 names no owners or dates and that the mechanical and electrical needs depend on each other.

The project engineer does not accept the returns because they match the classical table. The engineer checks each finding against the cited record, checks that neither agent proposed 600 V motors as a resolution or treated C03 as a corrected submission, and checks that the agents left A02's open operating conditions open. The positions in the table above do not change. What changes is that the team can repeat these cross-checks each time a corrected submission or an interface assignment arrives.

The team divides the examination by A01's responsibilities:

| Contribution | Produced by | Examined by | The examination checks |
| --- | --- | --- | --- |
| B01 cross-check against the basis | Agent | Project engineer, then the electrical and mechanical engineers | Each finding against its record; no compatibility conclusion; open inputs kept open |
| B03 cross-check and proposed interface allocation | Agent | Project engineer, with each proposed supplying and receiving owner | Owners are people with the relevant responsibility; contributions are stated precisely; points of need are supported |
| Supplier questions | Agent drafting | Project engineer, with the discipline engineers | Each question names the project's required contribution and does not imply acceptance |
| Technical release account | Project engineer, with agent drafting | Project engineer, and a reviewer where the project requires independent review | Each position's source and standing, and the decisions still needed |

Suppose, as a teaching assumption, that a later agent run finds the mechanical and electrical drafts consistent with each other. The project engineer asks which basis both drafts used before treating that as integration evidence, because two drafts on one shared basis agree whether or not the basis is right.

## Transfer example: equipment-room renovation

A ventilation unit can meet its catalogue rating and still fail the room's intended activity: electrical load, structural support, airflow paths, controls, access, and maintenance interact.

Assign those interfaces before purchase and construction. Examine the combined operating conditions, and trace a changed unit through every affected contribution.

The specific calculations require competent discipline work, while project engineering makes their relationships and examination visible.

Agents can cross-check the unit's data against the electrical, structural, and controls contributions each time one changes. The owners of those interfaces, the facility staff who will operate and maintain the room, and the judgment whether the combination works stay where they were.

## Practice

Use A01 to A06, B01 to B03, and C03, in the exact revisions supplied in the case.

First, without an agent, compare B01 with A02, A03, A04, and B03, and list each discrepancy and gap with the record it rests on. You then know what an agent's cross-check should return. Work with an agent for every output that follows.

Prepare these outputs:

1. Prepare a technical basis table with sources and unresolved inputs.
2. Assign proposed owners to six Northbank interfaces.
3. Draft five supplier questions that request usable project information.
4. Prepare an integrated review agenda for one construction activity, one operating activity, and one maintenance activity.
5. Trace the effects of a proposed motor substitution across affected work.

Do not invent a selected motor, pump curve, adopted code, or technical approval. Instead, name the work and decisions needed to establish them.

For each output, keep the brief you gave the agent and a short note of what you checked in its return, what you found, and what you changed.

Then complete three further exercises:

1. **Examine an agent's interface entry.** An agent returns this interface entry, invented for the exercise: "Electrical supply to motors: 600 V, three phase, 60 Hz per A04. Motors to be supplied at 600 V. Supplier: electrical. Consumer: mechanical. Status: closed." Explain what the entry converts from an observation into a decision, which owner and examination it omits, and why "closed" is unsupported. Then write the sentence in the brief that would have guarded against it.
2. **Read an agreement.** Suppose, as a teaching assumption, that two agents drafted the mechanical and electrical review sections from one brief that supplied A03 instead of A04, and a third agent found the two sections consistent. State what the consistency check established, what it missed, and what check with a different basis would have found the error.
3. **Design the integration arrangement.** Design how the team would keep Northbank's interfaces examined while agents work on both sides of them: which cross-checks agents run, how often, against which identified basis, who examines the findings, how a decided change is propagated and its adoption confirmed, and where a person must examine the shared basis directly. State two tradeoffs in your design.

## Knowledge check

1. Why is Northbank's flow requirement insufficient for pump selection?
2. What does A04 establish, and what does it leave unresolved?
3. What information turns B03's interface names into usable assignments?
4. Why does a product brochure fail to establish a complete project configuration?
5. How can operations and maintenance review improve design before construction?
6. What must happen after an authorized substitution changes several interfaces?
7. Agents drafted the contributions on both sides of an interface from one brief, and an agent cross-check finds them consistent. What does that establish about the integrated result, and what does it not establish?
8. Agents make interface cross-checks cheap. Why does that change how often integration can be examined but not who owns each interface?
9. Why must configuration control and the identified basis keep pace when agents can propagate a change through connected work quickly?
10. A supplier submission arrives with every field complete. What does its completeness establish, and what does an agent comparison of it against the basis add and leave open?

## Assessed assignment

Prepare a technical coordination package for Northbank's existing scope, working with agents. Include the basis, interface assignments, supplier review position, activity reviews, and a substitution impact route. Add a short account of how you arranged the agents' cross-checks and other work and how you examined it, with the briefs you used.

Then defend the package to your instructor. Your instructor will change premises such as the supplier's offered configuration, the basis that agent outputs shared, or the point at which a substitution was propagated, and ask you to reason through the consequences. Your instructor rates the defense as the teaching guide describes; in text-only study it is rated on changed-premise reasoning with the medium recorded.

Use these seven observable criteria:

1. The basis preserves requirement, observation, proposal, and unresolved-input distinctions, and gives each value its source and standing.
2. Each selected interface has a supplier, consumer, contribution, point of need, and examination. The owners named are people with the relevant responsibility, and any agent work sits within an owner's contribution.
3. The supplier review identifies configuration gaps without inventing suitability or approval, and it distinguishes what an agent comparison established from what a competent person must determine.
4. The activity reviews cover construction, operation, and maintenance relationships.
5. The change route carries consequences into consumers, configuration records, and affected examination, identifies the basis revision each affected output uses, and confirms adoption.
6. The account of the arrangement shows the design: which cross-checks agents run and how often, against which identified basis, who examines each finding, and where a check with a different basis or a competent person is needed. Your own examination record shows what you actually checked in each agent return, what it found, if anything, and what you changed.
7. In the defense, you explain the package's main conclusions and their grounds, show what your examination of the agents' work found, identify which judgments are your own, and reason correctly through the changed premises your instructor poses.

Before the defense, explain one interface to both its proposed supplier and consumer, and revise it until both can identify the same required contribution. Repair defects found during that examination or the assessment, and retain the previous revision and the repair basis.

## Portfolio continuation and reading

Keep your interface package as Portfolio 09, and connect it to Course 08's readiness conditions. Carry the current configuration and open findings into Course 10's assurance plan.

Read management manual (Edition 9) chapter 3, §§4.3–4.6, chapter 5, §§6.1–6.2, and 8.1–8.3 in [References](../references.html). Their dependency, integration, and evidence principles support this course. §5.1 and §5.3 explain why agreement with a shared basis establishes consistency, not the basis's correctness.

The optional NASA technical management readings offer further methods. The Northbank records supply the core basis for the exercise, and NASA's agency procedures do not govern this fictional project.
