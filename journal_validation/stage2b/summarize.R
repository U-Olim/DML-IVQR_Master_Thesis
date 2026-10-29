args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==1L)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE)
rows<-rbind(read.csv(file.path(out,"primary_evaluations.csv"),stringsAsFactors=FALSE),
  read.csv(file.path(out,"contrasts_evaluations.csv"),stringsAsFactors=FALSE))
write_table<-function(x,name)write.csv(x,file.path(out,name),row.names=FALSE)
mean_f<-function(x){x<-x[is.finite(x)];if(length(x))mean(x)else NA_real_}
se_f<-function(x){x<-x[is.finite(x)];if(length(x)>1)sd(x)/sqrt(length(x))else NA_real_}
wilson<-function(p,n) {
  if(!n)return(c(NA_real_,NA_real_))
  z<-qnorm(.975);den<-1+z*z/n;mid<-(p+z*z/(2*n))/den
  h<-z*sqrt(p*(1-p)/n+z*z/(4*n*n))/den;c(mid-h,mid+h)
}
write_table(rows,"all_evaluations.csv")
group_key<-function(x)interaction(x$design,x$estimator,drop=TRUE)
summary_rows<-list();paired_rows<-list();compact<-list()
for(g in split(rows,group_key(rows))) {
  base<-g[g$variant=="V00",];wide<-data.frame(replication=base$replication)
  for(v in c("V00","V10","V01","V11")) {
    z<-g[g$variant==v,];z<-z[match(base$replication,z$replication),]
    valid<-!z$failed & is.finite(z$W);accept<-1-as.numeric(z$rejected[valid]);n<-sum(valid)
    coverage<-mean_f(accept);ci<-wilson(coverage,n)
    summary_rows[[length(summary_rows)+1L]]<-data.frame(design=z$design[1],tau=z$tau[1],kappa=z$kappa[1],
      estimator=z$estimator[1],variant=v,total=nrow(z),successful=n,failures=sum(!valid),
      mean_W=mean_f(z$W),mean_W_MCSE=se_f(z$W),coverage=coverage,rejection=1-coverage,
      coverage_MCSE=if(n)sqrt(coverage*(1-coverage)/n)else NA_real_,
      Wilson95_lower=ci[1],Wilson95_upper=ci[2],
      mean_orthogonality_intercept=mean_f(z$orthogonality_intercept),
      mean_orthogonality_slopes=mean_f(z$orthogonality_slopes),
      max_orthogonality=max(z$orthogonality_max,na.rm=TRUE))
    wide[[paste0("W_",v)]]<-z$W
    wide[[paste0("A_",v)]]<-1-as.numeric(z$rejected)
  }
  wide$design<-base$design;wide$estimator<-base$estimator;wide$tau<-base$tau;wide$kappa<-base$kappa
  for(v in c("V10","V01","V11")) {
    wide[[paste0("delta_W_",v)]]<-wide[[paste0("W_",v)]]-wide$W_V00
    wide[[paste0("delta_A_",v)]]<-wide[[paste0("A_",v)]]-wide$A_V00
  }
  wide$interaction_W<-wide$W_V11-wide$W_V10-wide$W_V01+wide$W_V00
  wide$interaction_A<-wide$A_V11-wide$A_V10-wide$A_V01+wide$A_V00
  paired_rows[[length(paired_rows)+1L]]<-wide
}
summary<-do.call(rbind,summary_rows);pairs<-do.call(rbind,paired_rows)
write_table(summary,"variant_summary.csv");write_table(pairs,"paired_factorial.csv")
paired_summary<-list()
for(g in split(pairs,group_key(pairs)))for(effect in c("V10","V01","V11","interaction")) {
  w<-if(effect=="interaction")g$interaction_W else g[[paste0("delta_W_",effect)]]
  a<-if(effect=="interaction")g$interaction_A else g[[paste0("delta_A_",effect)]]
  paired_summary[[length(paired_summary)+1L]]<-data.frame(design=g$design[1],estimator=g$estimator[1],
    effect=effect,complete_pairs=sum(is.finite(w)&is.finite(a)),mean_delta_W=mean_f(w),W_MCSE=se_f(w),
    mean_delta_acceptance=mean_f(a),acceptance_MCSE=se_f(a),
    rejection_to_acceptance=if(effect=="interaction")NA_integer_ else sum(a==1,na.rm=TRUE),
    acceptance_to_rejection=if(effect=="interaction")NA_integer_ else sum(a== -1,na.rm=TRUE))
}
paired_summary<-do.call(rbind,paired_summary);write_table(paired_summary,"paired_effect_summary.csv")

