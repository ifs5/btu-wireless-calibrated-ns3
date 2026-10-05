#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,math,statistics
from collections import defaultdict
from pathlib import Path
METRICS=['aggregate_throughput_mbps','pdr_pct','mean_delay_ms','jain_fairness']
KEYS=['project_id','scenario_id','model_label','standard','band_ghz','channel_width_mhz','topology','ap_placement','n_sta','distance_m','path_loss_exponent','tx_power_dbm','offered_load_mbps_per_sta','packet_size','enable_rts','rate_manager','data_mode','mobility_speed_mps']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('inputs',nargs='+',type=Path); ap.add_argument('--output',type=Path,default=Path('summary.csv')); args=ap.parse_args()
    groups=defaultdict(list)
    for path in args.inputs:
        with path.open(newline='',encoding='utf-8-sig') as f:
            for r in csv.DictReader(f): groups[tuple(r.get(k,'') for k in KEYS)].append(r)
    fields=KEYS+['replicates']+[f'{m}_{s}' for m in METRICS for s in ['mean','sd','ci95']]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for key,rows in sorted(groups.items()):
            out=dict(zip(KEYS,key)); out['replicates']=len(rows)
            for m in METRICS:
                vals=[]
                for r in rows:
                    try: vals.append(float(r[m]))
                    except Exception: pass
                if vals:
                    mean=statistics.fmean(vals); sd=statistics.stdev(vals) if len(vals)>1 else 0.0
                    ci=1.96*sd/math.sqrt(len(vals)) if len(vals)>1 else 0.0
                    out[f'{m}_mean']=f'{mean:.6f}'; out[f'{m}_sd']=f'{sd:.6f}'; out[f'{m}_ci95']=f'{ci:.6f}'
            w.writerow(out)
    print(args.output)
if __name__=='__main__': main()
