hash_object <- function(x) digest::digest(x,algo="sha256",serialize=TRUE)
set_stream <- function(state)assign(".Random.seed",state,envir=.GlobalEnv)
state_text <- function(x)paste(x,collapse=";")
true_beta <- function(p)c(1,rep(5,7),rep(0,p-7))
max_abs <- function(x)max(abs(x))

capture_adaptive <- function(Xw,yw,original) {
  # Private closure only; historical namespace and files are never modified.
  capture <- new.env(parent=emptyenv());capture$calls<-list()
  ns <- asNamespace("hdm")
  local_env <- new.env(parent=ns)
  solver <- get("LassoShooting.fit",ns)
  local_env$LassoShooting.fit <- function(x,y,lambda,...) {
    fit <- solver(x,y,lambda,...)
    capture$calls[[length(capture$calls)+1L]] <- list(lambda=lambda,coefficients=fit$coefficients,
      iterations=fit$num.it,x_hash=hash_object(unname(x)),y_hash=hash_object(unname(y)))
    fit
  }
  fun <- get("rlasso.default",ns);environment(fun)<-local_env
  fit <- fun(Xw,yw,post=FALSE,intercept=TRUE,
    penalty=original$options$penalty,control=original$options$control)
  stopifnot(length(capture$calls)>0L,
    max_abs(as.numeric(fit$coefficients)-as.numeric(original$coefficients))<1e-11)
  last <- capture$calls[[length(capture$calls)]]
  centered_X <- scale(Xw,colMeans(Xw),FALSE)
  centered_y <- matrix(yw-mean(yw),ncol=1)
  replay <- solver(centered_X,centered_y,last$lambda)
  b <- as.numeric(replay$coefficients)
  coef <- c(mean(yw)-sum(colMeans(Xw)*b),b)
  stopifnot(max_abs(coef-as.numeric(original$coefficients))<1e-11,
    max_abs(as.numeric(last$coefficients)-b)<1e-11)
  list(last_penalty=last$lambda,trace=capture$calls,replay_difference=max_abs(coef-as.numeric(original$coefficients)),
    options=fit$options,reported_next_penalty=fit$lambda)
}

projection_diagnostics <- function(X,Z,f,psi,coef,transformed_error,penalty=NULL,gram=NULL,design=NULL) {
  n<-nrow(X);Xt<-cbind(1,X)
  ortho<-crossprod(Xt,f*t(psi))/n
  out<-list(orthogonality=ortho,orthogonality_intercept=max_abs(ortho[1,,drop=FALSE]),
    orthogonality_slopes=max_abs(ortho[-1,,drop=FALSE]),orthogonality_max=max_abs(ortho),
    coefficient=coef,psi=psi,density_hash=hash_object(f),
    gram_condition=if(is.null(gram))NA_real_ else kappa(gram),
    design_rank=if(is.null(design))NA_integer_ else qr(design)$rank,
    design_columns=if(is.null(design))NA_integer_ else ncol(design))
  if(!is.null(penalty)) {
    checks<-lapply(seq_len(ncol(Z)),function(j){
      gradient<-2*crossprod(sqrt(f)*X,transformed_error[,j])
      beta<-coef[-1,j];lam<-as.numeric(penalty[[j]])
      active<-abs(beta)>0
      residual<-ifelse(active,abs(as.numeric(gradient)-lam*sign(beta)),pmax(abs(as.numeric(gradient))-lam,0))
      data.frame(instrument=j,max_KKT_violation=max(residual),
        max_KKT_violation_over_n=max(residual)/n,
        lambda_min=min(lam),lambda_max=max(lam),active_slopes=sum(active),
        ordinary_transformed_intercept_gradient=2*sum(transformed_error[,j]),
        weighted_intercept_gradient=2*sum(sqrt(f)*transformed_error[,j]))
    })
    out$penalty_conditions<-do.call(rbind,checks)
  }
  out
}