outcome_rows<-conditional_rows<-unconditional_rows<-projection_rows<-penalty_rows<-assertions<-warnings<-list()
tasks<-readRDS(file.path(out,"tasks.rds"))
for(task in tasks) {
  record<-readRDS(task$result_path)
  if(length(record$warnings))warnings[[length(warnings)+1L]]<-data.frame(task_id=task$id,warning=record$warnings)
  if(!is.null(record$task_error))next # Failure rows already retained in all_evaluations.
  o<-record$outcome;est<-task$estimator
  X<-readRDS(task$data_path)$X
  if(est=="Oracle-GMM")X<-X[,1:10]
  error<-as.numeric(o$beta)-o$truth
  outcome_rows[[length(outcome_rows)+1L]]<-data.frame(task_id=task$id,design=task$design,estimator=est,
    replication=task$replication,estimated_intercept=o$beta[1],intercept_error=error[1],
    coefficient_l2_error=sqrt(sum(error^2)),coefficient_max_error=max(abs(error)),
    nuisance_prediction_RMS=sqrt(mean((cbind(1,X)%*%error)^2)),
    known_residual_identity_error=o$known_identity_error,
    estimated_mean_score=record$moments$estimated$unconditional$mean_score,
    known_mean_score=record$moments$known$unconditional$mean_score,
    estimated_rank_indicator_mismatch=record$moments$estimated$unconditional$rank_score_mismatch,
    known_rank_indicator_mismatch=record$moments$known$unconditional$rank_score_mismatch,
    intercept_penalty_score_target=if(is.null(o$lambda))NA_real_ else as.numeric(o$lambda[1])*sign(o$beta[1])/(2*nrow(X)),
    exact_zero_residuals=sum(o$e==0),near_zero_residuals_1e7=sum(abs(o$e)<=1e-7),
    density_min=min(o$f),density_max=max(o$f))
  for(nuisance in c("estimated","known")) {
    md<-record$moments[[nuisance]]
    d<-md$conditional;d$task_id<-task$id;d$design<-task$design;d$estimator<-est;d$replication<-task$replication;d$nuisance<-nuisance
    conditional_rows[[length(conditional_rows)+1L]]<-d
    u<-md$unconditional
    unconditional_rows[[length(unconditional_rows)+1L]]<-data.frame(task_id=task$id,design=task$design,estimator=est,
      replication=task$replication,nuisance=nuisance,
      moment=c("mean_score",paste0("X",0:(length(u$control_moments)-1L)),"Z1","Z2"),
      value=c(u$mean_score,u$control_moments,u$raw_instrument_moments))
  }
  for(projection in c("original","modified")) {
    p<-record$projections[[projection]];m<-p$orthogonality
    grid<-expand.grid(regressor=0:(nrow(m)-1),instrument=1:ncol(m))
    grid$value<-as.vector(m);grid$task_id<-task$id;grid$design<-task$design;grid$estimator<-est;grid$replication<-task$replication;grid$projection<-projection
    projection_rows[[length(projection_rows)+1L]]<-grid
    if(!is.null(p$penalty_conditions)) {
      pc<-p$penalty_conditions;pc$task_id<-task$id;pc$design<-task$design;pc$replication<-task$replication;pc$projection<-projection
      penalty_rows[[length(penalty_rows)+1L]]<-pc
    }
  }
  r<-record$rows
  assertions[[length(assertions)+1L]]<-data.frame(task_id=task$id,
    canonical_difference=record$reference_difference,
    same_data=length(unique(r$data_hash))==1L,same_density=length(unique(r$density_hash))==1L,
    same_residual_across_projection=r$outcome_residual_hash[1]==r$outcome_residual_hash[3]&&r$outcome_residual_hash[2]==r$outcome_residual_hash[4],
    same_projection_across_outcomes=r$projection_hash[1]==r$projection_hash[2]&&r$projection_hash[3]==r$projection_hash[4],
    same_penalty=record$projections$penalty_identical,
    rank_and_dimension_ok=all(r$design_rank==r$design_columns),
    known_score_rank_identity=record$moments$known$unconditional$rank_score_mismatch==0,
    penalty_replay_difference=if(est=="DML-IVQR-BC")max(vapply(record$projections$trace,`[[`,numeric(1),"replay_difference"))else 0,
    stored_next_vs_used_penalty_difference=if(est=="DML-IVQR-BC")max(vapply(record$projections$trace,function(t)max(abs(t$reported_next_penalty-t$last_penalty)),numeric(1)))else 0)
}
bind<-function(x)if(length(x))do.call(rbind,x)else data.frame()
od<-bind(outcome_rows);cond<-bind(conditional_rows);ortho<-bind(projection_rows);pen<-bind(penalty_rows);checks<-bind(assertions)
write_table(od,"outcome_diagnostics.csv");write_table(cond,"conditional_moments.csv")
write_table(bind(unconditional_rows),"unconditional_moments.csv");write_table(ortho,"weighted_orthogonality.csv")
write_table(pen,"projection_penalty_conditions.csv");write_table(checks,"isolation_checks.csv")
write_table(bind(warnings),"warnings.csv")
write_table(rows[rows$failed,],"failures.csv")
bool<-c("same_data","same_density","same_residual_across_projection","same_projection_across_outcomes","same_penalty","rank_and_dimension_ok","known_score_rank_identity")
stopifnot(all(as.matrix(checks[,bool])),max(checks$canonical_difference)<1e-11,max(checks$penalty_replay_difference)<1e-11)

