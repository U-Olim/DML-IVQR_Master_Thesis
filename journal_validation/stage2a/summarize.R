args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==1)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE)
ab<-read.csv(file.path(out,"ab_pairs.csv"),stringsAsFactors=FALSE)
pilot<-read.csv(file.path(out,"pilot_pairs.csv"),stringsAsFactors=FALSE)
write_table<-function(x,name)write.csv(x,file.path(out,name),row.names=FALSE)
# Independently check that the ONLY RNG consumption in DML fitting was the
# pivotal Uniform matrix. Instrument regressions must not add hidden randomness.
rng_checks<-lapply(c(ab$task_id,pilot$task_id),function(id){
  record<-readRDS(file.path(out,"details",paste0(id,".rds")))
  expected<-record$task$stream
  if(record$task$estimator=="DML-IVQR-BC") {
    assign(".Random.seed",expected,envir=.GlobalEnv)
    invisible(runif(record$summary$n*1000L))
    expected<-get(".Random.seed",envir=.GlobalEnv)
  }
  data.frame(task_id=id,baseline_only_expected_rng=identical(expected,record$baseline$rng_after),
    alternative_only_expected_rng=identical(expected,record$alternative$rng_after))
})
rng_checks<-do.call(rbind,rng_checks)
write_table(rng_checks,"rng_consumption_checks.csv")
stopifnot(all(rng_checks$baseline_only_expected_rng),all(rng_checks$alternative_only_expected_rng))
finite<-function(x)x[is.finite(x)]
mean_f<-function(x)if(length(finite(x)))mean(finite(x)) else NA_real_
range_f<-function(x)if(length(finite(x)))range(finite(x)) else c(NA_real_,NA_real_)
wilson<-function(success,n) {
  if(!n)return(c(NA_real_,NA_real_))
  z<-qnorm(.975);p<-success/n;den<-1+z*z/n
  center<-(p+z*z/(2*n))/den
  half<-z*sqrt(p*(1-p)/n+z*z/(4*n*n))/den
  c(center-half,center+half)
}

# Details contain every coefficient vector and instrument penalty/loading vector.
evals<-lapply(seq_len(nrow(ab)),function(i){
  row<-ab[i,];fit<-readRDS(file.path(out,"details",paste0(row$task_id,".rds")))$baseline
  if(fit$failed)return(data.frame(task_id=row$task_id,lambda_intercept=NA,lambda_min=NA,lambda_max=NA,beta_l2=NA,selected_controls=NA))
  data.frame(task_id=row$task_id,lambda_intercept=fit$value$lambda[1],
    lambda_min=min(fit$value$lambda),lambda_max=max(fit$value$lambda),
    beta_l2=sqrt(sum(fit$value$beta^2)),selected_controls=sum(abs(fit$value$beta[-1])>1e-6))
})
ev<-do.call(rbind,evals);a<-merge(ab,ev,by="task_id",sort=FALSE)
write_table(a,"A_evaluations.csv")
per_dataset<-lapply(split(a,interaction(a$sample_id,a$tau,drop=TRUE)),function(g){
  good<-g[!g$failed_baseline,,drop=FALSE]
  betas<-lapply(good$task_id,function(id)readRDS(file.path(out,"details",paste0(id,".rds")))$baseline$value$beta)
  beta_matrix<-if(length(betas))do.call(cbind,betas)else matrix(NA_real_,1,1)
  data.frame(n=g$n[1],tau=g$tau[1],kappa=g$kappa[1],sample_id=g$sample_id[1],
    evaluations=nrow(g),successful=nrow(good),failures=sum(g$failed_baseline),
    W_min=range_f(good$W_baseline)[1],W_max=range_f(good$W_baseline)[2],W_sd=sd(good$W_baseline),
    reject_count=sum(good$rejected_baseline),
    decision_changes=length(unique(good$rejected_baseline))>1,
    lambda_intercept_min=range_f(good$lambda_intercept)[1],lambda_intercept_max=range_f(good$lambda_intercept)[2],
    max_beta_coordinate_range=max(apply(beta_matrix,1,function(b)diff(range(b)))),stringsAsFactors=FALSE)
})
ad<-do.call(rbind,per_dataset);write_table(ad,"A_per_dataset.csv")
at<-do.call(rbind,lapply(split(ad,interaction(ad$n,ad$tau,ad$kappa,drop=TRUE)),function(g)
  data.frame(n=g$n[1],tau=g$tau[1],kappa=g$kappa[1],datasets=nrow(g),evaluations=sum(g$evaluations),
    failures=sum(g$failures),datasets_with_decision_changes=sum(g$decision_changes),
    mean_within_dataset_W_sd=mean_f(g$W_sd),max_within_dataset_W_range=max(g$W_max-g$W_min),
    max_beta_coordinate_range=max(g$max_beta_coordinate_range))))
at<-at[order(at$n,at$tau,-at$kappa),];write_table(at,"A_summary.csv")

