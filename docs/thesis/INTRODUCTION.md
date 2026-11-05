# Purpose, Participation, and Judgment

**An introduction to the Chirality thesis**

Work begins with something that matters. A person meets a need, describes it
for the first time, and tries to act. As the work reveals what was overlooked,
the description changes. Other people contribute. Tools make some actions possible and some consequences
visible. What counts as a useful result depends on the work and on the world in
which the result will be used.

AI agents enlarge all of this. They can investigate a question, interpret
sources, develop alternatives, operate software, and see repairs through over
long stretches of work. Their contribution can change what a person has time to
consider and what a small team can attempt. It also changes the demands on the
environment around the work: more output can bring more useful inquiry, more
unexamined assumptions, or both. The important question is how that added capacity becomes
purposeful work whose reasons and consequences people can still understand and
correct.

This thesis examines that question through the shared methods of Chirality and
the development of two applications. The App supports workflow authoring;
SWBPIPE supports piping design. Their cases test whether the methods preserve
meaning, evidence and responsibility when used in software. Experience can
change an operation, a method, or the understanding of what the work is for.

## One undertaking, three perspectives

The thesis asks what should guide
human–agent work, and why the means of doing it must stay open to revision. Its
concern is broader than a set of repository instructions. Any arrangement for
work embodies choices: what participants can perceive, what they can do, what
they must examine, and who can make a commitment that matters. Roles, methods,
tools, and artifacts put those choices into practice, and they can be changed
when experience shows that they no longer serve their purpose.

This is the **normative** emphasis. It names commitments and gives reasons for
them: useful work, reasons that can be inspected, authority that can be
understood, a person who answers for the work, and attention to consequences.
Applicable obligations constrain the arrangement, but the particular mechanisms
chosen remain design hypotheses. A requirement to preserve responsibility does
not determine a unique hierarchy of agents, sequence of approvals, or format for
records.

