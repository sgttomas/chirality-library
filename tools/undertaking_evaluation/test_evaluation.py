"""Handcrafted fixtures only; no operational records are kept in this suite."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.undertaking_evaluation.core import (
    EvaluationError, CASE_SCHEMA, codex_usage, inspect_case, compare_reports,
    render_html, write_report, main,
)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.repo = self.root / 'repo'; self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        (self.repo / 'instructions.md').write_text('Original instruction\n')
        (self.repo / 'preserved.md').write_text('Preserved basis\n')
        self.git('add', '.'); self.git('commit', '-qm', 'before')
        self.before = self.git('rev-parse', 'HEAD').strip()
        (self.repo / 'instructions.md').write_text('Revised instruction\n')
        (self.repo / 'added.md').write_text('Added source\n')
        self.git('rm', '-q', 'preserved.md'); self.git('add', '.')
        self.git('commit', '-qm', 'after')
        self.after = self.git('rev-parse', 'HEAD').strip()
        self.case_path = self.root / 'case.json'
        self.case = {'schema': CASE_SCHEMA, 'case_id': 'instruction-repair', 'trial_id': 'baseline',
                     'question': 'Does the actual caller remain usable?',
                     'hypothesis': 'A bounded caller check improves the instruction repair.',
                     'conditions': ['Current caller still works'], 'before': self.before,
                     'after': self.after, 'paths': ['.'], 'examination_basis': 'fixture-check/v1',
                     'environment': 'fixture-environment', 'resource_budget': {'minutes': 10, 'enforcement': 'instructional'},
                     'configuration': {'brief': 'baseline'},
                     'outcome': {'status': 'unknown', 'summary': 'Not examined by this fixture', 'evidence': []}}
        self.save()

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], text=True)

    def save(self):
        self.case_path.write_text(json.dumps(self.case))

    def usage(self, response='response-1', turn='selected', value=10, time='2026-01-01T00:00:00Z'):
        return {'type': 'token_usage_record', 'timestamp': time, 'payload': {
            'response_id': response, 'turn_id': turn,
            'usage': {'input_tokens': value, 'cached_input_tokens': 4, 'output_tokens': 2, 'total_tokens': value+2},
            'turn_token_usage': {'input_tokens': 999999}, 'thread_token_usage': {'input_tokens': 99999999}}}

    def trace(self, records):
        p = self.root / 'records.jsonl'
        p.write_text('\n'.join(json.dumps(r) for r in records)+'\n')
        return p

    def report(self):
        self.save();return inspect_case(self.case_path, self.repo)

    def test_git_state_is_bound_without_working_tree_leak(self):
        (self.repo/'instructions.md').write_text('Uncommitted secret fixture')
        report,_ = self.report()
        files = {f['path']:f for f in report['repository']['files']}
        self.assertEqual({p:f['change'] for p,f in files.items()},
                         {'added.md':'added','instructions.md':'modified','preserved.md':'removed'})
        self.assertEqual(files['instructions.md']['after']['git_object'], self.git('rev-parse', self.after+':instructions.md').strip())
        self.assertNotIn('Uncommitted secret fixture',json.dumps(report))
        self.assertEqual(report['supplied_assessment']['status'],'unknown')

    def test_path_selection_and_missing_selection(self):
        self.case['paths']=['instructions.md'];report,_=self.report()
        self.assertEqual(len(report['repository']['files']),1)
        self.case['paths']=['absent.md']
        with self.assertRaises(EvaluationError):self.report()

    def test_literal_paths_cannot_escape_or_be_pathspecs(self):
        for value in ['../outside','/absolute',':(glob)*','--help','folder\\file']:
            self.case['paths']=[value]
            with self.subTest(value=value),self.assertRaises(EvaluationError):self.report()

    def test_full_revision_required_and_unknown_revision_fails(self):
        for ref in ['HEAD','--help','f'*40]:
            self.case['before']=ref
            with self.subTest(ref=ref),self.assertRaises(EvaluationError):self.report()

    def test_source_evidence_bound_without_content_copy(self):
        p=self.root/'private-evidence.txt';p.write_text('private-fixture-no-copy')
        self.case['outcome']={'status':'established','summary':'Assessor statement', 'evidence':[
            {'kind':'file','path':str(p),'claim':'Selected observed result'},
            {'kind':'git','path':'instructions.md','revision':self.after,'claim':'Updated source'}]}
        report,protected=self.report()
        self.assertEqual(report['supplied_assessment']['evidence'][0]['sha256'],hashlib.sha256(p.read_bytes()).hexdigest())
        self.assertNotIn('private-fixture-no-copy',json.dumps(report))
        self.assertNotIn(str(p),json.dumps(report))
        self.assertIn(p,protected)
        self.assertIn('did not verify',report['supplied_assessment']['standing'])

    def test_assessment_requires_evidence_and_evidence_must_exist(self):
        self.case['outcome']['status']='established'
        with self.assertRaises(EvaluationError):self.report()
        self.case['outcome']['evidence']=[{'kind':'file','path':'missing','claim':'Missing evidence'}]
        with self.assertRaises(EvaluationError):self.report()

    def test_usage_dedup_ignores_cumulative_and_other_turns(self):
        row=self.usage()
        records=[row,row,self.usage('response-2',value=20,time='2026-01-01T00:00:05Z'),self.usage('other','unselected',100000),
                 {'type':'event_msg','payload':{'type':'token_count','info':{'total_token_usage':{'input_tokens':999999}}}},
                 {'type':'response_item','payload':{'type':'message','content':'private-fixture-prompt'}}]
        result=codex_usage(self.trace(records),['selected'])
        self.assertEqual(result['imported_responses'],2)
        self.assertEqual(result['duplicate_records_ignored'],1)
        self.assertEqual(result['observations']['input_tokens']['observed_sum'],30)
        self.assertEqual(result['observed_response_span_seconds'],5)
        self.assertIsNone(result['elapsed_work_seconds'])
        self.assertIsNone(result['cost'])
        self.assertNotIn('private-fixture-prompt',json.dumps(result))

    def test_conflicting_usage_is_not_averaged(self):
        with self.assertRaises(EvaluationError):codex_usage(self.trace([self.usage(),self.usage(value=99)]),['selected'])

    def test_partial_usage_unknown_fields_and_absent_turn(self):
        row=self.usage();del row['payload']['usage']['input_tokens']
        result=codex_usage(self.trace([row]),['selected','missing'])
        self.assertIsNone(result['observations']['input_tokens']['observed_sum'])
        self.assertEqual(result['missing_requested_turns'],1)
        self.assertIsNone(result['observations']['reasoning_output_tokens']['observed_sum'])

    def test_malformed_record_retained_as_coverage_gap(self):
        p=self.trace([self.usage()]);p.write_text(p.read_text()+'{bad\n')
        result=codex_usage(p,['selected'])
        self.assertEqual(len(result['issues']),1)
        self.assertEqual(result['imported_responses'],1)

    def test_invalid_usage_values_not_added(self):
        for value in [-1,True,1.2]:
            row=self.usage();row['payload']['usage']['input_tokens']=value
            result=codex_usage(self.trace([row]),['selected'])
            self.assertEqual(result['imported_responses'],0)
            self.assertTrue(result['issues'])

    def test_unsupported_cumulative_only_route_stays_unknown(self):
        p=self.trace([{'type':'event_msg','payload':{'type':'token_count','info':{'total_token_usage':{'input_tokens':999}}}}])
        result=codex_usage(p,['selected'])
        self.assertEqual(result['imported_responses'],0)
        self.assertIsNone(result['observations']['input_tokens']['observed_sum'])
        self.assertEqual(result['missing_requested_turns'],1)

    def test_missing_turn_selection_refused(self):
        with self.assertRaises(EvaluationError):codex_usage(self.trace([self.usage()]),[])

    def test_comparison_exposes_changed_conditions_and_same_trial(self):
        a,_=self.report();p=self.root/'a.json';p.write_text(json.dumps(a))
        same,_=compare_reports(p,p);self.assertIn('distinct_trial_identity',same['basis_differences'])
        self.case['trial_id']='variant';self.case['configuration']={'brief':'variant'}
        b,_=self.report();q=self.root/'b.json';q.write_text(json.dumps(b))
        compared,_=compare_reports(p,q);self.assertEqual(compared['status'],'declared_basis_matches')
        self.assertEqual(compared['variant_minus_baseline_observed_tokens'],{})
        self.case['examination_basis']='changed-check/v2';b,_=self.report();q.write_text(json.dumps(b))
        compared,_=compare_reports(p,q);self.assertIn('examination_basis',compared['basis_differences'])

    def test_tampered_basis_fails(self):
        a,_=self.report();a['comparison_basis']['before_commit']='tampered'
        p=self.root/'tampered.json';p.write_text(json.dumps(a))
        with self.assertRaises(EvaluationError):compare_reports(p,p)

    def test_html_treats_input_as_text(self):
        self.case['question']='<script>alert("fixture")</script><img src="https://invalid.example/">'
        report,_=self.report();markup=render_html(report)
        self.assertNotIn('<script>',markup);self.assertNotIn('<img ',markup)
        self.assertIn('&lt;script&gt;',markup);self.assertIn("default-src 'none'",markup)

    def test_safe_fresh_output_and_no_overwrite(self):
        report,protected=self.report();dest=self.root/'report';write_report(dest,report,protected)
        self.assertTrue((dest/'report.html').is_file())
        self.assertEqual((dest/'report.json').stat().st_mode&0o777,0o600)
        with self.assertRaises(EvaluationError):write_report(dest,report,protected)
        with self.assertRaises(EvaluationError):write_report(self.repo/'report',report,protected)
        with self.assertRaises(EvaluationError):write_report(self.case_path,report,protected)

    def test_compare_output_also_refuses_git_tree(self):
        report,_=self.report();a=self.root/'a.json';a.write_text(json.dumps(report))
        compared,protected=compare_reports(a,a)
        with self.assertRaises(EvaluationError):write_report(self.repo/'report',compared,protected)

    def test_symlink_output_parent_refused(self):
        report,protected=self.report();link=self.root/'link';link.symlink_to(self.root,target_is_directory=True)
        with self.assertRaises(EvaluationError):write_report(link/'report',report,protected)

    def test_duplicate_case_keys_fail(self):
        self.case_path.write_text('{"schema":"one","schema":"two"}')
        with self.assertRaises(EvaluationError):inspect_case(self.case_path,self.repo)

    def test_malformed_turn_identity_is_a_coverage_issue(self):
        for identity in [[], {}, None, 3]:
            row=self.usage();row['payload']['turn_id']=identity
            result=codex_usage(self.trace([row]),['selected'])
            self.assertEqual(result['imported_responses'],0)
            self.assertTrue(result['issues'])

    def test_incomplete_comparison_report_rejected(self):
        from tools.undertaking_evaluation.core import digest,canonical,REPORT_SCHEMA
        p=self.root/'incomplete.json'
        p.write_text(json.dumps({'schema':REPORT_SCHEMA,'comparison_basis':{},
            'comparison_basis_sha256':digest(canonical({})), 'repository':{},
            'supplied_assessment':{},'trial_id':'fake'}))
        with self.assertRaises(EvaluationError):compare_reports(p,p)

    def test_contradictory_report_state_rejected(self):
        report,_=self.report();report['repository']['before_commit']=self.after
        p=self.root/'contradiction.json';p.write_text(json.dumps(report))
        with self.assertRaises(EvaluationError):compare_reports(p,p)

    def test_git_replace_cannot_relabel_the_before_state(self):
        before,_=self.report()
        self.git('replace',self.before,self.after)
        after,_=self.report()
        self.assertEqual(before['repository'],after['repository'])

    def test_git_environment_cannot_select_another_repository(self):
        import os
        from unittest.mock import patch
        with patch.dict(os.environ,{'GIT_DIR':str(self.root/'missing'), 'GIT_WORK_TREE':str(self.root)}):
            report,_=self.report()
        self.assertEqual(report['repository']['before_commit'],self.before)

    def test_changed_question_limits_comparison(self):
        report,_=self.report();a=self.root/'a.json';a.write_text(json.dumps(report))
        self.case['trial_id']='variant';self.case['question']='A different intended use'
        report,_=self.report();b=self.root/'b.json';b.write_text(json.dumps(report))
        compared,_=compare_reports(a,b)
        self.assertIn('question',compared['basis_differences'])

    def test_malformed_outcome_status_is_refused(self):
        self.case['outcome']['status']=[]
        with self.assertRaises(EvaluationError):self.report()

    def test_written_private_locator_recovers_case_and_escapes_filename(self):
        self.case_path=self.root/'<img src=x onerror=fixture>.json'
        report,protected=self.report();dest=self.root/'locator-report'
        write_report(dest,report,protected)
        saved=json.loads((dest/'report.json').read_text())
        locator=saved['input_locators'][0]
        self.assertEqual((dest/locator['relative_path']).resolve(),self.case_path)
        self.assertEqual(locator['sha256'],hashlib.sha256(self.case_path.read_bytes()).hexdigest())
        self.assertNotIn(str(self.root),(dest/'report.json').read_text())
        markup=(dest/'report.html').read_text()
        self.assertNotIn('<img src=x',markup)
        self.assertIn('&lt;img src=x',markup)
        self.assertNotIn('href=',markup)

    def test_written_comparison_locates_original_reports(self):
        a,_=self.report();ap=self.root/'a.json';ap.write_text(json.dumps(a))
        self.case['trial_id']='variant';b,_=self.report();bp=self.root/'b.json';bp.write_text(json.dumps(b))
        report,protected=compare_reports(ap,bp);dest=self.root/'comparison'
        write_report(dest,report,protected)
        saved=json.loads((dest/'report.json').read_text())
        self.assertEqual([(dest/x['relative_path']).resolve() for x in saved['input_locators']],[ap,bp])
        self.assertEqual([x['kind'] for x in saved['input_locators']],['baseline_report','variant_report'])

    def test_cli_roundtrip(self):
        output=self.root/'cli-report'
        self.assertEqual(main(['inspect','--case',str(self.case_path),'--repo',str(self.repo),'--output',str(output)]),0)
        self.assertEqual(json.loads((output/'report.json').read_text())['case_id'],self.case['case_id'])
        self.assertEqual(main(['inspect','--case',str(self.case_path),'--repo',str(self.repo),'--output',str(output)]),2)


if __name__ == '__main__':
    unittest.main()
