---
name: thesis-readme
description: Purpose, Participation, and Judgment.
metadata:
  kind: explanation
  surface: reference
---
# Purpose, Participation, and Judgment

**The Chirality thesis**

This thesis examines how people direct work with AI agents, how software
supports that work, and how its results can be examined. Chirality App and
SWBPIPE provide application cases within the argument. They are not separate
manuscripts.

Start with the [introduction](INTRODUCTION.md) (Chapter 1), then follow the
chapters below.
The [worked example](WORKED_EXAMPLE.md) applies the argument to an illustrative
engineering task. The [conclusion](CONCLUSION.md) (Chapter 10) brings the findings and
open questions together. The [glossary](glossary.md) defines the terms.

## Research question

What makes agent capability into purposeful, accountable work, and why should
its supporting environment develop through revisable roles, methods, tools and
artifacts?

## Warrant status

This is explanatory, agent-drafted research under the owner's direction. It is
nonbinding and does not establish regulatory endorsement, professional
acceptance or a controlled productivity result. The conversation, repository
instructions and adopted product commitments still govern development.

## Reading the thesis

| Chapter | Subject |
|---|---|
| [Front matter](00_front_matter.md) | Abstract, author's note and contents |
| [1. Introduction](INTRODUCTION.md) | Question, perspectives, contribution and limits |
| [2. Literature review](02_literature_review.md) | Precedents and scope of comparison |
| [3. Philosophical framework](03_philosophical_framework.md) | Four perspectives; reckoning, judgment and situated knowing |
| [4. Architecture](04_architecture.md) | Responsibilities, artifacts, queries and host boundaries |
| [5. Epistemic architecture](05_epistemic_architecture.md) | Evidence, uncertainty, interpretation and reliance |
| [6. Professional practice](06_professional_practice.md) | The bounded professional-practice interpretation |
| [7. Systems engineering analysis](07_se_design_analysis.md) | Design methods, contributions and limits |
| [8. Evidence and evaluation](08_implementation.md) | Observed implementation and limits of the findings |
| [9. Discussion](09_discussion.md) | Tensions, generalisation and evaluation |
| [10. Conclusion](CONCLUSION.md) | What the case supports and what remains open |
| [Appendix A](appendix_a_invariant_catalog.md) | Historical controls and present interpretation |
| [Appendix C](appendix_c_apega_mapping.md) | Regulatory mapping and limitations |
| [Appendix D](appendix_d_framework_s.md) | Bounded philosophical conjecture |
| [Appendix E](appendix_e_development_history.md) | Development history, retired arrangements and lessons |
| [References](references.md) / [Glossary](glossary.md) | Sources and terms |

[The Chirality Framework](CHIRALITY_FRAMEWORK.md) offers a short path through
the conceptual account. It can be read on its own or used to revisit the
argument; it is not a required additional volume. The former standalone
Systems Engineering Design Analysis summary and the separate numbered
introduction and conclusion chapters were consolidated into Chapter 7,
INTRODUCTION.md and CONCLUSION.md on 2026-11-04. There is no Appendix B; current role instructions are indexed
in [AGENTS.md](../../AGENTS.md).

## Source basis and historical editions

The original implementation account retains Chirality revision
`a602024416ace9652f61bb2043889c307fd4e09d` (October 10, 2026). The
[dated evidence extension](08_implementation.md#81-subject-and-evidence-basis),
examined October 30, follows App redevelopment through its October 14–16 native
walkthrough and examines stored SWBPIPE comparison records. It identifies App
revision `032725d32b67e117b8e1fb2b5fa9aa47b30de12e`, SWBPIPE revision
`bc9f7961acee72441ec06c104ed97d4f1c77faa4` and the earlier source subjects
separately. It reports documentary/source examination and checks of stored
comparison evidence, not fresh product or solver runs.

Regulatory discussion keeps its identified July 2, 2026 basis and source
editions. Older editions remain in the Git history of the private `sgttomas/chirality` repository; the
[development history](appendix_e_development_history.md) distinguishes dated
observations, owner testimony and the October 30 synthesis.

App v4's [foundation copy](https://github.com/sgttomas/chirality-app/blob/main/foundation/thesis/README.md)
retains its historical source basis unchanged. January–April history comes from
the owner's account; surviving Git history begins with the migrated May snapshot.

## Maintained source

This directory is the single maintained thesis manuscript. The App and SWBPIPE
repositories refer to it. The website publishes a snapshot of a named revision;
it is not another authoring source.

The October 30 revision incorporates the former application manuscripts' lessons
about workflow trials, interruption, model inputs, operation consistency and
numerical limits into Chapter 8. Their earlier full texts remain in Git history
at `sgttomas/chirality-app@40415db3` and `sgttomas/SWBPIPE@2fcd0b526`.
The App's frozen `foundation/thesis` is an earlier evidence snapshot, not another
maintained manuscript. Historical observations retain their identified basis.
The October 30 evidence extension makes the longitudinal finding explicit:
working software, preserved core meaning through redevelopment, functional
extensions and repairs show what the method achieved in this one
human-directed, agent-executed undertaking. A single case without a comparison
condition, resting partly on private evidence, does not establish efficacy
beyond it ([§9.2.1](09_discussion.md#921-what-the-case-shows-and-comparative-questions)).
Human steering is foundational throughout.