outcome_summary<-bind(lapply(split(od,group_key(od)),function(g)data.frame(design=g$design[1],estimator=g$estimator[1],
  replications=nrow(g),mean_intercept_error=mean(g$intercept_error),mean_coefficient_l2_error=mean(g$coefficient_l2_error),
  mean_nuisance_prediction_RMS=mean(g$nuisance_prediction_RMS),
  estimated_mean_score=mean(g$estimated_mean_score),estimated_mean_score_MCSE=se_f(g$estimated_mean_score),
  known_mean_score=mean(g$known_mean_score),known_mean_score_MCSE=se_f(g$known_mean_score),
  mean_rank_mismatch_fraction=mean(g$estimated_rank_indicator_mismatch)/1000)))
outcome_summary$intercept_penalty_score_target<-vapply(seq_len(nrow(outcome_summary)),function(i){
  g<-od[od$design==outcome_summary$design[i]&od$estimator==outcome_summary$estimator[i],]
  mean_f(g$intercept_penalty_score_target)
},numeric(1))
write_table(outcome_summary,"outcome_summary.csv")
conditional_summary<-bind(lapply(split(cond,interaction(cond$design,cond$estimator,cond$nuisance,cond$partition,cond$bin,drop=TRUE)),function(g)
  data.frame(design=g$design[1],estimator=g$estimator[1],nuisance=g$nuisance[1],partition=g$partition[1],bin=g$bin[1],
    replications=nrow(g),mean_score=mean_f(g$mean_score),across_replication_MCSE=se_f(g$mean_score),
    mean_target=mean_f(g$target),zero_restriction=g$zero_restriction[1])))
write_table(conditional_summary,"conditional_moment_summary.csv")

for(g in split(summary,group_key(summary))) {
  row<-data.frame(design=g$design[1],tau=g$tau[1],kappa=g$kappa[1],estimator=g$estimator[1],N=g$total[1])
  for(v in c("V00","V10","V01","V11")) {
    z<-g[g$variant==v,]
    row[[paste0(v,"_mean_W")]]<-z$mean_W;row[[paste0(v,"_coverage")]]<-z$coverage;row[[paste0(v,"_failures")]]<-z$failures
  }
  compact[[length(compact)+1L]]<-row
}
compact<-bind(compact);write_table(compact,"compact_factorial.csv")
lines<-c("| Design | Estimator | N | V00 | V10 | V01 | V11 |","|---|---|---:|---:|---:|---:|---:|")
for(i in seq_len(nrow(compact))) {
  z<-compact[i,];cells<-vapply(c("V00","V10","V01","V11"),function(v)sprintf("%.3f / %.3f",z[[paste0(v,"_mean_W")]],z[[paste0(v,"_coverage")]]),character(1))
  lines<-c(lines,paste0("| ",paste(c(as.character(z$design),as.character(z$estimator),as.character(z$N),cells),collapse=" | ")," |"))
}
writeLines(c("Each variant cell: mean W / acceptance frequency (diagnostic coverage).", "",lines),file.path(out,"compact_factorial.md"))

primary<-pairs[pairs$design=="primary",]
png(file.path(out,"primary_factorial_W.png"),width=1500,height=750,res=130)
par(mfrow=c(1,2),mar=c(5,5,3,1))
effects<-c("V10","V01","V11")
cols<-c("Oracle-GMM"="#3673A5","Full-GMM"="#BD6A32","DML-IVQR-BC"="#6D5798")
values<-unlist(lapply(effects,function(v)primary[[paste0("delta_W_",v)]]))
short<-c("Oracle-GMM"="Oracle","Full-GMM"="Full","DML-IVQR-BC"="DML")
groups<-unlist(lapply(effects,function(v)paste(short[primary$estimator],v,sep="/")))
boxplot(values~factor(groups),las=2,col="#C5DCE8",ylab="W(variant) - W(V00)",main="Primary: paired W differences",cex.axis=.75)
abline(h=0,lty=2,col="gray50")
boxplot(interaction_W~estimator,data=primary,col=unname(cols[sort(unique(primary$estimator))]),
  ylab="W11 - W10 - W01 + W00",main="Primary: factorial interaction",cex.axis=.8)
abline(h=0,lty=2,col="gray50");dev.off()
cat("COMPACT_FACTORIAL\n");print(compact,row.names=FALSE)
cat("PAIRED_EFFECTS\n");print(paired_summary,row.names=FALSE)
cat("OUTCOME_DIAGNOSTICS\n");print(outcome_summary,row.names=FALSE)
cat("NUMERICAL_FAILURES",sum(rows$failed),"WARNINGS",nrow(bind(warnings)),"\n")
cat("SUMMARY_COMPLETE\n")