The [App case](08_implementation.md#851-operative-perspective-the-app) asks how
that guidance becomes actionable within software. A
general-purpose agent needs a meaningful connection to the application's objects
and operations: a reference must point to the right object, a proposed change
must apply to the version that was examined, and a reported outcome must
distinguish what happened from what was only intended. The person must be able
to understand and direct that activity.

This is the **operative** emphasis. The App, which is built for authoring
workflows, makes a useful first example because its subject is the method of
work itself. A person and an agent can develop a method through conversation,
try it, examine the result, and make it available for other work. The
application can help keep what was learned while leaving room for circumstances
that the method's author did not foresee. It must also justify the effort that
its own machinery demands.

The [engineering case](08_implementation.md#852-evaluative-perspective-piping) asks
what this arrangement can establish once it enters an engineering practice.
SWBPIPE is one example of software through which agents take part in domain
work. Its models describe proposed physical arrangements, its calculations depend
on analytical idealizations, and its results affect choices whose consequences
reach beyond the application. A successful operation, a verified numerical
result, and an adequate design are three different achievements.

This is the **evaluative** emphasis. Engineering gives the shared argument a
subject that can push back on its assumptions. A model can be internally
consistent and still miss a relevant condition. A calculated improvement can make
construction or maintenance harder. A common interface can preserve a software
operation while losing part of what it means in practice. Findings like these
help assess both the domain application and the shared arrangements that were
meant to support it.

The three emphases are not separate territories. Root needs evidence about its
own methods. The App makes normative choices in its defaults and permissions.
Piping depends on workable operations, and on values that cannot be read from a
results table. The cases examine the same relationships in different settings.

## Four questions throughout

Ontology, epistemology, praxeology, and axiology give the inquiry a second frame,
which applies within each of the three perspectives.

**Ontology asks what the work consists of and how its parts relate.** A physical
support, the model object that represents it, a proposed change, an applied
operation, and an acceptance are different things, and the difference matters
when someone acts. A file or field can represent an object or an act without
establishing that the represented condition holds.

**Epistemology asks what supports understanding and a claim.** A source has a
scope, a calculation has assumptions, and an observation concerns particular
conditions. Evidence can support an inference, contradict it, or leave the
question unsettled. The presence of a citation, a passing test, or an approval
record cannot settle all of these relationships.

**Praxeology asks how intent becomes usable work.** Inquiry, production,
examination, repair, and integration have to connect. A contribution helps the
work when it reaches a use that keeps its relevant meaning intact. Continuing
ownership, suitable tools, and recoverable outcomes can support that connection,
and their value is assessed by the activity they make possible.

**Axiology asks what matters, to whom, and with what consequences.** A candidate
result may serve one purpose while frustrating another. Applicable obligations
and adopted constraints have to be told apart from preferences that allow
tradeoffs. Attention, delay, maintenance, and lost opportunities are also costs
of a method. Values are already involved in deciding what deserves
investigation, before any final comparison of results.

The four questions correct one another. A new consequence can show that the
model left out an important relation. That omission can change the
evidence needed and the action worth taking. A costly examination can still be
justified when the possible failure is serious; an unnecessary control can
divert attention from that same failure. No single perspective gives a complete
account of the work.

## Iteration as learning

Iteration gives these relationships continuity. An outcome may call for a repair
within an established method. It may also show that the method was answering the
wrong question, or that its objects and criteria need revision. The participants
must be able to tell these cases apart and act within the relevant authority.

Learning takes more than repeating a cycle. A limitation, once discovered, must
affect the next relevant action. A corrected method must reach the place where it
is used. A useful numerical reference must stay available when the engine
changes. And when an implementation is replaced, the earlier code, its failures,
and its successful interactions can hold lessons that its written requirements do
not fully capture.

Iteration connects the shared methods and their applications. A
difficulty in SWBPIPE can expose a weakness in the App's account of perception or
action. That weakness can require a revised shared method. A burden in that
method can prompt a fresh examination of the normative reason for requiring it. A
finding gives grounds to reconsider; changing a reserved commitment remains with
the person who has the authority to make it.

## Knowing, reckoning, and judgment

The shared account depends on a distinction between recorded information and
situated knowing. Sources, models, methods, and explanations make material
available for understanding, but they do not contain everything a participant
brings to the work. In this framework, *knowledge* names a knower's situated
achievement, and it can be incomplete or mistaken. Evidence and criticism matter
because that understanding stays answerable to its subject and open to revision.

Agents contribute **reckoning**: investigation, inference, planning, criticism,
comparison, and adaptive action. The term covers substantial initiative and
reasoning. **Judgment** names the person's situated, committed engagement with
what the work means, what matters, and what they will stand behind. It shapes how
the work is framed, which evidence is chosen, how an unexpected result is handled,
and whether reliance is accepted. An approval can express that engagement without
capturing all of it or proving it.

The allocation of responsibility in this thesis applies to the professional and
institutional setting they examine. More capable agents can change what
delegation and supervision are suitable. Capability alone does not transfer the
person's commitment or supply a new decision right. The
[shared vocabulary](glossary.md) keeps these distinctions available throughout
the manuscript.

## What the reader can expect

The thesis combines a philosophical account, architectural proposals, and a
development case, and each has a different standing. Commitments state an
adopted orientation. Design hypotheses propose ways of serving it. Observations
supply evidence about identified implementations and circumstances. The
manuscript does not claim a controlled productivity result or a completed
demonstration of every proposed integration.

The original implementation observations keep repository basis
`a602024416ace9652f61bb2043889c307fd4e09d`. Chapter 8 separately identifies the
October 30 evidence extension: the App's traced redevelopment and native-use
record, and selected stored SWBPIPE comparisons. That extension establishes
observed continuity and useful evolution while retaining the original subjects
and limits of earlier evidence. Human purpose, judgment and steering are
foundational to the undertaking examined. Regulatory discussion keeps its
separately identified source editions and interpretive limits. The
[historical appendix](appendix_e_development_history.md) explains the development
behind the argument. The [philosophical conjecture](appendix_d_framework_s.md)
records a deeper orientation; the practical claims do not require accepting it.

The chapters develop the account of purpose, knowing, responsibility and
revisable methods. Chapter 8 examines application cases and their evidence.
The [worked example](WORKED_EXAMPLE.md) follows an illustrative design inquiry.
The [conclusion](CONCLUSION.md) returns to what the evidence supports and what
further experience must test.
