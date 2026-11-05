#!/usr/bin/env python3
"""Prepare/check current PKG/DEL localities without authoring commitments.

The shell entrypoints select this route with --current. Unflagged shell calls
retain their legacy contract. Python 3 and PyYAML are required.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import os
from pathlib import Path
import re
import stat
import sys
import uuid

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.deliverables.cli import Invalid, UniqueLoader, parse

PACKAGE = re.compile(r"PKG-(\d+)")
DELIVERABLE = re.compile(r"(DEL-(\d+)-\d+)(?:_[^/\\]+)?")


@contextmanager
def directory(path=None, *, parent=None, name=None):
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(str(path) if parent is None else name, flags, dir_fd=parent)
    try:
        yield fd
    finally:
        os.close(fd)


def read_regular(parent, name, *, required=False):
    try:
        fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    except FileNotFoundError:
        if required:
            raise Invalid(f"missing {name}")
        return None
    with os.fdopen(fd, "r", encoding="utf-8") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise Invalid(f"{name} must be a regular file, not a link or special file")
        return stream.read()


def inspect_work(parent, *, required=False):
    try:
        mode = os.stat("Work", dir_fd=parent, follow_symlinks=False).st_mode
    except FileNotFoundError:
        if required:
            raise Invalid("missing Work/")
        return
    if not stat.S_ISDIR(mode):
        raise Invalid("Work must be a directory, not a link or file")


def inspect_identity(parent, identity, package, *, required=False, authored=False):
    declaration = read_regular(parent, "deliverable.yaml", required=required)
    if declaration is not None:
        parse(declaration, "deliverable.yaml", expected_id=identity)
    scope = read_regular(parent, "ScopeOfWork.md", required=authored)
    if scope is not None:
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", scope, re.S)
        fields = yaml.load(match.group(1), Loader=UniqueLoader) if match else None
        if not isinstance(fields, dict) or (
            fields.get("schema") != "chirality-deliverable-sow/v1"
            or fields.get("deliverable_id") != identity
            or fields.get("package_id") != package
        ):
            raise Invalid("ScopeOfWork.md schema or package/deliverable identity disagrees")


def make_directory(parent, name, display):
    try:
        os.mkdir(name, dir_fd=parent)
    except FileExistsError:
        return
    print(f"CREATED_PATH: {display}")


def write_declaration(parent, identity, label, display):
    data = yaml.safe_dump({"id": identity, "name": label, "needs": []}, sort_keys=False)
    temporary = ".deliverable-" + uuid.uuid4().hex
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                 0o666, dir_fd=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(data)
        try:
            # Publish complete bytes without replacing a concurrent or older file.
            os.link(temporary, "deliverable.yaml", src_dir_fd=parent,
                    dst_dir_fd=parent, follow_symlinks=False)
        except FileExistsError:
            return
        print(f"CREATED_PATH: {display / 'deliverable.yaml'}")
    finally:
        os.unlink(temporary, dir_fd=parent)


def native_identity(value):
    match = DELIVERABLE.fullmatch(value)
    if not match:
        raise Invalid("expected an accepted DEL numeric identity, optionally with a suffix")
    return match.group(1), "PKG-" + match.group(2)


def prepare_package(args):
    if not PACKAGE.fullmatch(args.identity):
        raise Invalid("current package identity must be PKG-<number>")
    root = args.parent.resolve(strict=True)
    with directory(root) as parent:
        target = root / args.identity
        make_directory(parent, args.identity, target)
        with directory(parent=parent, name=args.identity):
            pass
    print(f"Package: {target}")


def prepare_deliverable(args):
    identity, package = native_identity(args.identity)
    root = args.parent.resolve(strict=True)
    if root.name != package:
        raise Invalid("deliverable package identity disagrees with supplied package folder")
    target = root / identity
    with directory(root) as parent:
        make_directory(parent, identity, target)
        with directory(parent=parent, name=identity) as folder:
            # Inspect existing work before adding anything inside an existing DEL.
            inspect_work(folder)
            inspect_identity(folder, identity, package)
            make_directory(folder, "Work", target / "Work")
            with directory(parent=folder, name="Work"):
                pass
            write_declaration(folder, identity, args.label, target)
            inspect_identity(folder, identity, package, required=True)
    print(f"Prepared: {target}; ScopeOfWork authoring remains separate")


def check(args):
    # Resolve the parent, preserving the final component for no-follow inspection.
    target = args.target.parent.resolve(strict=True) / args.target.name
    identity, package = native_identity(target.name)
    if target.name != identity or target.parent.name != package:
        raise Invalid("expected a current PKG-nn/DEL-nn-nn locality")
    if args.accepted and native_identity(args.accepted)[0] != identity:
        raise Invalid("accepted deliverable identity disagrees with the locality")
    with directory(target) as folder:
        inspect_work(folder, required=True)
        inspect_identity(folder, identity, package, required=True, authored=not args.prepared)
    stage = "prepared" if args.prepared else "authored"
    print(f"PASS: {identity} — {stage} locality structure/identity; no acceptance claim")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("package", "deliverable"):
        sub = commands.add_parser(command)
        sub.add_argument("parent", type=Path)
        sub.add_argument("identity")
        sub.add_argument("label")
    sub = commands.add_parser("check")
    sub.add_argument("target", type=Path)
    sub.add_argument("accepted", nargs="?")
    sub.add_argument("--prepared", action="store_true",
                     help="check structural preparation before ScopeOfWork authoring")
    args = parser.parse_args()
    try:
        if args.command != "check" and not args.label.strip():
            raise Invalid("the accepted name must be nonempty")
        {"package": prepare_package, "deliverable": prepare_deliverable, "check": check}[args.command](args)
    except (Invalid, OSError, ValueError, yaml.YAMLError, RecursionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1 if args.command == "check" else 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
