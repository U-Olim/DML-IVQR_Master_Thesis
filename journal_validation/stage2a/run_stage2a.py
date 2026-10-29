"""Run the isolated Stage 2A experiment; standard library only, no canonical writes."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RSCRIPT = Path(r"C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe")


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def protected_files():
    # Includes ignored frozen data and local libraries, not only tracked files.
    result = {}
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if rel.parts[0] == ".git" or p.is_dir() or HERE in p.parents:
            continue
        result[rel.as_posix()] = sha(p)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    if Path(args.run_id).name != args.run_id:
        parser.error("run-id must be a single directory name")
    out = HERE / "output" / args.run_id
    out.mkdir(parents=True, exist_ok=False)
    before = protected_files()
    (out / "protected_before.json").write_text(json.dumps(before, indent=2))
    commands = []

    def run(argv, logname):
        print("COMMAND", subprocess.list2cmdline([str(a) for a in argv]), flush=True)
        entry = {"argv": [str(a) for a in argv], "cwd": str(ROOT),
                 "started_utc": datetime.now(timezone.utc).isoformat(), "log": logname}
        commands.append(entry)
        with (out / logname).open("w", encoding="utf-8") as log:
            proc = subprocess.Popen(argv, cwd=ROOT, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, errors="replace")
            for line in proc.stdout:
                log.write(line)
                log.flush()
                print(line, end="", flush=True)
            entry["exit_status"] = proc.wait()
        entry["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (out / "commands.json").write_text(json.dumps(commands, indent=2))
        if entry["exit_status"]:
            raise RuntimeError(f"Command failed ({entry['exit_status']}): {argv}")

    status = "FAILED"
    try:
        branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
        if branch != "journal-validation":
            raise RuntimeError(f"Expected journal-validation branch; found {branch}")
        (out / "git_head.txt").write_text(subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True))
        for phase in ("validate", "ab", "pilot"):
            run([str(RSCRIPT), "--vanilla", str(HERE / "run_diagnostics.R"), phase, str(out)], f"{phase}_master.log")
        run([str(RSCRIPT), "--vanilla", str(HERE / "summarize.R"), str(out)], "summarize.log")
        status = "COMPLETE"
    finally:
        after = protected_files()
        (out / "protected_after.json").write_text(json.dumps(after, indent=2))
        changes = {"changed": [p for p in before if p in after and before[p] != after[p]],
                   "missing": sorted(before.keys() - after.keys()),
                   "added_outside_stage2a": sorted(after.keys() - before.keys()),
                   "files_checked": len(before), "run_status": status}
        (out / "preservation.json").write_text(json.dumps(changes, indent=2))
        print("PRESERVATION", json.dumps(changes), flush=True)
        if any(changes[k] for k in ("changed", "missing", "added_outside_stage2a")):
            raise RuntimeError("Protected filesystem changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
