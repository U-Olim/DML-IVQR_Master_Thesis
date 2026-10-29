"""Independent arithmetic and pairing checks on Stage 2B frozen diagnostic CSVs."""
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
    out = parser.parse_args().output.resolve()
    root = Path(__file__).resolve().parents[2]

    def read(name):
        with (out / name).open(newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))

    rows = read("all_evaluations.csv")
    assert len(rows) == 768
    grouped = defaultdict(dict)
    sample_hashes = defaultdict(set)
    for r in rows:
        key = (r["design"], r["estimator"], r["replication"])
        assert r["variant"] not in grouped[key]
        grouped[key][r["variant"]] = r
        sample_hashes[(r["design"], r["replication"])].add(r["data_hash"])
        assert r["failed"] == "FALSE"
        assert r["density_nonfinite"] == r["density_zero"] == "0"
        w = float(r["W"])
        assert math.isfinite(w) and w >= 0
        assert (r["rejected"] == "TRUE") == (w > -2*math.log(.05))
        assert r["design_rank"] == r["design_columns"]
        assert math.isfinite(float(r["gram_condition"])) and math.isfinite(float(r["covariance_condition"]))
    assert len(grouped) == 192 and len(sample_hashes) == 64
    assert all(len(s) == 1 for s in sample_hashes.values())
    for g in grouped.values():
        assert set(g) == {"V00", "V10", "V01", "V11"}
        assert len({r["density_hash"] for r in g.values()}) == 1
        assert len({r["data_hash"] for r in g.values()}) == 1
        assert len({r["pivotal_hash"] for r in g.values()}) == 1
        assert g["V00"]["projection_hash"] == g["V10"]["projection_hash"]
        assert g["V01"]["projection_hash"] == g["V11"]["projection_hash"]
        assert g["V00"]["outcome_residual_hash"] == g["V01"]["outcome_residual_hash"]
        assert g["V10"]["outcome_residual_hash"] == g["V11"]["outcome_residual_hash"]
        for v in ("V01", "V11"):
            assert float(g[v]["orthogonality_intercept"]) < 1e-10
            if g[v]["estimator"] != "DML-IVQR-BC":
                assert float(g[v]["orthogonality_max"]) < 1e-10

    with (root / "journal_validation/stage2a/output/controlled_20261022_01/pilot_pairs.csv").open(newline="") as f:
        previous = {(r["estimator"], r["sample_id"]): r for r in csv.DictReader(f)}
    previous_maxdiff = 0
    for (design, estimator, replication), g in grouped.items():
        if design != "primary":
            continue
        old = previous[(estimator, replication)]
        previous_maxdiff = max(previous_maxdiff, abs(float(g["V00"]["W"]) - float(old["W_baseline"])))
        assert g["V00"]["data_hash"] == old["data_sha256"]
        if estimator == "DML-IVQR-BC":
            assert g["V00"]["pivotal_hash"] == old["pivotal_sha256"]
    assert previous_maxdiff < 1e-11

    pair_rows = read("paired_factorial.csv")
    assert len(pair_rows) == 192
    for r in pair_rows:
        g = grouped[(r["design"], r["estimator"], r["replication"])]
        w = {v: float(x["W"]) for v, x in g.items()}
        a = {v: int(x["rejected"] == "FALSE") for v, x in g.items()}
        for v in ("V10", "V01", "V11"):
            assert math.isclose(float(r[f"delta_W_{v}"]), w[v]-w["V00"], abs_tol=1e-10)
            assert float(r[f"delta_A_{v}"]) == a[v]-a["V00"]
        assert math.isclose(float(r["interaction_W"]), w["V11"]-w["V10"]-w["V01"]+w["V00"], abs_tol=1e-10)
        assert float(r["interaction_A"]) == a["V11"]-a["V10"]-a["V01"]+a["V00"]
    for s in read("variant_summary.csv"):
        g = [r for r in rows if (r["design"],r["estimator"],r["variant"]) == (s["design"],s["estimator"],s["variant"])]
        n = 40 if s["design"] == "primary" else 12
        assert len(g) == int(s["successful"]) == int(s["total"]) == n
        w = [float(r["W"]) for r in g]
        p = sum(r["rejected"] == "FALSE" for r in g)/n
        assert math.isclose(float(s["mean_W"]), statistics.mean(w), abs_tol=1e-12)
        assert math.isclose(float(s["mean_W_MCSE"]), statistics.stdev(w)/math.sqrt(n), abs_tol=1e-12)
        assert math.isclose(float(s["coverage"]), p, abs_tol=1e-12)
        assert math.isclose(float(s["rejection"]), 1-p, abs_tol=1e-12)
        assert math.isclose(float(s["coverage_MCSE"]), math.sqrt(p*(1-p)/n), abs_tol=1e-12)
        z = 1.959963984540054
        center = (p+z*z/(2*n))/(1+z*z/n)
        half = z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
        assert math.isclose(float(s["Wilson95_lower"]), center-half, abs_tol=1e-12)
        assert math.isclose(float(s["Wilson95_upper"]), center+half, abs_tol=1e-12)
    for s in read("paired_effect_summary.csv"):
        g = [r for r in pair_rows if r["design"] == s["design"] and r["estimator"] == s["estimator"]]
        effect = s["effect"]
        w = [float(r["interaction_W"] if effect == "interaction" else r[f"delta_W_{effect}"]) for r in g]
        a = [float(r["interaction_A"] if effect == "interaction" else r[f"delta_A_{effect}"]) for r in g]
        for col, val in [("mean_delta_W",statistics.mean(w)),("W_MCSE",statistics.stdev(w)/math.sqrt(len(w))),
                         ("mean_delta_acceptance",statistics.mean(a)),("acceptance_MCSE",statistics.stdev(a)/math.sqrt(len(a)))]:
            assert math.isclose(float(s[col]), val, abs_tol=1e-12)

    detail_checks = read("independent_detail_checks.csv")
    assert len(detail_checks) == 192
    assert all(r["checked"] == r["known_beta_exact"] == r["penalty_exact"] == r["all_weights_finite"] == "TRUE" for r in detail_checks)
    isolation = read("isolation_checks.csv")
    assert len(isolation) == 192
    for r in isolation:
        for name in ("same_data","same_density","same_residual_across_projection","same_projection_across_outcomes","same_penalty","rank_and_dimension_ok","known_score_rank_identity"):
            assert r[name] == "TRUE"
        assert float(r["canonical_difference"]) == 0
    assert len(read("failures.csv")) == 0
    preservation = json.loads((out / "preservation.json").read_text())
    assert preservation["run_status"] == "COMPLETE"
    assert not any(preservation[k] for k in ("changed","missing","added_outside_stage2b"))
    report = {"status":"PASS","variant_evaluations":768,"factorial_tasks":192,
              "primary_replications":40,"contrast_replications_each":12,
              "canonical_candidate_max_difference":0,"stage2a_primary_max_difference":previous_maxdiff,
              "independent_W_max_difference":max(float(r["W_max_difference"]) for r in detail_checks),
              "known_residual_rank_mismatches":0,"preserved_files":preservation["files_checked"],
              "preserved_stage2a_files":preservation["stage2a_files_checked"]}
    (out / "output_verification.json").write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
