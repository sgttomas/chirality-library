#!/bin/zsh
# write_status.sh
# Writes or updates _STATUS.md with a lifecycle state transition.
# Appends to History section; updates Current State.
# Enforces objective transition preconditions BEFORE any file edit:
# state-machine shape (ordered states, no skips, no backward moves except the
# human-ruled CHECKING -> IN_PROGRESS reversal), actor class (CHECKING/ISSUED
# and the reversal are human-only), committed-ruling path, and approval-SHA
# reachability where the project's adapter manifest (_harness/adapter.yaml,
# found by walking up from DEL_PATH) declares it.
#
# Reversal (SPEC §3.3/§3.4): CHECKING -> IN_PROGRESS is the sole exit from an
# unsuccessful or withdrawn check. It requires a HUMAN actor and --ruling naming
# the ruling record (always required for the reversal, independent of
# guard_requires_committed_ruling_path; git-tracked when in a git repo), plus
# --approval-sha where the adapter declares that schema. The history line is
# suffixed "[reversal from CHECKING; ruling: <path>]". Existing approval-SHA /
# Authorization Basis fields are left as history; the next CHECKING entry
# replaces them.
#
# Reopening (SPEC §3.3, D-GOV-50, D-GOV-51): ISSUED -> IN_PROGRESS is admitted
# only under an accepted scope-change amendment. It requires a HUMAN actor, a git
# repository, --approval-sha on every root (well formed, a reachable commit, and
# an ancestor of HEAD), and --amendment <id-or-path> that passes
# tools/validation/check_amendment_reopen.py --at-commit <approval SHA>: every
# amendment record is read from the approval commit, never the working tree
# (group 3 accepted; register bound by hash in the governing group-2
# ACCEPTED_MANIFEST.csv and unchanged; no REMOVE of the deliverable and a
# DELIVERABLE row with MODIFY, or RECLASSIFY with ScopeChanging YES), and
# _STATUS.md must not already record a reopening under the same amendment (one
# tool-recorded reopening per accepted amendment; a human may record a further
# one directly). Without --amendment it stays BLOCKED as a backward transition.
# The history line is suffixed "[reopened from ISSUED; amendment: <ID> (<group-3
# snapshot>); action: <register> ActionSeq <n> <type>; approval SHA: <sha>]".
# Every other backward move stays BLOCKED. --force-human-override cannot waive
# the reversal's ruling preconditions or any reopening precondition.
#
# Usage: ./write_status.sh <DEL_PATH> <STATE> <ACTOR> [--ruling <path>] [--approval-sha <sha>] [--amendment <id-or-path>] [--force-human-override <reason>]
#
# Inputs:
#   DEL_PATH — Path to deliverable folder (must exist)
#   STATE    — Lifecycle state (OPEN|INITIALIZED|SEMANTIC_READY|IN_PROGRESS|CHECKING|ISSUED)
#   ACTOR    — Who triggered the transition (e.g., PREPARATION, TASK+four-documents, human)
#   --ruling <path>       — Ruling/decision record authorizing a human-gate transition.
#                           Required for CHECKING/ISSUED when the adapter manifest sets
#                           guard_requires_committed_ruling_path (default true in a git
#                           repo when no manifest is found); always required for the
#                           CHECKING -> IN_PROGRESS reversal. Must exist and be git-tracked.
#   --approval-sha <sha>  — Git commit SHA evidencing the ruling. Required for
#                           CHECKING/ISSUED and the reversal when the adapter manifest sets
#                           guard_requires_approval_sha; must match ^[0-9a-f]{7,64}$ and
#                           be reachable (git cat-file -e <sha>^{commit}). Roots that do
#                           not declare an approval-SHA schema get a REVIEW note and proceed.
#                           Required on every root for ISSUED -> IN_PROGRESS, where it
#                           must also be an ancestor of HEAD and is the commit the
#                           amendment records are read from.
#   --amendment <id-or-path>
#                         — Accepted scope-change amendment authorizing ISSUED -> IN_PROGRESS:
#                           an amendment ID (SCA-NNN, SCA-APP-NNN; read from <execution
#                           root>/_ScopeChange/ of DEL_PATH) or its snapshot or group-3
#                           decision path, resolved in the approval commit. A usage error
#                           for any other transition. --ruling is not used for reopening.
#   --force-human-override <reason>
#                         — HUMAN-actor-only: converts a BLOCK into a recorded override;
#                           the reason is appended to the history line as
#                           "[override: <reason>]". Never overrides usage errors.
#
# Outputs:
#   Written/updated _STATUS.md in the deliverable folder (new file only at OPEN).
#   Refusals edit nothing. REVIEW/WARN notes go to stderr.
#   On CHECKING with a declared approval-SHA schema, also upserts the manifest-named
#   SHA field (default "**Checking Approval SHA:**") and an "**Authorization Basis:**"
#   line referencing the ruling path (repo-relative).
#
# Exit codes: 0 = written (REVIEW/WARN notes may exist); 1 = BLOCK (refused);
#             2 = usage or operational error (invalid state is now exit 2, not 1).
#
# Example:
#   ./write_status.sh ./execution/PKG-001_.../1_Working/DEL-001-01_... INITIALIZED TASK+four-documents
#   ./write_status.sh ./execution/PKG-001_.../1_Working/DEL-001-01_... CHECKING human \
#     --ruling execution/_Coordination/_DECISIONS/D-XX.md --approval-sha abc1234
#   ./write_status.sh ./execution/PKG-001_.../1_Working/DEL-001-01_... IN_PROGRESS human \
#     --ruling execution/_Coordination/_DECISIONS/D-YY_check_withdrawn.md --approval-sha def5678
#   ./write_status.sh ./execution/PKG-001_.../1_Working/DEL-001-01_... IN_PROGRESS human \
#     --amendment SCA-007 --approval-sha 0123abc
#
# K-GATE-1: this guard checks objective preconditions only (ruling path committed,
# SHA verifiable, actor class, state-machine shape); it never evaluates or blocks
# the CHECKING→ISSUED judgment itself.
# Preconditions reconciled with frontend transition.ts (DEL-07-04) — divergences
# recorded in tools/practitioner_harness/README.md §Guard reconciliation.

