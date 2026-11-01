"""Bound full-precision LP assembly rounding without solving or refitting."""
from fractions import Fraction as F
import json
import sys
from pathlib import Path
import numpy as np


def q(x):return F.from_float(float(x))


def rec(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator),'float':float(x)}


def main():
    run=Path(sys.argv[1]);folder=run/'pilot_021/P10/full_precision_lp'
    d=np.load(folder/'lp_inputs.npz');X=d['X'];C=d['C'];rhs=d['rhs'];ties=d['ties'];inactive=d['inactive']
    score=d['score'];target=d['target'];lo=d['lo'];hi=d['hi'];fixed=np.flatnonzero(~ties);ix=np.flatnonzero(ties)
    intervals=np.flatnonzero(inactive);budgets=[]
    for j in range(101):
        exact_fixed=sum((q(X[i,j])*q(score[i]) for i in fixed),F(0))
        exact_rhs=(q(target[j])-exact_fixed)/1000
        radius=abs(exact_rhs-q(rhs[j]))
        for k,i in enumerate(ix):
            radius+=abs(q(X[i,j])/1000-q(C[j,k]))*max(abs(q(lo[k])),abs(q(hi[k])))
        for k,coord in enumerate(intervals,start=len(ix)):
            exact_c=F(-int(j==coord),1000)
            radius+=abs(exact_c-q(C[j,k]))*max(abs(q(lo[k])),abs(q(hi[k])))
        budgets.append(radius)
    delta=max(budgets)
    s=json.loads((run/'pilot_021/P10/summary.json').read_text())['full_precision']
    lower=q(s['lower'])-delta;upper=q(s['upper'])+delta
    gate=q(1e-7)
    result={'status':'PASS','scope':'Exact saved binary64 X and fixed score values, same historical tie and coefficient classifications; no BLAS/dot/division rounding in mathematical LP.',
            'max_uniform_objective_perturbation':rec(delta),
            'unrounded_LP_lower':rec(lower),'unrounded_LP_upper':rec(upper),
            'classification':'Certified failure' if lower>gate else 'Numerically indeterminate',
            'proof':'Uniform residual perturbation <= delta over entire finite box implies |t_exact-t_assembled| <= delta.',
            'coordinate_bounds':[rec(t) for t in budgets]}
    (run/'assembly_rounding_certificate.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='coordinate_bounds'},indent=2))


if __name__=='__main__':main()
