out <- 'journal_validation/stage2g/end_to_end_certification/results'
old <- 'journal_validation/stage2g/full_path_validation/results'
src <- 'journal_validation/stage2e/output/paired_20261029T093009Z'
source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('journal_validation/stage2b/diagnostics.R')
getbin <- function(p,n) { c<-file(p,'rb'); on.exit(close(c)); readBin(c,'double',n,size=8,endian='little') }
put <- function(x,p) { c<-file(p,'wb'); on.exit(close(c)); writeBin(as.double(x),c,size=8,endian='little') }
tasks <- read.csv(file.path(old,'tasks.csv'),stringsAsFactors=FALSE)
rows <- calls <- list()
RNGkind("L'Ecuyer-CMRG","Inversion")
for(k in seq_len(nrow(tasks))) {
 id<-tasks$id[k]; variant<-tasks$variant[k]; fdir<-file.path(old,id,variant)
 task<-readRDS(file.path(src,id,'historical_task.rds')); dat<-task$dat
 e<-getbin(file.path(fdir,'outcome_residual.bin'),1000)
 rank<-getbin(file.path(fdir,'rank.bin'),1000)
 f<-dnorm(e,mean(e),var(e)); stopifnot(identical(f,getbin(file.path(fdir,'density.bin'),1000)))
 w<-sqrt(diag(f)); Xw<-w%*%dat$X; coeff<-matrix(0,101,2); psi<-matrix(0,2,1000)
 set_stream(task$post_penalty_state); before<-.Random.seed
 for(j in 1:2) {
  fit<-hdm::rlasso(w%*%dat$Z[,j]~w%*%dat$X,post=FALSE)
  coeff[,j]<-as.numeric(fit$coefficients)
  psi[j,]<-drop(dat$Z[,j]-cbind(1,dat$X)%*%matrix(fit$coefficients,ncol=1))
  if(variant=='C') {
   dir<-file.path(out,id); dir.create(dir,recursive=TRUE,showWarnings=FALSE)
   cap<-new.env(parent=emptyenv()); cap$calls<-list(); ns<-asNamespace('hdm'); env<-new.env(parent=ns)
   solver<-get('LassoShooting.fit',ns)
   env$LassoShooting.fit<-function(x,y,lambda,...) {
    ans<-solver(x,y,lambda,...); a<-list(...); z<-length(cap$calls)+1L
    prefix<-file.path(dir,paste0('j',j,'_call',z,'_'))
    XX<-if(is.null(a$XX)) crossprod(x) else a$XX
    Xy<-if(is.null(a$Xy)) crossprod(x,y) else a$Xy
    put(as.vector(t(XX)),paste0(prefix,'XX.bin'));put(Xy,paste0(prefix,'Xy.bin'))
    put(lambda,paste0(prefix,'lambda.bin'));put(as.vector(t(ans$coef.list)),paste0(prefix,'iterates.bin'))
    put(ans$coefficients,paste0(prefix,'final.bin'))
    cap$calls[[z]]<-list(coefficients=ans$coefficients,lambda=lambda)
    calls[[length(calls)+1L]]<<-data.frame(id=id,instrument=j,call=z,sweeps=ncol(ans$coef.list)-1,
      reported_iterations=ans$num.it,prefix=basename(prefix),start_is_fixed_export=TRUE)
    ans
   }
   fun<-get('rlasso.default',ns); environment(fun)<-env
   replay<-fun(Xw,drop(w%*%dat$Z[,j]),post=FALSE,intercept=TRUE,penalty=fit$options$penalty,control=fit$options$control)
   stopifnot(identical(as.numeric(replay$coefficients),as.numeric(fit$coefficients)))
  }
 }
 stopifnot(identical(before,.Random.seed),identical(as.vector(t(coeff)),getbin(file.path(fdir,'instrument_coefficients.bin'),202)),
  identical(as.vector(psi),getbin(file.path(fdir,'psi.bin'),2000)))
 obs<-(.9-rank)*t(psi); g<-colSums(obs); S<-crossprod(obs); W<-drop(t(g)%*%solve(S)%*%g)
 stopifnot(identical(W,getbin(file.path(fdir,'W.bin'),1)),identical(as.vector(t(S)),getbin(file.path(fdir,'second_moment.bin'),4)))
 rows[[k]]<-data.frame(id=id,variant=variant,status='PASS',W=W,rng_unchanged=TRUE,coefficients_identical=TRUE,density_identical=TRUE,psi_identical=TRUE,S_identical=TRUE)
 cat('PASS',id,variant,'\n');flush.console()
}
write.csv(do.call(rbind,rows),file.path(out,'native_replay.csv'),row.names=FALSE)
write.csv(do.call(rbind,calls),file.path(out,'shooting_calls.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(out,'R_sessionInfo.txt'))
