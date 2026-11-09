"""Export frozen population diagnostics, without estimating them from pilot outcomes."""
from pathlib import Path
import csv,json,math
P=Path(__file__).resolve().parent
run=Path((P/'LATEST_RUN.txt').read_text().strip())
source=P.parent/'readiness/results/analytical_density_checks.csv'
rows=list(csv.DictReader(source.open()))
out=[]
for row in rows:
 if float(row['Q1_plus_Q2'])!=0:continue
 for arm in ['A','B']:
  k=float(row['kappa']);tau=float(row['tau'])
  out.append({'arm':arm,'tau':tau,'kappa':k,'local_profile_Jacobian_magnitude_per_instrument':abs(float(row['local_profile_Jacobian_per_instrument'])) if arm=='B' else '', 'Jacobian_scope':'bounded ideal-population local QR profile' if arm=='B' else 'not asserted: original inverse-treatment expectation diverges; bounded differentiation proof does not apply','population_cov_D_Qj':(.9 if arm=='B' else 1)*k/(2*math.sqrt(2*math.pi)),'population_linear_R2':k*k/(8*math.pi*(math.asin(.75)/(2*math.pi))),'population_treatment_variance':(.81 if arm=='B' else 1)*math.asin(.75)/(2*math.pi),'full_conditioning_uniform_density_lower_bound':0,'source':'frozen readiness derivation and scalar quadrature'})
with (run/'analytical_relevance.csv').open('x',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
print('Exported 12 prespecified analytical arm/cell diagnostics')