# Git reads below (and in the amendment checker, which inherits these) ignore
# local replace refs and grafts, so object substitution cannot change what the
# approval commit contains or which commits are its ancestors.
export GIT_NO_REPLACE_OBJECTS=1
export GIT_GRAFT_FILE=/dev/null

usage() {
  echo "Usage: $0 <DEL_PATH> <STATE> <ACTOR> [--ruling <path>] [--approval-sha <sha>] [--amendment <id-or-path>] [--force-human-override <reason>]" >&2
  exit 2
}

# The reopening checker ships beside this tool (tools/validation/).
CHECKER="${0:A:h}/../validation/check_amendment_reopen.py"

DEL_PATH="$1"
STATE="$2"
ACTOR="$3"
if [ -z "$DEL_PATH" ] || [ -z "$STATE" ] || [ -z "$ACTOR" ]; then
  usage
fi
shift 3

RULING=""
APPROVAL_SHA=""
AMENDMENT=""
OVERRIDE=0
OVERRIDE_REASON=""
while [ $# -gt 0 ]; do
  case "$1" in
    --ruling)
      [ -n "$2" ] || usage
      RULING="$2"; shift 2 ;;
    --approval-sha)
      [ -n "$2" ] || usage
      APPROVAL_SHA="$2"; shift 2 ;;
    --amendment)
      [ -n "$2" ] || usage
      AMENDMENT="$2"; shift 2 ;;
    --force-human-override)
      [ -n "$2" ] || usage
      OVERRIDE=1; OVERRIDE_REASON="$2"; shift 2 ;;
    *)
      echo "ERROR: unknown argument '$1'" >&2
      usage ;;
  esac
done

