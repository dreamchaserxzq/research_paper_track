"""Contract and data-loss regressions beyond paper selection and publication."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import papertrack as p


def event():
    return {'event_id':'test', 'event_type':'assessment', 'recorded_at':'2026-09-12T02:00:00Z',
            'paper':{'arxiv_id':'2609.01234'},
            'evidence':[{'url':'https://arxiv.org/abs/2609.01234','kind':'arxiv_abstract','checked_at':'2026-09-12T01:00:00Z'}]}


def run():
    return {'run_id':'published-2026-W37', 'task_type':'published','status':'success',
            'started_at':'2026-09-12T01:00:00Z','completed_at':'2026-09-12T02:00:00Z',
            'coverage_start':'2026-09-10T00:00:00Z','coverage_end':'2026-09-12T01:00:00Z',
            'previous_successful_coverage_end':None,
            'queries':[{'query':'PDE','source':'Publisher','status':'success','candidate_ids':['doi:10.1234/pde']}],
            'candidates':[{'doi':'10.1234/pde','arxiv_id':None,'submitted_at':None,'updated_at':None,
                           'discovered_at':'2026-09-12T01:20:00Z','decision':'selected','reason':'Verified formal version','discovery_type':'backfill'}]}


class RegistryContracts(unittest.TestCase):
    def repository_fixture(self, root):
        snap=root/p.SNAPSHOT;snap.mkdir(parents=True)
        (root/'docs').mkdir();(root/'docs/LANDMARK_MODELS.md').write_text('# Models\n')
        (snap/'seen_papers.txt').write_text('')
        (snap/'manifest.json').write_text(json.dumps({'files':[{'snapshot_path':str((snap/'seen_papers.txt').relative_to(root)), 'sha256':hashlib.sha256(b'').hexdigest()}]}))
        (root/'metadata/runs').mkdir();(root/'digests').mkdir()
        return root

    def test_successful_daily_report_and_run_selection_must_agree(self):
        with tempfile.TemporaryDirectory() as d:
            root=self.repository_fixture(Path(d))
            path=root/'digests/PDE-FM-日报-20260912.md'
            path.write_text('# 日报\n## 方向A\n📄 Test paper\n- 🔗 链接：https://arxiv.org/abs/2609.01234\n- ⭐ 相关度评分：8/10\n')
            r=run();r.update(task_type='daily',run_id='daily-2026-09-12',digest_path=str(path.relative_to(root)))
            r['candidates'][0].update(arxiv_id='2609.01234',doi=None)
            r['queries'][0]['candidate_ids']=['2609.01234']
            record_path=root/'metadata/runs/run.json';record_path.write_text(json.dumps(r))
            first=p.outputs(root)
            self.assertIn('2609.01234', first['seen_papers.txt'])
            r['candidates'][0]['decision']='excluded';record_path.write_text(json.dumps(r))
            with self.assertRaisesRegex(ValueError,'cards disagree'):p.outputs(root)

    def test_snapshot_bytes_are_checked_before_any_build(self):
        with tempfile.TemporaryDirectory() as d:
            root=self.repository_fixture(Path(d))
            (root/p.SNAPSHOT/'seen_papers.txt').write_text('2609.01234\n')
            with self.assertRaisesRegex(ValueError,'snapshot changed'):p.outputs(root)

    def test_score_schemes_cannot_be_mixed_or_incomplete(self):
        e = event()
        e['paper'].update(score_scheme='daily-v1',score_relevance=4,score_generality=3,score_innovation=2,score_total=9)
        p.validate_event(e)
        for changes in [dict(score_total=10),dict(score_value=2),dict(score_relevance=5),dict(score_scheme='unknown'),dict(score_innovation=None)]:
            bad = copy.deepcopy(e);bad['paper'].update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValueError):p.validate_event(bad)
        pub = event();pub['paper'].update(score_scheme='published-v2',score_relevance=5,score_generality=3,score_value=2,score_total=10)
        p.validate_event(pub)

    def test_evidence_cannot_be_checked_in_the_future_of_recording(self):
        e = event();e['evidence'][0]['checked_at']='2026-09-13T01:00:00Z'
        with self.assertRaises(ValueError):p.validate_event(e)

    def test_doi_only_weekly_candidate_and_shared_aliases(self):
        r=run();self.assertEqual(p.validate_run(r)['selected'],1)
        r['candidates'][0]['arxiv_id']='2609.01234'
        r['queries'][0]['candidate_ids'] += ['2609.01234','arxiv:2609.01234']
        self.assertEqual(p.validate_run(r)['candidates'],1)
        r['candidates'].append(dict(r['candidates'][0],arxiv_id='2609.01235'))
        with self.assertRaises(ValueError):p.validate_run(r)

    def test_coverage_skips_failed_and_degraded_runs(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'metadata/runs').mkdir(parents=True)
            successful=run();(root/'metadata/runs/one.json').write_text(json.dumps(successful))
            degraded=copy.deepcopy(successful);degraded.update(run_id='later',status='degraded',completed_at='2026-09-13T02:00:00Z',coverage_end='2026-09-13T01:00:00Z')
            (root/'metadata/runs/two.json').write_text(json.dumps(degraded))
            result=subprocess.run([sys.executable,str(Path(p.__file__)),'--root',d,'coverage','--task','published','--at','2026-09-14T01:00:00Z'],capture_output=True,text=True,check=True)
            self.assertEqual(json.loads(result.stdout)['previous_successful_coverage_end'],successful['coverage_end'])
            self.assertEqual(json.loads(result.stdout)['coverage_start'],'2026-09-10T01:00:00Z')

    def test_normalized_ids_preserve_version_independent_identity(self):
        self.assertEqual(p.normalize_arxiv('https://arxiv.org/abs/2609.01234v2'),'2609.01234')
        self.assertEqual(p.normalize_doi('HTTPS://doi.org/10.1234/AbC'),'10.1234/abc')
        for bad in ['prefix2609.01234','2609.01234garbage']:
            with self.assertRaises(ValueError):p.normalize_arxiv(bad)


if __name__=='__main__':unittest.main()
