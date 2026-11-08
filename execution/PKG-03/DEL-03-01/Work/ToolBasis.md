# Existing tool support and current limits

For the accepted R18/A9 increment, see [Evaluation extension](#evaluation-extension).
Earlier case/basis statements below retain their recorded subjects and limits.

Maturity: selected operations have bounded evidence; full toolkit fulfillment is
not established. The adjacent ScopeOfWork defines the utility claims. The
accepted decomposition basis is `fd847ac9ac68250b2f35d2e9c0087c16e86b510a`.

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

The explicit `--current` scaffolding and checks separate structural preparation
from ScopeOfWork authoring. Accepted decomposition §6.1 identifies PR #1779's
checked source and verification, applicable to unchanged preservation, collision
and legacy compatibility behavior. Actual locality setup and authored-contract
checks support the selected use, not every failure case or product criterion.
No phase directories, lifecycle files or blank contracts are required.

Preparation requires Python and PyYAML; the documented `PYTHON` override selects
an interpreter when the default lacks PyYAML.

## Query use and an instruction discrepancy

`tools/deliverables/cli.py` and its README require `--project`. The corrected
`workflows/dependency-extract/resources/tools.md` states the same requirement;
its examples already supplied the argument. Consumer-local adaptations retain
their own contracts.

Queries read live declarations, including uncommitted files, and report source
observations and unknown suitability. They do not execute pointers, evaluate
conditions or accept work. Cycles require a use-specific reading; a named query
does not require a global DAG.

## Remaining examination

Use maintained caller contracts and fixtures before any utility change. Reuse
applicable prior evidence and exercise only changed or uncovered claims. Named
external compatibility (Q-04) and publication/update claims (Q-05) still need
their own source bindings. No file-only adapter, namespace repair or bespoke
service has been selected. The native needs distinguish actual metadata/caller
inputs from these conditional claims.

## Post-60 usage-contract examination

At `547e7d7f833f9bec351f7a034bddd7c1a37db15a`, examination covered preparation
and current-locality helpers, ScopeOfWork validation and checklist callers, and
the runtime guide's package selection and brief normalization. Selected setup
and ScopeOfWork sources matched PR #1779's checked basis, so its applicable
preservation and collision evidence remains relevant. The selected query use
preserved distinct input conditions, unknown bindings and suitability limits.
Source-qualified preparation, project-setup and scope-of-work selections resolved
their requested resources; scope-of-work required its documented `scope_path`.
Selection without an authorized brief supplied no write capability.

`normalize_brief.load_brief` imports PyYAML even for JSON-only `--brief` input.
A Python `-S` call with an empty JSON object failed at that import before
assignment validation. The runtime guide declares this dependency, traceback
failure and direct-reading fallback limits; executable behavior was unchanged.

For archive use, retain the helpers and imports, role/registry/catalog metadata,
selected package resources, applicable legacy maps, `common.py` and the
ScopeOfWork ID catalog. Preparation requires zsh, Python, PyYAML and suitable
platform/filesystem support; native queries also require Git and HEAD. These
requirements do not establish cross-platform qualification or Git-free queries.

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