VALID_STATES="OPEN INITIALIZED SEMANTIC_READY IN_PROGRESS CHECKING ISSUED"
state_index() {
  case "$1" in
    OPEN) echo 0 ;;
    INITIALIZED) echo 1 ;;
    SEMANTIC_READY) echo 2 ;;
    IN_PROGRESS) echo 3 ;;
    CHECKING) echo 4 ;;
    ISSUED) echo 5 ;;
    *) echo -1 ;;
  esac
}

TARGET_IDX=$(state_index "$STATE")
if [ "$TARGET_IDX" -lt 0 ]; then
  echo "ERROR: Invalid state '$STATE'. Valid: $VALID_STATES" >&2
  exit 2
fi

if [ ! -d "$DEL_PATH" ]; then
  echo "ERROR: DEL_PATH is not an existing directory: $DEL_PATH" >&2
  exit 2
fi
DEL_ABS=$(cd "$DEL_PATH" && pwd -P) || exit 2

# Actor normalization (reconciled with transition.ts normalizeActor):
# upper-case, whitespace -> underscore; USER/OPERATOR/HUMAN* -> HUMAN.
NORM_ACTOR=$(printf '%s' "$ACTOR" | tr '[:lower:]' '[:upper:]' \
  | sed -E -e 's/^[[:space:]]+//' -e 's/[[:space:]]+$//' -e 's/[[:space:]]+/_/g')
case "$NORM_ACTOR" in
  USER|OPERATOR|HUMAN*) NORM_ACTOR="HUMAN" ;;
esac

if [ $OVERRIDE -eq 1 ] && [ "$NORM_ACTOR" != "HUMAN" ]; then
  echo "NOTE: --force-human-override ignored — ACTOR '$ACTOR' does not normalize to HUMAN (D-GOV-02: overrides are human-only)" >&2
  OVERRIDE=0
fi

# Repo root resolved at runtime from the deliverable's location (never hardcoded).
REPO_ROOT=$(git -C "$DEL_ABS" rev-parse --show-toplevel 2>/dev/null)
if [ -n "$REPO_ROOT" ]; then
  REPO_ROOT=$(cd "$REPO_ROOT" && pwd -P) || exit 2
  IN_GIT=1
else IN_GIT=0; fi

# Root governance mode is a hard read-only source boundary. This check runs
# before the ordinary human-override machinery and cannot be overridden.
if [ "$IN_GIT" -eq 1 ] && [[ "$DEL_ABS" == "$REPO_ROOT/execution/"* ]]; then
  ROOT_ADAPTER="$REPO_ROOT/execution/_harness/adapter.yaml"
  if [ -f "$ROOT_ADAPTER" ]; then
    python3 - "$ROOT_ADAPTER" <<'PYROOT'
import sys
try:
    import yaml
    data = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Root adapter is not a mapping")
    if "mode" in data:
        raise ValueError("Explicit Root mode prohibits ordinary source lifecycle writes; use its governed instrument")
except Exception as exc:
    print(f"BLOCK: Root source write refused: {exc}", file=sys.stderr)
    sys.exit(1)
PYROOT
    [ $? -eq 0 ] || exit 1
  fi
fi

# Adapter-manifest discovery: walk up from DEL_PATH looking for _harness/adapter.yaml;
# stop at repo root (when in a git repo) or filesystem root.
MANIFEST=""
_d="$DEL_ABS"
while :; do
  if [ -f "$_d/_harness/adapter.yaml" ]; then
    MANIFEST="$_d/_harness/adapter.yaml"
    break
  fi
  if [ $IN_GIT -eq 1 ] && [ "$_d" = "$REPO_ROOT" ]; then break; fi
  if [ "$_d" = "/" ]; then break; fi
  _d=$(dirname "$_d")
done

manifest_value() {
  # $1 = flat key; prints the value with trailing comment and surrounding quotes stripped.
  sed -n -E "s/^${1}:[[:space:]]*//p" "$MANIFEST" | head -1 \
    | sed -E -e 's/[[:space:]]+#.*$//' -e 's/^"(.*)"$/\1/' -e 's/[[:space:]]+$//'
}

