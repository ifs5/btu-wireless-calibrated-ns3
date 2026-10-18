"""Only stdlib; fake ns3 verifies file safety, not actual ns-3 PHY/MAC semantics."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_matrix.py"
MOCK_NS3 = r'''#!/usr/bin/env python3
import csv, os, pathlib, shlex, sys
root = pathlib.Path(__file__).parent
with (root / 'calls.txt').open('a') as f: f.write(' '.join(sys.argv[1:]) + '\n')
if sys.argv[1] == 'build':
    if os.environ.get('FAIL_BUILD'): sys.exit(31)
    sys.exit(0)
if sys.argv[1] != 'run': sys.exit(32)
opts = dict(x[2:].split('=', 1) for x in shlex.split(sys.argv[2])[1:] if x.startswith('--'))
if os.environ.get('FAIL_RUN') == opts['run'] and opts['modelLabel'].startswith('P0-'):
    sys.exit(33)
p = pathlib.Path(opts['outputCsv'])
fields = ['project_id','scenario_id','model_label','seed','run', 'aggregate_throughput_mbps','pdr_pct','mean_delay_ms','jain_fairness']
with p.open('a', newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields)
    if f.tell()==0: w.writeheader()
    w.writerow({'project_id':opts['projectId'], 'scenario_id':opts['scenarioId'],
        'model_label':opts['modelLabel'],'seed':opts.get('seed','20261005'),'run':opts['run'],
        'aggregate_throughput_mbps':3,'pdr_pct':95,'mean_delay_ms':2,'jain_fairness':0.9})
'''

class MatrixSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.repo = root / 'repo'
        self.ns3 = root / 'ns-3.48'
        for p in [self.repo/'ns3',self.repo/'calibration/outputs',self.repo/'calibration',self.repo/'results',self.ns3/'scratch']:
            p.mkdir(parents=True,exist_ok=True)
        (self.repo/'ns3/btu-calibrated-wifi.cc').write_text('int main() { return 0; }\n')
        self.fake=self.ns3/'ns3'
        self.fake.write_text(MOCK_NS3)
        self.fake.chmod(0o755)
        self.matrix=self.repo/'matrix.json'
        self.matrix.write_text(json.dumps({
            'project_id':'P01','runner':'common','source':'btu-calibrated-wifi.cc',
            'base_args':{'nSta':5,'modelLabel':'P0-textbook','pathLossExponent':'$N_TEXTBOOK'},
            'runs':[1,2],
            'cases':[
                {'scenario_id':'five-P0','args':{'modelLabel':'P0-textbook','pathLossExponent':'$N_TEXTBOOK'}},
                {'scenario_id':'five-P1','args':{'modelLabel':'P1-calibrated','pathLossExponent':'$N_MEDIAN'}}]
        }))
        self.demo=self.repo/'calibration/outputs/calibrated-channel.json'
        self.demo.write_text(json.dumps({'band_ghz':5.0,'unit_count':2,'n_textbook':2.0,'n_q1':2.1,'n_median':2.2,'n_q3':2.3,'reference_loss_db':46.4}))
        self.approved=self.repo/'calibration/outputs/class_calibration_v1.json'
        self.approved.write_text(json.dumps({'calibration_id':'class_calibration_v1','data_origin':'measured_los','band_ghz':5.0,
            'unit_count':6,'n_textbook':2.0,'n_q1':2.1,'n_median':2.2,'n_q3':2.3,'reference_loss_db':46.4}))
        self.lock=self.repo/'calibration/APPROVED_CORE_CALIBRATION.json'
        self.lock.write_text(json.dumps({'status':'approved','calibration_id':'class_calibration_v1',
            'sha256':hashlib.sha256(self.approved.read_bytes()).hexdigest()}))
        self.output=self.repo/'results/P01_raw.csv'
        self.manifest=self.repo/'results/P01_raw.csv.manifest.json'

    def call(self,*args,env=None):
        variables=os.environ.copy()
        if env: variables.update(env)
        return subprocess.run([sys.executable,str(SCRIPT),'--repo-root',str(self.repo),'--ns3-root',str(self.ns3),
            '--matrix',str(self.matrix),*map(str,args)], text=True,capture_output=True,env=variables)

    def approved_args(self): return ('--calibration',str(self.approved))

    def test_dry_run_no_writes_and_existing_results_preserved(self):
        self.output.write_bytes(b'PRECIOUS RESULTS\n')
        self.manifest.write_bytes(b'PRECIOUS MANIFEST\n')
        r=self.call('--dry-run')
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(self.output.read_bytes(),b'PRECIOUS RESULTS\n')
        self.assertEqual(self.manifest.read_bytes(),b'PRECIOUS MANIFEST\n')
        self.assertFalse((self.ns3/'scratch/btu-calibrated-wifi.cc').exists())
        self.assertFalse((self.ns3/'calls.txt').exists())
        self.assertEqual(len(list((self.repo/'results').glob('.*.pending.csv'))),0)

    def test_dry_run_creates_no_missing_output_directory(self):
        d=self.repo/'missingdir'
        r=self.call('--dry-run','--output',d/'file.csv')
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertFalse(d.exists())

    def test_real_requires_explicit_calibration_and_lock(self):
        r=self.call()
        self.assertNotEqual(r.returncode,0)
        self.assertIn('--calibration',r.stderr)
        self.assertFalse((self.ns3/'calls.txt').exists())
        r=self.call('--calibration',str(self.demo))
        self.assertNotEqual(r.returncode,0)
        self.assertFalse((self.ns3/'calls.txt').exists())

    def test_tampered_approved_calibration_rejected(self):
        self.approved.write_text(self.approved.read_text().replace('2.2','4.4'))
        r=self.call(*self.approved_args())
        self.assertNotEqual(r.returncode,0)
        self.assertIn('SHA-256',r.stderr)
        self.assertFalse((self.ns3/'calls.txt').exists())

    def test_success_outputs_four_rows_and_manifest(self):
        r=self.call(*self.approved_args())
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(len(self.output.read_text().splitlines()),5)
        data=json.loads(self.manifest.read_text())
        self.assertEqual(data['run_count'],4)
        self.assertEqual(data['calibration_sha256'],hashlib.sha256(self.approved.read_bytes()).hexdigest())
        self.assertEqual(data['output_sha256'],hashlib.sha256(self.output.read_bytes()).hexdigest())

    def test_existing_output_refused_without_overwrite_before_build(self):
        self.output.write_text('EXISTING')
        r=self.call(*self.approved_args())
        self.assertNotEqual(r.returncode,0)
        self.assertIn('--overwrite',r.stderr)
        self.assertEqual(self.output.read_text(),'EXISTING')
        self.assertFalse((self.ns3/'calls.txt').exists())

    def test_failed_overwrite_keeps_existing_file_and_manifest(self):
        self.output.write_text('KEEP ME')
        self.manifest.write_text('KEEP METADATA')
        r=self.call(*self.approved_args(),'--overwrite',env={'FAIL_RUN':'2'})
        self.assertNotEqual(r.returncode,0)
        self.assertEqual(self.output.read_text(),'KEEP ME')
        self.assertEqual(self.manifest.read_text(),'KEEP METADATA')
        self.assertIn('Kısmi kanıt',r.stderr)
        self.assertTrue(list((self.repo/'results').glob('.*.pending.csv')))

    def test_successful_explicit_overwrite(self):
        self.output.write_text('OLD')
        self.manifest.write_text('OLD MANIFEST')
        r=self.call(*self.approved_args(),'--overwrite')
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIn('five-P0',self.output.read_text())
        self.assertEqual(json.loads(self.manifest.read_text())['status'],'complete')

    def test_bad_scenario_and_unknown_placeholder_preflight_no_build(self):
        m=json.loads(self.matrix.read_text())
        m['cases'][1]['scenario_id']=m['cases'][0]['scenario_id']
        self.matrix.write_text(json.dumps(m))
        r=self.call(*self.approved_args())
        self.assertNotEqual(r.returncode,0)
        self.assertIn('scenario_id',r.stderr)
        self.assertFalse((self.ns3/'calls.txt').exists())
        m['cases'][1]['scenario_id']='other-P1'
        m['cases'][1]['args']['pathLossExponent']='$UNKNOWN'
        self.matrix.write_text(json.dumps(m))
        r=self.call(*self.approved_args())
        self.assertNotEqual(r.returncode,0)
        self.assertIn('$UNKNOWN',r.stderr)
        self.assertFalse((self.ns3/'calls.txt').exists())

    def test_different_scratch_source_not_overwritten(self):
        path=self.ns3/'scratch/btu-calibrated-wifi.cc'
        path.write_text('MY OWN SOURCE')
        r=self.call(*self.approved_args())
        self.assertNotEqual(r.returncode,0)
        self.assertEqual(path.read_text(),'MY OWN SOURCE')
        self.assertFalse((self.ns3/'calls.txt').exists())

    def test_output_path_with_spaces(self):
        special = self.repo / 'results' / 'ölçüm grubu' / 'P01 sonuç.csv'
        r=self.call(*self.approved_args(),'--output',str(special))
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(len(special.read_text().splitlines()),5)

    def test_specialized_project_refused(self):
        m=json.loads(self.matrix.read_text());m['runner']='specialized'
        self.matrix.write_text(json.dumps(m))
        r=self.call('--dry-run')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('özel starter',r.stderr)

if __name__=='__main__': unittest.main()