project_pair <- function(dat,X,f,estimator) {
  Z<-dat$Z;n<-nrow(X);p<-ncol(X);Xt<-cbind(1,X);w<-sqrt(f)
  F<-diag(f)
  if(estimator!="DML-IVQR-BC") {
    J<-t(X)%*%F%*%X
    delta<-(t(Z)%*%F%*%X)%*%solve(J)
    psi0<-t(Z)-delta%*%t(X)
    coef0<-rbind(0,t(delta))
    J1<-t(Xt)%*%F%*%Xt
    delta1<-(t(Z)%*%F%*%Xt)%*%solve(J1)
    psi1<-t(Z)-delta1%*%t(Xt)
    coef1<-t(delta1)
    return(list(original=projection_diagnostics(X,Z,f,psi0,coef0,NULL,gram=J,design=w*X),
      modified=projection_diagnostics(X,Z,f,psi1,coef1,NULL,gram=J1,design=w*Xt),
      penalty_identical=TRUE,trace=NULL))
  }
  # Preserve original matrix multiplication/formula path for V00.
  distribition<-sqrt(diag(f));psi0<-matrix(0,nrow=ncol(Z),ncol=n)
  coef0<-coef1<-matrix(NA_real_,p+1,ncol(Z));psi1<-psi0
  err0<-err1<-matrix(NA_real_,n,ncol(Z));penalties<-traces<-vector("list",ncol(Z))
  Xw<-distribition%*%X
  centered0<-scale(Xw,colMeans(Xw),FALSE)
  # Partial out the unpenalized transformed constant w, NOT the ordinary constant.
  projected_X<-Xw-w%o%drop(crossprod(w,Xw)/sum(w*w))
  for(j in seq_len(ncol(Z))) {
    fit<-hdm::rlasso(distribition%*%Z[,j] ~ distribition%*%X,post=FALSE)
    coef0[,j]<-as.numeric(fit$coefficients)
    psi0[j,]<-drop(Z[,j]-cbind(1,X)%*%matrix(fit$coefficients,ncol=1))
    yw<-drop(distribition%*%Z[,j])
    captured<-capture_adaptive(Xw,yw,fit)
    penalties[[j]]<-captured$last_penalty;traces[[j]]<-captured
    projected_y<-matrix(yw-w*sum(w*yw)/sum(w*w),ncol=1)
    # Same historical final quadratic solver, default tolerances, same slope penalties.
    solution<-hdm:::LassoShooting.fit(projected_X,projected_y,penalties[[j]])
    gamma<-as.numeric(solution$coefficients)
    intercept<-sum(w*(yw-Xw%*%gamma))/sum(w*w)
    coef1[,j]<-c(intercept,gamma)
    psi1[j,]<-drop(Z[,j]-Xt%*%coef1[,j])
    err0[,j]<-drop(yw-coef0[1,j]-Xw%*%coef0[-1,j])
    err1[,j]<-drop(yw-w*coef1[1,j]-Xw%*%coef1[-1,j])
    stopifnot(max_abs(err1[,j]-w*psi1[j,])<1e-11)
  }
  list(original=projection_diagnostics(X,Z,f,psi0,coef0,err0,penalties,
      gram=crossprod(centered0),design=cbind(1,Xw)),
    modified=projection_diagnostics(X,Z,f,psi1,coef1,err1,penalties,
      gram=crossprod(projected_X),design=cbind(w,Xw)),
    penalty_identical=TRUE,penalties=penalties,trace=traces,
    projection_definition="Final original adaptive penalty frozen; same historical quadratic solver, transformed unpenalized constant")
}

outcome_fit <- function(dat,X,tau,estimator,state) {
  set_stream(state);lambda<-NULL;draw_hash<-NA_character_
  if(estimator=="DML-IVQR-BC") {
    U<-matrix(runif(nrow(X)*1000L),nrow(X));draw_hash<-hash_object(U)
    set_stream(state)
    lambda<-lambda_BC_author(X,R=1000,tau=tau,c=2,alpha=.1)
    fit<-quantreg::rq(dat$y-alpha_true(tau)*dat$D ~ X,tau=tau,method="lasso",lambda=lambda)
  } else fit<-quantreg::rq(dat$y-alpha_true(tau)*dat$D ~ X,tau=tau)
  beta<-matrix(fit$coefficients,ncol=1)
  # Original GMM uses row beta then transpose; same matrix-vector product.
  e<-drop(dat$y-alpha_true(tau)*dat$D-cbind(1,X)%*%beta)
  truth<-true_beta(ncol(X))
  known<-drop(dat$y-alpha_true(tau)*dat$D-cbind(1,X)%*%truth)
  analytic<-dat$D*(dat$primitives$u-qnorm(tau))
  stopifnot(max_abs(known-analytic)<1e-11,identical(known<=0,analytic<=0),all(dat$D>0))
  # Freeze both values and convention at V00 for ALL four cells.
  f<-c(dnorm(e,mean(e),var(e)))
  if(any(!is.finite(f))||any(f<0))stop("Nonfinite/negative density weights")
  list(beta=beta,truth=truth,e=e,known=known,analytic=analytic,f=f,lambda=lambda,
    draw_hash=draw_hash,rng_after=get(".Random.seed",.GlobalEnv),
    known_identity_error=max_abs(known-analytic),data_hash=hash_object(dat))
}

