"""Dimension-generic exact outcome checks; LP proposes, rationals decide.

Shared low-level integer arithmetic is reused read-only. No saved optimal
basis, coefficient, rank or tie set is used to construct this certificate.
"""
from common_v1 import *
import math
from analyze import determinant
def certify(X,y,lam,proposed_beta,proposed_e,tau,proposal_threshold):
 n,p=X.shape;xx,EX=dyadic(X);yy,EY=dyadic(y);Xi=xx.tolist();yi=yy.tolist();pen=[F(float(v)) for v in lam]
 active=np.flatnonzero(abs(proposed_beta)>proposal_threshold).tolist()
 ties=np.flatnonzero(abs(proposed_e)<=proposal_threshold).tolist()
 if not len(active)==len(ties)>0:raise ArithmeticError('OUTCOME_UNRESOLVED: no square proposed basis')
 A=[[Xi[i][j] for j in active] for i in ties];det,pivots=determinant(A)
 if not det:raise ArithmeticError('OUTCOME_UNRESOLVED: singular proposed basis')
 b=[F(0)]*p
 for j,v in zip(active,integer_solve_rational_rhs(A,[F(yi[i],1<<EY)*(1<<EX) for i in ties])):b[j]=v
 P,e,D,pred,PD,bn,LB=exact_objective(Xi,EX,yi,EY,b,pen,tau)
 assert [i for i,v in enumerate(e) if not v]==ties
 assert [j for j,v in enumerate(b) if v]==active
 tied=set(ties);fixed=[i for i in range(n) if i not in tied];v=[None]*n
 for i in fixed:v[i]=tau if e[i]>0 else tau-1
 rhs=[pen[j]*(1 if b[j]>0 else -1)*(1<<EX)/2-sum(Xi[i][j]*v[i] for i in fixed) for j in active]
 for i,z in zip(ties,integer_solve_rational_rhs([[Xi[i][j] for i in ties] for j in active],rhs)):v[i]=z
 assert all(tau-1<=z<=tau for z in v)
 LV=math.lcm(*(z.denominator for z in v));vn=[z.numerator*(LV//z.denominator) for z in v]
 grad=[F(sum(row[j]*z for row,z in zip(Xi,vn)),(1<<EX)*LV) for j in range(p)]
 assert all(abs(g)<=l/2 for g,l in zip(grad,pen))
 assert all(grad[j]==pen[j]*(1 if b[j]>0 else -1)/2 for j in active)
 dual=F(sum(a*z for a,z in zip(yi,vn)),(1<<EY)*LV);assert P==dual
 inactive=[j for j in range(p) if j not in set(active)]
 score_margin=min(min(v[i]-(tau-1),tau-v[i]) for i in ties)
 penalty_margin=min((pen[j]/2-abs(grad[j]) for j in inactive),default=F(1))
 if score_margin<=0 or penalty_margin<=0:raise ArithmeticError('OUTCOME_UNRESOLVED: strict uniqueness proof unavailable')
 return {'version':'2G-D.1','status':'EXACT_OPTIMUM_CERTIFIED','n':n,'p_with_intercept':p,'tau':record(tau),
  'primal':record(P),'dual':record(dual),'gap':record(P-dual),
  'beta_numerators':[str(z) for z in bn],'beta_denominator':str(LB),
  'residual_numerators':[str(z) for z in e],'residual_denominator':str(D),
  'fitted_numerators':[str(z) for z in pred],'fitted_denominator':str(PD),
  'dual_numerators':[str(z) for z in vn],'dual_denominator':str(LV),
  'active_coefficients_zero_based':active,'tied_observations_one_based':[i+1 for i in ties],
  'inactive_coefficients_zero_based':inactive,'basis_integer_determinant':str(det),'basis_integer_pivots':pivots,
  'minimum_tied_dual_box_margin':record(score_margin),'minimum_inactive_penalty_margin':record(penalty_margin),
  'unique_beta_and_fitted_values':True,'uniqueness_proof':'Strict tie-dual box and inactive penalty margins plus nonsingular tied/active system.',
  'proposal_threshold_is_not_a_tie_rule':True}
