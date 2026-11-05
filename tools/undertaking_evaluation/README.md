# Repository change and undertaking evaluation

A local command-line tool for inspecting selected committed repository states,
binding supplied outcome evidence and optional Codex response-usage observations,
and comparing identified trials. It supplies observations and an inspectable
report. The human and the selected evaluation practice determine whether the
state change justifies its effort under the relevant conditions.

## Supported first route

- Python 3.10+ standard library and Git; no Python package installation or network.
- Full immutable Git commit IDs; explicit literal paths, including `.` only when
  the whole committed tree is deliberately selected. No working-tree capture.
- Optional **Codex desktop JSONL `token_usage_record`** events with explicit
  `turn_ids`, `response_id` and per-response `usage` fields. Inspect only records
  authorized for the undertaking. Freeze live records before analysis.
- Supplied outcome assessments with immutable Git-file or local-file evidence
  bindings. The tool verifies that evidence is available and hashes its bytes;
  it does not decide whether the claim follows or confer acceptance.
- Existing host invocation/return mechanisms carry actual trials. This tool does
  not start agents, simulate their results, run arbitrary check commands or
  impose an automatic benchmark at reconciliation.

The schema is intentionally bounded to this route. Other host records, cumulative
usage-only records, working-tree state and unavailable observations are not
silently converted into equivalent evidence.

## Prepare a case

Use `workflows/evaluate-repository-change/WORKFLOW.md` when the selected Library
provides that method, or prepare the same explicit basis under the actual brief.
Keep the case and raw/normalized records **outside the public repository**. This
illustrative JSON uses placeholder revisions that must be replaced with actual
40- or 64-character Git commit IDs:

```json
{
  "schema": "chirality-evaluation-case/v1",
  "case_id": "caller-instruction-repair",
  "trial_id": "baseline-1",
  "question": "Does the repaired instruction describe the actual caller?",
  "hypothesis": "A focused caller reference reduces reconstruction while preserving the result.",
  "conditions": ["The selected caller remains usable", "The explanation matches the checked result"],
  "before": "<full starting commit>",
  "after": "<full resulting commit>",
  "paths": ["workflows/example/WORKFLOW.md"],
  "examination_basis": "<identified outcome-check procedure/version>",
  "environment": "<declared host/model/tool environment>",
  "resource_budget": {"minutes": 10, "enforcement": "instructional, not host-enforced"},
  "configuration": {"brief": "baseline"},
  "outcome": {
    "status": "unknown",
    "summary": "The outcome has not yet been independently examined.",
    "evidence": []
  }
}
```

`hypothesis` is optional for repository-only examination. `configuration` is
optional and reports the selected intervention without treating it as controlled
experiment evidence. Resource and environment values are caller declarations;
the tool does not enforce or independently establish them.

Outcome `status` is `established`, `not_established` or `unknown`. Both non-unknown
statuses require evidence. A `git` binding identifies a file at a full commit:

```json
{"kind":"git","path":"docs/check-basis.md","revision":"<full commit>","claim":"The selected examination basis"}
```

A `file` binding identifies an actual local observation/check result:

```json
{"kind":"file","path":"checks/result.json","claim":"Observed result under the stated check conditions"}
```

Relative file paths resolve beside the case file. The report retains hashes and
the supplied claims, not file contents or absolute evidence paths. A matching
hash establishes identity, not meaning or independence of the evidence. Retain the
exact case file and its named source/evidence inputs privately alongside the
report. Written reports include informational relative `input_locators` to the exact
case (or original baseline/variant reports), paired with their source hashes.
They resolve from that original report’s directory and are escaped text, not
active links or executable paths. The retained case then supplies the authorized
evidence discovery route; a hash alone cannot supply that location. An embedded
report’s locators remain relative to its original file, not the comparison file. Do not discard those inputs while the findings need to remain inspectable.

To include actual effort observations, add:

```json
"codex_jsonl": {"path":"frozen-session.jsonl","turn_ids":["<actual selected turn ID>"]}
```

Choose the turn from the actual session/undertaking relationship. A whole session
may contain several unrelated undertakings. The tool does not discover sessions
or infer which work a turn concerns. Unknown or incomplete coverage remains a
limit on any effort comparison.

## Inspect and compare

From the selected Library root:

