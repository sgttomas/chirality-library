# P6 — Upstream-ID citation convention for INIT contracts (request item 7)

**Disposition:** ADOPTED-PROPOSED (AMENDED — one of the two forms the request
proposes is **not currently safe**)
**Basis:** VERIFIED by executing `tools/scope_of_work/common.py`'s live ID
regex against both citation forms in this run. The B2 wave evidence
(DEL-02-07 CLM-007, DEL-01-01 CLM-009 collision) is ASSERTED-UPSTREAM.

## 1. The gap

Neither `SKILL.md` nor any companion says how an INIT-authored contract cites
an upstream deliverable's local IDs. A bare `DEL-01-06-REQ-004` is scanned as
an unresolved *local* `REQ-004`, or collides with the authoring contract's own
`REQ-004`.

**Mechanism, VERIFIED.** `common.py` line 63 compiles the reference regex to:

```
\b(?:AC|AX|CLM|CON|OUT|REM|REQ|TBD|VER)-\d{3}\b
```

`DEL` is not in `id_catalog.json`'s definitions, so a `DEL-` qualifier is not
consumed by the alternation, and the separator (`/` or `-`) is a non-word
character, so the leading `\b` matches cleanly at the prefix letter. Executed:

```
'DEL-01-02/REQ-003'                -> ['REQ-003']
'DEL-01-02-REQ-004'                -> ['REQ-004']
'See DEL-07-11/AC-004 and REQ-003' -> ['AC-004', 'REQ-003']
```

Every qualified form is silently truncated to its bare local tail and recorded
in `SowDocument.references`. Line 238–240 then reports it as an "unresolved
local reference", `resolve_production_format` marks the format INVALID
(line 362), and every downstream tool that gates on `resolution.valid` refuses
to run — `derive_review_checklist.py:172`, `report_scope_of_work_parity.py:145`,
validate, and render.

**The contract has no way to express a cross-deliverable reference.**

## 2. Amendment to the request

The request offers the B2 wave's de facto convention as two options:

(a) quote upstream text inside §4-provision blockquotes, plus an explicit
    upstream-context carve-out sentence; **and/or**
(b) a `DEL-NN-NN/REQ-NNN` qualified form.

**(a) works. (b) does not — not today.** As executed above, the slash form is
extracted exactly like the bare form and fails validation identically. Blessing
it in `SKILL.md` would document a convention the tooling rejects.

So the choice is:

- **Option 1 (contract-only, recommended now):** adopt (a) only. Zero tool
  change, lands immediately, matches what the 12 accepted wave contracts
  already do.
- **Option 2 (contract + tool):** adopt (a) and (b), and change `common.py` in
  the same tranche so the qualified form is recognized. Strictly better
  long-term; needs a tested regex change and a re-validation of every accepted
  contract.

## 3. Option 1 — proposed exact text (contract only)

ADD to `skills/scope-of-work/SKILL.md`, in the Non-negotiable constraints block
(after line 66, the "Never integrate the evidence-rich migration candidate"
bullet):

```
- Cite an upstream deliverable's local IDs only inside a blockquote. Local-ID
  syntax is deliverable-scoped: a bare `REQ-004` in contract prose always means
  *this* contract's `REQ-004`, so an upstream ID written in own-voice prose
  either collides with a local definition or scans as an unresolved local
  reference. Quote the upstream text in a `> ` blockquote and add an explicit
  carve-out sentence — "ID-shaped text inside this quotation is upstream source
  context, not a local definition or reference" — naming the upstream
  deliverable in own-voice prose around the quotation.
```

ADD to `skills/scope-of-work/QA_CHECKS.md` as item 19 (after line 32, before
the closing clause):

```
19. Every upstream deliverable's local ID appears only inside a blockquote with
    an explicit upstream-context carve-out; no own-voice prose carries an
    ID-shaped token that is not a local definition or local reference.
```

**Why the blockquote works, VERIFIED:** `common.py` line 186 blanks any line
matching `^ {0,3}>` before ID extraction, so IDs inside blockquotes are never
collected as definitions or references. `derive_review_checklist.py:44-45`
applies the same rule.

**One caveat that must be stated in the contract if adopted:** the exemption
regex is `^ {0,3}>` — a blockquote indented **4 or more** spaces (legal
Markdown for a quote nested in a list item) is **not** exempt and its IDs are
extracted. VERIFIED. Recommend appending to the constraint bullet:

```
  The blockquote marker must sit at column 0–3; a blockquote indented four or
  more spaces is not exempt from ID extraction.
```

## 4. Option 2 — the tool change, if the owner wants the qualified form

A left-context guard on the reference regex, `common.py` line 63:

```
return re.compile(rf"\b(?:{prefixes})-\d{{{self.width}}}\b")
```

becomes

```
return re.compile(rf"(?<![-/\w])(?:{prefixes})-\d{{{self.width}}}\b")
```

A negative lookbehind for `-`, `/`, or a word character means
`DEL-01-02/REQ-003` and `DEL-01-02-REQ-004` are no longer harvested as local
`REQ-003`/`REQ-004`, while a standalone `REQ-003` still is.

**Do not adopt this without:**
1. a test in a `tools/scope_of_work/` test file covering both qualified forms,
   the bare form, and the existing blockquote exemption;
2. a re-validation pass over every accepted `ScopeOfWork.md` — the lookbehind
   *removes* references, so a contract that currently passes could newly fail
   if some legitimate local reference happens to follow a hyphen; and
3. a decision on which qualified spelling is canonical. There are currently
   **three** spellings in play: `DEL-NN-NN/REQ-NNN` (the request's),
   `DEL-NN-NN-REQ-NNN` (the B2 collision case), and
   `derive_review_checklist.py:111,124`'s minted
   `qualified_id = f"{deliverable_id}-{ac_id}"` → `DEL-01-02-AC-001`. The third
   is generated by the deriver into checklist JSON and, unlike the slash form,
   cannot be unambiguously parsed back into its parts.

**Recommendation: Option 1 now, Option 2 as a separate tranche.** Option 1 is
what the wave actually did, needs no tool change, and closes the contract gap.
Option 2 is a real improvement but drags in a canonical-spelling decision and a
corpus re-validation that should not ride along with a contract clarification.

## 5. Compatibility

- Option 1 is contract text only. The 12 accepted B2-wave contracts already
  follow it (ASSERTED-UPSTREAM), so they become conforming rather than
  exceptional.
- Adding QA item 19 extends the list rather than renumbering it; existing item
  numbers cited in run records stay stable.
- **Mode scoping:** item 19 is mode-agnostic. P1 §2e(ii) in this packet carries
  the canonical QA mode-scoping header and already names items 19 and 20 in the
  mode-agnostic set; do not restate it here. **If P6 is adopted without P1**,
  add this sentence to `QA_CHECKS.md` alongside item 19: "Item 19 applies to
  every mode."
