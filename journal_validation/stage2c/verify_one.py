"""Read-only independent checks; caller records returned evidence inside Stage 2C."""
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def read(path):
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def verify(folder):
    folder = Path(folder)
    cfg = json.loads((Path(__file__).parent / 'config.json').read_text())
    evaluations = read(folder / 'evaluations.csv')
    observations = read(folder / 'observations.csv')
    coefficients = read(folder / 'coefficients.csv')
    diagnostics = read(folder / 'data_diagnostics.csv')
    X = np.loadtxt(folder / 'design.csv', delimiter=',', skiprows=1)
    y = np.array([float(x['ystar']) for x in diagnostics])
    f = np.array([float(x['density']) for x in diagnostics])
    n, p = X.shape
    assert (n, p) == (1000, 101)
    assert len(evaluations) == 5 and np.isfinite(f).all() and (f > 0).all()
    for name in ['data_hash', 'density_hash', 'projection_hash', 'original_penalty_hash']:
        assert len({r[name] for r in evaluations}) == 1, name
    by_arm = {r['arm']: r for r in evaluations}
    lam0 = np.array([float(r['penalty']) for r in coefficients if r['arm'] == 'P11'])
    assert (lam0 > 0).all()
    report = {'folder': folder.name, 'status': 'PASS', 'arms': {}}
    reference_psi = None
    for arm, row in by_arm.items():
        cr = [r for r in coefficients if r['arm'] == arm]
        ob = [r for r in observations if r['arm'] == arm]
        beta = np.array([float(r['coefficient']) for r in cr])
        lam = np.array([float(r['penalty']) for r in cr])
        e = np.array([float(r['residual']) for r in ob])
        score = .9 - (e <= 0).astype(float)
        psi = np.array([[float(r['psi1']), float(r['psi2'])] for r in ob])
        assert np.max(np.abs(y - X @ beta - e)) < 1e-10
        if reference_psi is None:
            reference_psi = psi
        assert np.array_equal(psi, reference_psi)
        if arm == 'KNOWN':
            assert np.array_equal(e <= 0, np.array([r['true_rank'] == '1' for r in ob]))
        else:
            expected = lam0.copy()
            if arm in ('P01', 'P00'):
                expected[0] = 0
            if arm in ('P10', 'P00'):
                expected[1:] = 0
            assert np.array_equal(expected, lam), arm
        moment = (psi * score[:, None]).sum(axis=0)
        second = (psi * score[:, None]).T @ (psi * score[:, None])
        W = float(moment @ np.linalg.solve(second, moment))
        assert abs(W - float(row['W'])) < 1e-9
        assert (row['accepted'] == 'TRUE') == (W <= -2 * math.log(.05))
        assert abs(score.mean() - float(row['mean_rank_score'])) < 1e-12
        assert np.linalg.eigvalsh(second).min() > 0
        evidence = {'W_difference': abs(W - float(row['W'])), 'second_moment_condition': float(np.linalg.cond(second))}
        if arm != 'KNOWN':
            # Feasibility of check-loss subgradients, with interval-valued scores
            # at numerical ties, and interval-valued L1 subgradients at zero beta.
            ties = np.abs(e) <= cfg['kkt_residual_tolerance']
            inactive = (np.abs(beta) <= cfg['kkt_coefficient_tolerance']) & (lam > 0)
            fixed = X[~ties].T @ score[~ties]
            target = .5 * lam * np.sign(beta)
            target[inactive] = 0
            C = np.concatenate([X[ties].T, -np.eye(p)[:, inactive]], axis=1) / n
            rhs = (target - fixed) / n
            bounds = [(-.1, .9)] * int(ties.sum())
            bounds += [(-lam[j] / 2, lam[j] / 2) for j in np.flatnonzero(inactive)]
            A = np.vstack([np.column_stack([C, -np.ones(p)]), np.column_stack([-C, -np.ones(p)])])
            b = np.concatenate([rhs, -rhs])
            objective = np.zeros(C.shape[1] + 1)
            objective[-1] = 1
            result = linprog(objective, A_ub=A, b_ub=b, bounds=bounds + [(0, None)], method='highs',
                             options={'primal_feasibility_tolerance': 1e-9, 'dual_feasibility_tolerance': 1e-9})
            assert result.success, (arm, result.message)
            stationarity = float(result.x[-1])
            assert stationarity <= cfg['kkt_stationarity_over_n_tolerance'], (arm, stationarity)
            subgrad = score.copy()
            subgrad[ties] = result.x[:int(ties.sum())]
            primal = float(np.sum(e * (.9 - (e < 0))) + .5 * np.sum(lam * np.abs(beta)))
            dual = float(y @ subgrad)
            evidence.update(kkt_stationarity_over_n=stationarity, numerical_ties=int(ties.sum()),
                            exact_ties=int((e == 0).sum()), primal_objective=primal,
                            reconstructed_dual_value=dual, primal_minus_dual=primal - dual)
            # LP allows tiny stationarity tolerance; quantify rather than claim exact dual optimality.
            assert abs(primal - float(row['objective'])) < 1e-8
        report['arms'][arm] = evidence
    r = read(folder / 'r_validation.csv')[0]
    assert float(r['canonical_W_difference']) <= cfg['canonical_tolerance']
    assert float(r['canonical_beta_difference']) <= cfg['canonical_tolerance']
    assert float(r['canonical_psi_difference']) <= cfg['canonical_tolerance']
    assert float(r['objective_difference']) / (1 + abs(float(r['ordinary_objective']))) < cfg['objective_relative_tolerance']
    # Coefficient equality is unnecessary; explicitly gate fitted-value agreement.
    assert float(r['p00_ordinary_fitted_max_difference']) < cfg['p00_fitted_value_tolerance'], r
    report['p00_ordinary_objective_difference'] = float(r['objective_difference'])
    report['p00_ordinary_fitted_max_difference'] = float(r['p00_ordinary_fitted_max_difference'])
    return report


if __name__ == '__main__':
    print(json.dumps(verify(sys.argv[1]), indent=2))
