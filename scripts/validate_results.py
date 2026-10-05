#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv
from pathlib import Path
REQUIRED={'project_id','scenario_id','model_label','seed','run','aggregate_throughput_mbps','pdr_pct','mean_delay_ms','jain_fairness'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('csv',type=Path); args=ap.parse_args()
    with args.csv.open(newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f); missing=REQUIRED-set(reader.fieldnames or []); rows=list(reader)
    if missing: raise SystemExit(f'Eksik sütunlar: {sorted(missing)}')
    seen=set(); dups=[]
    for i,r in enumerate(rows,2):
        key=(r['project_id'],r['scenario_id'],r['model_label'],r['seed'],r['run'])
        if key in seen: dups.append((i,key))
        seen.add(key)
        for m in ['aggregate_throughput_mbps','pdr_pct','mean_delay_ms','jain_fairness']:
            try: float(r[m])
            except Exception: raise SystemExit(f'Sayısal olmayan {m} satır {i}: {r[m]!r}')
    if dups: raise SystemExit(f'Tekrarlanan project/scenario/model/seed/run satırları: {dups[:5]}')
    print(f"PASS: {len(rows)} satır; duplicate run key yok; zorunlu metric'ler sayısal.")
if __name__=='__main__': main()
