#!/usr/bin/env python3
"""Grup/ölçüm birimi başına log-distance exponent ve robust sınıf kalibrasyonu üretir.

Girdi alanları:
unit_id, session_id, device_id, bssid, band_ghz, distance_m, sample, rssi_dbm, notes

Fit edilen model: RSSI(d) = A + m*log10(d), n = -m/10.
Sınıf kalibrasyonunda grup başına n tahminlerinin median değeri kullanılır;
böylece daha fazla örnek toplayan bir grup aggregate sonucu orantısız domine etmez.
"""
from __future__ import annotations
import argparse, csv, json, math, statistics
from collections import defaultdict
from pathlib import Path

C = 299_792_458.0
REQUIRED = {"unit_id", "distance_m", "rssi_dbm"}

def fit_xy(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    if len(xs) < 3: raise ValueError("En az üç nokta gerekli")
    xbar=statistics.fmean(xs); ybar=statistics.fmean(ys)
    sxx=sum((x-xbar)**2 for x in xs)
    if sxx <= 0: raise ValueError("En az iki farklı mesafe gerekli")
    sxy=sum((x-xbar)*(y-ybar) for x,y in zip(xs,ys))
    slope=sxy/sxx; intercept=ybar-slope*xbar
    yhat=[intercept+slope*x for x in xs]
    ss_res=sum((y-yh)**2 for y,yh in zip(ys,yhat)); ss_tot=sum((y-ybar)**2 for y in ys)
    r2=1.0-ss_res/ss_tot if ss_tot>0 else float("nan")
    return slope,intercept,r2

def percentile(values: list[float], q: float) -> float:
    vals=sorted(values)
    if not vals: return float("nan")
    if len(vals)==1: return vals[0]
    pos=(len(vals)-1)*q; lo=math.floor(pos); hi=math.ceil(pos)
    return vals[lo] if lo==hi else vals[lo]+(vals[hi]-vals[lo])*(pos-lo)

def friis_reference_loss_db(freq_ghz: float, d_m: float=1.0) -> float:
    return 20.0*math.log10(4.0*math.pi*d_m*(freq_ghz*1e9)/C)

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("input_csv",type=Path)
    ap.add_argument("--band-ghz",type=float,default=5.0,help="Dosyada birden fazla band varsa kullanılacak band")
    ap.add_argument("--output-json",type=Path,default=Path("calibrated-channel.json"))
    ap.add_argument("--summary-csv",type=Path,default=Path("calibration-units.csv"))
    args=ap.parse_args()

    with args.input_csv.open(newline="",encoding="utf-8-sig") as f:
        reader=csv.DictReader(f); missing=REQUIRED-set(reader.fieldnames or [])
        if missing: raise SystemExit(f"Zorunlu sütunlar eksik: {sorted(missing)}")
        groups=defaultdict(list); meta=defaultdict(lambda: defaultdict(set))
        for row in reader:
            try:
                band=float(row.get("band_ghz") or args.band_ghz)
                if abs(band-args.band_ghz)>0.2: continue
                d=float(row["distance_m"]); rssi=float(row["rssi_dbm"])
            except (TypeError,ValueError): continue
            if d<=0: continue
            unit=(row.get("unit_id") or "UNKNOWN").strip()
            groups[unit].append((math.log10(d),rssi))
            for key in ("device_id","bssid","session_id"):
                val=(row.get(key) or "").strip()
                if val: meta[unit][key].add(val)

    unit_rows=[]
    for unit,pts in sorted(groups.items()):
        if len(pts)<3 or len({x for x,_ in pts})<3: continue
        slope,intercept,r2=fit_xy([p[0] for p in pts],[p[1] for p in pts])
        unit_rows.append({"unit_id":unit,"n":-slope/10.0,"slope_db_per_decade":slope,
          "intercept_A_dbm":intercept,"r_squared":r2,"sample_count":len(pts),
          "device_count":len(meta[unit]["device_id"]),"bssid_count":len(meta[unit]["bssid"]),
          "session_count":len(meta[unit]["session_id"])})
    if not unit_rows:
        raise SystemExit("Geçerli dBm değerleriyle en az 3 farklı mesafeye sahip ölçüm birimi bulunamadı.")

    ns=[r["n"] for r in unit_rows]; med=statistics.median(ns); q1=percentile(ns,.25); q3=percentile(ns,.75)
    reference_loss=friis_reference_loss_db(args.band_ghz)
    args.summary_csv.parent.mkdir(parents=True,exist_ok=True)
    with args.summary_csv.open("w",newline="",encoding="utf-8") as f:
        fields=list(unit_rows[0].keys()); w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in unit_rows: w.writerow({k:f"{v:.6f}" if isinstance(v,float) else v for k,v in r.items()})
    config={"schema_version":"1.0","band_ghz":args.band_ghz,"reference_distance_m":1.0,
      "reference_loss_db":round(reference_loss,6),
      "reference_loss_method":"1 m Friis; ölçülen RSSI intercept değerinin path loss olduğu varsayılmaz",
      "n_textbook":2.0,"n_median":round(med,6),"n_q1":round(q1,6),"n_q3":round(q3,6),
      "n_iqr":round(q3-q1,6),"unit_count":len(unit_rows),
      "aggregation":"ölçüm birimi başına log-distance exponent tahminlerinin medianı"}
    args.output_json.parent.mkdir(parents=True,exist_ok=True)
    args.output_json.write_text(json.dumps(config,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(config,indent=2,ensure_ascii=False))
    for r in unit_rows:
        if r["bssid_count"]>1:
            print(f"UYARI: {r['unit_id']} için {r['bssid_count']} BSSID bulundu; yayın amaçlı kullanmadan önce kontrol edin.")
    return 0
if __name__=="__main__": raise SystemExit(main())