REQ_RULING="true"              # default: required when in a git repo (also when no manifest found)
REQ_SHA=""                     # empty = no manifest / schema undeclared
SHA_FIELD="Checking Approval SHA"
if [ -n "$MANIFEST" ]; then
  _v=$(manifest_value guard_requires_committed_ruling_path)
  [ -n "$_v" ] && REQ_RULING="$_v"
  _v=$(manifest_value guard_requires_approval_sha)
  [ -n "$_v" ] && REQ_SHA="$_v"
  _v=$(manifest_value guard_approval_sha_field)
  [ -n "$_v" ] && SHA_FIELD="$_v"
fi

STATUS_FILE="$DEL_PATH/_STATUS.md"
CREATING=0
CURRENT=""
CUR_IDX=-1
if [ -f "$STATUS_FILE" ]; then
  CURRENT=$(sed -n -E 's/^\*\*Current State:\*\*[[:space:]]*//p' "$STATUS_FILE" | head -1 \
    | sed -E 's/[[:space:]]+$//')
  CUR_IDX=$(state_index "$CURRENT")
  if [ "$CUR_IDX" -lt 0 ]; then
    echo "ERROR: cannot resolve current state from $STATUS_FILE (found: '${CURRENT:-<none>}')" >&2
    exit 2
  fi
else
  CREATING=1
fi

# ---- Check phase (no file is edited before all checks pass or are overridden) ----
BLOCKED=0
OVERRIDE_USED=0
block() {
  local code="$1"; shift
  if [ $OVERRIDE -eq 1 ]; then
    echo "OVERRIDE recorded (HUMAN): $code — $*" >&2
    OVERRIDE_USED=1
    return 0
  fi
  echo "BLOCK $code: $*" >&2
  BLOCKED=1
}
# hard_block: a refusal --force-human-override cannot waive (the reversal's
# ruling preconditions and every ISSUED -> IN_PROGRESS precondition, which SPEC
# §3.3/§3.4 reserve to a recorded ruling and an accepted scope-change amendment
# respectively).
hard_block() {
  local code="$1"; shift
  echo "BLOCK $code: $* (not overridable)" >&2
  BLOCKED=1
}
warn() { echo "WARN: $*" >&2 }
review() { echo "REVIEW: $*" >&2 }

sha_format_ok() {
  printf '%s' "$1" | grep -qiE '^[0-9a-f]{7,64}$'
}

SAME_STATE=0
REVERSAL=0
REOPEN=0
if [ $CREATING -eq 1 ]; then
  if [ "$STATE" != "OPEN" ]; then
    block NEW_FILE_NOT_OPEN "no existing _STATUS.md at $STATUS_FILE — new-file creation is allowed only at OPEN (requested: $STATE)"
  fi
else
  if [ "$STATE" = "$CURRENT" ]; then
    SAME_STATE=1
    warn "same-state re-assert ($STATE) — allowed, history appended (idempotent; divergence from transition.ts recorded)"
  elif [ "$TARGET_IDX" -lt "$CUR_IDX" ]; then
    if [ "$CURRENT>$STATE" = "CHECKING>IN_PROGRESS" ]; then
      # SPEC §3.3: human reversal, the sole exit from an unsuccessful or withdrawn check.
      REVERSAL=1
    elif [ "$CURRENT>$STATE" = "ISSUED>IN_PROGRESS" ] && [ -n "$AMENDMENT" ]; then
      # SPEC §3.3: reopening under an accepted scope-change amendment (checked below).
      REOPEN=1
    elif [ "$CURRENT>$STATE" = "ISSUED>IN_PROGRESS" ]; then
      hard_block BACKWARD_TRANSITION "backward transitions are not allowed ($CURRENT -> $STATE) without --amendment; ISSUED changes use the governed scope-change process, and reopening needs an accepted amendment (SPEC §3.3)"
    else
      block BACKWARD_TRANSITION "backward transitions are not allowed ($CURRENT -> $STATE); the only admitted reversal is the human-ruled CHECKING -> IN_PROGRESS"
    fi
  else
    case "$CURRENT>$STATE" in
      "OPEN>INITIALIZED"|"INITIALIZED>SEMANTIC_READY"|"INITIALIZED>IN_PROGRESS"|"SEMANTIC_READY>IN_PROGRESS"|"IN_PROGRESS>CHECKING"|"CHECKING>ISSUED")
        : ;;
      *)
        block TRANSITION_NOT_ALLOWED "transition $CURRENT -> $STATE is not an allowed step" ;;
    esac
  fi
