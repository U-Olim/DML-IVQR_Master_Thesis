args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==1L)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE)
source("thesis_extension/environment/check_author_environment.R")
assert_author_environment("thesis_extension",write_outputs=FALSE)
tasks<-readRDS(file.path(out,"tasks.rds"));checks<-list()
for(task in tasks) {
  r<-readRDS(task$result_path)
  if(!is.null(r$task_error)) {
    checks[[length(checks)+1L]]<-data.frame(task_id=task$id,checked=FALSE,reason=r$task_error,
      W_max_difference=NA_real_,orthogonality_max_difference=NA_real_,known_beta_exact=NA,
      penalty_exact=NA,coefficient_reconstruction_max=NA_real_,all_weights_finite=NA)
    next
  }
  dat<-readRDS(task$data_path);X<-if(task$estimator=="Oracle-GMM")dat$X1 else dat$X
  stopifnot(identical(r$outcome$truth,c(1,rep(5,7),rep(0,ncol(X)-7))))
  coef_difference<-ortho_difference<-W_difference<-0
  for(projection in c("original","modified")) {
    p<-r$projections[[projection]]
    psi<-t(dat$Z-cbind(1,X)%*%p$coefficient)
    coef_difference<-max(coef_difference,max(abs(psi-p$psi)))
    M<-crossprod(cbind(1,X),r$outcome$f*t(p$psi))/nrow(X)
    ortho_difference<-max(ortho_difference,max(abs(M-p$orthogonality)))
  }
  for(v in c("V00","V10","V01","V11")) {
    known<-v%in%c("V10","V11");modified<-v%in%c("V01","V11")
    e<-if(known)r$outcome$known else r$outcome$e
    psi<-r$projections[[if(modified)"modified" else "original"]]$psi
    score<-task$tau-as.numeric(e<=0)
    observations<-sweep(psi,2,score,`*`)
    summed<-rowSums(observations)
    # Independent O(n) second-moment route, avoiding the candidate's n*n diagonal.
    value<-sum(summed*solve(tcrossprod(observations),summed))
    W_difference<-max(W_difference,abs(value-r$variants[[v]]$W))
  }
  penalty_exact<-TRUE
  if(task$estimator=="DML-IVQR-BC")for(j in 1:2) {
    penalty_exact<-penalty_exact&&identical(r$projections$penalties[[j]],r$projections$trace[[j]]$last_penalty)
    stopifnot(r$projections$trace[[j]]$options$penalty$c==.5,
      r$projections$trace[[j]]$options$penalty$gamma==.1/log(1000))
  }
  stopifnot(W_difference<1e-10,ortho_difference<1e-12,coef_difference<1e-10,penalty_exact,
    all(is.finite(r$outcome$f)),all(r$outcome$f>0))
  checks[[length(checks)+1L]]<-data.frame(task_id=task$id,checked=TRUE,reason="",
    W_max_difference=W_difference,orthogonality_max_difference=ortho_difference,known_beta_exact=TRUE,
    penalty_exact=penalty_exact,coefficient_reconstruction_max=coef_difference,all_weights_finite=TRUE)
}
write.csv(do.call(rbind,checks),file.path(out,"independent_detail_checks.csv"),row.names=FALSE)
cat("INDEPENDENT_DETAIL_CHECKS",sum(vapply(checks,function(x)x$checked,logical(1))),"of",length(tasks),"\n")
