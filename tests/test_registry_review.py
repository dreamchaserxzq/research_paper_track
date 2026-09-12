"""Independent regression checks for registry identities and admission evidence."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "papertrack_registry_review", Path(__file__).resolve().parents[1] / "scripts" / "papertrack.py"
)
registry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(registry)


def record(source_id, arxiv=None, doi=None, title=None, author="Author"):
    return {
        "source_id": source_id,
        "priority": 30,
        "source_kind": "legacy",
        "paper": {"arxiv_id": arxiv, "doi": doi, "title": title, "authors": [author]},
    }


def event(evidence_url="https://publisher.example/article/123"):
    return {
        "event_id": "publication-example",
        "event_type": "publication",
        "recorded_at": "2026-09-12T03:00:00Z",
        "paper": {"arxiv_id": "2609.01234", "status": "published", "venue": "Example Journal"},
        "evidence": [{"url": evidence_url, "kind": "publisher", "checked_at": "2026-09-12T02:00:00Z"}],
    }


def run_record():
    return {
        "run_id": "daily-2026-09-12",
        "task_type": "daily",
        "status": "success",
        "started_at": "2026-09-12T01:00:00Z",
        "completed_at": "2026-09-12T02:00:00Z",
        "coverage_start": "2026-09-10T00:00:00Z",
        "coverage_end": "2026-09-12T01:00:00Z",
        "previous_successful_coverage_end": "2026-09-11T01:00:00Z",
        "queries": [{"source": "arxiv", "query": "PDE foundation", "status": "success", "candidate_ids": ["2609.01234"]}],
        "candidates": [{
            "arxiv_id": "2609.01234", "discovered_at": "2026-09-12T01:15:00Z",
            "submitted_at": "2026-09-11T12:00:00Z", "updated_at": None,
            "decision": "selected", "reason": "Cross-equation pretrained model", "discovery_type": "new",
        }],
    }


def minimal_snapshot(root):
    snapshot = root / registry.SNAPSHOT
    snapshot.mkdir(parents=True)
    (root / "docs").mkdir()
    (root / "docs/LANDMARK_MODELS.md").write_text("# Landmarks\n")
    contents = {
        "paper_registry.jsonl": json.dumps({"arxiv_id": "2609.00001", "title": "Original", "status": "arxiv"}) + "\n",
        "seen_papers.txt": "2609.00001\n",
    }
    entries = []
    for name, text in contents.items():
        path = snapshot / name
        path.write_text(text)
        entries.append({"snapshot_path": str(path.relative_to(root)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    (snapshot / "manifest.json").write_text(json.dumps({"files": entries}))


class RegistryReviewTests(unittest.TestCase):
    def test_title_bridges_cannot_transitively_merge_distinct_arxiv_ids(self):
        rows = [
            record("arxiv-a", arxiv="2609.00001", title="Title A"),
            record("doi-a", doi="10.1234/example", title="Title A"),
            record("doi-b", doi="10.1234/example", title="Title B"),
            record("arxiv-b", arxiv="2609.00002", title="Title B"),
        ]
        groups, _ = registry.identity_groups(rows)
        for group in groups:
            arxiv_ids = {r["paper"]["arxiv_id"] for r in group if r["paper"].get("arxiv_id")}
            self.assertLessEqual(len(arxiv_ids), 1, "title matching must respect identities already joined by DOI")

    def test_conflicting_shared_doi_does_not_collapse_distinct_arxiv(self):
        rows = [record("a", "2609.00001", "10.1234/shared"), record("b", "2609.00002", "10.1234/shared")]
        groups, conflicts = registry.identity_groups(rows)
        self.assertEqual(len(groups), 2)
        self.assertTrue(any(c.get("field") == "identity" for c in conflicts))

    def test_unique_title_author_bridge_preserves_both_identifier_sources(self):
        rows = [record("a", arxiv="2609.00001", title="One Paper"), record("b", doi="10.1234/paper", title="One Paper")]
        groups, conflicts = registry.identity_groups(rows)
        self.assertEqual(len(groups), 1)
        self.assertEqual(conflicts, [])
        paper, _ = registry.merge_group(groups[0])
        self.assertEqual(paper["identifier_aliases"], {"arxiv": ["2609.00001"], "doi": ["10.1234/paper"]})
        self.assertEqual(set(paper["sources"]), {"a", "b"})

    def test_ambiguous_title_chain_is_unattached_for_every_record_order(self):
        rows = [
            record("arxiv-a", arxiv="2609.00001", title="Title A"),
            record("doi-a", doi="10.1234/example", title="Title A"),
            record("doi-b", doi="10.1234/example", title="Title B"),
            record("arxiv-b", arxiv="2609.00002", title="Title B"),
        ]
        expected = {frozenset({"arxiv-a"}), frozenset({"doi-a", "doi-b"}), frozenset({"arxiv-b"})}
        for order in itertools.permutations(rows):
            groups, conflicts = registry.identity_groups(copy.deepcopy(order))
            with self.subTest(order=[r["source_id"] for r in order]):
                self.assertEqual({frozenset(r["source_id"] for r in g) for g in groups}, expected)
                self.assertTrue(any(c.get("field") == "identity" and c.get("resolution") == "pending" for c in conflicts))

    def test_corrected_doi_drops_wrong_edge_but_keeps_original_source(self):
        wrong = record("wrong", "2609.00001", "10.1234/wrong", "Wrong title")
        correction = record("correction", "2609.00001", "10.1234/correct", "Correct title")
        correction.update(source_kind="event", priority=100, supersedes=["wrong"])
        unrelated = record("unrelated", doi="10.1234/wrong", title="Wrong title")
        groups, _ = registry.identity_groups([wrong, correction, unrelated])
        self.assertEqual(len(groups), 2)
        corrected = next(g for g in groups if any(r["source_id"] == "correction" for r in g))
        paper, conflicts = registry.merge_group(corrected)
        self.assertEqual(set(paper["sources"]), {"wrong", "correction"})
        self.assertEqual(paper["identifier_aliases"]["doi"], ["10.1234/correct"])
        self.assertEqual(paper["provenance"]["doi"], "correction")
        self.assertEqual(conflicts, [])

    def test_superseded_title_does_not_attach_new_doi_record(self):
        old = record("old", arxiv="2609.00001", title="Mistaken title")
        correction = record("correction", arxiv="2609.00001", title="Correct title")
        correction.update(source_kind="event", priority=100, supersedes=["old"])
        other = record("other", doi="10.1234/other", title="Mistaken title")
        groups, _ = registry.identity_groups([old, correction, other])
        self.assertEqual({frozenset(r["source_id"] for r in g) for g in groups},
                         {frozenset({"old", "correction"}), frozenset({"other"})})

    def test_direct_arxiv_identity_correction_requires_separate_migration(self):
        old = record("old", arxiv="2609.00001")
        correction = record("correction", arxiv="2609.00002")
        correction["supersedes"] = ["old"]
        with self.assertRaises(ValueError):
            registry.identity_groups([old, correction])

    def test_indirect_arxiv_identity_correction_cannot_bridge_through_doi_only(self):
        old = record("old", arxiv="2609.00001")
        intermediate = record("intermediate", doi="10.1234/paper")
        intermediate["supersedes"] = ["old"]
        correction = record("correction", arxiv="2609.00002", doi="10.1234/paper")
        correction["supersedes"] = ["intermediate"]
        with self.assertRaises(ValueError):
            registry.identity_groups([old, intermediate, correction])

    def test_event_id_cannot_impersonate_historical_source_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            minimal_snapshot(root)
            inbox = root / "metadata/inbox"
            inbox.mkdir()
            assertion = event()
            assertion["event_id"] = f"{registry.SNAPSHOT}/paper_registry.jsonl:1"
            (inbox / "collision.jsonl").write_text(json.dumps(assertion) + "\n")
            with self.assertRaises(ValueError):
                registry.load_inputs(root)

    def test_identifier_normalization_preserves_raw_event_assertion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            minimal_snapshot(root)
            inbox = root / "metadata/inbox"
            inbox.mkdir()
            assertion = event()
            assertion["paper"].update(arxiv_id="https://arxiv.org/abs/2609.01234v2",
                                      doi="https://doi.org/10.1234/MixedCase")
            (inbox / "original.jsonl").write_text(json.dumps(assertion) + "\n")
            records = registry.load_inputs(root)
            registry.identity_groups(records)
            imported = next(r for r in records if r["source_id"] == assertion["event_id"])
            self.assertEqual(imported["paper"]["arxiv_id"], "2609.01234")
            self.assertEqual(imported["paper"]["doi"], "10.1234/mixedcase")
            self.assertEqual(imported["raw"], assertion)

    def test_accepted_to_published_retains_both_sources_without_false_conflict(self):
        old = record("accepted-source", arxiv="2609.01234")
        old["paper"].update(status="accepted", venue="Example Journal")
        assertion = event()
        new = {"source_id": assertion["event_id"], "source_kind": "event", "priority": 100,
               "paper": assertion["paper"], "evidence": assertion["evidence"], "raw": assertion}
        groups, _ = registry.identity_groups([old, new])
        paper, conflicts = registry.merge_group(groups[0])
        self.assertEqual(paper["status"], "published")
        self.assertEqual(paper["verification"], "source_checked")
        self.assertEqual(paper["provenance"]["status"], "publication-example")
        self.assertEqual(set(paper["sources"]), {"accepted-source", "publication-example"})
        self.assertEqual(conflicts, [])

    def test_formal_evidence_needs_a_real_http_host(self):
        with self.assertRaises(ValueError):
            registry.validate_event(event("https:/missing-host/article"))

    def test_arxiv_doi_is_not_publisher_evidence(self):
        for url in [
            "https://arxiv.org/abs/2609.01234",
            "https://doi.org/10.48550/arXiv.2609.01234",
            "https://doi.org/10.48550%2FarXiv.2609.01234",
        ]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                registry.validate_event(event(url))

    def test_conflicting_venue_prevents_source_checked_claim(self):
        old = record("old-record", arxiv="2609.01234")
        old["paper"].update(status="preprint", venue="Old Claimed Venue")
        assertion = event()
        new = {"source_id": assertion["event_id"], "priority": 100, "source_kind": "event",
               "paper": assertion["paper"], "evidence": assertion["evidence"]}
        groups, _ = registry.identity_groups([old, new])
        paper, conflicts = registry.merge_group(groups[0])
        self.assertTrue(any(c["field"] == "venue" for c in conflicts))
        self.assertEqual(paper["verification"], "conflict_pending")
        self.assertEqual(set(paper["sources"]), {"old-record", "publication-example"})

    def test_digest_admission_uses_explicit_paper_link_not_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "digests").mkdir()
            (root / "digests/PDE-FM-日报-20260912.md").write_text(
                "# 日报\n## 方向A\n📄 Selected work\n"
                "- 对比基线：https://arxiv.org/abs/2608.00001\n"
                "- 🔗 链接：https://arxiv.org/abs/2609.00002\n"
                "- ⭐ 相关度评分：8/10\n"
                "## 附：本期未入选但值得关注的论文\n"
                "📄 Excluded candidate\n- 🔗 链接：https://arxiv.org/abs/2609.00003\n",
                encoding="utf-8",
            )
            rows = registry.digest_records(root)
        self.assertEqual([r["paper"]["arxiv_id"] for r in rows], ["2609.00002"])

    def test_non_card_baseline_and_appendix_never_become_selected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "digests").mkdir()
            (root / "digests/PDE-FM-日报-20260912.md").write_text(
                "# 日报\n- 已有基线：https://arxiv.org/abs/2608.00001\n"
                "## 附：本期未入选但值得关注的论文\n"
                "📄 Candidate only\n- 🔗 链接：https://arxiv.org/abs/2609.00003\n",
                encoding="utf-8",
            )
            self.assertEqual(registry.digest_records(root), [])

    def test_failed_source_cannot_report_successful_coverage(self):
        run = run_record()
        run["queries"][0].update(status="failed", error="HTTP 403")
        with self.assertRaises(ValueError):
            registry.validate_run(run)

    def test_old_submission_requires_explicit_backfill_classification(self):
        run = run_record()
        run["candidates"][0]["submitted_at"] = "2026-08-01T00:00:00Z"
        with self.assertRaises(ValueError):
            registry.validate_run(run)
        run["candidates"][0]["discovery_type"] = "backfill"
        self.assertEqual(registry.validate_run(run)["selected"], 1)

    def test_coverage_and_candidate_provenance_gaps_rejected(self):
        for alter in [
            lambda r: r.update(coverage_start="2026-09-11T02:00:00Z"),
            lambda r: r["queries"][0].update(candidate_ids=[]),
            lambda r: r["candidates"].append(copy.deepcopy(r["candidates"][0])),
        ]:
            run = run_record()
            alter(run)
            with self.assertRaises(ValueError):
                registry.validate_run(run)

    def test_rebuilding_views_never_reingests_generated_registry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            minimal_snapshot(root)
            first = registry.outputs(root)
            for name, text in first.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
            second = registry.outputs(root)
            self.assertEqual(first, second)
            papers = [json.loads(line) for line in second["metadata/papers.jsonl"].splitlines()]
            self.assertEqual(len(papers), 1)
            self.assertEqual(papers[0]["verification"], "legacy_unverified")
            self.assertEqual(len(papers[0]["sources"]), 2)


if __name__ == "__main__":
    unittest.main()
