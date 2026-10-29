stage2b_config <- list(
  n=1000L, primary_replications=40L, contrast_replications=12L,
  designs=data.frame(design=c("primary","median","weak"),tau=c(.9,.5,.9),kappa=c(1,1,.1)),
  estimators=c("Oracle-GMM","Full-GMM","DML-IVQR-BC"),
  variants=c("V00","V10","V01","V11"),workers=2L,
  source_run="journal_validation/stage2a/output/controlled_20261022_01",
  contrast_penalty_master_seed=20261024L,
  density="Frozen V00 dnorm(e_est,mean(e_est),var(e_est)), per dataset/estimator/design",
  projection_penalty="DML: actual last solver penalty vector from original adaptive fit, held fixed",
  cutoff=qchisq(.95,2), coefficient_tolerance=1e-10, identity_tolerance=1e-11)
