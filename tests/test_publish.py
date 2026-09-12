"""Publication tests use disposable repositories and local bare remotes only."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "papertrack_publish", Path(__file__).resolve().parents[1] / "scripts" / "publish.py"
)
publish = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publish)


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise AssertionError(f"git {' '.join(args)} failed: {result.stderr}")
    return result.stdout.strip()


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="test-papertrack-publish-")
        self.addCleanup(self.temporary.cleanup)
        base = Path(self.temporary.name)
        self.repo = base / "working"
        self.repo.mkdir()
        self.remote = base / "remote.git"
        git(base, "init", "--bare", str(self.remote))
        git(self.repo, "init", "-b", "main")
        self.configure(self.repo)
        self.write("README.md", "initial\n")
        self.write("metadata/state.txt", "initial\n")
        self.write("scripts/papertrack.py", (
            "from pathlib import Path\n"
            "import sys\n"
            "assert sys.argv[1:] == ['check']\n"
            "assert Path('README.md').read_text() != 'needs-metadata\\n' "
            "or Path('metadata/state.txt').read_text() == 'matching\\n', "
            "'metadata mismatch in snapshot'\n"
            "print('fixture check passed')\n"
        ))
        git(self.repo, "add", "README.md", "metadata/state.txt", "scripts/papertrack.py")
        git(self.repo, "commit", "-m", "Initialize fixture")
        self.initial = git(self.repo, "rev-parse", "HEAD")
        git(self.repo, "remote", "add", "origin", str(self.remote))
        git(self.repo, "push", "-u", "origin", "main")
        git(self.remote, "symbolic-ref", "HEAD", "refs/heads/main")
        self.rival = base / "rival"
        git(base, "clone", str(self.remote), str(self.rival))
        self.configure(self.rival)

    @staticmethod
    def configure(repo):
        git(repo, "config", "user.name", "Test Bot")
        git(repo, "config", "user.email", "test@example.invalid")
        git(repo, "config", "commit.gpgsign", "false")
        git(repo, "config", "core.hooksPath", "/dev/null")

    def write(self, path, content):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def cli(self, *arguments):
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            status = publish.main(["--repo", str(self.repo), *arguments])
        return status, output.getvalue(), errors.getvalue()

    def send(self, *paths):
        return self.cli("publish", "--message", "Repair scoped digest publication", "--files", *paths)

    def advance_rival(self, path="README.md", content="concurrent update\n"):
        git(self.rival, "pull", "--ff-only", "origin", "main")
        target = self.rival / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        git(self.rival, "add", "--", path)
        git(self.rival, "commit", "-m", "Concurrent publication")
        git(self.rival, "push", "origin", "main")

    def test_publish_exact_scope_and_both_required_pushes(self):
        git(self.repo, "switch", "-c", "codex/publication")
        self.write("README.md", "updated\n")
        self.write("pelican-bicycle.html", "unrelated\n")
        self.write("docs/unrelated.md", "unselected\n")
        status, output, error = self.send("README.md")
        self.assertEqual(status, 0, error)
        head = git(self.repo, "rev-parse", "HEAD")
        self.assertEqual(git(self.remote, "rev-parse", "refs/heads/main"), head)
        self.assertEqual(git(self.remote, "rev-parse", "refs/heads/codex/publication"), head)
        self.assertEqual(git(self.repo, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"), "README.md")
        self.assertIn("verified_remote_main", output)
        self.assertIn("?? pelican-bicycle.html", git(self.repo, "status", "--short"))
        self.assertIn("?? docs/", git(self.repo, "status", "--short"))

    def test_existing_staged_outsider_is_retained_and_rejected(self):
        self.write("README.md", "updated\n")
        self.write("docs/unrelated.md", "do not commit\n")
        git(self.repo, "add", "docs/unrelated.md")
        before = git(self.repo, "write-tree")
        status, _, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("outside --files", error)
        self.assertEqual(git(self.repo, "write-tree"), before)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.initial)

    def test_rejects_html_directory_glob_and_pathspec(self):
        self.write("pelican-bicycle.html", "unrelated\n")
        for path in ["pelican-bicycle.html", "metadata", "metadata/*.txt", ":(top)README.md", "../README.md"]:
            with self.subTest(path=path):
                status, _, _ = self.send(path)
                self.assertEqual(status, 1)
        self.assertEqual(git(self.repo, "diff", "--cached", "--name-only"), "")

    def test_rejects_symlink_in_scope(self):
        (self.repo / "metadata" / "linked.txt").symlink_to(self.repo / "README.md")
        status, _, error = self.send("metadata/linked.txt")
        self.assertEqual(status, 1)
        self.assertIn("symlinks", error)

    def test_staged_snapshot_check_catches_omitted_dependency(self):
        self.write("README.md", "needs-metadata\n")
        self.write("metadata/state.txt", "matching\n")
        status, output, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("fixture check passed", output)
        self.assertIn("metadata mismatch in snapshot", output)
        self.assertIn("check failed", error)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.initial)
        self.assertEqual(git(self.remote, "rev-parse", "main"), self.initial)

    def test_staged_diff_whitespace_check_blocks_commit(self):
        self.write("README.md", "trailing space \n")
        status, _, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("diff --cached --check", error)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.initial)

    def test_non_fast_forward_retains_commit_without_rebase(self):
        self.advance_rival()
        self.write("README.md", "local publication\n")
        status, _, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("No automatic rebase", error)
        self.assertNotEqual(git(self.repo, "rev-parse", "HEAD"), self.initial)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD^"), self.initial)
        self.assertEqual((self.repo / "README.md").read_text(), "local publication\n")
        self.assertEqual(git(self.remote, "show", "main:README.md"), "concurrent update")

    def test_verify_rejects_commit_absent_from_remote_main(self):
        self.write("README.md", "local only\n")
        git(self.repo, "add", "README.md")
        git(self.repo, "commit", "-m", "Unpublished change")
        status, _, error = self.cli("verify", "--commit", "HEAD", "--files", "README.md")
        self.assertEqual(status, 1)
        self.assertIn("does not contain submitted commit", error)

    def test_verify_does_not_certify_a_nonexistent_path(self):
        status, _, error = self.cli("verify", "--commit", "HEAD", "--files", "docs/typo.md")
        self.assertEqual(status, 1)
        self.assertIn("do not exist in the submitted snapshot", error)

    def test_remote_race_changes_published_file_before_readback(self):
        self.write("README.md", "publication\n")
        original_git = publish.git
        raced = []

        def race_git(repo, *args, **kwargs):
            if args[0] == "fetch" and not raced:
                raced.append(True)
                self.advance_rival()
            return original_git(repo, *args, **kwargs)

        with patch.object(publish, "git", side_effect=race_git):
            status, _, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("content or mode changed before readback", error)
        submitted = git(self.repo, "rev-parse", "HEAD")
        self.assertEqual(git(self.remote, "rev-parse", "main^"), submitted)

    def test_remote_race_on_unrelated_path_keeps_scope_verified(self):
        self.write("README.md", "publication\n")
        original_git = publish.git
        raced = []

        def race_git(repo, *args, **kwargs):
            if args[0] == "fetch" and not raced:
                raced.append(True)
                self.advance_rival("docs/concurrent.md", "independent update\n")
            return original_git(repo, *args, **kwargs)

        with patch.object(publish, "git", side_effect=race_git):
            status, output, error = self.send("README.md")
        self.assertEqual(status, 0, error)
        self.assertIn("verified", output)

    def test_current_branch_push_failure_is_partial_success(self):
        self.write("README.md", "publication\n")
        original_git = publish.git

        def branch_failure(repo, *args, **kwargs):
            if args == ("push", "origin", "HEAD"):
                return subprocess.CompletedProcess(args, 1, b"", b"branch permission denied")
            return original_git(repo, *args, **kwargs)

        with patch.object(publish, "git", side_effect=branch_failure):
            status, _, error = self.send("README.md")
        self.assertEqual(status, 1)
        self.assertIn("only partially complete", error)
        self.assertEqual(git(self.remote, "rev-parse", "main"), git(self.repo, "rev-parse", "HEAD"))

    def test_deleted_scoped_file_is_verified_as_absent(self):
        self.write("docs/obsolete.md", "obsolete\n")
        git(self.repo, "add", "docs/obsolete.md")
        git(self.repo, "commit", "-m", "Add obsolete fixture")
        git(self.repo, "push", "origin", "main")
        (self.repo / "docs/obsolete.md").unlink()
        status, output, error = self.send("docs/obsolete.md")
        self.assertEqual(status, 0, error)
        self.assertIn('"docs/obsolete.md": null', output)

    def test_audit_distinguishes_missing_and_prepared_recovery(self):
        path = "digests/PDE-FM-日报-20260911.md"
        git(self.rival, "switch", "-c", "codex/unfinished")
        target = self.rival / path
        target.parent.mkdir(parents=True)
        original = "# Historical digest\n"
        target.write_text(original, encoding="utf-8")
        git(self.rival, "add", path)
        git(self.rival, "commit", "-m", "Prepare digest")
        git(self.rival, "push", "origin", "HEAD")
        git(self.repo, "fetch", "origin")
        status, output, error = self.cli("audit-branches")
        self.assertEqual(status, 0, error)
        self.assertEqual(json.loads(output)["findings"][0]["status"], "missing_from_main")
        digest = hashlib.sha256(original.encode()).hexdigest()
        oid = git(self.rival, "rev-parse", f"HEAD:{path}")
        self.write(path, original)
        self.write("metadata/recovery_fixture.json", json.dumps({"recovered_digests": [{
            "source_path": path, "source_blob": oid, "restored_path": path,
            "sha256": digest, "restored_sha256": digest, "byte_identical": True,
        }]}))
        status, output, error = self.cli("audit-branches")
        self.assertEqual(status, 0, error)
        self.assertEqual(json.loads(output)["findings"][0]["status"], "recovered_worktree_pending_publication")
        self.write(path, "# Altered content\n")
        status, output, _ = self.cli("audit-branches")
        self.assertEqual(json.loads(output)["findings"][0]["status"], "missing_from_main")
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), self.initial)


class SchemaExamplesTests(unittest.TestCase):
    """Keep public examples runnable; this is not a JSON Schema engine."""

    def test_synthetic_examples_pass_the_executable_validator(self):
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location("papertrack_schema_examples", root / "scripts/papertrack.py")
        core = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(core)
        examples = sorted((root / "schemas/examples").glob("*.json"))
        self.assertTrue(examples)
        for path in examples:
            with self.subTest(example=path.name):
                value = json.loads(path.read_text())
                if path.name.endswith(".event.json"):
                    core.validate_event(value)
                elif path.name.endswith(".run.json"):
                    core.validate_run(value)
                else:
                    self.fail(f"Example must identify its validator: {path.name}")

    def test_schema_local_references_resolve(self):
        root = Path(__file__).resolve().parents[1]
        schemas = sorted((root / "schemas").glob("*.schema.json"))
        self.assertEqual({path.name for path in schemas}, {"event.schema.json", "run.schema.json"})
        for path in schemas:
            document = json.loads(path.read_text())

            def walk(value):
                if isinstance(value, dict):
                    if "$ref" in value:
                        reference = value["$ref"]
                        self.assertTrue(reference.startswith("#/"), reference)
                        target = document
                        for part in reference[2:].split("/"):
                            target = target[part.replace("~1", "/").replace("~0", "~")]
                        self.assertIsInstance(target, dict)
                    for child in value.values():
                        walk(child)
                elif isinstance(value, list):
                    for child in value:
                        walk(child)

            with self.subTest(schema=path.name):
                walk(document)


if __name__ == "__main__":
    unittest.main()
