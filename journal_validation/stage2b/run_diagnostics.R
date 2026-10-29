args<-commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==2L,args[1]%in%c("validate","primary","contrasts"))
phase<-args[1];out<-normalizePath(args[2],winslash="/",mustWork=TRUE)
root<-normalizePath(".",winslash="/",mustWork=TRUE)
source("thesis_extension/environment/check_author_environment.R")
assert_author_environment("thesis_extension",write_outputs=FALSE)
for(f in c("dgp_kappa.R","author_oracle_wrapper.R","author_bc_dml_wrapper.R"))source(file.path("thesis_extension/src",f))
source("journal_validation/stage2b/config.R")
source("journal_validation/stage2b/diagnostics.R")
cfg<-stage2b_config
RNGkind("L'Ecuyer-CMRG","Inversion")
if(phase=="validate") {
  writeLines(capture.output(sessionInfo()),file.path(out,"sessionInfo.txt"))
  write.csv(installed.packages(lib.loc=.libPaths())[,c("Package","Version","LibPath")],file.path(out,"packages.csv"),row.names=FALSE)
  dput(cfg,file.path(out,"config_used.R"))
  writeLines(capture.output({print(hdm:::rlasso.default);print(hdm:::LassoShooting.fit);print(hdm:::lambdaCalculation)}),
    file.path(out,"historical_library_functions.txt"))
  dir.create(file.path(out,"samples"),showWarnings=FALSE)
  dir.create(file.path(out,"details"),showWarnings=FALSE)
  dir.create(file.path(out,"validation_details"),showWarnings=FALSE)
  source_streams<-readRDS(file.path(cfg$source_run,"rng_streams.rds"))
  set.seed(cfg$contrast_penalty_master_seed)
  contrast_streams<-vector("list",24L)
  for(i in seq_along(contrast_streams)) {
    contrast_streams[[i]]<-.Random.seed
    .Random.seed<-parallel::nextRNGStream(.Random.seed)
  }
  saveRDS(list(primary=source_streams$penalty[241:280],contrast=contrast_streams,
    source_data=source_streams$data[7:46]),file.path(out,"rng_streams.rds"))
  manifests<-tasks<-list();idx<-0L
  for(design in cfg$designs$design) {
    spec<-cfg$designs[cfg$designs$design==design,]
    count<-if(design=="primary")cfg$primary_replications else cfg$contrast_replications
    for(r in seq_len(count)) {
      src<-file.path(cfg$source_run,"samples",sprintf("pilot_%03d.rds",r))
      baseline<-readRDS(src)
      dat<-if(spec$kappa==1)baseline else make_kappa_dataset(baseline$primitives,spec$kappa)
      # Exact DGP coefficients, treatment/outcome, and observed instruments unchanged.
      stopifnot(max_abs(drop(dat$y)-(1+dat$D+5*rowSums(dat$X[,1:7])+dat$primitives$u*dat$D))<1e-11)
      path<-file.path(out,"samples",sprintf("%s_%03d.rds",design,r));saveRDS(dat,path)
      state<-if(design=="primary")source_streams$penalty[[240L+r]]else contrast_streams[[if(design=="median")r else 12L+r]]
      manifests[[length(manifests)+1L]]<-data.frame(design=design,replication=r,
        source_path=src,source_data_hash=hash_object(baseline),data_hash=hash_object(dat),
        source_data_stream=state_text(source_streams$data[[6L+r]]),
        penalty_stream=state_text(state),path=path,tau=spec$tau,kappa=spec$kappa,stringsAsFactors=FALSE)
      for(est in cfg$estimators) {
        idx<-idx+1L;id<-sprintf("%s_%03d_%s",design,r,est)
        tasks[[idx]]<-list(id=id,design=design,replication=r,tau=spec$tau,kappa=spec$kappa,
          estimator=est,data_path=path,stream=state,result_path=file.path(out,"details",paste0(id,".rds")))
      }
    }
  }
  write.csv(do.call(rbind,manifests),file.path(out,"sample_stream_manifest.csv"),row.names=FALSE)
  saveRDS(tasks,file.path(out,"tasks.rds"))
  checks<-list()
  # Two matched replicates from EACH design, each estimator, before pilot execution.
  selected<-Filter(function(t)t$replication<=2L,tasks)
  for(task in selected) {
    task$result_path<-file.path(out,"validation_details",paste0(task$id,".rds"))
    rows<-run_task(task)
    if(any(rows$failed))stop("Validation task failed: ",task$id," ",paste(unique(rows$error),collapse=" | "))
    record<-readRDS(task$result_path)
    stopifnot(length(unique(rows$density_hash))==1L,length(unique(rows$data_hash))==1L,
      rows$outcome_residual_hash[1]==rows$outcome_residual_hash[3],
      rows$outcome_residual_hash[2]==rows$outcome_residual_hash[4],
      rows$projection_hash[1]==rows$projection_hash[2],rows$projection_hash[3]==rows$projection_hash[4],
      record$projections$modified$orthogonality_intercept<1e-10,
      if(task$estimator!="DML-IVQR-BC")record$projections$modified$orthogonality_max<1e-10 else TRUE,
      record$outcome$known_identity_error<1e-11,
      record$moments$known$unconditional$rank_score_mismatch==0L)
    checks[[length(checks)+1L]]<-data.frame(task_id=task$id,passed=TRUE,
      reference_difference=record$reference_difference,
      known_residual_identity_error=record$outcome$known_identity_error,
      density_nonfinite=sum(rows$density_nonfinite),
      modified_intercept_orthogonality=record$projections$modified$orthogonality_intercept,
      penalty_replay_difference=if(task$estimator=="DML-IVQR-BC")max(vapply(record$projections$trace,`[[`,numeric(1),"replay_difference"))else 0)
    cat("VALIDATED",task$id,"\n");flush.console()
  }
  write.csv(do.call(rbind,checks),file.path(out,"validation_checks.csv"),row.names=FALSE)
  writeLines("PASS: 18 matched factorial tasks, canonical replay, known coefficients, frozen factors, intercept and penalty checks",file.path(out,"VALIDATION_PASS.txt"))
  cat("VALIDATION_PASS\n");quit(status=0)
}
stopifnot(file.exists(file.path(out,"VALIDATION_PASS.txt")))
tasks<-readRDS(file.path(out,"tasks.rds"))
tasks<-Filter(function(t)if(phase=="primary")t$design=="primary" else t$design!="primary",tasks)
stopifnot(!any(file.exists(vapply(tasks,`[[`,character(1),"result_path"))))
cl<-parallel::makePSOCKcluster(cfg$workers,outfile=file.path(out,paste0(phase,"_workers.log")))
parallel::clusterExport(cl,"root",envir=environment())
environment_records<-parallel::clusterEvalQ(cl,{
  setwd(root)
  source("thesis_extension/environment/check_author_environment.R")
  assert_author_environment("thesis_extension",write_outputs=FALSE)
  for(f in c("dgp_kappa.R","author_oracle_wrapper.R","author_bc_dml_wrapper.R"))source(file.path("thesis_extension/src",f))
  source("journal_validation/stage2b/diagnostics.R")
  list(pid=Sys.getpid(),session=capture.output(sessionInfo()))
})
saveRDS(environment_records,file.path(out,paste0(phase,"_worker_sessions.rds")))
rows<-list()
tryCatch({
  for(first in seq(1L,length(tasks),by=12L)) {
    block<-tasks[first:min(first+11L,length(tasks))]
    rows<-c(rows,parallel::parLapplyLB(cl,block,run_task))
    cat(phase,"completed",length(rows),"of",length(tasks),"four-variant tasks\n");flush.console()
  }
},finally=parallel::stopCluster(cl))
results<-do.call(rbind,rows)
write.csv(results,file.path(out,paste0(phase,"_evaluations.csv")),row.names=FALSE)
cat("PHASE_COMPLETE",phase,"replication/estimator tasks",length(tasks),"failed variant rows",sum(results$failed),"\n")
