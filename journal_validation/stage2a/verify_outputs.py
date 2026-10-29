"""Independent, read-only numerical checks; writes one check report under the run."""
from __future__ import annotations
import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    out = parser.parse_args().output

    def rows(name):
        with (out / name).open(newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))

    ab, pilot = rows("ab_pairs.csv"), rows("pilot_pairs.csv")
    assert len(ab) == 240 and len(pilot) == 120
    all_rows = ab + pilot
    assert len({r["task_id"] for r in all_rows}) == 360
    assert len(list((out / "details").glob("*.rds"))) == 360
    assert len(list((out / "samples").glob("*.rds"))) == 52
    cutoff = -2 * math.log(.05)
    for r in all_rows:
        assert r["paired_data_identical"] == r["pivotal_verified"] == "TRUE"
        assert r["paired_beta_identical"] == r["paired_residuals_identical"] == "TRUE"
        assert r["rng_after_identical"] == "TRUE"
        assert r["failed_baseline"] == r["failed_alternative"] == "FALSE"
        for v in ("baseline", "alternative"):
            w = float(r[f"W_{v}"])
            assert math.isfinite(w) and w >= 0
            assert (r[f"rejected_{v}"] == "TRUE") == (w > cutoff)
        assert math.isclose(float(r["delta_W"]), float(r["W_alternative"]) - float(r["W_baseline"]), abs_tol=1e-10)
        if r["estimator"] == "DML-IVQR-BC":
            assert r["paired_penalty_identical"] == "TRUE"

    groups = defaultdict(list)
    for r in ab:
        groups[(r["sample_id"], r["tau"])].append(r)
    assert len(groups) == 24
    for g in groups.values():
        assert len(g) == 10 and len({r["data_sha256"] for r in g}) == 1
        assert len({r["stream"] for r in g}) == len({r["pivotal_sha256"] for r in g}) == 10
    assert len({r["stream"] for r in ab}) == 240
    assert len({r["pivotal_sha256"] for r in ab}) == 240

    pilot_by_sample = defaultdict(list)
    for r in pilot:
        pilot_by_sample[r["sample_id"]].append(r)
    assert len(pilot_by_sample) == 40
    for g in pilot_by_sample.values():
        assert len(g) == 3 and len({r["data_sha256"] for r in g}) == 1
    pilot_dml = [r for r in pilot if r["estimator"] == "DML-IVQR-BC"]
    assert len({r["stream"] for r in pilot_dml}) == 40
    assert not ({r["stream"] for r in pilot_dml} & {r["stream"] for r in ab})
    assert not ({r["data_sha256"] for r in pilot} & {r["data_sha256"] for r in ab})

    for s in rows("C_coverage_summary.csv"):
        g = [r for r in pilot if r["estimator"] == s["estimator"]]
        accepted = sum(r[f"rejected_{s['variant']}"] == "FALSE" for r in g)
        p = accepted / 40
        assert math.isclose(float(s["coverage"]), p, abs_tol=1e-12)
        assert math.isclose(float(s["MCSE"]), math.sqrt(p * (1-p) / 40), abs_tol=1e-12)
        z = 1.959963984540054
        center = (p + z*z/80) / (1 + z*z/40)
        half = z * math.sqrt(p*(1-p)/40 + z*z/(4*40*40)) / (1+z*z/40)
        assert math.isclose(float(s["Wilson95_lower"]), center-half, abs_tol=1e-12)
        assert math.isclose(float(s["Wilson95_upper"]), center+half, abs_tol=1e-12)
    for s in rows("C_paired_summary.csv"):
        g = [r for r in pilot if r["estimator"] == s["estimator"]]
        diffs = [int(r["rejected_alternative"] == "FALSE") - int(r["rejected_baseline"] == "FALSE") for r in g]
        assert math.isclose(float(s["paired_coverage_difference"]), statistics.mean(diffs), abs_tol=1e-12)
        assert math.isclose(float(s["paired_difference_MCSE"]), statistics.stdev(diffs)/math.sqrt(40), abs_tol=1e-12)
    for r in rows("rng_consumption_checks.csv"):
        assert r["baseline_only_expected_rng"] == r["alternative_only_expected_rng"] == "TRUE"
    stability = rows("numerical_stability.csv")
    assert len(stability) == 720
    assert all(r["failed"] == "FALSE" and r["warning_count"] == "0" and
               r["density_zero_count"] == r["density_nonfinite_count"] == "0" for r in stability)
    preservation = json.loads((out / "preservation.json").read_text())
    assert preservation["run_status"] == "COMPLETE"
    assert not any(preservation[k] for k in ("changed", "missing", "added_outside_stage2a"))
    report = {"status": "PASS", "AB_pairs": len(ab), "pilot_pairs": len(pilot),
              "fixed_dataset_quantile_groups": len(groups),
              "fixed_groups_with_penalty_decision_changes": sum(len({r['rejected_baseline'] for r in g}) > 1 for g in groups.values()),
              "AB_density_decision_flips": sum(r["decision_flip"] == "TRUE" for r in ab),
              "pilot_density_decision_flips": sum(r["decision_flip"] == "TRUE" for r in pilot),
              "canonical_files_preserved": preservation["files_checked"]}
    (out / "output_verification.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
