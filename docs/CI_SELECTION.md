# Shared-library development verification

`harness` is the single required result for Chirality's shared library. It joins
repository/tool verification and fails if that work fails, is cancelled or never
runs. App v4 and SWBPIPE own their product verification in
[chirality-app](https://github.com/sgttomas/chirality-app) and
[SWBPIPE](https://github.com/sgttomas/SWBPIPE); their build jobs, selectors and
cache warmers no longer execute here.

Root tool selection uses the complete merge-base diff, retaining both sides of
renames/deletions. `tools/tools-test-routing.json` maps inputs; unknown tool
inputs or missing diffs select the full registered estate. Use
`python3 tools/run_affected_tests.py --dry-run` to inspect selection, then omit
`--dry-run` to execute it. Consumed role/workflow checks, deliverable structure,
conflict, credential and private-term checks remain in the repository job.

Shared changes identify external consumers and their selected library revisions;
product adoption occurs through their own independently reviewable changes.
Do not restore a product job here when merging an old monorepo branch. Historical
product checks and recovery references remain available through original Git
history; a green Root result does not claim a product's verification or release.
