#!/usr/bin/env python3
"""BTÜ ns-3 deney matrisi çalıştırıcısı — güvenli öğrenci başlangıç altyapısı.

Dry-run dosya oluşturmaz, değiştirmez veya silmez. Gerçek core koşusunda
öğretmen tarafından onaylanmış kalibrasyon ve kilit SHA-256 gerekir.
Çıktı önce staging CSV'ye yazılır; ancak tam koşu doğrulanınca yayımlanır.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

C = 299_792_458.0
REQUIRED_OUTPUT = {"project_id", "scenario_id", "model_label", "seed", "run"}
APPROVAL_FILE = "calibration/APPROVED_CORE_CALIBRATION.json"


class PreflightError(ValueError):
    """Çalıştırma başlamadan tespit edilen güvenlik/konfigürasyon sorunu."""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PreflightError(f"JSON okunamıyor: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise PreflightError(f"JSON üst düzeyde bir nesne olmalı: {path}")
    return value


def validate_approved_calibration(cal: dict, file: Path, lock_file: Path) -> None:
    """Kaza sonucu sentetik/yanlış dosya kullanımını önler; imza sistemi değildir."""
    if not file.is_file():
        raise PreflightError(f"Kalibrasyon dosyası yok: {file}")
    if not lock_file.is_file():
        raise PreflightError(
            f"Onay kilidi yok: {lock_file}. Eğitmen gerçek sınıf verisini "
            "onaylayıp kilidi yayımlamadan core deney yapılamaz."
        )
    lock = read_json(lock_file)
    expected_sha = lock.get("sha256")
    if not isinstance(expected_sha, str) or not re.fullmatch(r"[a-f0-9]{64}", expected_sha):
        raise PreflightError("Onay kilidinde geçerli küçük harfli SHA-256 bulunamadı")
    if lock.get("status") != "approved" or lock.get("calibration_id") != "class_calibration_v1":
        raise PreflightError("Onay kilidi onaylı class_calibration_v1 kaydı değil")
    if sha256_file(file) != expected_sha:
        raise PreflightError("Kalibrasyon SHA-256, eğitmen onay kilidiyle eşleşmiyor")
    if cal.get("calibration_id") != "class_calibration_v1" or cal.get("data_origin") != "measured_los":
        raise PreflightError("Kalibrasyon JSON kaynağı 'measured_los/class_calibration_v1' değil")
    if cal.get("unit_count", 0) < 4:
        raise PreflightError("En az dört bağımsız eski laboratuvar grubunun ölçümü gerekli")
    band = cal.get("band_ghz")
    if not isinstance(band, (int, float)) or not math.isclose(band, 5.0, abs_tol=0.2):
        raise PreflightError("Core sınıf kalibrasyonu, doğrulanmış 5 GHz ölçümüne ait olmalı")
    try:
        n0, q1, med, q3 = [float(cal[k]) for k in ("n_textbook", "n_q1", "n_median", "n_q3")]
    except (KeyError, TypeError, ValueError) as exc:
        raise PreflightError("Onaylı kalibrasyonda P0/P1/P2/P3 exponent değerleri eksik") from exc
    if not all(math.isfinite(n) and n > 0 for n in (n0, q1, med, q3)):
        raise PreflightError("Exponent değerleri pozitif sonlu sayılar olmalı")
    if not math.isclose(n0, 2.0, abs_tol=1e-9) or not q1 <= med <= q3:
        raise PreflightError("P0 veya Q1 <= medyan <= Q3 sırası tutarsız")


def friis(freq_ghz: float) -> float:
    return 20.0 * math.log10(4.0 * math.pi * (freq_ghz * 1e9) / C)


def resolve(value, cal: dict):
    if not isinstance(value, str) or not value.startswith("$"):
        return value
    placeholders = {
        "$N_TEXTBOOK": cal.get("n_textbook", 2.0),
        "$N_MEDIAN": cal["n_median"], "$N_Q1": cal["n_q1"], "$N_Q3": cal["n_q3"],
        "$REF_LOSS": cal["reference_loss_db"], "$FRIIS_2_4": friis(2.4),
        "$FRIIS_5": friis(5.0), "$FRIIS_6": friis(6.0),
    }
    if value not in placeholders:
        raise PreflightError(f"Bilinmeyen matris placeholder: {value}")
    return placeholders[value]


def cli_value(value) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (dict, list)) or value is None:
        raise PreflightError("CLI matris parametresi sayı/string/bool olmalı")
    return str(value)


def plan_runs(matrix: dict, cal: dict, output: Path) -> list[tuple[tuple[str, str, str, str, str], str]]:
    project = matrix.get("project_id")
    if not isinstance(project, str) or not re.fullmatch(r"P\d{2}", project):
        raise PreflightError("Geçersiz matrix project_id")
    if matrix.get("runner", "common") != "common":
        raise PreflightError(f"{project} özel starter gerektirir. Common runner kullanılamaz.")
    if matrix.get("source") != "btu-calibrated-wifi.cc":
        raise PreflightError("Yalnız doğrulanması hedeflenen common starter source kabul edilir")
    cases, runs = matrix.get("cases"), matrix.get("runs")
    if not isinstance(cases, list) or not cases or not isinstance(runs, list) or not runs:
        raise PreflightError("Matris cases ve runs boş olmayan listeler olmalı")
    if any(type(run) is not int or run <= 0 for run in runs) or len(set(runs)) != len(runs):
        raise PreflightError("Run numaraları tekil pozitif tamsayılar olmalı")
    scenarios = []
    plan = []
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("args"), dict):
            raise PreflightError("case.args sözlük olmalı")
        scenario = case.get("scenario_id")
        if not isinstance(scenario, str) or not re.fullmatch(r"[a-zA-Z0-9_.-]+", scenario):
            raise PreflightError("Geçersiz senaryo kimliği")
        scenarios.append(scenario)
        merged = dict(matrix.get("base_args", {}))
        merged.update(case["args"])
        merged = {k: resolve(v, cal) for k, v in merged.items()}
        if "outputCsv" in merged or "scenarioId" in merged or "projectId" in merged or "run" in merged:
            raise PreflightError("Matris kimlik/çıktı alanlarını override edemez")
        model = merged.get("modelLabel")
        if not isinstance(model, str) or not model.startswith(("P0-", "P1-", "P2-", "P3-")):
            raise PreflightError(f"modelLabel bulunamadı/geçersiz: {scenario}")
        for run in runs:
            args = dict(merged)
            args.update({"projectId": project, "scenarioId": scenario, "run": run, "outputCsv": str(output)})
            argstr = " ".join(f"--{k}={cli_value(v)}" for k, v in args.items())
            key = (project, scenario, model, str(args.get("seed", 20261005)), str(run))
            plan.append((key, f"scratch/btu-calibrated-wifi {argstr}"))
    if len(set(scenarios)) != len(scenarios):
        raise PreflightError("Aynı scenario_id birden çok kez verilmiş")
    if len(set(key for key, _ in plan)) != len(plan):
        raise PreflightError("Matriste tekrarlanan output identity bulundu")
    return plan


def verify_staged_results(stage: Path, expected: set[tuple[str, str, str, str, str]]) -> None:
    if not stage.is_file():
        raise PreflightError("ns-3 çıktı dosyası üretemedi")
    with stage.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not REQUIRED_OUTPUT.issubset(set(reader.fieldnames or [])):
            raise PreflightError("CSV çıktı kimlik alanları eksik")
        seen = set()
        for row in reader:
            key = tuple(row[k] for k in ("project_id", "scenario_id", "model_label", "seed", "run"))
            if key in seen:
                raise PreflightError(f"CSV'de yinelenen run: {key}")
            seen.add(key)
    if seen != expected:
        raise PreflightError(f"Eksik/fazla sonuç satırı: {len(seen)} / beklenen {len(expected)}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--ns3-root", type=Path, required=True)
    ap.add_argument("--matrix", type=Path, required=True)
    ap.add_argument("--calibration", type=Path, default=None)
    ap.add_argument("--approval-lock", type=Path, default=None, help="Eğitmenin yayımladığı SHA-256 JSON kilidi")
    ap.add_argument("--output", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true", help="Sadece plan; hiçbir dosya değiştirmez")
    ap.add_argument("--overwrite", action="store_true", help="Başarılı koşudan sonra mevcut CSV'yi değiştir")
    args = ap.parse_args(argv)

    repo = args.repo_root.resolve()
    ns3 = args.ns3_root.resolve()
    matrix_file = args.matrix.resolve()
    matrix = read_json(matrix_file)
    project = matrix.get("project_id")
    output = (args.output or repo / "results" / f"{project}_raw.csv").resolve()
    cal_path = (args.calibration or repo / "calibration/outputs/calibrated-channel.json").resolve()
    cal = read_json(cal_path)
    lock = (args.approval_lock or repo / APPROVAL_FILE).resolve()

    # Planı ve placeholder'ları herhangi bir mutasyondan önce doğrula.
    plan = plan_runs(matrix, cal, output)
    if args.dry_run:
        print("DRY-RUN: hiçbir dosya oluşturulmadı, değiştirilmedi veya silinmedi.")
        print("UYARI: Bu çalışma yalnız planlama içindir; demo kalibrasyon araştırma sonucu değildir.")
        print(f"Plan: proje={project}, toplam={len(plan)}, çıktı={output}")
        for i, (_, command) in enumerate(plan, 1):
            print(f"[{i}/{len(plan)}] {command}")
        return 0

    if args.calibration is None:
        raise PreflightError("Gerçek koşuda --calibration ile class_calibration_v1.json açıkça belirtilmeli")
    validate_approved_calibration(cal, cal_path, lock)
    if not ns3.is_dir() or not (ns3 / "ns3").is_file() or not (ns3 / "scratch").is_dir():
        raise PreflightError(f"ns-3 kökünde ./ns3 ve scratch/ bulunamadı: {ns3}")
    source = repo / "ns3/btu-calibrated-wifi.cc"
    if not source.is_file():
        raise PreflightError(f"Starter source bulunamadı: {source}")
    target = ns3 / "scratch" / source.name
    if target.exists() and sha256_file(target) != sha256_file(source):
        raise PreflightError(f"ns-3 scratch kaynağı farklı; dosya otomatik ezilmez: {target}")
    manifest_target = output.with_suffix(output.suffix + ".manifest.json")
    if (output.exists() or manifest_target.exists()) and not args.overwrite:
        raise PreflightError("Çıktı/manifest zaten var; korundu. Bilinçli yeniden koşu için --overwrite gerekir")
    if not output.parent.is_dir():
        output.parent.mkdir(parents=True, exist_ok=True)

    # Önce build, sonra staging: build başarısızsa çıktı dosyasına dokunulmaz.
    if not target.exists():
        shutil.copy2(source, target)
    subprocess.run(["./ns3", "build", "scratch/btu-calibrated-wifi"], cwd=ns3, check=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{output.stem}.", suffix=".pending.csv", dir=output.parent)
    os.close(fd)
    stage = Path(tmp_name)
    stage.unlink()  # ns-3 ilk satırda header yazabilsin.
    print(f"Koşu başlamadan mevcut çıktı korundu. Geçici dosya: {stage}", flush=True)
    try:
        for i, (_, spec) in enumerate(plan, 1):
            # Plan içindeki outputCsv değerini yalnız stage path ile değiştir.
            command = spec.replace(f"--outputCsv={output}", f"--outputCsv={stage}")
            print(f"[{i}/{len(plan)}] {command}", flush=True)
            subprocess.run(["./ns3", "run", command, "--no-build"], cwd=ns3, check=True)
        verify_staged_results(stage, {key for key, _ in plan})
        manifest = {
            "schema_version": "1.0", "project_id": project, "status": "complete",
            "matrix_sha256": sha256_file(matrix_file), "calibration_sha256": sha256_file(cal_path),
            "starter_sha256": sha256_file(source), "calibration_id": cal["calibration_id"],
            "run_count": len(plan), "output_sha256": sha256_file(stage),
            "note": "Record ns-3/compiler/OS commit in student report; manifest is not a scientific-model validation."
        }
        manifest_tmp = output.parent / (stage.name + ".manifest.json")
        manifest_tmp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        os.replace(stage, output)
        os.replace(manifest_tmp, manifest_target)
        print(f"BAŞARILI: {len(plan)} sonuç. CSV={output}, manifest={manifest_target}")
        return 0
    except Exception:
        print(f"HATA: Eski çıktı korunmuştur. Kısmi kanıt varsa burada: {stage}", file=sys.stderr)
        raise


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (PreflightError, subprocess.CalledProcessError) as exc:
        print(f"HATA: {exc}", file=sys.stderr)
        raise SystemExit(2)
