"""Verify and inventory completed Stage 2B artifacts without fitting models."""
from __future__ import annotations
import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from run_stage2b import HERE, ROOT, sha, snapshot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    out = parser.parse_args().output.resolve()
    if HERE / "output" not in out.parents:
        raise RuntimeError("Output must be an existing Stage 2B output directory")
    cmd = [sys.executable, "-B", str(HERE / "verify_outputs.py"), str(out)]
    result = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    (out / "final_verification.log").write_text(result.stdout, encoding="utf-8")
    (out / "finalization_command.json").write_text(json.dumps({
        "invocation": [sys.executable, "-B", str(Path(__file__).resolve()), str(out)],
        "verification_argv": cmd, "verification_exit_status": result.returncode,
        "cwd": str(ROOT), "timestamp_utc": datetime.now(timezone.utc).isoformat()}, indent=2))
    print(result.stdout, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    original = json.loads((out / "protected_before.json").read_text())
    final = snapshot()
    preservation = {"files_checked": len(original), "changed": [p for p in original if p in final and original[p] != final[p]],
                    "missing": sorted(original.keys()-final.keys()),
                    "added_outside_stage2b": sorted(final.keys()-original.keys()),
                    "stage2a_files_checked": sum(p.startswith("journal_validation/stage2a/") for p in original)}
    (out / "final_preservation.json").write_text(json.dumps(preservation, indent=2))
    if any(preservation[k] for k in ("changed","missing","added_outside_stage2b")):
        raise RuntimeError("Final preservation check failed")
    (out / "source_sha256.json").write_text(json.dumps({p.name: sha(p) for p in HERE.iterdir() if p.is_file()}, indent=2))
    paths = sorted(p for p in out.rglob("*") if p.is_file() and p.name != "artifact_manifest.csv")
    with (out / "artifact_manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path","bytes","sha256"])
        writer.writeheader()
        for p in paths:
            writer.writerow({"path":p.relative_to(HERE).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)})
    print("FINAL_PRESERVATION", json.dumps(preservation), flush=True)
    print("ARTIFACTS_INVENTORIED",len(paths),flush=True)


if __name__ == "__main__":
    main()
