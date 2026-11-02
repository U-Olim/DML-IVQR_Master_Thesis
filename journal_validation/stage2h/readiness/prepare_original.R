# Only original DGP diagnostics. No bounded-treatment sample or outcome exists.
source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('thesis_extension/src/dgp_kappa.R')
source('thesis_extension/src/author_bc_dml_wrapper.R')
source('journal_validation/stage2b/diagnostics.R')
base<-'journal_validation/stage2h/readiness';input<-file.path(base,'inputs')
design<-read.csv(file.path(base,'DESIGN.csv'),stringsAsFactors=FALSE)
put<-function(x,p){c<-file(p,'wb');on.exit(close(c));writeBin(as.double(x),c,size=8,endian='little')}
RNGkind("L'Ecuyer-CMRG","Inversion");set.seed(2026110201L);stream<-.Random.seed
primitive_list<-list();data_states<-list()
for(n in c(500L,1000L)) {
 set_stream(stream);data_states[[as.character(n)]]<-stream
 primitive_list[[as.character(n)]]<-generate_kappa_primitives(n,100L)
 saveRDS(list(primitives=primitive_list[[as.character(n)]],before=stream,after=.Random.seed),file.path(input,paste0('primitives_n',n,'.rds')))
 stream<-parallel::nextRNGStream(stream)
}
penalties<-list();records<-list()
for(k in seq_len(nrow(design))) {
 a<-design[k,];n<-a$n;tau<-a$tau;kappa<-a$kappa;id<-a$id
 folder<-file.path(input,id);dir.create(folder,showWarnings=FALSE)
 primitives<-primitive_list[[as.character(n)]];dat<-make_kappa_dataset(primitives,kappa,7L)
 key<-paste(n,tau,sep='_')
 if(is.null(penalties[[key]])) {
  # Independent of data; prespecified shared penalty stream across kappa.
  state<-data_states[[as.character(n)]]
  for(j in seq_len(match(tau,c(.1,.5,.9))))state<-parallel::nextRNGSubStream(state)
  set_stream(state);t<-proc.time()[3]
  lambda<-lambda_BC_author(dat$X,R=1000,tau=tau,c=2,alpha=.1)
  penalties[[key]]<-list(lambda=lambda,before=state,after=.Random.seed,seconds=proc.time()[3]-t)
 }
 pen<-penalties[[key]];alpha<-alpha_true(tau);ystar<-drop(dat$y-alpha*dat$D)
 saveRDS(list(dat=dat,ystar=ystar,tau=tau,kappa=kappa,alpha=alpha,lambda=pen$lambda,
   penalty_state=pen$before,post_penalty_state=pen$after),file.path(folder,'task.rds'))
 put(cbind(1,dat$X),file.path(folder,'X_column_major.bin'))
 put(as.vector(t(cbind(1,dat$X))),file.path(folder,'X_row_major.bin'))
 put(ystar,file.path(folder,'response.bin'));put(pen$lambda,file.path(folder,'lambda.bin'))
 put(as.vector(t(dat$Z)),file.path(folder,'Z_row_major.bin'))
 put(dat$D,file.path(folder,'D.bin'));put(dat$y,file.path(folder,'Y.bin'))
 put(c(tau,kappa,alpha),file.path(folder,'parameters.bin'))
 writeLines(c(state_text(pen$before),state_text(pen$after)),file.path(folder,'penalty_rng_states.txt'))
 records[[k]]<-data.frame(id=id,n=n,tau=tau,kappa=kappa,alpha=alpha,penalty_seconds=pen$seconds,
   D_min=min(dat$D),D_max=max(dat$D),D_exact_zero=sum(dat$D==0),D_exact_one=sum(dat$D==1),
   cor_D_Q1=cor(dat$D,primitives$z1+primitives$v1),cor_D_Q2=cor(dat$D,primitives$z2+primitives$v2),
   outcome_penalty_hash=hash_object(pen$lambda),data_hash=hash_object(dat))
 cat('PREPARED',id,'\n');flush.console()
}
write.csv(do.call(rbind,records),file.path(input,'preparation.csv'),row.names=FALSE)
writeLines(capture.output(sessionInfo()),file.path(input,'R_sessionInfo.txt'))