score_statistic <- function(e,psi,tau) {
  s<-matrix(tau-as.numeric(e<=0),ncol=1)
  g<-psi%*%s
  S<-psi%*%diag(diag(s%*%t(s)))%*%t(psi)
  W<-drop(t(g)%*%solve(S)%*%g)
  if(!is.finite(W))stop("Nonfinite W")
  list(W=W,s=drop(s),moment=drop(g/ncol(psi)),second_moment=S/ncol(psi),condition=kappa(S))
}

moment_diagnostics <- function(dat,X,outcome,tau,known) {
  e<-if(known)outcome$known else outcome$e
  s<-tau-as.numeric(e<=0);Xt<-cbind(1,X)
  unconditional<-list(mean_score=mean(s),control_moments=drop(crossprod(Xt,s)/length(s)),
    raw_instrument_moments=drop(crossprod(dat$Z,s)/length(s)),
    rank_score_mismatch=sum((e<=0)!=(dat$primitives$u<=qnorm(tau))))
  # Fixed observable partitions. These are descriptive sample checks, not tests
  # that recover an infinite-dimensional conditional moment restriction.
  Zclean<-cbind(dat$Z[,1]-X[,2]-X[,3]-X[,4],dat$Z[,2]-X[,7]-X[,8]-X[,9]-X[,10])
  partitions<-list(X1=cut(X[,1],c(-Inf,.25,.5,.75,Inf),labels=FALSE),
    Z1clean=cut(Zclean[,1],c(-Inf,sqrt(2)*qnorm(c(.25,.5,.75)),Inf),labels=FALSE),
    Z2clean=cut(Zclean[,2],c(-Inf,sqrt(2)*qnorm(c(.25,.5,.75)),Inf),labels=FALSE),
    D=cut(dat$D,pnorm(c(-Inf,sqrt(3)*qnorm(c(.25,.5,.75)),Inf)),labels=FALSE))
  rows<-list()
  # E[s|D] need not vanish because D is endogenous. Its correct analytic value
  # follows u|T ~ N(.1*T,.97), T=Phi^{-1}(D).
  conditional_D_target<-tau-pnorm((qnorm(tau)-.1*dat$d)/sqrt(.97))
  for(name in names(partitions))for(bin in 1:4) {
    ix<-which(partitions[[name]]==bin)
    rows[[length(rows)+1L]]<-data.frame(partition=name,bin=bin,count=length(ix),
      mean_score=if(length(ix))mean(s[ix])else NA_real_,
      target=if(name=="D" && length(ix))mean(conditional_D_target[ix])else 0,
      nominal_binomial_SE=if(length(ix))sqrt(tau*(1-tau)/length(ix))else NA_real_,
      zero_restriction=name!="D")
  }
  list(unconditional=unconditional,conditional=do.call(rbind,rows))
}

task_failure_rows <- function(task,message) {
  data.frame(task_id=task$id,design=task$design,replication=task$replication,
    n=1000L,tau=task$tau,kappa=task$kappa,estimator=task$estimator,
    variant=c("V00","V10","V01","V11"),W=NA_real_,rejected=NA,failed=TRUE,error=message,
    data_hash=NA_character_,density_hash=NA_character_,projection_hash=NA_character_,
    outcome_residual_hash=NA_character_,pivotal_hash=NA_character_,density_nonfinite=NA_integer_,
    density_zero=NA_integer_,covariance_condition=NA_real_,orthogonality_intercept=NA_real_,
    orthogonality_slopes=NA_real_,orthogonality_max=NA_real_,gram_condition=NA_real_,
    design_rank=NA_integer_,design_columns=NA_integer_,worker_pid=Sys.getpid(),stringsAsFactors=FALSE)
}

