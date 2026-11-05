# D-T0-25 / D-T0-26 Effective-State Validation Plan

1. Confirm the exact closeout basis.
2. Confirm each publication commit is the second parent of its effective merge
   and both merges are ancestral to the closeout basis.
3. Confirm each decision and frozen application package is byte-identical to
   its publication commit.
4. Reproduce the frozen application manifests at 26/26 and 21/21.
5. Confirm exact PublicationSHA/EffectiveSHA parity across decision records,
   live register rows, closeout records, and Receipt 31.
6. Confirm the exact five-surface write envelope.
7. Confirm the verbatim owner direction and approved Agent 0 recommendation.
8. Confirm profile bytes, profile validation bytes, harness production/test
   bytes, and all product/runtime/implementation surfaces remain unchanged.
9. Run both profile and complete practitioner-harness validation.
10. Run artifact-manifest, whitespace, terminal-newline, and
    `git diff --check` validation.
