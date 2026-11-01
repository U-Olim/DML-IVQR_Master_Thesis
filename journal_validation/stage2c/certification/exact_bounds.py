"""Solver-independent rational bounds for a box-constrained minimax LP."""
from fractions import Fraction as F
import math
import numpy as np


def dyadic(values):
    """Return integers and E with EXACT values = integers / 2**E."""
    a = np.asarray(values, dtype=float)
    ratios = [float(v).as_integer_ratio() for v in a.flat]
    E = max((d.bit_length()-1 for _, d in ratios), default=0)
    integers = [n << (E-(d.bit_length()-1)) for n, d in ratios]
    return np.array(integers, dtype=object).reshape(a.shape), E


def record(f):
    f = F(f)
    v = float(f)
    down = math.nextafter(v, -math.inf) if F(v) > f else v
    up = math.nextafter(v, math.inf) if F(v) < f else v
    return {'numerator': str(f.numerator), 'denominator': str(f.denominator),
            'float': v, 'outward_lower': down, 'outward_upper': up}


def certificate(C, rhs, lo, hi, x, q):
    # A clamped x is exactly box-feasible for the binary64 input problem.
    x = np.minimum(hi, np.maximum(lo, np.asarray(x)))
    cr, E = dyadic(np.column_stack([C, rhs]))
    Ci, ri = cr[:, :-1].tolist(), cr[:, -1].tolist()
    xx, H = dyadic(np.concatenate([x, lo, hi]));m=len(x)
    xi, li, ui = xx[:m].tolist(), xx[m:2*m].tolist(), xx[2*m:].tolist()
    deviations = [sum(a*b for a,b in zip(row,xi))-(r << H) for row,r in zip(Ci,ri)]
    upper = F(max(map(abs,deviations),default=0),1 << (E+H))
    qi,G=dyadic(q);qi=qi.tolist();norm=sum(map(abs,qi))
    lower=F(0)
    if norm:
        qc=[sum(qi[i]*Ci[i][j] for i in range(len(qi))) for j in range(m)]
        numerator=(sum(a*b for a,b in zip(qi,ri)) << H)-sum(max(v*l,v*u) for v,l,u in zip(qc,li,ui))
        lower=max(F(0),F(numerator,(1 << (E+H))*norm))
    assert lower<=upper
    gate=F(float(1e-7)) # exact binary64 historical comparison threshold
    verdict='Certified pass' if upper<=gate else 'Certified failure' if lower>gate else 'Numerically indeterminate'
    maxnum=max(map(abs,deviations),default=0)
    binding=[i for i,d in enumerate(deviations) if abs(d)==maxnum]
    return {'lower':record(lower),'upper':record(upper),'width':record(upper-lower),
            'classification':verdict,'max_coordinates_zero_based':binding,
            'normalized_coordinate_discrepancies':[float(F(d,1 << (E+H))) for d in deviations],
            'witness_x':x.tolist(),'witness_q':np.asarray(q).tolist(),
            'proof':'Exact dyadic arithmetic: upper=max|Cx-r| at box-feasible x; lower=(q*r-support_box(C^T q))/||q||_1, clipped at zero.'}


def bareiss_solve(A,b):
    """Exact integer elimination and rational back substitution; no QR fit."""
    a=[list(map(int,row))+[int(v)] for row,v in zip(A,b)];n=len(a);previous=1
    for k in range(n-1):
        pivotrow=next((i for i in range(k,n) if a[i][k]),None)
        if pivotrow is None:raise ValueError('Singular exact basis')
        if pivotrow!=k:a[k],a[pivotrow]=a[pivotrow],a[k]
        pivot=a[k][k]
        for i in range(k+1,n):
            multiplier=a[i][k]
            for j in range(k+1,n+1):
                numerator=a[i][j]*pivot-multiplier*a[k][j]
                value,remainder=divmod(numerator,previous)
                if remainder:raise ArithmeticError('Nonexact Bareiss division')
                a[i][j]=value
            a[i][k]=0
        previous=pivot
    if not a[-1][-2]:raise ValueError('Singular exact basis')
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(F(a[i][-1])-sum(F(a[i][j])*x[j] for j in range(i+1,n)))/a[i][i]
    return x


def qr_exact_certificate(X,y,beta,lam,approx_v):
    """Exact feasible dual for P10 via rational basis reconstruction, if possible."""
    assert np.all(lam[1:]==0) and lam[0]>0
    free=np.flatnonzero((approx_v>-.1+1e-7)&(approx_v<.9-1e-7))
    if len(free)!=100:raise ValueError('Expected 100 free dual coordinates; got '+str(len(free)))
    fixed=np.array([i for i in range(len(y)) if i not in set(free)],dtype=int)
    Xi,EX=dyadic(X);Yi,EY=dyadic(y);Bi,EB=dyadic(beta);Li,EL=dyadic(lam)
    Xi=Xi.tolist();Yi=Yi.tolist();Bi=Bi.tolist();Li=Li.tolist()
    fixed_numerators={int(i):(9 if approx_v[i]>.4 else -1) for i in fixed}
    A=[[Xi[int(i)][j] for i in free] for j in range(1,101)]
    b=[-sum(Xi[i][j]*v for i,v in fixed_numerators.items()) for j in range(1,101)]
    z=bareiss_solve(A,b)
    v=[F(0)]*len(y)
    for i,t in fixed_numerators.items():v[i]=F(t,10)
    for i,t in zip(free,z):v[int(i)]=t/10
    L=math.lcm(*(t.denominator for t in v));vi=[t.numerator*(L//t.denominator) for t in v]
    assert all(-L<=10*t<=9*L for t in vi),'Exact box violation'
    gradients=[sum(row[j]*t for row,t in zip(Xi,vi)) for j in range(101)]
    assert all(g==0 for g in gradients[1:]),'Exact zero-penalty equality failed'
    g0=F(gradients[0],(1 << EX)*L)
    assert abs(g0)<=F(Li[0],2 << EL),'Exact intercept constraint failed'
    dual=F(sum(a*b for a,b in zip(Yi,vi)),(1 << EY)*L)
    ER=max(EY,EX+EB)
    residuals=[(Yi[i] << (ER-EY))-(sum(a*b for a,b in zip(Xi[i],Bi)) << (ER-EX-EB)) for i in range(len(y))]
    check=sum(9*r if r>=0 else -r for r in residuals)
    penalty=F(sum(abs(a)*b for a,b in zip(Bi,Li)),2 << (EB+EL))
    primal=F(check,10 << ER)+penalty
    gap=primal-dual;assert gap>=0
    loss_comp=F(0)
    for r,t in zip(residuals,vi):
        term=F(9*r if r>=0 else -r,10 << ER)-F(r*t,(1 << ER)*L)
        assert term>=0;loss_comp+=term
    penalty_comp=penalty-sum(F(b*g,(1 << (EB+EX))*L) for b,g in zip(Bi,gradients))
    assert penalty_comp>=0 and loss_comp+penalty_comp==gap
    return {'status':'EXACT_DUAL_FEASIBLE','tau':'9/10',
            'input_semantics':'Saved binary64 X, candidate-adjusted y, beta and lambda treated as exact rationals; residuals recomputed exactly.',
            'dual_numerators':[str(t) for t in vi],'dual_common_denominator':str(L),
            'free_observation_indices_zero_based':free.tolist(),
            'exact_zero_penalty_equalities':100,'intercept_gradient':record(g0),
            'primal_objective':record(primal),'dual_objective':record(dual),'gap':record(gap),
            'loss_complementarity':record(loss_comp),'penalty_complementarity':record(penalty_comp)}
