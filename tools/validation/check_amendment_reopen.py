#!/usr/bin/env python3
"""Check that an accepted scope-change amendment authorizes reopening an
``ISSUED`` deliverable (``ISSUED -> IN_PROGRESS``; SPEC section 3.3, D-GOV-50,
D-GOV-51).

Usage::

    python3 tools/validation/check_amendment_reopen.py \\
        --deliverable <DEL-ID | deliverable folder> \\
        --amendment <AMENDMENT_ID | amendment snapshot path> \\
        [--at-commit <commit>] [--status-file <_STATUS.md>] \\
        [--scope-change-root <dir>] [--project-root <dir>] [--json]

Modes:

- **At commit** (``--at-commit <commit>``; importable ``at_commit=``). Every
  amendment record the check relies on is read from that commit through git,
  never from the working tree: the group-3 ``DECISION.md`` and
  ``ACCEPTED_MANIFEST.csv``, every group-2 ``ACCEPTED_MANIFEST.csv`` and the
  bound register. ``checkpoint_snapshots/`` is enumerated from the commit's
  tree, so untracked or uncommitted folders do not count. The commit must be
  an ancestor of ``HEAD`` (``git merge-base --is-ancestor``). Paths resolve
  as tree entries; a symlink entry is followed only when its target resolves
  inside the scope-change root. Git replace refs and grafts are ignored, so
  local object substitution cannot change what is read. The project root must be the git top level.
  ``tools/scaffolding/write_status.sh`` uses only this mode, with the
  approval SHA.
- **Working tree** (no ``--at-commit``). The same checks read the working
  tree. The result is unanchored: it binds no commit and may differ from any
  committed record. It serves CLI inspection only; ``write_status.sh`` never
  uses it.

The amendment is admitted only when all of these hold:

1. **Group 3 accepted.** A decision folder
   ``checkpoint_snapshots/<ID>_GROUP-3_[AMENDMENT-<K>_]<YYYY-MM-DD>[_<N>]``
   under the scope-change root holds ``ACCEPTED_MANIFEST.csv`` and a
   ``DECISION.md`` whose first non-blank line is the heading
   ``# <ID> checkpoint group 3 — accepted``, with ``accepted`` directly after
   the dash and followed by whitespace, ``.``, ``,``, ``;`` or the end of the
   line. Group-1 or group-2 decisions, candidate folders with any other name,
   and candidate ``SCA-*`` snapshots do not count. Scope-change group 3
   either accepts or returns the poststate; a qualified acceptance such as
   ``accepted with a limited basis`` is the accepted outcome, and its
   qualifications are the decision text this check does not interpret.
2. **Register bound by hash.** The governing group-2 decision snapshot binds
   one action register: the latest ``checkpoint_snapshots/<ID>_GROUP-2_*``
   folder (highest ``AMENDMENT-<K>``, then date, then ``_<N>``) whose
   ``ACCEPTED_MANIFEST.csv`` binds a row whose file name begins
   ``Amendment_Actions`` and ends ``.csv``. A revised group-2 acceptance
   therefore supersedes an earlier binding; one without such a row leaves
   the earlier binding in force. Where one manifest binds several such rows,
   the register is the single row whose ``Role`` is ``action register`` or
   ``exact final action register`` (case-insensitive), optionally followed
   by a parenthesized note. The register lies inside the scope-change root
   and its SHA-256 equals the bound value.
3. **Qualifying row.** Register rows naming the deliverable have
   ``EntityType`` ``DELIVERABLE``, ``EntityID`` equal to the deliverable ID
   (or the ID followed by ``_`` and a label), and ``AmendmentID`` equal to
   the amendment ID, or blank. No such row is ``REMOVE``; one is ``MODIFY``,
   or ``RECLASSIFY`` with ``ScopeChanging`` ``YES``. A register without the
   ``ScopeChanging`` column is a legacy register: its ``RECLASSIFY`` rows are
   refused, and the human records that reopening directly; its ``MODIFY``
   rows are admitted. Values are not stripped: a relevant value or column
   name with leading or trailing whitespace is refused as a schema error.
4. **Not already used.** With ``--status-file``, the deliverable's
   ``_STATUS.md`` history does not already record
   ``reopened from ISSUED; amendment: <ID>``: one tool-recorded reopening
   per accepted amendment. A human may still record a further reopening
   directly.

The scope-change root is ``<execution root>/_ScopeChange``. When the
deliverable is given as a folder, its execution root is its outermost
ancestor folder named ``execution``; where an adapter manifest
(``_harness/adapter.yaml``, found by walking up from the deliverable as
``write_status.sh`` does) exists, it must imply the same execution root (the
adapter folder itself when named ``execution``, otherwise its ``execution/``
child). A ``_ScopeChange/`` inside a package or deliverable folder is never
used, and a scope-change root given or derived from ``--amendment`` must be
that one. Every path is resolved inside the project root (the git top level
by default); amendment records must lie inside the scope-change root.

Limits: the check reads recorded structure and hashes. It does not establish
that the human's act was genuine or interpret the decision text beyond the
heading; it grants nothing (K-AUTH-1). A run that records group 3 only by
moving ``_LATEST.md``, or has no hash-bound group-2 decision snapshot, is
refused; the human then records a lawful reopening directly.

Exit codes: 0 admitted; 1 refused (``REFUSE <CODE>: <reason>`` on stderr, or
the JSON object on stdout with ``--json``); 2 usage or operational error.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import posixpath
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

ADMITTED = "ADMITTED"

# Refusal codes (stable; mirrored by consumers such as the App validator).
AMENDMENT_UNRESOLVED = "AMENDMENT_UNRESOLVED"
SCOPE_CHANGE_ROOT_NOT_FOUND = "SCOPE_CHANGE_ROOT_NOT_FOUND"
PATH_ESCAPE = "PATH_ESCAPE"
AMENDMENT_OUTSIDE_DELIVERABLE_ROOT = "AMENDMENT_OUTSIDE_DELIVERABLE_ROOT"
APPROVAL_SHA_UNREACHABLE = "APPROVAL_SHA_UNREACHABLE"
APPROVAL_SHA_NOT_ANCESTOR = "APPROVAL_SHA_NOT_ANCESTOR"
AMENDMENT_ALREADY_USED = "AMENDMENT_ALREADY_USED"
GROUP3_NOT_ACCEPTED = "GROUP3_NOT_ACCEPTED"
GROUP2_MANIFEST_MISSING = "GROUP2_MANIFEST_MISSING"
MANIFEST_SCHEMA = "MANIFEST_SCHEMA"
REGISTER_NOT_BOUND = "REGISTER_NOT_BOUND"
REGISTER_AMBIGUOUS = "REGISTER_AMBIGUOUS"
REGISTER_MISSING = "REGISTER_MISSING"
REGISTER_HASH_MISMATCH = "REGISTER_HASH_MISMATCH"
REGISTER_SCHEMA = "REGISTER_SCHEMA"
NO_DELIVERABLE_ACTION = "NO_DELIVERABLE_ACTION"
DELIVERABLE_REMOVED = "DELIVERABLE_REMOVED"
RECLASSIFY_LEGACY_REGISTER = "RECLASSIFY_LEGACY_REGISTER"
RECLASSIFY_NOT_SCOPE_CHANGING = "RECLASSIFY_NOT_SCOPE_CHANGING"
ACTION_NOT_AUTHORIZING = "ACTION_NOT_AUTHORIZING"

REFUSAL_CODES = (
    AMENDMENT_UNRESOLVED,
    SCOPE_CHANGE_ROOT_NOT_FOUND,
    PATH_ESCAPE,
    AMENDMENT_OUTSIDE_DELIVERABLE_ROOT,
    APPROVAL_SHA_UNREACHABLE,
    APPROVAL_SHA_NOT_ANCESTOR,
    AMENDMENT_ALREADY_USED,
    GROUP3_NOT_ACCEPTED,
    GROUP2_MANIFEST_MISSING,
    MANIFEST_SCHEMA,
    REGISTER_NOT_BOUND,
    REGISTER_AMBIGUOUS,
    REGISTER_MISSING,
    REGISTER_HASH_MISMATCH,
    REGISTER_SCHEMA,
    NO_DELIVERABLE_ACTION,
    DELIVERABLE_REMOVED,
    RECLASSIFY_LEGACY_REGISTER,
    RECLASSIFY_NOT_SCOPE_CHANGING,
    ACTION_NOT_AUTHORIZING,
)

_ID = r"SCA-(?:[A-Z][A-Z0-9]*-)*\d+"
AMENDMENT_ID_RE = re.compile(rf"^{_ID}$")
DELIVERABLE_ID_RE = re.compile(r"^DEL-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)+$")
FOLDER_ID_RE = re.compile(rf"^({_ID})_")
# Anything named like a checkpoint folder, and the decision-snapshot names that count.
GROUP_PREFIX_RE = re.compile(rf"^({_ID})_GROUP-(\d+)_")
GROUP_FOLDER_RE = re.compile(
    rf"^({_ID})_GROUP-([123])_(?:AMENDMENT-(\d+)_)?(\d{{4}}-\d{{2}}-\d{{2}})(?:_(\d+))?$"
)
REGISTER_NAME_RE = re.compile(r"^Amendment_Actions[^/]*\.csv$")
REGISTER_ROLE_RE = re.compile(r"^(?:exact final )?action register(?: \([^()]*\))?$", re.IGNORECASE)
REGISTER_COLUMNS = ("AmendmentID", "ActionType", "EntityType", "EntityID", "ScopeChanging")
UNANCHORED_NOTE = (
    "working-tree read: UNANCHORED; the records were read from the working tree, not from a commit, "
    "and may differ from any committed record; write_status.sh never uses this mode"
)


class UsageError(Exception):
    """Unusable arguments or an operational failure (exit 2)."""


@dataclass
class ReopenDecision:
    admitted: bool
    code: str
    reason: str
    deliverable_id: str = ""
    amendment_id: str = ""
    mode: str = "working-tree"
    anchored: bool = False
    at_commit: str = ""
    execution_root: str = ""
    scope_change_root: str = ""
    group3_snapshot: str = ""
    group3_decision: str = ""
    group2_manifest: str = ""
    register_path: str = ""
    register_sha256: str = ""
    action_seq: str = ""
    action_type: str = ""
    scope_changing: str | None = None
    notes: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return asdict(self)


class _Refusal(Exception):
    def __init__(self, code: str, reason: str) -> None:
        super().__init__(reason)
        self.code = code
        self.reason = reason


@dataclass
class _Entry:
    path: str  # resolved, project-root-relative POSIX path ("" is the project root)
    kind: str  # "tree", "blob" or "other"
    oid: str = ""


def _inside_rel(path: str, root: str) -> bool:
    return root == "" or path == root or path.startswith(root + "/")


def _join(*parts: str) -> str:
    return "/".join(p for p in parts if p)


def _escape(what: str, rel: str, within: str) -> _Refusal:
    bound = within or "the project root"
    return _Refusal(PATH_ESCAPE, f"{what} {rel or '.'} resolves outside {bound} (path or symlink escape)")


class _WorkTree:
    """Read records from the working tree (unanchored)."""

    anchored = False

    def __init__(self, proj: Path) -> None:
        self.proj = proj

    def resolve(self, rel: str, within: str, what: str) -> _Entry | None:
        target = self.proj / rel if rel else self.proj
        real = Path(os.path.realpath(target))
        bound = self.proj / within if within else self.proj
        if not (real == bound or bound in real.parents):
            raise _escape(what, rel, within)
        if real.is_dir():
            kind = "tree"
        elif real.is_file():
            kind = "blob"
        elif not os.path.lexists(target) and not real.exists():
            return None
        else:
            kind = "other"
        resolved = real.relative_to(self.proj).as_posix()
        return _Entry("" if resolved == "." else resolved, kind)

    def children(self, rel: str) -> list[str]:
        return sorted(os.listdir(self.proj / rel))

    def read(self, entry: _Entry) -> bytes:
        return (self.proj / entry.path).read_bytes()


class _GitTree:
    """Read records from one commit's tree (anchored)."""

    anchored = True
    _MAX_LINKS = 40

    def __init__(self, proj: Path, commit: str) -> None:
        self.proj = proj
        self.commit = commit
        self._trees: dict[str, dict[str, tuple[str, str, str]] | None] = {}

    def _git(self, *args: str) -> bytes | None:
        out = subprocess.run(
            ["git", "-C", str(self.proj), *args], capture_output=True, check=False, env=_git_env()
        )
        return out.stdout if out.returncode == 0 else None

    def _tree(self, rel: str) -> dict[str, tuple[str, str, str]] | None:
        if rel not in self._trees:
            data = self._git("ls-tree", "-z", f"{self.commit}:{rel}")
            entries: dict[str, tuple[str, str, str]] | None = None
            if data is not None:
                entries = {}
                for record in data.split(b"\0"):
                    if not record:
                        continue
                    meta, _, name = record.partition(b"\t")
                    mode, typ, oid = meta.decode("ascii").split(" ")
                    entries[name.decode("utf-8", "surrogateescape")] = (mode, typ, oid)
            self._trees[rel] = entries
        return self._trees[rel]

    def resolve(self, rel: str, within: str, what: str) -> _Entry | None:
        pending = [c for c in rel.split("/") if c not in ("", ".")]
        done: list[str] = []
        kind, oid, links = "tree", "", 0
        while pending:
            name = pending.pop(0)
            if name == "..":
                if not done:
                    raise _escape(what, rel, within)
                done.pop()
                kind, oid = "tree", ""
                continue
            if kind != "tree":
                return None
            entries = self._tree("/".join(done))
            if entries is None or name not in entries:
                return None
            mode, typ, entry_oid = entries[name]
            if mode == "120000":
                links += 1
                target = (self._git("cat-file", "blob", entry_oid) or b"").decode("utf-8", "surrogateescape")
                if links > self._MAX_LINKS or not target or target.startswith("/"):
                    raise _escape(what, rel, within)
                pending = [c for c in target.split("/") if c not in ("", ".")] + pending
                continue
            if typ not in ("tree", "blob"):
                return None
            done.append(name)
            kind, oid = typ, entry_oid
        path = "/".join(done)
        if not _inside_rel(path, within):
            raise _escape(what, rel, within)
        return _Entry(path, kind, oid)

    def children(self, rel: str) -> list[str]:
        return sorted(self._tree(rel) or {})

    def read(self, entry: _Entry) -> bytes:
        data = self._git("cat-file", "blob", entry.oid)
        if data is None:
            raise OSError(f"cannot read {entry.path} at {self.commit}")
        return data


