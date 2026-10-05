#!/usr/bin/env python3
"""Bir proje matrisini ns-3.48 ağacı üzerinde çalıştırır.

İstenen starter source dosyasını ns-3/scratch altına kopyalar, bir kez build eder,
sonra her case/run kombinasyonunu --no-build ile çalıştırıp ortak CSV'ye ekler.
"""
from __future__ import annotations
import argparse,json,math,shutil,subprocess
from pathlib import Path
C=299_792_458.0
def friis(freq_ghz): return 20*math.log10(4*math.pi*(freq_ghz*1e9)/C)
def resolve(value,cal):
    if not isinstance(value,str) or not value.startswith('$'): return value
    m={'$N_TEXTBOOK':cal.get('n_textbook',2.0),'$N_MEDIAN':cal['n_median'],
       '$N_Q1':cal['n_q1'],'$N_Q3':cal['n_q3'],'$REF_LOSS':cal['reference_loss_db'],
       '$FRIIS_2_4':friis(2.4),'$FRIIS_5':friis(5.0),'$FRIIS_6':friis(6.0)}
    if value not in m: raise KeyError(f'Unknown placeholder {value}')
    return m[value]
def cli_value(v): return '1' if v is True else '0' if v is False else str(v)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--ns3-root',type=Path,required=True); ap.add_argument('--matrix',type=Path,required=True)
    ap.add_argument('--calibration',type=Path,default=None); ap.add_argument('--output',type=Path,default=None)
    ap.add_argument('--dry-run',action='store_true'); args=ap.parse_args()
    repo=args.repo_root.resolve(); ns3=args.ns3_root.resolve(); matrix=json.loads(args.matrix.read_text())
    cal_path=args.calibration or repo/'calibration/outputs/calibrated-channel.json'; cal=json.loads(cal_path.read_text())
    if matrix.get('runner','common')!='common':
        raise SystemExit(f"{matrix['project_id']} özel starter kullanır. ns-3.48 içindeki {matrix.get('upstream_example','(see guide)')} örneğinden başlayın ve {matrix.get('starter_guide','docs/ADVANCED_STARTERS.md')} kılavuzunu izleyin. Common runner bilerek durur.")
    source=repo/'ns3'/matrix['source']
    if not source.exists(): raise SystemExit(f'Starter source bulunamadı: {source}')
    target=ns3/'scratch'/source.name; output=(args.output or repo/'results'/f"{matrix['project_id']}_raw.csv").resolve()
    output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists(): output.unlink()
    print(f'Kaynak: {source}'); print(f'ns-3: {ns3}'); print(f'Çıktı: {output}')
    if not args.dry_run:
        shutil.copy2(source,target); subprocess.run(['./ns3','build',f'scratch/{source.stem}'],cwd=ns3,check=True)
    total=len(matrix['cases'])*len(matrix['runs']); done=0
    for case in matrix['cases']:
        merged=dict(matrix.get('base_args',{})); merged.update(case.get('args',{}))
        merged={k:resolve(v,cal) for k,v in merged.items()}
        merged['projectId']=matrix['project_id']; merged['scenarioId']=case['scenario_id']; merged['outputCsv']=str(output)
        for run in matrix['runs']:
            done+=1; this=dict(merged); this['run']=run
            argstr=' '.join(f'--{k}={cli_value(v)}' for k,v in this.items())
            spec=f'scratch/{source.stem} {argstr}'; print(f'[{done}/{total}] {spec}')
            if not args.dry_run: subprocess.run(['./ns3','run',spec,'--no-build'],cwd=ns3,check=True)
    return 0
if __name__=='__main__': raise SystemExit(main())
