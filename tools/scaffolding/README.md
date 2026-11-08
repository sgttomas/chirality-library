---
name: tools-scaffolding-guide
description: Scaffolding tools.
metadata:
  kind: instruction
  surface: tool
---
# Scaffolding tools

## Guard reconciliation (write_status.sh vs transition.ts)

`tools/scaffolding/write_status.sh` now enforces preconditions reconciled with
chirality-app-dev's `frontend/src/lib/lifecycle/transition.ts` (DEL-07-04):
same six-state order with backward-transition blocking (except the reversal
in divergence 7); same allowed forward from→to pairs; HUMAN-only
CHECKING/ISSUED; same approval-SHA format rule
(`^[0-9a-f]{7,64}$`). Adapter-declared per root (D-GOV-03): app-dev declares
approval-SHA fields, so the git-verifiable SHA precondition blocks there;
piping's status schema carries no SHA fields, so an absent SHA surfaces as
REVIEW and proceeds (schema alignment is a separately-ruled parked item).
Recorded divergences from transition.ts:

1. **Laxer pre-human actor vocabulary.** `transition.ts` binds each transition
   to a fixed actor list (e.g. OPEN→INITIALIZED only `4_DOCUMENTS`); the guard
   accepts any non-empty actor for pre-CHECKING transitions because the live
   corpus contains more spellings (`PREPARATION`, `TASK+*`, `ORCHESTRATOR*`,
   `CHIRALITY_FRAMEWORK`, `WORKING_ITEMS`) and hard enforcement would
   false-block lawful scaffold flows. CHECKING/ISSUED remain HUMAN-only, with
   the same actor normalization (uppercase, whitespace→`_`,
   USER/OPERATOR/HUMAN*→HUMAN).
2. **Same-state re-assert allowed with WARN** (`transition.ts` refuses it as
   TRANSITION_NOT_ALLOWED); the corpus contains lawful re-assert history lines.
3. **New-file creation permitted at OPEN** (`transition.ts` only transitions
   existing documents); creation at any other state is refused.
4. **`--force-human-override <reason>` exists** (HUMAN-only; reason recorded in
   the history line as `[override: ...]`; never overrides usage errors, the
   reversal's `--ruling` preconditions, or any `ISSUED → IN_PROGRESS`
   reopening precondition) —
   BLOCK override is human-only and recorded, per D-GOV-02. `transition.ts`
   has no override path.
5. **Approval-SHA requirement is adapter-conditional**
   (`guard_requires_approval_sha` in `_harness/adapter.yaml`), not
   unconditional as in `transition.ts`; no-schema roots get REVIEW-and-proceed.
   The SHA is additionally checked for git reachability
   (`git cat-file -e <sha>^{commit}`), which `transition.ts` does not do.
   Format matched case-insensitively, mirroring `transition.ts`.
6. **Invalid state is exit 2 (usage)** rather than the pre-guard script's
   exit 1, aligning with the adopted operational-error convention.
7. **Human-ruled `CHECKING → IN_PROGRESS` reversal is admitted** (SPEC §3.3:
   the sole exit from an unsuccessful or withdrawn check). It requires a HUMAN
   actor and `--ruling` in every root (git-tracked in a git repo, independent
   of `guard_requires_committed_ruling_path`), plus `--approval-sha` where the
   adapter declares that schema; the history line carries
   `[reversal from CHECKING; ruling: <path>]`. Existing approval-SHA and
   Authorization Basis fields are left as history. `transition.ts` still
   rejects the reversal as `BACKWARD_TRANSITION`; adopting it there is the App
   loop's decision.
8. **Reopening `ISSUED → IN_PROGRESS` under an accepted amendment is admitted**
   (SPEC §3.3, D-GOV-50, D-GOV-51). It requires a HUMAN actor, a git
   repository, `--approval-sha` on every root (a reachable commit that is an
   ancestor of `HEAD`, else `APPROVAL_SHA_NOT_ANCESTOR`), and `--amendment
   <id-or-path>` that passes `tools/validation/check_amendment_reopen.py
   --at-commit <approval SHA> --status-file <_STATUS.md>`. The checker reads
   every amendment record from the approval commit, never the working tree,
   so uncommitted or untracked edits do not count (group 3 accepted; register
   bound by hash in the governing group-2 `ACCEPTED_MANIFEST.csv` and
   unchanged; no `REMOVE` of the deliverable and a `DELIVERABLE` row with
   `MODIFY`, or `RECLASSIFY` with `ScopeChanging` `YES`; no reopening already
   recorded in `_STATUS.md` under the same amendment). The guard never uses the
   checker's unanchored working-tree mode. Every refusal is not overridable;
   without `--amendment` the transition stays `BACKWARD_TRANSITION`. The
   history line carries `[reopened from ISSUED; amendment: <ID> (<group-3
   snapshot>); action: <register> ActionSeq <n> <type>; approval SHA: <sha>]`,
   and that line is what the once-per-amendment check reads; a human may still
   record a further reopening directly. The approval SHA fixes which records
   are read; it does not show that the human's act happened at that commit.
   `transition.ts` still rejects the transition; the App loop mirrors the
   checker in its own change.

Stated honestly: tool usage is guided operationally, not enforced — hand edits
bypass any guard. The guard hardens the sanctioned path only.
