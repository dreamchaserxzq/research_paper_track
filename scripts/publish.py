#!/usr/bin/env python3
"""Publish an explicitly scoped, checked snapshot and verify remote main.

No command rebases, resets, cleans, or stages unrelated files. A rejected push
leaves the local commit available for inspection and a fresh deduplication pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath


ROOT_FILES = {
    "README.md", "CLAUDE.md", "AGENTS.md", "seen_papers.txt", "run_log.md",
    "run_log_published.md", "run_log_status.md", "run_log_status_update.md", ".gitignore", ".gitattributes",
}
ALLOWED_DIRECTORIES = {"digests", "docs", "metadata", "scripts", "tests", "schemas", ".github"}
ALLOWED_SUFFIXES = {".md", ".json", ".jsonl", ".txt", ".py", ".yml", ".yaml"}
DAILY_NAME = re.compile(r"(?:PDE-FM|AI-for-PDE)-日报-\d{8}\.md$")


class PublicationError(RuntimeError):
    """An actionable publication or verification failure."""


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(
        ["git", "-C", str(repo), "--literal-pathspecs", *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        detail = (result.stderr or result.stdout).decode("utf-8", "replace").strip()
        raise PublicationError(f"git {' '.join(args)} failed: {detail}")
    return result


def git_text(repo: Path, *args: str) -> str:
    return git(repo, *args).stdout.decode("utf-8", "replace").strip()


def repository(path: str) -> Path:
    return Path(git_text(Path(path).resolve(), "rev-parse", "--show-toplevel"))


def validate_paths(repo: Path, paths: list[str]) -> list[str]:
    """Accept only literal, repository-relative files in maintenance locations."""
    checked = []
    for raw in paths:
        path = PurePosixPath(raw)
        if (
            not raw or raw != path.as_posix() or path.is_absolute()
            or ".." in path.parts or raw.startswith(("-", ":"))
            or any(char in raw for char in "*?[]\\\n\r\0")
        ):
            raise PublicationError(f"Use an exact repository-relative file path: {raw!r}")
        allowed = raw in ROOT_FILES or (
            len(path.parts) > 1 and path.parts[0] in ALLOWED_DIRECTORIES
            and path.suffix in ALLOWED_SUFFIXES
        )
        if not allowed:
            raise PublicationError(f"Path is outside the publication allowlist: {raw}")
        local = repo / raw
        if local.is_dir():
            raise PublicationError(f"Directories are not publication scopes: {raw}")
        # Also reject symlinks within the repository, since checkout-index would
        # otherwise validate through a link that could escape the staged copy.
        cursor = local
        while cursor != repo:
            if cursor.is_symlink():
                raise PublicationError(f"Publication paths cannot traverse symlinks: {raw}")
            cursor = cursor.parent
        if raw not in checked:
            checked.append(raw)
    if not checked:
        raise PublicationError("At least one explicit file path is required.")
    return checked


def staged_paths(repo: Path) -> set[str]:
    return {
        name.decode("utf-8") for name in git(
            repo, "diff", "--cached", "--name-only", "--no-renames", "-z"
        ).stdout.split(b"\0") if name
    }


def check_scope(repo: Path, paths: list[str]) -> None:
    outsiders = staged_paths(repo) - set(paths)
    if outsiders:
        raise PublicationError(
            "Already staged files are outside --files; inspect the index first: "
            + ", ".join(sorted(outsiders))
        )


def check_snapshot(root: Path) -> None:
    checker = root / "scripts" / "papertrack.py"
    if not checker.is_file():
        raise PublicationError(f"Required validator is missing: {checker}")
    result = subprocess.run(
        [sys.executable, str(checker), "check"], cwd=root,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode:
        raise PublicationError("papertrack.py check failed; no commit or push was performed.")


def tree_files(repo: Path, revision: str) -> dict[str, tuple[str, str]]:
    files = {}
    for entry in git(repo, "ls-tree", "-r", "-z", revision).stdout.split(b"\0"):
        if entry:
            head, path = entry.split(b"\t", 1)
            mode, kind, oid = head.decode().split()
            files[path.decode("utf-8")] = (mode, oid)
    return files


def verify(repo: Path, commit: str, paths: list[str]) -> dict:
    """Refresh the remote tracking ref and compare the submitted files to main."""
    submitted = git_text(repo, "rev-parse", "--verify", "--end-of-options", f"{commit}^{{commit}}")
    git(repo, "fetch", "--no-tags", "origin", "+refs/heads/main:refs/remotes/origin/main")
    remote = git_text(repo, "rev-parse", "refs/remotes/origin/main")
    ancestry = git(repo, "merge-base", "--is-ancestor", submitted, remote, check=False)
    if ancestry.returncode:
        if ancestry.returncode != 1:
            raise PublicationError(ancestry.stderr.decode("utf-8", "replace"))
        raise PublicationError(
            f"Remote main {remote} does not contain submitted commit {submitted}. "
            "Publication is incomplete; inspect main and rebuild against its latest data."
        )
    expected = tree_files(repo, submitted)
    actual = tree_files(repo, remote)
    deletions = {
        name.decode("utf-8") for name in git(
            repo, "diff-tree", "--no-commit-id", "--name-only", "--diff-filter=D",
            "-z", "-r", "-m", submitted,
        ).stdout.split(b"\0") if name
    }
    unknown = [path for path in paths if path not in expected and path not in deletions]
    if unknown:
        raise PublicationError(
            "Requested paths do not exist in the submitted snapshot and are not deletions in that commit: "
            + ", ".join(unknown)
        )
    mismatched = [path for path in paths if expected.get(path) != actual.get(path)]
    if mismatched:
        raise PublicationError(
            f"Remote main contains {submitted}, but file content or mode changed before readback: "
            + ", ".join(mismatched)
            + ". Inspect concurrent changes; this snapshot is not confirmed as the current publication."
        )
    return {
        "status": "verified", "submitted_commit": submitted,
        "verified_remote_main": remote,
        "files": {path: actual.get(path, (None, None))[1] for path in paths},
        "boundary": "Verified at fetch time; later remote changes are not covered.",
    }


def publish(repo: Path, message: str, paths: list[str]) -> dict:
    if not message.strip() or not message.isascii() or not re.search(r"[A-Za-z]", message):
        raise PublicationError("Use a nonempty English commit message.")
    if "\n" in message or "\r" in message:
        raise PublicationError("Use a one-line scoped English commit message.")
    git_text(repo, "symbolic-ref", "--quiet", "--short", "HEAD")
    check_scope(repo, paths)
    check_snapshot(repo)
    git(repo, "add", "--", *paths)
    check_scope(repo, paths)
    git(repo, "diff", "--cached", "--check")
    if not staged_paths(repo):
        raise PublicationError("No scoped changes to commit; use verify for an existing commit.")
    # Validation of the working tree alone could include fixes omitted by the
    # explicit --files list. Check exactly what will be committed as well.
    tree = git_text(repo, "write-tree")
    with tempfile.TemporaryDirectory(prefix="papertrack-index-") as temp:
        git(repo, "checkout-index", "--all", "--prefix", str(Path(temp)) + "/")
        check_snapshot(Path(temp))
    print(git_text(repo, "diff", "--cached", "--stat"))
    if git_text(repo, "write-tree") != tree:
        raise PublicationError("The index changed during validation; inspect and retry.")
    git(repo, "commit", "-m", message)
    submitted = git_text(repo, "rev-parse", "HEAD")
    if git_text(repo, "rev-parse", "HEAD^{tree}") != tree:
        raise PublicationError(
            f"Commit {submitted} differs from the validated index, possibly due to a hook; "
            "nothing was pushed. Inspect and rerun validation."
        )
    main_push = git(repo, "push", "origin", "HEAD:main", check=False)
    if main_push.returncode:
        raise PublicationError(
            f"Main push failed; local commit {submitted} is retained. "
            "Fetch origin, review concurrent changes, rebuild/deduplicate the registry and reports, "
            "then validate again. No automatic rebase or retry was attempted.\n"
            + main_push.stderr.decode("utf-8", "replace").strip()
        )
    branch_push = git(repo, "push", "origin", "HEAD", check=False)
    result = verify(repo, submitted, paths)
    if branch_push.returncode:
        raise PublicationError(
            f"Main was verified at {result['verified_remote_main']}, but the required current-branch "
            "push failed; publication is only partially complete. Retry that push after inspecting "
            "the branch state.\n" + branch_push.stderr.decode("utf-8", "replace").strip()
        )
    result["current_branch_push"] = "succeeded"
    return result


def sha256_blob(repo: Path, oid: str) -> str:
    return hashlib.sha256(git(repo, "cat-file", "blob", oid).stdout).hexdigest()


def recovery_records(repo: Path, main_files: dict) -> list[dict]:
    records = []
    # Main manifests establish published provenance. Working tree manifests can
    # only establish that a recovery is prepared, pending publication.
    candidates = [("remote_main", name) for name in main_files
                  if re.fullmatch(r"metadata/recovery[^/]*\.json", name)]
    candidates += [("worktree", path.relative_to(repo).as_posix())
                   for path in sorted((repo / "metadata").glob("recovery*.json"))]
    for location, name in candidates:
        try:
            raw = (git(repo, "cat-file", "blob", main_files[name][1]).stdout
                   if location == "remote_main" else (repo / name).read_bytes())
            document = json.loads(raw)
            for record in document.get("recovered_digests", []):
                records.append({**record, "manifest": name, "manifest_location": location})
        except (OSError, ValueError, TypeError) as error:
            raise PublicationError(f"Cannot read recovery manifest {name}: {error}") from error
    return records


def audit_branches(repo: Path) -> dict:
    """Inspect existing remote refs only; do not fetch or mutate repository state."""
    main = git_text(repo, "rev-parse", "--verify", "refs/remotes/origin/main")
    main_files = tree_files(repo, main)
    daily_main = {name: value for name, value in main_files.items() if DAILY_NAME.search(name)}
    main_by_name = {}
    for name, value in daily_main.items():
        main_by_name.setdefault(PurePosixPath(name).name, []).append((name, value))
    records = recovery_records(repo, main_files)
    refs = git_text(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").splitlines()
    findings, examined = [], 0
    for ref in refs:
        if ref in {"refs/remotes/origin/main", "refs/remotes/origin/HEAD"}:
            continue
        if git(repo, "merge-base", "--is-ancestor", ref, main, check=False).returncode == 0:
            continue
        examined += 1
        for path, value in tree_files(repo, ref).items():
            if not DAILY_NAME.search(path):
                continue
            matches = main_by_name.get(PurePosixPath(path).name, [])
            if any(value == main_value for _, main_value in matches):
                continue
            finding = {
                "branch": ref.removeprefix("refs/remotes/"), "path": path, "source_blob": value[1],
                "status": "content_diverged" if matches else "missing_from_main",
                "main_paths_with_same_name": [name for name, _ in matches],
            }
            for record in records:
                if record.get("source_path") != path or record.get("source_blob") != value[1]:
                    continue
                restored = record.get("restored_path")
                digest = record.get("restored_sha256")
                if (not restored or not digest or not record.get("byte_identical")
                        or digest != record.get("sha256")
                        or record.get("sha256") != sha256_blob(repo, value[1])):
                    continue
                remote_entry = main_files.get(restored)
                if remote_entry and sha256_blob(repo, remote_entry[1]) == digest:
                    finding.update(status="recovered_on_main", manifest=record["manifest"], restored_path=restored)
                    break
                local = repo / restored
                if (record["manifest_location"] == "worktree" and local.is_file()
                        and local.resolve().is_relative_to(repo)
                        and hashlib.sha256(local.read_bytes()).hexdigest() == digest):
                    finding.update(status="recovered_worktree_pending_publication", manifest=record["manifest"], restored_path=restored)
            findings.append(finding)
    return {
        "status": "audited_local_remote_refs", "remote_main": main,
        "branches_examined": examined, "findings": findings,
        "boundary": "No network fetch performed; run git fetch origin --prune first for current remote refs. "
                    "Different content is reported for review, not treated as a missing run or an equivalent recovery.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root (default: current directory)")
    commands = parser.add_subparsers(dest="command", required=True)
    send = commands.add_parser("publish", help="Validate, explicitly stage, commit, push, and verify")
    send.add_argument("--message", required=True)
    send.add_argument("--files", nargs="+", required=True)
    readback = commands.add_parser("verify", help="Fetch and verify a previously submitted commit")
    readback.add_argument("--commit", required=True)
    readback.add_argument("--files", nargs="+", required=True)
    commands.add_parser("audit-branches", help="Read-only audit of existing remote branch refs")
    args = parser.parse_args(argv)
    try:
        repo = repository(args.repo)
        if args.command == "audit-branches":
            result = audit_branches(repo)
        else:
            paths = validate_paths(repo, args.files)
            result = (publish(repo, args.message, paths) if args.command == "publish"
                      else verify(repo, args.commit, paths))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (PublicationError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
