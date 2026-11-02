out<-'journal_validation/stage2g/full_path_validation/results'
source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
getbin<-function(p,n){con<-file(p,'rb');x<-readBin(con,'double',n=n,size=8,endian='little');close(con);stopifnot(length(x)==n);x}
put<-function(x,p){stopifnot(!file.exists(p));con<-file(p,'wb');writeBin(as.double(x),con,size=8,endian='little');close(con)}
writeLines(capture.output(get('init_values',asNamespace('hdm'))),file.path(out,'historical_init_values.txt'))
source_path<-'journal_validation/stage2e/output/paired_20261029T093009Z'
tasks<-read.csv(file.path(out,'tasks.csv'),stringsAsFactors=FALSE);records<-list();baseline<-list()
for(k in seq_len(nrow(tasks))) {
 id<-tasks$id[k];variant<-tasks$variant[k];folder<-file.path(out,id,variant)
 task<-readRDS(file.path(source_path,id,'historical_task.rds'));details<-readRDS(file.path(folder,'downstream_details.rds'))
 coefs<-matrix(getbin(file.path(folder,'instrument_coefficients.bin'),202),nrow=101,byrow=TRUE)
 stopifnot(identical(details$rng_before,task$post_penalty_state),identical(details$rng_after,task$post_penalty_state),identical(details$repeated_coefficients,coefs))
 e<-getbin(file.path(folder,'outcome_residual.bin'),1000);f<-getbin(file.path(folder,'density.bin'),1000)
 stopifnot(identical(f,dnorm(e,mean(e),var(e))))
 for(j in 1:2) {
  fit<-details$fits[[j]];tr<-details$traces[[j]];last<-tr$trace[[length(tr$trace)]]
  stopifnot(identical(as.numeric(fit$coefficients),coefs[,j]),identical(as.numeric(last$coefficients),coefs[-1,j]),
   identical(as.numeric(last$lambda),getbin(file.path(folder,paste0('instrument_',j,'_last_penalty.bin')),100)),
   fit$options$post==FALSE,fit$options$intercept==TRUE,
   fit$options$penalty$homoscedastic==FALSE,fit$options$penalty$X.dependent.lambda==FALSE,fit$options$penalty$c==.5)
  prefix<-file.path(folder,paste0('instrument_',j,'_'))
  put(as.vector(t(do.call(rbind,lapply(tr$trace,function(z)as.numeric(z$coefficients))))),paste0(prefix,'trace_coefficients.bin'))
  put(as.vector(t(do.call(rbind,lapply(tr$trace,function(z)as.numeric(z$lambda))))),paste0(prefix,'trace_penalties.bin'))
  xc<-matrix(getbin(paste0(prefix,'centered_X.bin'),100000),nrow=1000,byrow=TRUE)
  yc<-getbin(paste0(prefix,'centered_y.bin'),1000)
  put(hdm:::init_values(xc,matrix(yc,ncol=1))$residuals,paste0(prefix,'initial_residual.bin'))
  put(c(fit$lambda0,fit$options$penalty$c,fit$options$penalty$gamma,fit$options$control$tol,fit$options$control$numIter),paste0(prefix,'adaptive_parameters.bin'))
 }
 records[[k]]<-data.frame(id=id,variant=variant,status='PASS',rng_state_matches=TRUE,repeated_coefficients_identical=TRUE,used_final_penalties_verified=TRUE)
 if(variant=='C') {
  independent<-readRDS(file.path(source_path,id,'independent_path.rds'))
  for(side in c('historical','independent')) {
   b<-getbin(file.path(source_path,id,paste0(side,'_beta.bin')),101)
   er<-drop(task$ystar-cbind(1,task$dat$X)%*%b)
   fr<-dnorm(er,mean(er),var(er))
   pr<-if(side=='historical')task$projection else independent$projection
   ps<-sapply(1:2,function(j)drop(task$dat$Z[,j]-cbind(1,task$dat$X)%*%matrix(pr$coefficients[[j]],ncol=1)))
   stopifnot(identical(er,getbin(file.path(source_path,id,paste0(side,'_residual.bin')),1000)),
    identical(fr,getbin(file.path(source_path,id,paste0(side,'_density.bin')),1000)),
    identical(as.vector(t(ps)),getbin(file.path(source_path,id,paste0(side,'_psi.bin')),2000)))
   baseline[[length(baseline)+1L]]<-data.frame(id=id,policy=side,status='SAVED_PATH_RECONSTRUCTION_PASS')
  }
 }
}
write.csv(do.call(rbind,records),file.path(out,'native_verification.csv'),row.names=FALSE)
write.csv(do.call(rbind,baseline),file.path(out,'baseline_verification.csv'),row.names=FALSE)
cat('VERIFIED',length(records),'new native paths and',length(baseline),'saved baseline paths\n')
