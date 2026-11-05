# Frozen products

App v3 (`chirality-app-dev`) and Runtime (`chirality-runtime`) are
retired. Their complete tracked trees, and the old App exporter, are recoverable
at `archive/pre-frozen-products-2026-10-10`. They are not development targets or
verified products on main.

From this repository, inspect a file without restoring the project:

```sh
git show archive/pre-frozen-products-2026-10-10:projects/chirality-runtime/docs/PRD.md
```

For the complete pre-removal checkout:

```sh
git worktree add --detach /tmp/chirality-frozen archive/pre-frozen-products-2026-10-10
```

For App v3's historical instruction documents and packaging basis, use
`archive/pre-docs-cleanup-1` instead. Neither tag is a promise that old external
dependencies remain obtainable. No history was rewritten. Recovering files does
not reactivate a product, reinstate its procedures or authorize a release;
reactivation requires an explicit owner decision.

## Pre-library Root execution

The old Root `execution/` was removed for the fresh Library PRD on 2026-10-31.
Its complete pre-removal tree is preserved by
`archive/pre-library-execution-2026-10-31` at
`f80f1510fb50799764720303b86c36da64b75d19`. Inspect any old file with
`git show archive/pre-library-execution-2026-10-31:<path>`.
The new library entry remains at `execution/_Coordination/LOOP_INIT.md`.
Recovery does not reinstate old plans, commitments or lifecycle state.