run_task <- function(task) {
  warnings<-character();start<-proc.time()[3]
  result<-tryCatch(withCallingHandlers({
    dat<-readRDS(task$data_path);data_hash<-hash_object(dat)
    X<-if(task$estimator=="Oracle-GMM")dat$X1 else dat$X
    outcome<-outcome_fit(dat,X,task$tau,task$estimator,task$stream)
    projections<-project_pair(dat,X,outcome$f,task$estimator)
    stopifnot(identical(data_hash,hash_object(dat)),
      identical(outcome$rng_after,get(".Random.seed",.GlobalEnv)),projections$penalty_identical)
    variants<-list();rows<-list()
    for(v in c("V00","V10","V01","V11")) {
      known<-v %in% c("V10","V11");modified<-v %in% c("V01","V11")
      proj<-if(modified)projections$modified else projections$original
      e<-if(known)outcome$known else outcome$e
      attempt<-tryCatch(score_statistic(e,proj$psi,task$tau),error=function(e)list(error=conditionMessage(e)))
      failed<-!is.null(attempt$error)
      variants[[v]]<-attempt
      rows[[v]]<-data.frame(task_id=task$id,design=task$design,replication=task$replication,
        n=nrow(X),tau=task$tau,kappa=dat$kappa,estimator=task$estimator,variant=v,
        W=if(failed)NA_real_ else attempt$W,rejected=if(failed)NA else attempt$W>qchisq(.95,2),
        failed=failed,error=if(failed)attempt$error else "",data_hash=data_hash,
        density_hash=hash_object(outcome$f),projection_hash=hash_object(proj$psi),
        outcome_residual_hash=hash_object(e),pivotal_hash=outcome$draw_hash,
        density_nonfinite=sum(!is.finite(outcome$f)),density_zero=sum(outcome$f==0),
        covariance_condition=if(failed)NA_real_ else attempt$condition,
        orthogonality_intercept=proj$orthogonality_intercept,
        orthogonality_slopes=proj$orthogonality_slopes,orthogonality_max=proj$orthogonality_max,
        gram_condition=proj$gram_condition,design_rank=proj$design_rank,design_columns=proj$design_columns,
        worker_pid=Sys.getpid(),stringsAsFactors=FALSE)
    }
    # Canonical reference for EVERY task, with exactly the same RNG start.
    set_stream(task$stream)
    ref_fun<-if(task$estimator=="DML-IVQR-BC")author_bc_candidate else author_gmm_candidate
    reference<-ref_fun(dat$y,dat$D,X,dat$Z,task$tau,alpha_true(task$tau),TRUE)
    reference_difference<-abs(reference$W-variants$V00$W)
    stopifnot(reference_difference<1e-11,
      max_abs(reference$psi-projections$original$psi)<1e-11,
      max_abs(reference$e-outcome$e)<1e-11,
      identical(outcome$rng_after,get(".Random.seed",.GlobalEnv)))
    if(task$estimator=="DML-IVQR-BC")stopifnot(identical(reference$lambda,outcome$lambda))
    md<-list(estimated=moment_diagnostics(dat,X,outcome,task$tau,FALSE),
             known=moment_diagnostics(dat,X,outcome,task$tau,TRUE))
    list(task=task,outcome=outcome,projections=projections,variants=variants,
      moments=md,rows=do.call(rbind,rows),reference_difference=reference_difference,
      paired_assertions=TRUE)
  },warning=function(w){warnings<<-c(warnings,conditionMessage(w));invokeRestart("muffleWarning")}),
    error=function(e)list(task=task,task_error=conditionMessage(e)))
  result$warnings<-warnings;result$elapsed<-unname(proc.time()[3]-start)
  saveRDS(result,task$result_path)
  if(!is.null(result$task_error)) {
    cat("TASK_FAILURE",task$id,result$task_error,"\n")
    return(task_failure_rows(task,result$task_error))
  }
  result$rows
}
