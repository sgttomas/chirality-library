"""Resolve references into archived agent run records (D-GOV-45).

tools/archive_agent_runs.py removes closed run records from the working tree
and lists them in `<execution>/_Coordination/AgentRuns/ARCHIVE_INDEX.json`,
with the immutable tag that holds their exact bytes. A reference to an
archived run folder, or to a path inside one, or to an archived file, is a
reference to preserved history: it resolves, and archived records are not
re-checked (run records are history, not tested).
"""
from __future__ import annotations

from functools import lru_cache
import json
from pathlib import Path, PurePosixPath

INDEX_GLOBS = ("execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json",
               "projects/*/execution/_Coordination/AgentRuns/ARCHIVE_INDEX.json")


@lru_cache(maxsize=8)
def _entries(repo_root: str) -> tuple[dict[str, str], dict[str, str]]:
    runs: dict[str, str] = {}
    files: dict[str, str] = {}
    root = Path(repo_root)
    for pattern in INDEX_GLOBS:
        for index in sorted(root.glob(pattern)):
            for archive in json.loads(index.read_text(encoding="utf-8")).get("archives", []):
                # Only run records can be archived: an index entry outside
                # `_Coordination/AgentRuns/<RUN>` never resolves anything.
                runs.update({run: archive["tag"] for run in archive.get("runs", []) if _run_record(run)})
                files.update({path: archive["tag"] for path in archive.get("files", []) if _run_record(path)})
    return runs, files


def _run_record(path: str) -> bool:
    head, sep, rest = path.partition("_Coordination/AgentRuns/")
    return bool(sep and rest and ".." not in path.split("/") and (head == "" or head.endswith("execution/")))


def archive_tag(repo_root: Path, path: Path | str) -> str | None:
    """Tag holding `path` if it is (inside) an archived record, else None."""
    root = Path(repo_root).resolve()
    candidate = Path(path)
    if candidate.is_absolute():
        try:
            candidate = candidate.resolve().relative_to(root)
        except (OSError, ValueError):
            return None
    rel = PurePosixPath(candidate.as_posix())
    if ".." in rel.parts:
        return None
    runs, files = _entries(str(root))
    text = rel.as_posix().rstrip("/")
    if text in files:
        return files[text]
    for ancestor in [rel, *rel.parents]:
        if ancestor.as_posix() in runs:
            return runs[ancestor.as_posix()]
    return None