fi

if [ -n "$AMENDMENT" ] && [ $REOPEN -eq 0 ]; then
  echo "ERROR: --amendment applies only to ISSUED -> IN_PROGRESS (current: ${CURRENT:-<none>}, requested: $STATE)" >&2
  usage
fi

# Reopening preconditions (SPEC §3.3, D-GOV-50/51). Every refusal is hard.
REOPEN_AMENDMENT_ID=""
REOPEN_GROUP3=""
REOPEN_REGISTER=""
REOPEN_SEQ=""
REOPEN_ACTION=""
if [ $REOPEN -eq 1 ]; then
  if [ "$NORM_ACTOR" != "HUMAN" ]; then
    hard_block UNAUTHORIZED_ACTOR "reopening ISSUED -> IN_PROGRESS requires a HUMAN actor (got '$ACTOR' -> '$NORM_ACTOR'); SPEC §3.3"
  fi
  if [ -n "$RULING" ]; then
    echo "NOTE: --ruling is not used for reopening; the accepted amendment is the authorizing record" >&2
  fi
  if [ $IN_GIT -eq 0 ]; then
    hard_block REOPEN_REQUIRES_GIT "reopening ISSUED -> IN_PROGRESS needs a git repository to verify --approval-sha and the amendment record"
  else
    SHA_OK=0
    if [ -z "$APPROVAL_SHA" ]; then
      hard_block APPROVAL_SHA_REQUIRED "reopening ISSUED -> IN_PROGRESS requires --approval-sha on every root"
    elif ! sha_format_ok "$APPROVAL_SHA"; then
      hard_block INVALID_APPROVAL_SHA "--approval-sha must be a git SHA-like hexadecimal token (7-64 chars); got '$APPROVAL_SHA'"
    elif ! git -C "$REPO_ROOT" cat-file -e "${APPROVAL_SHA}^{commit}" 2>/dev/null; then
      hard_block APPROVAL_SHA_UNREACHABLE "--approval-sha $APPROVAL_SHA is not a reachable commit in this repository"
    elif ! git -C "$REPO_ROOT" merge-base --is-ancestor "$APPROVAL_SHA" HEAD 2>/dev/null; then
      hard_block APPROVAL_SHA_NOT_ANCESTOR "--approval-sha $APPROVAL_SHA is not an ancestor of HEAD; cite a commit on this branch's history"
    else
      SHA_OK=1
    fi
    if [ ! -f "$CHECKER" ]; then
      hard_block AMENDMENT_CHECK_ERROR "reopening checker not found: $CHECKER"
    elif [ $SHA_OK -eq 1 ]; then
      # Anchored check only: every amendment record is read from the approval
      # commit. The checker's unanchored working-tree mode is never used here.
      CHECK_JSON=$(python3 "$CHECKER" --deliverable "$DEL_ABS" --amendment "$AMENDMENT" \
        --at-commit "$APPROVAL_SHA" --status-file "$DEL_ABS/_STATUS.md" \
        --project-root "$REPO_ROOT" --json 2>/dev/null)
      CHECK_RC=$?
      # One field per line (whitespace collapsed), then an END sentinel so an
      # empty trailing field is not lost to command substitution.
      CHECK_FIELDS=("${(@f)$(printf '%s' "$CHECK_JSON" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(3)
for key in ("code", "reason", "amendment_id", "group3_snapshot", "at_commit",
            "register_path", "action_seq", "action_type"):
    print(" ".join(str(d.get(key) or "").split()))
print("anchored" if d.get("anchored") is True else "unanchored")
print("END")
' 2>/dev/null)}")
      if [ ${#CHECK_FIELDS} -ne 10 ] || [ "${CHECK_FIELDS[10]}" != "END" ]; then
        hard_block AMENDMENT_CHECK_ERROR "the reopening checker could not decide (exit $CHECK_RC); run tools/validation/check_amendment_reopen.py --deliverable '$DEL_PATH' --amendment '$AMENDMENT' --at-commit '$APPROVAL_SHA' for details"
      elif [ $CHECK_RC -eq 0 ] && [ "${CHECK_FIELDS[1]}" = "ADMITTED" ] && [ "${CHECK_FIELDS[9]}" = "anchored" ] && [ -n "${CHECK_FIELDS[5]}" ]; then
        REOPEN_AMENDMENT_ID="${CHECK_FIELDS[3]}"
        REOPEN_GROUP3="${CHECK_FIELDS[4]}"
        REOPEN_REGISTER="${CHECK_FIELDS[6]}"
        REOPEN_SEQ="${CHECK_FIELDS[7]}"
        REOPEN_ACTION="${CHECK_FIELDS[8]}"
      elif [ $CHECK_RC -eq 0 ]; then
        hard_block AMENDMENT_CHECK_ERROR "the reopening checker admitted without reading the approval commit; refusing"
      else
        hard_block AMENDMENT_NOT_ADMITTED "${CHECK_FIELDS[1]}: ${CHECK_FIELDS[2]}"
      fi
    fi
  fi
fi

RULING_ABS=""
if [ "$STATE" = "CHECKING" ] || [ "$STATE" = "ISSUED" ] || [ $REVERSAL -eq 1 ]; then
  if [ "$NORM_ACTOR" != "HUMAN" ]; then
    if [ $REVERSAL -eq 1 ]; then
      block UNAUTHORIZED_ACTOR "reversal CHECKING -> IN_PROGRESS requires a HUMAN actor (got '$ACTOR' -> '$NORM_ACTOR'); SPEC §3.3"
    else
      block UNAUTHORIZED_ACTOR "state $STATE requires a HUMAN actor (got '$ACTOR' -> '$NORM_ACTOR'); SPEC §3.3"
    fi
  fi

  if [ $IN_GIT -eq 0 ]; then
    review "not a git repository — committed-ruling and SHA reachability checks unavailable here"
    if [ $REVERSAL -eq 1 ]; then
      if [ -z "$RULING" ]; then
        hard_block RULING_REQUIRED "reversal CHECKING -> IN_PROGRESS requires --ruling <ruling path>"
      elif [ ! -e "$RULING" ]; then
        hard_block RULING_PATH_MISSING "--ruling path not found: $RULING"
      fi
    fi
    if [ -n "$APPROVAL_SHA" ] && ! sha_format_ok "$APPROVAL_SHA"; then
      block INVALID_APPROVAL_SHA "--approval-sha must be a git SHA-like hexadecimal token (7-64 chars)"
    fi
  else
    # Committed-ruling precondition (always required for the reversal).
    if [ -z "$RULING" ]; then
      if [ $REVERSAL -eq 1 ]; then
        hard_block RULING_REQUIRED "reversal CHECKING -> IN_PROGRESS requires --ruling <committed ruling path>"
      elif [ "$REQ_RULING" = "true" ]; then
        block RULING_REQUIRED "state $STATE requires --ruling <committed ruling path> (guard_requires_committed_ruling_path)"
      fi
    else
      if [ -e "$RULING" ]; then
        RULING_ABS="$(cd "$(dirname "$RULING")" && pwd -P)/$(basename "$RULING")"
      elif [ -e "$REPO_ROOT/$RULING" ]; then
        RULING_ABS="$REPO_ROOT/$RULING"
      elif [ $REVERSAL -eq 1 ]; then
        hard_block RULING_PATH_MISSING "--ruling path not found: $RULING"
      else
        block RULING_PATH_MISSING "--ruling path not found: $RULING"
      fi
      if [ -n "$RULING_ABS" ] && ! git -C "$REPO_ROOT" ls-files --error-unmatch -- "$RULING_ABS" >/dev/null 2>&1; then
        if [ $REVERSAL -eq 1 ]; then
          hard_block RULING_NOT_COMMITTED "--ruling path is not git-tracked: $RULING"
        else
          block RULING_NOT_COMMITTED "--ruling path is not git-tracked: $RULING"
        fi
      fi
    fi

    # Approval-SHA precondition (adapter-declared).
    if [ "$REQ_SHA" = "true" ]; then
      if [ -z "$APPROVAL_SHA" ]; then
        block APPROVAL_SHA_REQUIRED "state $STATE on this root requires --approval-sha (guard_requires_approval_sha)"
      elif ! sha_format_ok "$APPROVAL_SHA"; then
        block INVALID_APPROVAL_SHA "--approval-sha must be a git SHA-like hexadecimal token (7-64 chars); got '$APPROVAL_SHA'"
      elif ! git -C "$REPO_ROOT" cat-file -e "${APPROVAL_SHA}^{commit}" 2>/dev/null; then
        block APPROVAL_SHA_UNREACHABLE "--approval-sha $APPROVAL_SHA is not a reachable commit in this repository"
      fi
    else
      if [ -z "$APPROVAL_SHA" ]; then
        if [ "$REQ_SHA" = "false" ]; then
          review "root declares no approval-SHA schema; absent SHA surfaced for human review (piping schema alignment is a separately-ruled parked item)"
        else
          review "no adapter manifest declares an approval-SHA schema here; absent SHA surfaced for human review"
        fi
      else
        if ! sha_format_ok "$APPROVAL_SHA"; then
          warn "--approval-sha provided but malformed (expected ^[0-9a-f]{7,64}$); root declares no approval-SHA schema — surfaced, not blocking"
        elif ! git -C "$REPO_ROOT" cat-file -e "${APPROVAL_SHA}^{commit}" 2>/dev/null; then
          warn "--approval-sha provided but not a reachable commit; root declares no approval-SHA schema — surfaced, not blocking"
        fi
      fi
    fi
  fi
fi

if [ $BLOCKED -eq 1 ]; then
  exit 1
fi

# ---- Write phase ----
DEL_NAME=$(basename "$DEL_ABS")
DEL_ID="${DEL_NAME%%_*}"
TODAY=$(date +%Y-%m-%d)
RULING_DISPLAY="$RULING"
if [ -n "$RULING_ABS" ] && [ -n "$REPO_ROOT" ]; then
  RULING_DISPLAY="${RULING_ABS#$REPO_ROOT/}"
fi
HISTORY_SUFFIX=""
if [ $REVERSAL -eq 1 ]; then
  HISTORY_SUFFIX=" [reversal from CHECKING; ruling: ${RULING_DISPLAY:-none}]"
fi
if [ $REOPEN -eq 1 ]; then
  HISTORY_SUFFIX=" [reopened from ISSUED; amendment: $REOPEN_AMENDMENT_ID ($REOPEN_GROUP3); action: $REOPEN_REGISTER ActionSeq ${REOPEN_SEQ:-?} $REOPEN_ACTION; approval SHA: $APPROVAL_SHA]"
fi
if [ $OVERRIDE_USED -eq 1 ]; then
  HISTORY_SUFFIX="$HISTORY_SUFFIX [override: $OVERRIDE_REASON]"
fi

if [ $CREATING -eq 0 ]; then
  # Update existing: replace Current State line, append to History.
  # One awk pass through a tmp file: BSD sed's `-i ''` is not portable to GNU
  # sed (silent field-update no-op on Linux); values ride ENVIRON like
  # upsert_field so regex metacharacters are never interpreted.
  tmp="${STATUS_FILE}.tmp.$$"
  if ! WS_STATE="$STATE" WS_TODAY="$TODAY" awk '
    index($0, "**Current State:**") == 1 { print "**Current State:** " ENVIRON["WS_STATE"]; next }
    index($0, "**Last Updated:**") == 1  { print "**Last Updated:** " ENVIRON["WS_TODAY"]; next }
    { print }
  ' "$STATUS_FILE" > "$tmp"; then
    rm -f "$tmp"
    echo "ERROR: cannot update state fields in $STATUS_FILE" >&2
    exit 2
  fi
  mv "$tmp" "$STATUS_FILE"
  echo "- $TODAY — State set to $STATE ($ACTOR)$HISTORY_SUFFIX" >> "$STATUS_FILE"
else
  # Create new (only reachable at OPEN, or via recorded human override)
  cat > "$STATUS_FILE" << EOF
# Status: $DEL_ID

**Current State:** $STATE
**Last Updated:** $TODAY

## History
- $TODAY — State set to $STATE ($ACTOR)$HISTORY_SUFFIX
EOF
fi

upsert_field() {
  # $1 = field name, $2 = value; updates the "**field:** value" line or inserts it
  # after "**Last Updated:**" (fallback: after "**Current State:**"). Values pass
  # through awk ENVIRON so sed/regex metacharacters (&, |, \) are never interpreted.
  local field="$1" value="$2" tmp
  tmp="${STATUS_FILE}.tmp.$$"
  if UF_FIELD="$field" awk '
    BEGIN { prefix = "**" ENVIRON["UF_FIELD"] ":**"; found = 0 }
    index($0, prefix) == 1 { found = 1; exit }
    END { exit !found }
  ' "$STATUS_FILE"; then
    UF_FIELD="$field" UF_VALUE="$value" awk '
      BEGIN {
        prefix = "**" ENVIRON["UF_FIELD"] ":**"
        line   = prefix " " ENVIRON["UF_VALUE"]
      }
      index($0, prefix) == 1 { print line; next }
      { print }
    ' "$STATUS_FILE" > "$tmp"
  else
    if ! UF_FIELD="$field" UF_VALUE="$value" awk '
      BEGIN {
        prefix = "**" ENVIRON["UF_FIELD"] ":**"
        line   = prefix " " ENVIRON["UF_VALUE"]
        done = 0
      }
      { print }
      !done && index($0, "**Last Updated:**") == 1 { print line; done = 1 }
      END { if (!done) exit 3 }
    ' "$STATUS_FILE" > "$tmp"; then
      # No "**Last Updated:**" anchor: retry after "**Current State:**".
      if ! UF_FIELD="$field" UF_VALUE="$value" awk '
        BEGIN {
          prefix = "**" ENVIRON["UF_FIELD"] ":**"
          line   = prefix " " ENVIRON["UF_VALUE"]
          done = 0
        }
        { print }
        !done && index($0, "**Current State:**") == 1 { print line; done = 1 }
        END { if (!done) exit 3 }
      ' "$STATUS_FILE" > "$tmp"; then
        rm -f "$tmp"
        echo "ERROR: cannot record required field '${field}': no '**Last Updated:**' or '**Current State:**' anchor line in $STATUS_FILE" >&2
        exit 2
      fi
    fi
  fi
  mv "$tmp" "$STATUS_FILE"
}

# Field updates only on roots that declare an approval-SHA schema (app-dev conventions).
if [ "$STATE" = "CHECKING" ] && [ "$REQ_SHA" = "true" ] && [ -n "$APPROVAL_SHA" ]; then
  upsert_field "$SHA_FIELD" "$APPROVAL_SHA"
  if [ -n "$RULING" ]; then
    upsert_field "Authorization Basis" "ruling: $RULING_DISPLAY"
  fi
fi

if [ $REVERSAL -eq 1 ]; then
  echo "Status: $DEL_ID → $STATE (by $ACTOR; reversal from CHECKING)"
elif [ $REOPEN -eq 1 ]; then
  echo "Status: $DEL_ID → $STATE (by $ACTOR; reopened from ISSUED under $REOPEN_AMENDMENT_ID)"
else
  echo "Status: $DEL_ID → $STATE (by $ACTOR)"
fi
