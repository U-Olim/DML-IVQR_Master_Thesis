# Policy B: repeat historical calibration, then export last-used penalties.
# Refined fits are NEVER fed back into the adaptive loop.
out<-'journal_validation/stage2g/deterministic_implementation/results'
old<-'journal_validation/stage2g/full_path_validation/results'
src<-'journal_validation/stage2e/output/paired_20261029T093009Z'
source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('journal_validation/stage2b/diagnostics.R')
getbin<-function(p,n) {c<-file(p,'rb');on.exit(close(c));readBin(c,'double',n,size=8,endian='little')}
put<-function(x,p) {c<-file(p,'wb');on.exit(close(c));writeBin(as.double(x),c,size=8,endian='little')}
tasks<-read.csv(file.path(out,'outcome_validation.csv'),stringsAsFactors=FALSE)
rows<-list();RNGkind("L'Ecuyer-CMRG","Inversion")
for(k in seq_len(nrow(tasks))) {
 id<-tasks$id[k];folder<-file.path(out,id);reference<-file.path(old,id,'C')
 if(tasks$status[k]!='PASS') {rows[[k]]<-data.frame(id=id,status='OUTCOME_UNRESOLVED');next}
 start<-proc.time()[3];task<-readRDS(file.path(src,id,'historical_task.rds'));dat<-task$dat
 historical_coefficients<-sapply(1:2,function(j)as.numeric(task$projection$coefficients[[j]]))
 put(as.vector(t(historical_coefficients)),file.path(folder,'historical_instrument_coefficients.bin'))
 e<-getbin(file.path(folder,'outcome_residual.bin'),1000);rank<-getbin(file.path(folder,'rank.bin'),1000)
 stopifnot(identical(e,getbin(file.path(reference,'outcome_residual.bin'),1000)),identical(rank,getbin(file.path(reference,'rank.bin'),1000)))
 t<-proc.time()[3];f<-dnorm(e,mean(e),var(e));w<-sqrt(diag(f));Xw<-w%*%dat$X;density_seconds<-proc.time()[3]-t
 stopifnot(identical(f,getbin(file.path(reference,'density.bin'),1000)))
 put(f,file.path(folder,'density.bin'));put(c(mean(e),var(e)),file.path(folder,'density_parameters.bin'))
 put(as.vector(t(dat$Z)),file.path(folder,'Z_row_major.bin'))
 fits<-traces<-vector('list',2);coefs<-matrix(0,101,2);native_seconds<-capture_seconds<-0
 set_stream(task$post_penalty_state);before<-.Random.seed
 for(j in 1:2) {
  yw<-drop(w%*%dat$Z[,j]);t<-proc.time()[3]
  fit<-hdm::rlasso(w%*%dat$Z[,j]~w%*%dat$X,post=FALSE);native_seconds<-native_seconds+proc.time()[3]-t
  t<-proc.time()[3];captured<-capture_adaptive(Xw,yw,fit);capture_seconds<-capture_seconds+proc.time()[3]-t
  prefix<-file.path(folder,paste0('instrument_',j,'_'));xc<-scale(Xw,colMeans(Xw),FALSE);yc<-yw-mean(yw)
  stopifnot(identical(as.numeric(captured$last_penalty),getbin(file.path(reference,paste0('instrument_',j,'_last_penalty.bin')),100)))
  put(as.vector(t(xc)),paste0(prefix,'centered_X.bin'));put(yc,paste0(prefix,'centered_y.bin'))
  put(c(mean(yw),colMeans(Xw)),paste0(prefix,'centering.bin'));put(captured$last_penalty,paste0(prefix,'last_penalty.bin'))
  put(captured$reported_next_penalty,paste0(prefix,'next_penalty.bin'))
  put(as.vector(t(do.call(rbind,lapply(captured$trace,function(z)z$lambda)))),paste0(prefix,'trace_penalties.bin'))
  put(as.vector(t(do.call(rbind,lapply(captured$trace,function(z)z$coefficients)))),paste0(prefix,'trace_coefficients.bin'))
  coefs[,j]<-as.numeric(fit$coefficients);fits[[j]]<-fit;traces[[j]]<-captured
 }
 stopifnot(identical(before,.Random.seed),identical(as.vector(t(coefs)),getbin(file.path(reference,'instrument_coefficients.bin'),202)))
 put(as.vector(t(coefs)),file.path(folder,'calibration_native_coefficients.bin'))
 saveRDS(list(fits=fits,traces=traces,rng_before=before,rng_after=.Random.seed),file.path(folder,'calibration_details.rds'))
 rows[[k]]<-data.frame(id=id,status='PASS',density_seconds=density_seconds,native_calibration_seconds=native_seconds,
  trace_capture_seconds=capture_seconds,total_R_seconds=proc.time()[3]-start,rng_unchanged=TRUE,penalty_bytes_match_Policy_C=TRUE)
 cat('CALIBRATION',id,'PASS\n');flush.console()
}
cols<-unique(unlist(lapply(rows,names)));rows<-lapply(rows,function(r){for(n in setdiff(cols,names(r)))r[[n]]<-NA;r[,cols]})
write.csv(do.call(rbind,rows),file.path(out,'calibration_validation.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(out,'R_sessionInfo.txt'))
