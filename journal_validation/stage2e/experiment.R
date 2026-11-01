args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==2L)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE);phase<-args[2]
stopifnot(phase%in%c("prepare","evaluate"))
source("thesis_extension/environment/check_author_environment.R")
assert_author_environment("thesis_extension",write_outputs=FALSE)
source("thesis_extension/src/author_bc_dml_wrapper.R")
source("journal_validation/stage2b/diagnostics.R") # definitions only; original penalty tracing
put<-function(x,path){stopifnot(!file.exists(path));con<-file(path,"wb");writeBin(as.double(x),con,size=8,endian="little");close(con)}
getbin<-function(path,count){con<-file(path,"rb");x<-readBin(con,"double",n=count,size=8,endian="little");close(con);stopifnot(length(x)==count);x}
stream_at<-function(index){set.seed(2026102905L);s<-.Random.seed;if(index>1)for(k in seq_len(index-1))s<-parallel::nextRNGStream(s);s}
native_projection<-function(dat,f) {
 before<-.Random.seed;w<-sqrt(diag(f));psi<-matrix(0,2,nrow(dat$X));coefs<-captures<-list()
 for(j in 1:2) {
  fit<-hdm::rlasso(w%*%dat$Z[,j]~w%*%dat$X,post=FALSE)
  coefs[[j]]<-as.numeric(fit$coefficients)
  psi[j,]<-drop(dat$Z[,j]-cbind(1,dat$X)%*%matrix(fit$coefficients,ncol=1))
  captures[[j]]<-capture_adaptive(w%*%dat$X,drop(w%*%dat$Z[,j]),fit)
 }
 stopifnot(identical(before,.Random.seed))
 list(psi=psi,coefficients=coefs,penalty_traces=captures,rng_unchanged=TRUE,
  weighted_gram_condition=kappa(crossprod(sqrt(f)*dat$X)))
}
stat<-function(e,psi) {
 s<-.9-as.numeric(e<=0);obs<-s*t(psi);g<-colSums(obs);S<-crossprod(obs)
 W<-drop(t(g)%*%solve(S,g));stopifnot(is.finite(W))
 list(score=s,g=g,S=S,W=W,accepted=W<=qchisq(.95,2),condition=kappa(S))
}
datasets<-c("pilot_003","pilot_014","pilot_001","pilot_002","pilot_004","pilot_005","pilot_006","pilot_007")
RNGkind("L'Ecuyer-CMRG","Inversion")
if(phase=="prepare") {
 writeLines(capture.output(sessionInfo()),file.path(out,"R_sessionInfo.txt"))
 writeLines(capture.output(quantreg::rq.fit.lasso),file.path(out,"historical_rq_fit_lasso.txt"))
 write.csv(installed.packages(lib.loc=.libPaths())[,c("Package","Version","LibPath")],file.path(out,"R_packages.csv"),row.names=FALSE)
 put(qchisq(.95,2),file.path(out,"cutoff.bin"));tasks<-list();idx<-0L;false_idx<-0L
 for(name in datasets) {
  source_path<-file.path("journal_validation/stage2c/output/controlled_20261029_01",name,"details.rds")
  stopifnot(file.exists(source_path));saved<-readRDS(source_path);dat<-saved$dat
  stopifnot(nrow(dat$X)==1000,ncol(dat$X)==100,dat$kappa==1)
  for(offset in c(-.5,0,.5)) {
   idx<-idx+1L;label<-if(offset==0)"truth"else if(offset<0)"minus"else"plus"
   id<-paste(name,label,sep="_");folder<-file.path(out,id);stopifnot(!dir.exists(folder));dir.create(folder)
   a<-1+qnorm(.9)+offset;ystar<-drop(dat$y-a*dat$D);warnings<-character()
   state<-if(offset==0)saved$penalty_state else {false_idx<-false_idx+1L;stream_at(false_idx)}
   tryCatch(withCallingHandlers({
    if(offset==0) {
     lambda<-saved$lambda;b<-saved$arms$P11$beta
     set_stream(state);lambda_check<-lambda_BC_author(dat$X,R=1000,tau=.9,c=2,alpha=.1)
     stopifnot(identical(lambda,lambda_check),identical(.Random.seed,saved$after_lambda))
    } else {
     set_stream(state);lambda<-lambda_BC_author(dat$X,R=1000,tau=.9,c=2,alpha=.1)
     fit<-quantreg::rq(ystar~dat$X,tau=.9,method="lasso",lambda=lambda)
     b<-as.numeric(fit$coefficients)
     saveRDS(fit,file.path(folder,"historical_outcome_fit.rds"))
     writeLines(capture.output(str(fit)),file.path(folder,"historical_fit_structure.txt"))
    }
    post_penalty_state<-.Random.seed
    e<-drop(ystar-cbind(1,dat$X)%*%b);f<-dnorm(e,mean(e),var(e));stopifnot(all(is.finite(f)),all(f>0))
    projection<-native_projection(dat,f);s<-stat(e,projection$psi)
    if(offset==0)stopifnot(identical(e,saved$arms$P11$e),identical(f,saved$f),
     max(abs(projection$psi-saved$psi))<1e-11,abs(s$W-saved$arms$P11$statistic$W)<1e-10)
    task<-list(id=id,dataset=name,offset=offset,candidate=a,folder=folder,source_path=source_path,
     dat=dat,ystar=ystar,lambda=lambda,beta=b,e=e,f=f,projection=projection,statistic=s,
     penalty_state=state,post_penalty_state=post_penalty_state,
     false_stream_index=if(offset==0)NA_integer_ else false_idx,
     historical_outcome_reused=offset==0)
    saveRDS(task,file.path(folder,"historical_task.rds"))
    put(as.vector(t(cbind(1,dat$X))),file.path(folder,"X_row_major.bin"))
    put(ystar,file.path(folder,"response.bin"));put(lambda,file.path(folder,"lambda.bin"))
    put(b,file.path(folder,"historical_beta.bin"));put(e,file.path(folder,"historical_residual.bin"))
    put(f,file.path(folder,"historical_density.bin"));put(projection$psi,file.path(folder,"historical_psi.bin"))
    put(s$score,file.path(folder,"historical_score.bin"))
    write.csv(data.frame(coordinate=0:100,beta=b,lambda=lambda),file.path(folder,"historical_coefficients.csv"),row.names=FALSE)
    writeLines(c(state_text(state),state_text(post_penalty_state)),file.path(folder,"penalty_rng_states.txt"))
    saveRDS(list(start=state,after=post_penalty_state),file.path(folder,"penalty_rng_states.rds"))
    tasks[[idx]]<-data.frame(id=id,dataset=name,offset=offset,candidate=a,
     false_stream_index=if(offset==0)NA_integer_ else false_idx,reused_saved_outcome=offset==0,
     data_hash=hash_object(dat),penalty_hash=hash_object(lambda),historical_W=s$W,
     historical_accepted=s$accepted,warnings=length(warnings),stringsAsFactors=FALSE)
    cat("HISTORICAL_COMPLETE",id,"W",s$W,"\n");flush.console()
   },warning=function(w){warnings<<-c(warnings,conditionMessage(w));invokeRestart("muffleWarning")}),
   error=function(e){writeLines(c(conditionMessage(e),warnings),file.path(folder,"FAILURE.txt"));stop(e)})
   writeLines(warnings,file.path(folder,"historical_warnings.txt"))
  }
 }
 stopifnot(idx==24L,false_idx==16L)
 write.csv(do.call(rbind,tasks),file.path(out,"task_manifest.csv"),row.names=FALSE)
 quit(status=0)
}
tasks<-read.csv(file.path(out,"task_manifest.csv"),stringsAsFactors=FALSE);rows<-list()
for(id in tasks$id) {
 folder<-file.path(out,id);task<-readRDS(file.path(folder,"historical_task.rds"))
 statusfile<-file.path(folder,"independent_status.txt")
 if(!file.exists(statusfile)||readLines(statusfile)[1]!="SUCCESS") {
  rows[[length(rows)+1L]]<-data.frame(id=id,status="INDEPENDENT_SOLVER_FAILED",stringsAsFactors=FALSE)
  next
 }
 b<-getbin(file.path(folder,"independent_beta.bin"),101L);warnings<-character()
 tryCatch(withCallingHandlers({
  e<-drop(task$ystar-cbind(1,task$dat$X)%*%b)
  layerA<-stat(e,task$projection$psi)
  set_stream(task$post_penalty_state);before<-.Random.seed
  f<-dnorm(e,mean(e),var(e));stopifnot(all(is.finite(f)),all(f>0))
  projection<-native_projection(task$dat,f);stopifnot(identical(before,.Random.seed))
  layerB<-stat(e,projection$psi)
  differences<-list(beta_max=max(abs(b-task$beta)),beta_l2=sqrt(sum((b-task$beta)^2)),
   prediction_max=max(abs(cbind(1,task$dat$X)%*%(b-task$beta))),
   prediction_RMS=sqrt(mean((cbind(1,task$dat$X)%*%(b-task$beta))^2)),
   rank_changes=sum((e<=0)!=(task$e<=0)),density_max=max(abs(f-task$f)),
   psi_max=max(abs(projection$psi-task$projection$psi)),
   instrument_last_penalty_max=max(vapply(1:2,function(j)max(abs(projection$penalty_traces[[j]]$last_penalty-task$projection$penalty_traces[[j]]$last_penalty)),numeric(1))),
   instrument_penalty_replay_max=max(vapply(c(projection$penalty_traces,task$projection$penalty_traces),function(z)z$replay_difference,numeric(1))))
  saveRDS(list(beta=b,e=e,f=f,projection=projection,layerA=layerA,layerB=layerB,
   differences=differences,rng_before=before,rng_after=.Random.seed),file.path(folder,"independent_path.rds"))
  put(e,file.path(folder,"independent_residual.bin"));put(f,file.path(folder,"independent_density.bin"))
  put(projection$psi,file.path(folder,"independent_psi.bin"));put(layerA$score,file.path(folder,"independent_score.bin"))
  write.csv(data.frame(coordinate=0:100,beta=b,lambda=task$lambda),file.path(folder,"independent_coefficients.csv"),row.names=FALSE)
  row<-data.frame(id=id,status="SUCCESS",dataset=task$dataset,offset=task$offset,candidate=task$candidate,
   historical_W=task$statistic$W,A_independent_W=layerA$W,B_independent_W=layerB$W,
   A_delta_W=layerA$W-task$statistic$W,B_delta_W=layerB$W-task$statistic$W,
   historical_accepted=task$statistic$accepted,A_independent_accepted=layerA$accepted,B_independent_accepted=layerB$accepted,
   A_score1_delta=layerA$g[1]-task$statistic$g[1],A_score2_delta=layerA$g[2]-task$statistic$g[2],
   A_S11_delta=layerA$S[1,1]-task$statistic$S[1,1],A_S12_delta=layerA$S[1,2]-task$statistic$S[1,2],A_S22_delta=layerA$S[2,2]-task$statistic$S[2,2],
   B_score1_delta=layerB$g[1]-task$statistic$g[1],B_score2_delta=layerB$g[2]-task$statistic$g[2],
   B_S11_delta=layerB$S[1,1]-task$statistic$S[1,1],B_S12_delta=layerB$S[1,2]-task$statistic$S[1,2],B_S22_delta=layerB$S[2,2]-task$statistic$S[2,2],
   historical_condition=task$statistic$condition,A_condition=layerA$condition,B_condition=layerB$condition,
   downstream_rng_identical=identical(before,.Random.seed),warnings=length(warnings),stringsAsFactors=FALSE)
  for(name in names(differences))row[[name]]<-differences[[name]]
  rows[[length(rows)+1L]]<-row
  cat("PAIRED_PATH_COMPLETE",id,"H/A/B W",task$statistic$W,layerA$W,layerB$W,"\n");flush.console()
 },warning=function(w){warnings<<-c(warnings,conditionMessage(w));invokeRestart("muffleWarning")}),
 error=function(e){writeLines(c(conditionMessage(e),warnings),file.path(folder,"PATH_FAILURE.txt"));
  rows[[length(rows)+1L]]<<-data.frame(id=id,status="PATH_FAILURE",stringsAsFactors=FALSE)})
 writeLines(warnings,file.path(folder,"independent_path_warnings.txt"))
}
# Fill rectangular table even if a paired path failed; never drop it.
cols<-unique(unlist(lapply(rows,names)))
rows<-lapply(rows,function(r){for(n in setdiff(cols,names(r)))r[[n]]<-NA;r[,cols]})
write.csv(do.call(rbind,rows),file.path(out,"paired_paths_R.csv"),row.names=FALSE)