```sh
python3 -m tools.undertaking_evaluation inspect \
  --case /authorized/private/case.json \
  --repo /authorized/project \
  --output /authorized/private/inspection-1

python3 -m tools.undertaking_evaluation compare \
  --baseline /authorized/private/baseline/report.json \
  --variant /authorized/private/variant/report.json \
  --output /authorized/private/comparison-1
```

Output parent directories must exist. Each output directory must be new, outside
Git working trees, separate from the selected inputs/repository and not traverse
symlinks. The tool creates `report.json` and self-contained `report.html` with
private filesystem modes where the platform supports them. It refuses replacement
of an existing destination. It changes no source, Git state, instruction or
acceptance record. On a write failure, inspect the reported destination before
retrying; a partially created directory is not silently removed or overwritten.

Open the HTML locally. It renders all supplied text as escaped text, contains no
scripts or remote assets, and provides the complete report data for inspection.
The JSON can be consumed directly by a bounded evaluator. This is a local-output
boundary, not a host-enforced sandbox against other processes with access.

## What the result establishes

Repository observations bind full before/after commits and tree IDs. Git replacement
objects are disabled and inherited `GIT_*` repository/configuration overrides are
cleared for these read-only operations so they cannot silently substitute source. Each selected
file reports its Git object identity and mode before/after. Added, removed,
modified and unchanged are source observations. Renames appear as removal and
addition; symlink blobs are observed without following their targets. A selected
path missing from both states is rejected rather than reported as no change.
The working tree, untracked files, external dependencies and behavior are outside
this observation. Findings about behavior or value need their own examination.

Codex usage sums only distinct per-response `usage` observations in selected
turns. Identical duplicate response records are counted once; conflicting duplicates
fail rather than averaging contradictory evidence. `turn_token_usage`,
`thread_token_usage`, `event_msg/token_count` and all raw message/tool-output
bodies are ignored. Missing/invalid rows or fields remain explicit. No input,
output, cached-input or reasoning category is synthesized from another.
Categories may overlap and are never added to manufacture a new total.

The first/last observed response timestamps supply only an **observation span**.
They do not establish active effort, elapsed undertaking duration or concurrent
worker time. Monetary cost, human attention, retry meaning and causal attribution
are unknown in this route. A source hash binds the frozen bytes consumed;
ongoing mutation during the trace read causes failure.

Comparison inputs are supplied reports. Their schema, internal consistency and
comparison-basis digest are checked, but the comparison does not re-read the
original repository or trace, authenticate the producer, or prove that a report
has not been deliberately fabricated. Inspect its retained input basis for those
claims; do not use these reports as an untrusted reward oracle.

Comparisons require matching declared case ID, question, starting commit, selected
paths, conditions, examination basis, environment and budget, plus distinct trial
IDs. Differences yield `comparison_limited`; matching metadata yields
`declared_basis_matches`, not proof of control, statistical significance or a
causal improvement. Configuration and resulting state differences remain visible.
Observed token deltas are descriptive partial-record differences only, not a
quality ranking or a winner. Failed trials and repairs must remain in the selected
case's records; selecting successful trials alone narrows the resulting claim.

All reports remain **private by default**, even without raw transcript bodies:
source paths, supplied claims and aggregate observations can still be sensitive.
Publication requires separate examination and authority. This tool does not
perform clearance. Public tests use handcrafted fixtures only.

## Failure and recovery

Exit 0 means the requested report files were written; it does not mean the outcome
is successful. Exit 2 means an unavailable/invalid input, ambiguous identity,
unsupported source shape or write condition prevented completion. Error messages
avoid raw input content and host paths. Record-level malformed Codex input is
reported as incomplete coverage rather than silently discarded; conflicting usage
for the same response is a failure. Unknown outcomes and limited comparisons can
be valid reports. Never interpret them as passing criteria.

## Verification

```sh
python3 -m unittest tools.undertaking_evaluation.test_evaluation -v
```

The tests exercise Git state/source selection, immutable evidence, missing inputs,
partial and malformed usage, duplicate/conflicting counters, unsupported cumulative
records, comparison differences, HTML escaping and fresh-output/private-source
boundaries. These fixtures do not establish compatibility with every host export
or qualify a production benchmark. Actual-route and pilot evidence belongs in
the owning deliverable's Work, with its source and limits.
