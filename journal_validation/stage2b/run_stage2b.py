"""Isolated Stage 2B execution and content-preservation audit (stdlib only)."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RSCRIPT = Path(r"C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe")


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def snapshot():
    result = {}
    for directory, subdirs, files in os.walk(ROOT):
        base = Path(directory)
        subdirs[:] = [d for d in subdirs if base / d != HERE and not (base == ROOT and d == ".git")]
        for name in files:
            p = base / name
            result[p.relative_to(ROOT).as_posix()] = sha(p)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    if not args.run_id or Path(args.run_id).name != args.run_id or args.run_id in (".", ".."):
        parser.error("run-id must be a single new directory name")
    if subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip() != "journal-validation":
        raise RuntimeError("Work only on journal-validation")
    out = HERE / "output" / args.run_id
    out.mkdir(parents=True, exist_ok=False)
    print("Hashing protected files, including all Stage 2A artifacts", flush=True)
    before = snapshot()
    (out / "protected_before.json").write_text(json.dumps(before, indent=2))
    (out / "git_head.txt").write_text(subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True))
    commands = []

    def run(argv, logname):
        print("COMMAND", subprocess.list2cmdline([str(x) for x in argv]), flush=True)
        entry = {"argv": [str(x) for x in argv], "cwd": str(ROOT), "log": logname,
                 "started_utc": datetime.now(timezone.utc).isoformat()}
        commands.append(entry)
        with (out / logname).open("w", encoding="utf-8") as log:
            proc = subprocess.Popen(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    text=True, errors="replace")
            for line in proc.stdout:
                print(line, end="", flush=True)
                log.write(line)
                log.flush()
            entry["exit_status"] = proc.wait()
        entry["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (out / "commands.json").write_text(json.dumps(commands, indent=2))
        if entry["exit_status"]:
            raise RuntimeError(f"Command failed: exit={entry['exit_status']}, argv={argv}")

    status = "FAILED"
    try:
        for phase in ("validate", "primary", "contrasts"):
            run([str(RSCRIPT), "--vanilla", str(HERE / "run_diagnostics.R"), phase, str(out)], f"{phase}_master.log")
        run([str(RSCRIPT), "--vanilla", str(HERE / "summarize.R"), str(out)], "summarize.log")
        status = "COMPLETE"
    finally:
        after = snapshot()
        (out / "protected_after.json").write_text(json.dumps(after, indent=2))
        preservation = {"files_checked": len(before), "changed": [p for p in before if p in after and before[p] != after[p]],
                        "missing": sorted(before.keys() - after.keys()),
                        "added_outside_stage2b": sorted(after.keys() - before.keys()), "run_status": status,
                        "stage2a_files_checked": sum(p.startswith("journal_validation/stage2a/") for p in before)}
        (out / "preservation.json").write_text(json.dumps(preservation, indent=2))
        print("PRESERVATION", json.dumps(preservation), flush=True)
        if any(preservation[k] for k in ("changed", "missing", "added_outside_stage2b")):
            raise RuntimeError("Protected content changed")
    print("STAGE2B_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
