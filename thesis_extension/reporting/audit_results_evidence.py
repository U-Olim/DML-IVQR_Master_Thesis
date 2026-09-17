"""Read-only evidence checks for the Chapter 5 Results and Discussion rewrite.

This script reads frozen reporting CSVs only.  It neither estimates models nor
rewrites any canonical output.  Run from the repository root with Python 3.9+.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "thesis_extension" / "reporting" / "output"
ESTIMATORS = ("Oracle-GMM", "Full-GMM", "DML-IVQR-BC")
N_VALUES = (500, 1000)
TAUS = (0.10, 0.25, 0.50, 0.75, 0.90)
KAPPAS = (1.00, 0.50, 0.25, 0.10)
DELTAS = (-1.00, -0.50, -0.25, 0.25, 0.50, 1.00)


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for key, value in tuple(row.items()):
            try:
                row[key] = float(value)
            except (TypeError, ValueError):
                pass
    return rows


point = read_csv(OUT / "table_point_performance_full.csv")
coverage = read_csv(OUT / "table_coverage_full.csv")
info = read_csv(OUT / "table_cr_informativeness_full.csv")
power = read_csv(OUT / "table_power_full.csv")
domain = read_csv(OUT / "table_grid_domain_diagnostic.csv")
calibration = read_csv(OUT / "table_strength_calibration.csv")
audit = read_csv(
    ROOT / "thesis_extension" / "diagnostics" / "coverage_audit" / "output"
    / "coverage_audit_all_cells.csv"
)
selected_heatmap = read_csv(
    ROOT / "thesis" / "figures" / "generated" / "selected_heatmap_values.csv"
)
selected_power = read_csv(
    ROOT / "thesis" / "figures" / "generated" / "selected_power_values.csv"
)


def cell_key(row):
    return (int(row["n"]), row["tau"], row["kappa"], row["estimator"])


P = {cell_key(row): row for row in point}
C = {cell_key(row): row for row in coverage}
I = {cell_key(row): row for row in info}

expected = {
    (n, tau, kappa, estimator)
    for n in N_VALUES for tau in TAUS for kappa in KAPPAS
    for estimator in ESTIMATORS
}
assert set(P) == set(C) == set(I) == expected
assert len(power) == 720
assert len(audit) == 120
assert all(row["R_available"] == 500 for row in audit)
assert all(row["number_missing"] == 0 for row in audit)
assert all(row["number_non_finite"] == 0 for row in audit)
assert len(calibration) == 8
assert all(row["n_success"] == 100 and row["n_failed"] == 0
           for row in calibration)
assert len(selected_heatmap) == 120
assert len(selected_power) == 168

for row in selected_heatmap:
    key = cell_key(row)
    assert math.isclose(row["coverage"], C[key]["coverage"], abs_tol=1e-12)
    assert math.isclose(row["size"], C[key]["size"], abs_tol=1e-12)
    assert math.isclose(
        row["full_domain"], I[key]["all_41_acceptance_rate"], abs_tol=1e-12
    )

power_lookup = {
    (*cell_key(row), row["delta"]): row["power"] for row in power
}
for row in selected_power:
    key = cell_key(row)
    expected_rejection = (
        C[key]["size"] if row["delta"] == 0
        else power_lookup[(*key, row["delta"])]
    )
    assert math.isclose(row["rejection"], expected_rejection, abs_tol=1e-12)


def nondecreasing(values):
    return all(right >= left for left, right in zip(values, values[1:]))


rmse_monotone = 0
mae_monotone = 0
for n in N_VALUES:
    for tau in TAUS:
        for estimator in ESTIMATORS:
            rmse_monotone += nondecreasing(
                [P[n, tau, k, estimator]["RMSE"] for k in KAPPAS]
            )
            mae_monotone += nondecreasing(
                [P[n, tau, k, estimator]["MAE"] for k in KAPPAS]
            )

n_rmse_improves = sum(
    P[1000, tau, kappa, estimator]["RMSE"]
    < P[500, tau, kappa, estimator]["RMSE"]
    for tau in TAUS for kappa in KAPPAS for estimator in ESTIMATORS
)
dml_full_wins = sum(
    P[n, tau, kappa, "DML-IVQR-BC"]["RMSE"]
    < P[n, tau, kappa, "Full-GMM"]["RMSE"]
    for n in N_VALUES for tau in TAUS for kappa in KAPPAS
)
dml_oracle_wins = sum(
    P[n, tau, kappa, "DML-IVQR-BC"]["RMSE"]
    < P[n, tau, kappa, "Oracle-GMM"]["RMSE"]
    for n in N_VALUES for tau in TAUS for kappa in KAPPAS
)

n_measure_lower = n_measure_equal = 0
for tau in TAUS:
    for kappa in KAPPAS:
        for estimator in ESTIMATORS:
            a = I[500, tau, kappa, estimator]["median_grid_accepted_set_measure"]
            b = I[1000, tau, kappa, estimator]["median_grid_accepted_set_measure"]
            n_measure_lower += b < a
            n_measure_equal += b == a

wilson_below = sum(row["coverage_mc95_upper"] < 0.95 for row in audit)
wilson_above = sum(row["coverage_mc95_lower"] > 0.95 for row in audit)

result = {
    "row_counts": {
        "point": len(point), "coverage": len(coverage),
        "informativeness": len(info), "power": len(power),
        "domain": len(domain), "coverage_audit": len(audit),
        "calibration": len(calibration),
        "figure_heatmap": len(selected_heatmap),
        "figure_power": len(selected_power),
    },
    "point_accuracy": {
        "mae_monotone_as_kappa_falls": f"{mae_monotone}/30",
        "rmse_monotone_as_kappa_falls": f"{rmse_monotone}/30",
        "rmse_lower_at_n1000": f"{n_rmse_improves}/60",
        "dml_rmse_below_full": f"{dml_full_wins}/40",
        "dml_rmse_below_oracle": f"{dml_oracle_wins}/40",
    },
    "informativeness": {
        "median_measure_lower_at_n1000": f"{n_measure_lower}/60",
        "median_measure_equal_at_n1000": f"{n_measure_equal}/60",
    },
    "coverage_audit": {
        "evaluations": int(sum(row["R_available"] for row in audit)),
        "wilson_intervals_below_0.95": wilson_below,
        "wilson_intervals_above_0.95": wilson_above,
        "missing": int(sum(row["number_missing"] for row in audit)),
        "nonfinite_including_missing": int(
            sum(row["number_non_finite"] for row in audit)
        ),
    },
    "verified_dml_example_n1000_tau050_kappa010": {
        "coverage": C[1000, 0.50, 0.10, "DML-IVQR-BC"]["coverage"],
        "median_measure": I[1000, 0.50, 0.10, "DML-IVQR-BC"]
        ["median_grid_accepted_set_measure"],
        "all_41_acceptance_rate": I[1000, 0.50, 0.10, "DML-IVQR-BC"]
        ["all_41_acceptance_rate"],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
