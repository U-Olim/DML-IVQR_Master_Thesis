source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('thesis_extension/src/dgp_kappa.R')
source('thesis_extension/src/author_bc_dml_wrapper.R')
source('journal_validation/stage2b/diagnostics.R')
base<-Sys.getenv('STAGE2H_RUN'); input<-file.path(base,'inputs')
design<-read.csv(file.path(base,'DESIGN.csv'),stringsAsFactors=FALSE)
put<-function(x,p){con<-file(p,'wb');on.exit(close(con));writeBin(as.double(x),con,size=8,endian='little')}
RNGkind("L'Ecuyer-CMRG","Inversion");set.seed(2026110281L);stream<-.Random.seed
streams<-records<-list();ix<-0L
for(n in c(500L,1000L)) for(r in 1:20) {
 sampleid<-sprintf('n%d_r%02d',n,r); folder0<-file.path(input,sampleid);dir.create(folder0)
 set_stream(stream);before<-.Random.seed; primitives<-generate_kappa_primitives(n,100L);after<-.Random.seed
 saveRDS(list(primitives=primitives,before=before,after=after),file.path(folder0,'primitives.rds'))
 put(primitives$u,file.path(folder0,'u.bin'));put(primitives$epsilon,file.path(folder0,'epsilon.bin'))
 Q<-cbind(primitives$z1+primitives$v1,primitives$z2+primitives$v2);put(as.vector(t(Q)),file.path(folder0,'Q.bin'))
 streams[[length(streams)+1]]<-data.frame(sample_id=sampleid,kind='primitive',pair_id='',before=state_text(before),after=state_text(after))
 ds<-lapply(c(1,.1),function(k)make_kappa_dataset(primitives,k,7L)); substate<-parallel::nextRNGSubStream(stream)
 dd<-design[design$n==n & design$replication==r & design$arm=='A',]
 for(j in seq_len(nrow(dd))) {
  a<-dd[j,]; original<-ds[[match(a$kappa,c(1,.1))]]
  set_stream(substate);t<-proc.time()[3];lambda<-lambda_BC_author(original$X,R=1000,tau=a$tau,c=2,alpha=.1)
  penafter<-.Random.seed;pentime<-proc.time()[3]-t
  streams[[length(streams)+1]]<-data.frame(sample_id=sampleid,kind='penalty',pair_id=a$pair_id,before=state_text(substate),after=state_text(penafter))
  for(arm in c('A','B')) {
   dat<-original
   if(arm=='B') {dat$D<-.05+.90*original$D; b<-matrix(c(rep(5,7),rep(0,93)));dat$y<-1+dat$D+dat$X%*%b+primitives$u*dat$D}
   id<-paste0(a$pair_id,'_',arm); folder<-file.path(input,id);dir.create(folder)
   alpha<-alpha_true(a$tau)+a$offset;ystar<-drop(dat$y-alpha*dat$D)
   saveRDS(list(dat=dat,ystar=ystar,tau=a$tau,kappa=a$kappa,alpha=alpha,lambda=lambda,penalty_state=substate,post_penalty_state=penafter),file.path(folder,'task.rds'))
   put(cbind(1,dat$X),file.path(folder,'X_column_major.bin'));put(as.vector(t(cbind(1,dat$X))),file.path(folder,'X_row_major.bin'))
   put(ystar,file.path(folder,'response.bin'));put(lambda,file.path(folder,'lambda.bin'))
   put(as.vector(t(dat$Z)),file.path(folder,'Z_row_major.bin'));put(dat$D,file.path(folder,'D.bin'));put(dat$y,file.path(folder,'Y.bin'))
   put(c(a$tau,a$kappa,alpha),file.path(folder,'parameters.bin'))
   writeLines(c(state_text(substate),state_text(penafter)),file.path(folder,'penalty_rng_states.txt'))
   ix<-ix+1L; records[[ix]]<-data.frame(id=id,sample_id=sampleid,arm=arm,penalty_seconds=pentime,D_min=min(dat$D),D_max=max(dat$D),D_mean=mean(dat$D),D_variance=var(dat$D),primitive_hash=hash_object(primitives),lambda_hash=hash_object(lambda))
  }
  substate<-parallel::nextRNGSubStream(substate)
 }
 write.csv(do.call(rbind,records),file.path(input,'preparation.csv'),row.names=FALSE)
 write.csv(do.call(rbind,streams),file.path(input,'rng_streams.csv'),row.names=FALSE)
 cat('PREPARED',sampleid,'\n');flush.console();stream<-parallel::nextRNGStream(stream)
}
writeLines(capture.output(sessionInfo()),file.path(input,'R_sessionInfo.txt'))
