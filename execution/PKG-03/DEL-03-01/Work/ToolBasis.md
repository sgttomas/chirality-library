# Existing tool support and current limits

For the accepted R18/A9 increment, see [Evaluation extension](#evaluation-extension).
Earlier case/basis statements below retain their recorded subjects and limits.

Maturity: setup-use assessment, not full toolkit fulfillment. The adjacent
ScopeOfWork defines the utility claims. Source basis:
`fd847ac9ac68250b2f35d2e9c0087c16e86b510a`, plus this setup's local declarations.

## Pending Root adherence-result interface

Root's DEL-04-02 will propose the machine-readable adherence result required by
its R-24. The Library consumer interface is the output contract in
`workflows/evaluation-protocol/WORKFLOW.md` (Output structure, Report content
contract, Outputs and QA expectations), with `resources/contract.md` (Artifacts
and schemas), `resources/brief.md` and `resources/checks.md` kept consistent.
`evaluation-report` and `tools/evaluation/` remain available; this preparation
does not change their formats or claim adherence-format integration.

The proposed result must identify the deliverable, checked ScopeOfWork and code
revisions, per-acceptance-criterion met/not met/unknown verdicts with evidence,
checking session and date. Root will read the saved result through Git at an
identified revision. Exact schema, filename, revision conventions and evidence
locators remain for Root to propose and the two projects to agree; none is
implemented or fulfilled by this note.

The current workflow quarantines writes under the authorized `_Evaluation/`
targets and treats deliverables as read-only subjects. R-24 instead requires
this result in the checked deliverable's `Work/`. A later agreed amendment must
explicitly authorize that narrow result-file write in the output contract and
brief, while keeping the checked ScopeOfWork, code, commitments and other
subject material read-only. Do not infer permission from a schema or enlarge
the brief's write boundary. Preserve accepted evaluation basis/toolbelt,
evidence-linked findings, unknowns, invalid-return handling and optional scoring
only under an accepted rubric; a result file does not confer acceptance.

Root format production and the Library contract amendment remain a named
downstream input. They do not block unaffected holding-removal preparation and
are not a setup completion claim.

## Current setup path

PR #1779 supplied the explicit `--current` scaffolding and checks, separating
structural preparation from real ScopeOfWork authoring. The accepted decomposition
§6.1 identifies its checked head, equal-tree merge and reported verification.
That evidence remains available for unchanged preservation/collision/legacy
compatibility behavior; no new implementation is needed merely to populate this
deliverable.

Agent 0 used that route to prepare all seven numeric localities. The Type 2
authors then exercised the authored-locality and contract checks on actual
ScopeOfWork files. These uses establish the selected setup behavior, not every
failure case, query capability or product criterion. No phase directories,
lifecycle files or blank contracts were required.

Some author sessions resolved a Python without PyYAML; the documented `PYTHON`
override to an existing Python 3.13 environment with PyYAML enabled the locality
check. No installation or tool change was needed. Portable instructions should
declare the dependency and interpreter selection, not a machine-specific path.

## Query use and an instruction discrepancy

`tools/deliverables/cli.py` requires `--project`; its README agrees. During setup,
`workflows/dependency-extract/resources/tools.md` incorrectly described an App v4
default. The owner-approved correction updates that sentence to state the shared-library
CLI's required argument. Its examples already supply the argument, so the change
alters neither invocation nor executable behavior. Consumer-local adaptations
retain their own contracts. The owner approved this two-file correction with “you may.”

The queries read live declarations, including uncommitted files. They report
path/source observations and unknown suitability; they do not execute pointers,
evaluate conditions or accept work. Native cycles are allowed and require a
use-specific reading. A named query is not a requirement for a global DAG.

## Remaining examination

Use maintained caller contracts and fixtures before any utility change. Reuse
applicable prior evidence and exercise only changed or uncovered claims. Named
external compatibility (Q-04) and publication/update claims (Q-05) still need
their own source bindings. No file-only adapter, namespace repair or bespoke
service has been selected. The native needs distinguish actual metadata/caller
inputs from these conditional claims.

## Post-60 usage-contract examination

At `547e7d7f833f9bec351f7a034bddd7c1a37db15a`, a bounded contributor examined
three actual instruction/caller connections: preparation to current-locality
helpers, ScopeOfWork INIT/VERIFY to format validation/checklist, and the runtime
guide to package selection/brief normalization. Source comparison confirmed
the selected preparation and ScopeOfWork implementation/caller files unchanged
from PR #1779's checked basis. Its existing preservation/collision evidence,
actual seven-locality setup and F-02's focused resolver tests remain applicable;
no fresh scaffolding fixture was needed merely to repeat them.

Fresh calls derived DEL-03-01's seven ordered criteria without migration flags
or site packages and found no boundary-owner failure. Native check/neighborhood
reported seven localities and 61 needs without structural errors. Distinct
DEL-04-01 input conditions, unknown source bindings and suitability limits were
preserved. These are observations about this use, not all possible query claims.

Source-qualified preparation, project-setup and scope-of-work selections resolved
their requested resources. Scope-of-work selection required its documented
scope_path binding. No authorized brief meant no write targets or write capability;
selection did not authorize execution. Retirement and reflective-role evidence
from PR #1785 was reused after confirming those sources unchanged.

One real usage-contract gap was found: normalize_brief.load_brief imports yaml
unconditionally, so even JSON-only --brief input needs PyYAML. A controlled
Python -S call with an empty JSON object failed at that import before assignment
validation. This isolates dependency behavior, not a substantive brief failure.
The runtime README now proposes declaring that dependency, its current traceback
failure and the limits of direct-reading fallback. Executable code needs no
change for this finding. The owner approved this correction and its evidence in PR #1787.

For archive use, retain the helpers and their imports, role/registry/catalog
metadata, selected package resources, applicable legacy maps, common.py and the
ScopeOfWork ID catalog. Preparation requires zsh/Python/PyYAML and suitable
platform/filesystem support; native queries also require Git and HEAD. These
requirements bound the source-archive examination; no cross-platform qualification
or Git-free native-query implementation is inferred.

The complete source-candidate examination at `7c334bf5cb529a814e0f96f68bc8d9500b15cdd5`
subsequently exercised selected operations from an ordinary extracted archive.
[ConsumerBasis](../../../PKG-05/DEL-05-01/Work/ConsumerBasis.md#complete-library-source-candidate-after-the-60-decision)
records the preserved source identity, successful role/resource selections,
current validation/scaffolding/read-only normalization, actual rejected cases
and Git-free query fallback. This is selected standalone-use evidence; historical
and specialized holdings are not all behaviorally qualified by tree correspondence.

## Evaluation extension

This section records the original R18 allocation. Its accepted historical
standing and source recovery are identified in
[DEL-03-02’s current evaluation basis](../../../PKG-03/DEL-03-02/Work/EvaluationBasis.md#holding-transfer-and-current-availability).

The owner accepted SCA-20261101-UNDERTAKING-EVALUATION, including its audited
corrections, on 2026-11-01 against `e157d14910e84cf149f2ead524d585467b18e0f7`. PRD R18/A9 allocate the optional
work-and-repository evaluation capability. The state change and the conditions
under which it justifies effort are the evaluative subject; traces of work are
supporting observations. No tool implementation, host qualification or product
release is established by this scope amendment.

DEL-03-02 owns this selected tool contribution; DEL-03-01 continues to own its
existing scaffolding, validation and query utilities. Initial Q-02/TBD wording
in this contract records the earlier unselected tooling basis. The accepted
successor selects only R18/A9 and SOW-0034/0035; all other tooling remains
conditional. Existing toolkit evidence does not qualify a host adapter or
benchmark comparison.

The event recorder and governed-run runtime analyzer are possible reusable inputs,
not a demonstrated end-to-end workbench. Before changing an existing utility for
this use, bind the actual caller interface and its needed behavior, then examine
only the affected contract and checks. No existing utility change is selected
merely because the new contribution exists. The present setup uses the maintained
current scaffold, SOW validator and native-needs queries under Python/PyYAML.