bt<-do.call(rbind,lapply(split(ab,interaction(ab$n,ab$tau,ab$kappa,drop=TRUE)),function(g)
  data.frame(n=g$n[1],tau=g$tau[1],kappa=g$kappa[1],pairs=nrow(g),
    complete_pairs=sum(!g$failed_baseline & !g$failed_alternative),
    baseline_failures=sum(g$failed_baseline),alternative_failures=sum(g$failed_alternative),
    mean_density_rms_difference=mean_f(g$density_rms_diff),
    max_instrument_coefficient_difference=max(g$instrument_coef_max_abs_diff,na.rm=TRUE),
    max_residualized_instrument_difference=max(g$psi_max_abs_diff,na.rm=TRUE),
    mean_delta_W=mean_f(g$delta_W),min_delta_W=range_f(g$delta_W)[1],max_delta_W=range_f(g$delta_W)[2],
    decision_flips=sum(g$decision_flip,na.rm=TRUE))))
bt<-bt[order(bt$n,bt$tau,-bt$kappa),];write_table(bt,"B_summary.csv")

ct<-list();cp<-list()
for(est in unique(pilot$estimator)) {
  g<-pilot[pilot$estimator==est,,drop=FALSE]
  for(variant in c("baseline","alternative")) {
    failed<-g[[paste0("failed_",variant)]]
    accepted<-!g[[paste0("rejected_",variant)]][!failed]
    total<-length(accepted);success<-sum(accepted);ci<-wilson(success,total)
    ct[[length(ct)+1L]]<-data.frame(estimator=est,variant=variant,total=nrow(g),successful=total,
      failures=sum(failed),coverage=if(total)success/total else NA_real_,
      MCSE=if(total)sqrt((success/total)*(1-success/total)/total) else NA_real_,
      Wilson95_lower=ci[1],Wilson95_upper=ci[2])
  }
  good<-g[!g$failed_baseline & !g$failed_alternative,,drop=FALSE]
  diff<-as.numeric(!good$rejected_alternative)-as.numeric(!good$rejected_baseline)
  cp[[length(cp)+1L]]<-data.frame(estimator=est,complete_pairs=nrow(good),
    mean_delta_W=mean_f(good$delta_W),median_delta_W=median(good$delta_W),
    baseline_reject_alt_accept=sum(good$rejected_baseline & !good$rejected_alternative),
    baseline_accept_alt_reject=sum(!good$rejected_baseline & good$rejected_alternative),
    paired_coverage_difference=mean(diff),paired_difference_MCSE=sd(diff)/sqrt(length(diff)),
    delta_W_min=min(good$delta_W),delta_W_max=max(good$delta_W))
}
ct<-do.call(rbind,ct);cp<-do.call(rbind,cp)
write_table(ct,"C_coverage_summary.csv");write_table(cp,"C_paired_summary.csv")

stability<-lapply(c(ab$task_id,pilot$task_id),function(id){
  record<-readRDS(file.path(out,"details",paste0(id,".rds")))
  do.call(rbind,lapply(c("baseline","alternative"),function(v){
    fit<-record[[v]]
    data.frame(task_id=id,variant=v,failed=fit$failed,
      density_zero_count=if(fit$failed)NA else sum(fit$value$density==0),
      density_nonfinite_count=if(fit$failed)NA else sum(!is.finite(fit$value$density)),
      condition_J=if(is.null(fit$value$condition_J))NA else fit$value$condition_J,
      condition_second_moment=if(fit$failed)NA else fit$value$condition_second_moment,
      warning_count=length(fit$warnings),stringsAsFactors=FALSE)
  }))
})
write_table(do.call(rbind,stability),"numerical_stability.csv")

png(file.path(out,"paired_W_differences.png"),width=1500,height=750,res=130)
par(mfrow=c(1,2),mar=c(4.5,7,3,1))
labels<-sprintf("%d/%.1f/%.1f",ab$n,ab$tau,ab$kappa)
levels<-sprintf("%d/%.1f/%.1f",bt$n,bt$tau,bt$kappa)
boxplot(ab$delta_W~factor(labels,levels=rev(levels)),las=1,outline=TRUE,col="#B8D8E8",
  horizontal=TRUE,xlab="W(sd) - W(var)",ylab="",main="Fixed samples: n / tau / kappa")
abline(v=0,lty=2,col="gray40")
par(mar=c(4.5,4.5,3,1))
cols<-c("Oracle-GMM"="#3673A5","Full-GMM"="#BD6A32","DML-IVQR-BC"="#6D5798")
plot(range(as.numeric(pilot$sample_id)),range(c(0,pilot$delta_W),finite=TRUE),type="n",
  xlab="Pilot replication",ylab="W(sd) - W(var)",main="40-replication pilot")
abline(h=0,lty=2,col="gray40")
for(est in names(cols)) {
  g<-pilot[pilot$estimator==est,,drop=FALSE];g<-g[order(as.integer(g$sample_id)),]
  lines(as.integer(g$sample_id),g$delta_W,col=cols[est],type="b",pch=16,cex=.5)
}
legend("bottomleft",legend=names(cols),col=cols,pch=16,lty=1,bty="n",cex=.75)
dev.off()
cat("EXPERIMENT_A\n");print(at,row.names=FALSE)
cat("EXPERIMENT_B\n");print(bt,row.names=FALSE)
cat("EXPERIMENT_C\n");print(ct,row.names=FALSE);print(cp,row.names=FALSE)
cat("SUMMARIZE_COMPLETE\n")
