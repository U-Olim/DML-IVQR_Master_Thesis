# Run only through run_stage2a.py, which records commands and preservation hashes.
args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==2L, args[1] %in% c("validate","ab","pilot"))
phase <- args[1]
out <- normalizePath(args[2],winslash="/",mustWork=TRUE)
root <- normalizePath(".",winslash="/",mustWork=TRUE)
source("thesis_extension/environment/check_author_environment.R")
assert_author_environment("thesis_extension",write_outputs=FALSE)
for(f in c("dgp_kappa.R","author_oracle_wrapper.R","author_bc_dml_wrapper.R"))
  source(file.path("thesis_extension/src",f))
source("journal_validation/stage2a/diagnostic_functions.R")
RNGkind("L'Ecuyer-CMRG", "Inversion")
workers <- 2L
master_data_seed <- 20261022L
master_penalty_seed <- 20261023L
cutoff <- qchisq(.95,2)
dir.create(file.path(out,"samples"),showWarnings=FALSE)
dir.create(file.path(out,"details"),showWarnings=FALSE)

if(phase=="validate") {
  writeLines(capture.output(sessionInfo()),file.path(out,"sessionInfo_master.txt"))
  packages <- installed.packages(lib.loc=.libPaths())
  write.csv(packages[,c("Package","Version","LibPath"),drop=FALSE],file.path(out,"packages.csv"),row.names=FALSE)
  config <- list(RNGkind=RNGkind(),master_data_seed=master_data_seed,
    master_penalty_seed=master_penalty_seed,workers=workers,fixed_samples_per_n=3L,
    streams_per_setting=10L,pilot_replications=40L,cutoff=cutoff,
    BC_R=1000L,BC_c=2,BC_alpha=.1,
    numerical_settings="Inherited unchanged from quantreg 5.34 and hdm 0.2.0 defaults",
    interpretation="True-parameter tests only; no grid profiles or full Monte Carlo")
  dput(config,file=file.path(out,"config.R"))
  # Nonoverlapping CMRG streams allocated by index; every complete state is saved.
  set.seed(master_data_seed)
  data_streams <- vector("list",46L)
  for(i in seq_along(data_streams)) {
    data_streams[[i]] <- .Random.seed
    .Random.seed <- parallel::nextRNGStream(.Random.seed)
  }
  set.seed(master_penalty_seed)
  penalty_streams <- vector("list",400L)
  for(i in seq_along(penalty_streams)) {
    penalty_streams[[i]] <- .Random.seed
    .Random.seed <- parallel::nextRNGStream(.Random.seed)
  }
  saveRDS(list(data=data_streams,penalty=penalty_streams),file.path(out,"rng_streams.rds"))
  checks <- list(); manifest <- list(); data_index <- 0L
  for(n in c(500L,1000L)) for(j in 1:3) {
    data_index <- data_index+1L
    set_stream(data_streams[[data_index]])
    p <- generate_kappa_primitives(n)
    original_d <- p$z1+p$z2+p$epsilon
    original_D <- pnorm(original_d)
    original_Z <- cbind(p$z1+p$v1+p$X[,2]+p$X[,3]+p$X[,4],
                        p$z2+p$v2+p$X[,7]+p$X[,8]+p$X[,9]+p$X[,10])
    original_y <- 1+original_D+p$X%*%matrix(c(rep(5,7),rep(0,93)))+p$u*original_D
    # Independent reimplementation of original baseline primitive draw order.
    set_stream(data_streams[[data_index]])
    epsilon <- mvtnorm::rmvnorm(n,mean=c(0,0),sigma=matrix(c(1,.3,.3,1),2))
    xx <- matrix(rnorm(n*100),ncol=100); XX <- matrix(pnorm(xx),ncol=100)
    zz <- cbind(rnorm(n),rnorm(n)); vv1<-rnorm(n);vv2<-rnorm(n)
    stopifnot(identical(epsilon,p$epsilon_pair),identical(XX,p$X),identical(zz[,1],p$z1),
              identical(zz[,2],p$z2),identical(vv1,p$v1),identical(vv2,p$v2))
    baseline <- make_kappa_dataset(p,1)
    stopifnot(identical(baseline$d,original_d),identical(baseline$D,original_D),
              identical(baseline$Z,original_Z),identical(baseline$y,original_y))
    for(k in c(1,.1)) {
      dat <- make_kappa_dataset(p,k)
      id<-paste0("fixed_n",n,"_s",j,"_k",k)
      path<-file.path(out,"samples",paste0(id,".rds"));saveRDS(dat,path)
      manifest[[length(manifest)+1L]]<-data.frame(sample_id=id,n=n,kappa=k,
        data_stream_index=data_index,data_stream=state_text(data_streams[[data_index]]),
        sha256=object_hash(dat),path=path,stringsAsFactors=FALSE)
    }
    checks[[length(checks)+1L]]<-data.frame(check=paste0("baseline_dgp_n",n,"_s",j),max_abs_diff=0,passed=TRUE)
  }
  write.csv(do.call(rbind,manifest),file.path(out,"sample_manifest.csv"),row.names=FALSE)
  synthetic <- c(-2,-.5,0,.2,1,3)
  fb<-dnorm(synthetic,mean(synthetic),var(synthetic))
  fa<-dnorm(synthetic,mean(synthetic),sd(synthetic))
  stopifnot(identical(fb,dnorm(synthetic,mean=mean(synthetic),sd=var(synthetic))),
    identical(fa,dnorm(synthetic,mean=mean(synthetic),sd=sqrt(var(synthetic)))),any(abs(fa-fb)>1e-6))
  write.csv(data.frame(e=synthetic,baseline=fb,alternative=fa,difference=fa-fb),
    file.path(out,"synthetic_density.csv"),row.names=FALSE)
  # Assert reversing the single scale edit recovers the EXACT original AST.
  for(fun in list(dml_detail,gmm_detail)) {
    alt <- sd_variant(fun)
    txt <- paste(deparse(body(alt)),collapse="\n")
    reverted <- parse(text=sub("dnorm(e, mean(e), sd(e))","dnorm(e, mean(e), var(e))",txt,fixed=TRUE))[[1]]
    stopifnot(identical(body(fun),reverted))
  }
  # Instrumented baseline vs canonical candidate, including controlled pivotal draws.
  for(n in c(500L,1000L)) for(tau in c(.5,.9)) for(k in c(1,.1)) {
    dat<-readRDS(file.path(out,"samples",paste0("fixed_n",n,"_s1_k",k,".rds")))
    state<-penalty_streams[[1]]
    for(est in c("Oracle-GMM","Full-GMM","DML-IVQR-BC")) {
      controls<-if(est=="Oracle-GMM")dat$X1 else dat$X
      fun<-if(est=="DML-IVQR-BC")dml_detail else gmm_detail
      ref<-if(est=="DML-IVQR-BC")author_bc_candidate else author_gmm_candidate
      set_stream(state); old<-ref(dat$y,dat$D,controls,dat$Z,tau,alpha_true(tau),TRUE)
      reference_state<-.Random.seed
      fit<-safe_fit(fun,dat,controls,tau,state)
      stopifnot(!fit$failed,identical(old$W,fit$value$W),identical(old$lambda,fit$value$lambda),
        identical(old$beta,fit$value$beta),identical(old$e,fit$value$e),identical(old$psi,fit$value$psi),
        identical(reference_state,fit$rng_after))
      checks[[length(checks)+1L]]<-data.frame(check=paste(est,n,tau,k,sep="_"),max_abs_diff=0,passed=TRUE)
    }
  }
  write.csv(do.call(rbind,checks),file.path(out,"validation_checks.csv"),row.names=FALSE)
  writeLines("PASS: DGP, synthetic density, single AST edit, 24 canonical equivalence cases",
    file.path(out,"VALIDATION_PASS.txt"))
  cat("VALIDATION_PASS\n")
  quit(status=0L)
}