def _git_env() -> dict[str, str]:
    """Environment for git reads that ignores local replace refs and grafts."""
    env = dict(os.environ)
    env["GIT_NO_REPLACE_OBJECTS"] = "1"
    env["GIT_GRAFT_FILE"] = os.devnull
    return env


def _git_toplevel(start: Path) -> Path | None:
    probe = start if start.is_dir() else start.parent
    try:
        out = subprocess.run(
            ["git", "-C", str(probe), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=False,
            env=_git_env(),
        )
    except OSError:
        return None
    if out.returncode != 0 or not out.stdout.strip():
        return None
    return Path(out.stdout.strip())


def _real(path: Path) -> Path:
    return Path(os.path.realpath(path))


def _inside(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _to_rel(value: str, base: Path, proj: Path) -> str | None:
    """Project-relative POSIX form of a path argument, or None when it lies outside."""
    raw = Path(value)
    absolute = Path(os.path.normpath(raw if raw.is_absolute() else base / raw))
    for candidate in (absolute, _real(absolute)):
        if _inside(candidate, proj):
            rel = candidate.relative_to(proj).as_posix()
            return "" if rel == "." else rel
    return None


def _normalize_deliverable(deliverable: str, cwd: Path) -> tuple[str, Path | None]:
    candidate = Path(deliverable)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    if candidate.is_dir():
        name = _real(candidate).name
        del_id = name.split("_", 1)[0]
        if not DELIVERABLE_ID_RE.match(del_id):
            raise UsageError(f"deliverable folder name does not start with a deliverable ID: {name}")
        return del_id, candidate
    del_id = deliverable.strip().split("_", 1)[0]
    if not DELIVERABLE_ID_RE.match(del_id):
        raise UsageError(f"--deliverable is neither a folder nor a deliverable ID: {deliverable!r}")
    return del_id, None


def _execution_root(del_real: Path, proj: Path) -> str:
    """The deliverable's execution root: its outermost ``execution`` ancestor,
    consistent with the adapter manifest ``write_status.sh`` discovers."""
    parts = del_real.relative_to(proj).parts
    index = next((i for i, part in enumerate(parts[:-1]) if part == "execution"), None)
    if index is None:
        raise _Refusal(
            SCOPE_CHANGE_ROOT_NOT_FOUND,
            f"{del_real.relative_to(proj).as_posix()} is not inside an execution/ folder; pass --scope-change-root",
        )
    exec_rel = "/".join(parts[: index + 1])
    current = del_real
    while True:
        if (current / "_harness" / "adapter.yaml").is_file():
            implied = current if current.name == "execution" else current / "execution"
            if implied != proj / exec_rel:
                raise _Refusal(
                    SCOPE_CHANGE_ROOT_NOT_FOUND,
                    f"adapter manifest {(current / '_harness' / 'adapter.yaml').relative_to(proj).as_posix()} implies "
                    f"execution root {implied.relative_to(proj).as_posix() if _inside(implied, proj) else implied}, "
                    f"but the deliverable's execution root is {exec_rel}",
                )
            break
        if current == proj:
            break
        current = current.parent
    return exec_rel


def _resolve_amendment(
    store, amendment: str, base: Path, proj: Path
) -> tuple[str, str | None, str | None]:
    """Return (amendment_id, scope-change root or None, pinned group-3 folder or None)."""
    value = amendment.strip()
    if AMENDMENT_ID_RE.match(value):
        return value, None, None
    raw = Path(value)
    options = [raw] if raw.is_absolute() else [base / raw, proj / raw]
    rels = [r for r in (_to_rel(str(o), base, proj) for o in options) if r is not None]
    if not rels:
        raise _Refusal(PATH_ESCAPE, f"--amendment path {amendment!r} lies outside the project root")
    entry = None
    for rel in dict.fromkeys(rels):
        entry = store.resolve(rel, "", "--amendment path")
        if entry is not None:
            break
    if entry is None:
        where = " at the commit" if store.anchored else ""
        raise _Refusal(
            AMENDMENT_UNRESOLVED, f"--amendment is neither an amendment ID nor an existing path{where}: {amendment!r}"
        )
    path = entry.path
    if entry.kind == "blob":
        if posixpath.basename(path) != "DECISION.md":
            raise _Refusal(AMENDMENT_UNRESOLVED, f"--amendment file must be a group-3 DECISION.md: {amendment!r}")
        path = posixpath.dirname(path)
    name, parent = posixpath.basename(path), posixpath.dirname(path)
    if posixpath.basename(parent) == "checkpoint_snapshots":
        loose = GROUP_PREFIX_RE.match(name)
        if loose:
            if loose.group(2) != "3":
                raise _Refusal(
                    GROUP3_NOT_ACCEPTED,
                    f"{name} is a group-{loose.group(2)} decision; only an accepted checkpoint-group-3 decision authorizes reopening",
                )
            if not GROUP_FOLDER_RE.match(name):
                raise _Refusal(
                    GROUP3_NOT_ACCEPTED,
                    f"{name} is not a group-3 decision snapshot name ({loose.group(1)}_GROUP-3_[AMENDMENT-K_]YYYY-MM-DD[_N]); candidate folders do not count",
                )
            return loose.group(1), posixpath.dirname(parent), path
    folder = FOLDER_ID_RE.match(name)
    if folder and posixpath.basename(parent) == "_ScopeChange":
        return folder.group(1), parent, None
    raise _Refusal(
        AMENDMENT_UNRESOLVED,
        f"--amendment path is not an amendment snapshot or group-3 decision folder under _ScopeChange/: {amendment!r}",
    )


def _decode(data: bytes) -> str:
    return data.decode("utf-8-sig")


def _first_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.rstrip()
    return ""


def _group_folders(store, root: str, amendment_id: str, group: str) -> tuple[list[tuple[tuple, str, str]], list[str]]:
    """Return decision-snapshot folders of one group, oldest first, and ignored look-alikes."""
    snapshots = store.resolve(_join(root, "checkpoint_snapshots"), root, "checkpoint_snapshots")
    if snapshots is None or snapshots.kind != "tree":
        return [], []
    found, ignored = [], []
    for name in store.children(snapshots.path):
        loose = GROUP_PREFIX_RE.match(name)
        if not loose or loose.group(1) != amendment_id or loose.group(2) != group:
            continue
        match = GROUP_FOLDER_RE.match(name)
        if match is None:
            ignored.append(name)
            continue
        entry = store.resolve(_join(snapshots.path, name), root, f"group-{group} decision folder")
        if entry is not None and entry.kind == "tree":
            key = (int(match.group(3) or 0), match.group(4), int(match.group(5) or 0))
            found.append((key, name, entry.path))
    return sorted(found), ignored


def _heading_re(amendment_id: str) -> re.Pattern:
    return re.compile(
        rf"^#\s+{re.escape(amendment_id)}\s+checkpoint group 3\s+[—–-]+\s+accepted(?:\s|$|[.,;])",
        re.IGNORECASE,
    )


def _accepted_group3(store, root: str, amendment_id: str, pinned: str | None) -> tuple[str, str]:
    ignored: list[str] = []
    if pinned is not None:
        entry = store.resolve(pinned, root, "group-3 decision folder")
        folders = [(posixpath.basename(pinned), entry.path)] if entry and entry.kind == "tree" else []
    else:
        found, ignored = _group_folders(store, root, amendment_id, "3")
        folders = [(name, path) for _, name, path in reversed(found)]
    heading_re = _heading_re(amendment_id)
    problems = []
    for name, path in folders:
        decision = store.resolve(_join(path, "DECISION.md"), root, "group-3 DECISION.md")
        manifest = store.resolve(_join(path, "ACCEPTED_MANIFEST.csv"), root, "group-3 ACCEPTED_MANIFEST.csv")
        if not (decision and decision.kind == "blob" and manifest and manifest.kind == "blob"):
            problems.append(f"{name} lacks DECISION.md or ACCEPTED_MANIFEST.csv")
            continue
        heading = _first_line(_decode(store.read(decision)))
        if heading_re.match(heading):
            return path, decision.path
        problems.append(f"{name}/DECISION.md first line does not record group-3 acceptance: {heading!r}")
    if ignored:
        problems.append(
            f"ignored {', '.join(ignored)} (not named {amendment_id}_GROUP-3_[AMENDMENT-K_]YYYY-MM-DD[_N]; candidate folders do not count)"
        )
    if not folders:
        earlier = [name for g in ("1", "2") for _, name, _ in _group_folders(store, root, amendment_id, g)[0]]
        problems.insert(
            0,
            f"no checkpoint_snapshots/{amendment_id}_GROUP-3_* decision snapshot"
            + (" at the commit" if store.anchored else "")
            + (f" (only {', '.join(earlier)}; a group-1 or group-2 decision does not authorize reopening)" if earlier else ""),
        )
    raise _Refusal(GROUP3_NOT_ACCEPTED, "; ".join(problems))


def _read_manifest(text: str) -> tuple[list[str], list[dict[str, str]]]:
    reader = csv.DictReader(io.StringIO(text, newline=""))
    rows = [
        {(k or "").strip(): (v.strip() if isinstance(v, str) else "") for k, v in row.items()}
        for row in reader
    ]
    return [h.strip() for h in (reader.fieldnames or [])], rows


def _manifest_binding(store, manifest: _Entry, root: str) -> tuple[_Entry | None, str, str] | None:
    """Return (register entry or None when missing, lexical path, bound SHA) or None when unbound."""
    header, rows = _read_manifest(_decode(store.read(manifest)))
    lookup = {h.lower().replace("-", ""): h for h in header}
    path_col, sha_col, role_col = lookup.get("path"), lookup.get("sha256"), lookup.get("role")
    if not path_col or not sha_col:
        raise _Refusal(MANIFEST_SCHEMA, f"{manifest.path} has no Path and SHA256 columns")
    candidates = [r for r in rows if REGISTER_NAME_RE.match(posixpath.basename(r.get(path_col, "")))]
    if len(candidates) > 1 and role_col:
        named = [r for r in candidates if REGISTER_ROLE_RE.match(r.get(role_col, ""))]
        if len(named) == 1:
            candidates = named
    if not candidates:
        return None
    if len({(r[path_col], r[sha_col].lower()) for r in candidates}) > 1:
        raise _Refusal(
            REGISTER_AMBIGUOUS,
            f"{manifest.path} binds several Amendment_Actions*.csv files and no single row's Role is the action register",
        )
    raw_path = candidates[0][path_col]
    bound_sha = candidates[0][sha_col].lower()
    if raw_path.startswith("/") or Path(raw_path).is_absolute():
        raise _Refusal(PATH_ESCAPE, f"register path in {manifest.path} is absolute: {raw_path}")
    # Manifest paths are project-root relative; accept paths relative to the
    # execution root's parent too. A missing file resolves to the in-root
    # candidate so the refusal names the missing register, not an escape.
    project_dir = posixpath.dirname(posixpath.dirname(root))
    options = []
    for option in (raw_path, _join(project_dir, raw_path)):
        normal = posixpath.normpath(option)
        if normal != ".." and not normal.startswith("../") and normal not in options:
            options.append(normal)
    escaped, missing = False, None
    for option in options:
        try:
            entry = store.resolve(option, "", "register")
        except _Refusal:
            escaped = True
            continue
        if entry is None:
            if missing is None and _inside_rel(option, root):
                missing = option
            continue
        if not _inside_rel(entry.path, root):
            escaped = True
            continue
        return entry, option, bound_sha
    if escaped or missing is None:
        raise _Refusal(
            PATH_ESCAPE,
            f"register {raw_path} bound in {manifest.path} resolves outside the scope-change root (path or symlink escape)",
        )
    return None, missing, bound_sha


def _bound_register(store, root: str, amendment_id: str) -> tuple[_Entry | None, str, str, str]:
    """Binding of the latest group-2 decision snapshot that binds a register."""
    found, _ = _group_folders(store, root, amendment_id, "2")
    manifests = []
    for _, name, path in found:
        entry = store.resolve(_join(path, "ACCEPTED_MANIFEST.csv"), root, "group-2 ACCEPTED_MANIFEST.csv")
        if entry is not None and entry.kind == "blob":
            manifests.append(entry)
    if not manifests:
        raise _Refusal(
            GROUP2_MANIFEST_MISSING,
            f"no checkpoint_snapshots/{amendment_id}_GROUP-2_*/ACCEPTED_MANIFEST.csv binds the accepted register"
            + (" at the commit" if store.anchored else ""),
        )
    for manifest in reversed(manifests):
        binding = _manifest_binding(store, manifest, root)
        if binding is not None:
            entry, lexical, sha = binding
            return entry, lexical, sha, manifest.path
    raise _Refusal(REGISTER_NOT_BOUND, f"no group-2 ACCEPTED_MANIFEST.csv of {amendment_id} binds an Amendment_Actions*.csv register")


def _matches_deliverable(entity_id: str, del_id: str) -> bool:
    return entity_id == del_id or entity_id.startswith(del_id + "_")


def _qualifying_row(text: str, register_path: str, amendment_id: str, del_id: str) -> tuple[dict, bool]:
    reader = csv.DictReader(io.StringIO(text, newline=""))
    header = list(reader.fieldnames or [])
    rows = [{k: (v if isinstance(v, str) else "") for k, v in row.items() if k is not None} for row in reader]
    padded = [h for h in header if h != h.strip() and h.strip() in REGISTER_COLUMNS]
    if padded:
        raise _Refusal(REGISTER_SCHEMA, f"{register_path} column name(s) carry stray whitespace: {', '.join(map(repr, padded))}")
    missing = [c for c in ("ActionType", "EntityType", "EntityID") if c not in header]
    if missing:
        raise _Refusal(REGISTER_SCHEMA, f"{register_path} lacks column(s) {', '.join(missing)}")
    has_scope = "ScopeChanging" in header
    for index, row in enumerate(rows, start=2):
        if row.get("EntityType", "").strip().upper() != "DELIVERABLE":
            continue
        if not _matches_deliverable(row.get("EntityID", "").strip(), del_id):
            continue
        padded_values = [c for c in REGISTER_COLUMNS if row.get(c, "") != row.get(c, "").strip()]
        if padded_values:
            raise _Refusal(
                REGISTER_SCHEMA,
                f"{register_path} line {index} (ActionSeq {row.get('ActionSeq') or '?'}) has stray whitespace in "
                + ", ".join(f"{c} {row.get(c, '')!r}" for c in padded_values),
            )
    named = [
        r
        for r in rows
        if r.get("EntityType", "").upper() == "DELIVERABLE"
        and _matches_deliverable(r.get("EntityID", ""), del_id)
        and r.get("AmendmentID", "") in ("", amendment_id)
    ]
    if not named:
        raise _Refusal(NO_DELIVERABLE_ACTION, f"no {amendment_id} register row names DELIVERABLE {del_id}")
    seqs = ", ".join(f"{r.get('ActionSeq') or '?'} {r.get('ActionType') or '?'}" for r in named)
    removes = [r for r in named if r.get("ActionType", "").upper() == "REMOVE"]
    if removes:
        raise _Refusal(
            DELIVERABLE_REMOVED,
            f"{amendment_id} removes {del_id} (ActionSeq {', '.join(r.get('ActionSeq') or '?' for r in removes)}); "
            f"a removed deliverable is not reopened, whatever other rows name it ({seqs})",
        )
    for row in named:
        action = row.get("ActionType", "").upper()
        if action == "MODIFY":
            return row, has_scope
        if action == "RECLASSIFY" and has_scope and row.get("ScopeChanging", "").upper() == "YES":
            return row, has_scope
    reclassify = [r for r in named if r.get("ActionType", "").upper() == "RECLASSIFY"]
    if reclassify and not has_scope:
        raise _Refusal(
            RECLASSIFY_LEGACY_REGISTER,
            f"{del_id} is named only by RECLASSIFY in a register without the ScopeChanging column (legacy); "
            "the human records a scope-changing reopening directly, citing the accepted snapshot",
        )
    if reclassify:
        values = ", ".join(repr(r.get("ScopeChanging", "")) for r in reclassify)
        raise _Refusal(RECLASSIFY_NOT_SCOPE_CHANGING, f"{del_id} RECLASSIFY row(s) record ScopeChanging {values}, not YES")
    raise _Refusal(
        ACTION_NOT_AUTHORIZING,
        f"rows naming {del_id} ({seqs}) are not MODIFY or scope-changing RECLASSIFY",
    )


def _prior_reopening(status_text: str, amendment_id: str) -> str | None:
    pattern = re.compile(r"reopened from ISSUED; amendment: " + re.escape(amendment_id) + r"(?=[\s(;\]]|$)")
    for line in status_text.splitlines():
        if pattern.search(line):
            return line.strip()
    return None


def _anchor(proj: Path, at_commit: str) -> str:
    """Resolve ``at_commit`` to a full commit SHA that is an ancestor of HEAD."""
    value = at_commit.strip()
    if not value or value.startswith("-"):
        raise _Refusal(APPROVAL_SHA_UNREACHABLE, f"--at-commit {at_commit!r} is not a commit")
    out = subprocess.run(
        ["git", "-C", str(proj), "rev-parse", "--verify", "--quiet", f"{value}^{{commit}}"],
        capture_output=True,
        text=True,
        check=False,
        env=_git_env(),
    )
    if out.returncode != 0 or not out.stdout.strip():
        raise _Refusal(APPROVAL_SHA_UNREACHABLE, f"{at_commit} is not a reachable commit in this repository")
    full = out.stdout.strip()
    ancestry = subprocess.run(
        ["git", "-C", str(proj), "merge-base", "--is-ancestor", full, "HEAD"],
        capture_output=True,
        text=True,
        check=False,
        env=_git_env(),
    )
    if ancestry.returncode == 1:
        raise _Refusal(
            APPROVAL_SHA_NOT_ANCESTOR,
            f"{at_commit} is not an ancestor of HEAD; cite a commit on this branch's history (a side-branch commit does not count)",
        )
    if ancestry.returncode != 0:
        raise UsageError(f"cannot test whether {at_commit} is an ancestor of HEAD: {ancestry.stderr.strip()}")
    return full


def check_reopen(
    deliverable: str,
    amendment: str,
    *,
    at_commit: str | None = None,
    status_file: str | os.PathLike | None = None,
    scope_change_root: str | os.PathLike | None = None,
    project_root: str | os.PathLike | None = None,
    cwd: str | os.PathLike | None = None,
) -> ReopenDecision:
    """Decide whether ``amendment`` authorizes reopening ``deliverable``.

    With ``at_commit`` every amendment record is read from that commit, which
    must be an ancestor of ``HEAD``; without it the working tree is read and
    the decision is unanchored. ``status_file`` is the deliverable's live
    ``_STATUS.md``, checked for a prior reopening under the same amendment.

    Raises ``UsageError`` for unusable input; every other outcome is a
    ``ReopenDecision`` whose ``admitted`` is True only when all checks pass.
    """
    base = _real(Path(cwd) if cwd is not None else Path.cwd())
    del_id, del_path = _normalize_deliverable(deliverable, base)
    decision = ReopenDecision(False, "", "", deliverable_id=del_id)

    if project_root is not None:
        proj = Path(project_root)
        if not proj.is_absolute():
            proj = base / proj
    else:
        anchor = del_path or (Path(scope_change_root) if scope_change_root else base)
        if not anchor.is_absolute():
            anchor = base / anchor
        proj = _git_toplevel(anchor)
        if proj is None:
            raise UsageError("cannot resolve the project root (not a git checkout); pass --project-root")
    if not proj.is_dir():
        raise UsageError(f"project root is not a directory: {proj}")
    proj = _real(proj)

    status_text = None
    if status_file is not None:
        status_path = Path(status_file)
        if not status_path.is_absolute():
            status_path = base / status_path
        try:
            status_text = status_path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            raise UsageError(f"cannot read --status-file {status_file}: {exc}") from exc

    if at_commit is not None:
        top = _git_toplevel(proj)
        if top is None or _real(top) != proj:
            raise UsageError(f"--at-commit needs the project root to be the git top level (got {proj})")
        decision.mode = "at-commit"
    else:
        decision.notes.append(UNANCHORED_NOTE)

    try:
        store: _WorkTree | _GitTree
        if at_commit is not None:
            decision.at_commit = _anchor(proj, at_commit)
            decision.anchored = True
            store = _GitTree(proj, decision.at_commit)
        else:
            store = _WorkTree(proj)

        exec_root = None
        if del_path is not None:
            del_real = _real(del_path)
            if not _inside(del_real, proj):
                raise _Refusal(PATH_ESCAPE, f"deliverable folder {del_path} resolves outside {proj} (path or symlink escape)")
            exec_root = _execution_root(del_real, proj)
            decision.execution_root = exec_root

        amendment_id, derived_root, pinned = _resolve_amendment(store, amendment, base, proj)
        decision.amendment_id = amendment_id

        if status_text is not None:
            prior = _prior_reopening(status_text, amendment_id)
            if prior is not None:
                raise _Refusal(
                    AMENDMENT_ALREADY_USED,
                    f"_STATUS.md already records a reopening under {amendment_id} ({prior}); one tool-recorded "
                    "reopening per accepted amendment; a further reopening needs a new amendment or a direct human record",
                )

        root: str | None = None
        if scope_change_root is not None:
            rel = _to_rel(str(scope_change_root), base, proj)
            if rel is None:
                raise _Refusal(PATH_ESCAPE, f"--scope-change-root {scope_change_root} lies outside the project root")
            entry = store.resolve(rel, "", "--scope-change-root")
            if entry is None or entry.kind != "tree":
                raise _Refusal(SCOPE_CHANGE_ROOT_NOT_FOUND, f"--scope-change-root is not a directory: {scope_change_root}")
            root = entry.path
        if derived_root is not None:
            entry = store.resolve(derived_root, "", "scope-change root")
            if entry is None or entry.kind != "tree":
                raise _Refusal(AMENDMENT_UNRESOLVED, f"scope-change root {derived_root} of --amendment is not a directory")
            if root is not None and root != entry.path:
                raise _Refusal(AMENDMENT_UNRESOLVED, "--amendment path is not under --scope-change-root")
            root = entry.path
        expected = _join(exec_root, "_ScopeChange") if exec_root is not None else None
        if root is None:
            if expected is None:
                raise _Refusal(
                    SCOPE_CHANGE_ROOT_NOT_FOUND,
                    "an amendment ID with a deliverable ID needs --scope-change-root or a deliverable folder",
                )
            entry = store.resolve(expected, "", "scope-change root")
            if entry is None or entry.kind != "tree":
                raise _Refusal(
                    SCOPE_CHANGE_ROOT_NOT_FOUND,
                    f"no {expected}/ beside the deliverable's execution root" + (" at the commit" if store.anchored else ""),
                )
            root = entry.path
        decision.scope_change_root = root
        if expected is not None and root != expected:
            raise _Refusal(
                AMENDMENT_OUTSIDE_DELIVERABLE_ROOT,
                f"{root} is not {expected}, the scope-change root of the deliverable's execution root {exec_root}",
            )

        group3, group3_decision = _accepted_group3(store, root, amendment_id, pinned)
        decision.group3_snapshot = group3
        decision.group3_decision = group3_decision

        register, lexical, bound_sha, manifest = _bound_register(store, root, amendment_id)
        decision.group2_manifest = manifest
        decision.register_path = register.path if register is not None else lexical
        if register is None or register.kind != "blob":
            raise _Refusal(
                REGISTER_MISSING,
                f"bound register {decision.register_path} does not exist" + (" at the commit" if store.anchored else ""),
            )
        data = store.read(register)
        actual = hashlib.sha256(data).hexdigest()
        decision.register_sha256 = actual
        if actual != bound_sha:
            raise _Refusal(
                REGISTER_HASH_MISMATCH,
                f"{decision.register_path} SHA-256 {actual} differs from {bound_sha} bound in {decision.group2_manifest}",
            )

        row, has_scope = _qualifying_row(_decode(data), decision.register_path, amendment_id, del_id)
        if not has_scope:
            decision.notes.append("legacy register without ScopeChanging: RECLASSIFY is not admitted by this tool")
        decision.action_seq = row.get("ActionSeq", "")
        decision.action_type = row.get("ActionType", "").upper()
        decision.scope_changing = row.get("ScopeChanging") if has_scope else None
    except _Refusal as refusal:
        decision.code = refusal.code
        decision.reason = refusal.reason
        return decision
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        raise UsageError(f"cannot read amendment records: {exc}") from exc

    decision.admitted = True
    decision.code = ADMITTED
    where = f"at commit {decision.at_commit}" if decision.anchored else "in the working tree (unanchored)"
    decision.reason = (
        f"{amendment_id} accepted at group 3 ({decision.group3_snapshot}); register "
        f"{decision.register_path} matches its group-2 hash; ActionSeq {decision.action_seq or '?'} "
        f"{decision.action_type} names {del_id}; records read {where}"
    )
    return decision


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("--deliverable", required=True, help="deliverable ID or deliverable folder")
    parser.add_argument("--amendment", required=True, help="amendment ID (SCA-NNN, SCA-APP-NNN) or snapshot path")
    parser.add_argument(
        "--at-commit",
        help="read every amendment record from this commit (an ancestor of HEAD); without it the working tree is read, unanchored",
    )
    parser.add_argument("--status-file", help="the deliverable's _STATUS.md, checked for a reopening already recorded under the amendment")
    parser.add_argument("--scope-change-root", help="the _ScopeChange/ folder (default: <execution root>/_ScopeChange of the deliverable folder)")
    parser.add_argument("--project-root", help="containment root (default: git top level)")
    parser.add_argument("--json", action="store_true", help="print the decision as JSON on stdout")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        decision = check_reopen(
            args.deliverable,
            args.amendment,
            at_commit=args.at_commit,
            status_file=args.status_file,
            scope_change_root=args.scope_change_root,
            project_root=args.project_root,
        )
    except UsageError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(decision.to_json(), indent=2, sort_keys=True))
    elif decision.admitted:
        label = "ADMIT" if decision.anchored else "ADMIT (UNANCHORED working-tree read; not usable for write_status.sh)"
        print(f"{label}: {decision.reason}")
    if not decision.admitted:
        suffix = " [working tree, unanchored]" if decision.mode == "working-tree" else ""
        print(f"REFUSE {decision.code}: {decision.reason}{suffix}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
