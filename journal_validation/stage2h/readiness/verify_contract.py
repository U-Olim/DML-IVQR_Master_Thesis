"""Supplemental independent checks of generalized tau/score/cutoff wiring."""
from common_h0 import *
def main():
 checks=[]
 original_cut=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z/cutoff.bin'
 assert sha(original_cut)==sha(INPUT/'cutoff.bin')
 for d in tasks():
  id=d['id'];tau=F(float(read(INPUT/id/'parameters.bin')[0]));n=int(d['n'])
  for mode in ['sequential','repeat','parallel']:
   f=OUT/mode/id;r=load(f/'result.json')
   if r['status']!='PASS':checks.append({'id':id,'mode':mode,'status':'UNRESOLVED_RETAINED'});continue
   cert=load(f/'outcome_certificate.json');assert val(cert['tau'])==tau
   ranks=read(f/'rank.bin');scores=read(f/'score.bin')
   assert np.array_equal(scores,float(tau)-ranks)
   psi=read(f/'psi.bin',(n,2));obs=read(f/'observation_scores.bin',(n,2))
   assert np.array_equal(obs,psi*scores[:,None])
   assert np.array_equal(obs.sum(axis=0),read(f/'score_sum.bin'))
   assert np.array_equal(obs.T@obs,read(f/'second_moment.bin',(2,2)))
   hashes=load(f/'calibration_hashes.json')
   assert all(sha(f/name)==h for name,h in hashes.items())
   assert F(float(r['cutoff']))==F(float(read(INPUT/'cutoff.bin')[0]))
   checks.append({'id':id,'mode':mode,'status':'PASS','literal_tau_and_score_convention':'PASS','cutoff_bytes':'PASS','penalty_bytes_unchanged_since_native_calibration':'PASS'})
 table(OUT/'independent_contract_checks.csv',checks)
 dump(OUT/'independent_contract_checks.json',{'executions':36,'passed':sum(r['status']=='PASS' for r in checks),'status':'PASS' if all(r['status']=='PASS' for r in checks) else 'UNRESOLVED_RETAINED'})
if __name__=='__main__':main()