stopifnot(file.exists(file.path(out,"VALIDATION_PASS.txt")))
streams<-readRDS(file.path(out,"rng_streams.rds"))
tasks<-list()
add_task<-function(experiment,id,path,sample_id,tau,est,index) {
  tasks[[length(tasks)+1L]] <<- list(experiment=experiment,id=id,data_path=path,
    sample_id=sample_id,tau=tau,estimator=est,stream_index=index,stream=streams$penalty[[index]],
    result_path=file.path(out,"details",paste0(id,".rds")))
}
if(phase=="ab") {
  manifest<-read.csv(file.path(out,"sample_manifest.csv"),stringsAsFactors=FALSE)
  idx<-0L
  for(i in seq_len(nrow(manifest))) for(tau in c(.5,.9)) for(r in 1:10) {
    idx<-idx+1L
    add_task("AB",paste0("AB_",sprintf("%03d",idx)),manifest$path[i],manifest$sample_id[i],tau,"DML-IVQR-BC",idx)
  }
} else {
  stopifnot(file.exists(file.path(out,"AB_PASS.txt")))
  pilot_manifest<-list()
  for(r in 1:40) {
    data_idx<-6L+r
    set_stream(streams$data[[data_idx]])
    dat<-make_kappa_dataset(generate_kappa_primitives(1000L),1)
    path<-file.path(out,"samples",paste0("pilot_",sprintf("%03d",r),".rds"));saveRDS(dat,path)
    pilot_manifest[[r]]<-data.frame(sample_id=r,data_stream_index=data_idx,
      data_stream=state_text(streams$data[[data_idx]]),sha256=object_hash(dat),path=path,stringsAsFactors=FALSE)
    for(est in c("Oracle-GMM","Full-GMM","DML-IVQR-BC"))
      add_task("C",paste0("C_",sprintf("03%d",r),"_",est),path,as.character(r),.9,est,240L+r)
  }
  write.csv(do.call(rbind,pilot_manifest),file.path(out,"pilot_sample_manifest.csv"),row.names=FALSE)
}
stopifnot(!any(file.exists(vapply(tasks,`[[`,character(1),"result_path"))))
saveRDS(tasks,file.path(out,paste0(phase,"_tasks.rds")))
cl<-parallel::makePSOCKcluster(workers,outfile=file.path(out,paste0(phase,"_workers.log")))
parallel::clusterExport(cl,c("root"),envir=environment())
worker_environment<-parallel::clusterEvalQ(cl,{
  setwd(root)
  source("thesis_extension/environment/check_author_environment.R")
  assert_author_environment("thesis_extension",write_outputs=FALSE)
  for(f in c("dgp_kappa.R","author_oracle_wrapper.R","author_bc_dml_wrapper.R")) source(file.path("thesis_extension/src",f))
  source("journal_validation/stage2a/diagnostic_functions.R")
  list(pid=Sys.getpid(),session=capture.output(sessionInfo()),RNGkind=RNGkind())
})
saveRDS(worker_environment,file.path(out,paste0(phase,"_worker_environment.rds")))
rows<-list()
tryCatch({
  for(start in seq(1L,length(tasks),by=12L)) {
    block<-tasks[start:min(start+11L,length(tasks))]
    rows<-c(rows,parallel::parLapplyLB(cl,block,pair_task))
    cat(phase,"completed",length(rows),"of",length(tasks),"paired tasks\n");flush.console()
  }
},finally=parallel::stopCluster(cl))
results<-do.call(rbind,rows)
write.csv(results,file.path(out,paste0(phase,"_pairs.csv")),row.names=FALSE)
stopifnot(all(results$paired_data_identical),all(results$pivotal_verified))
valid<-!results$failed_baseline & !results$failed_alternative
stopifnot(all(results$paired_beta_identical[valid]),all(results$paired_residuals_identical[valid]),
  all(results$rng_after_identical[valid]))
if(phase=="ab") writeLines("PASS: paired data, pivotal streams, penalties, beta, residuals, RNG end states",file.path(out,"AB_PASS.txt"))
cat("PHASE_COMPLETE",phase,"failures",sum(results$failed_baseline)+sum(results$failed_alternative),"\n")
