source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('thesis_extension/src/dgp_kappa.R');source('thesis_extension/src/author_bc_dml_wrapper.R');source('journal_validation/stage2b/diagnostics.R')
base<-Sys.getenv('STAGE2H_RUN');input<-file.path(base,'inputs');design<-read.csv(file.path(base,'DESIGN.csv'),stringsAsFactors=FALSE)
getbin<-function(p,n){con<-file(p,'rb');on.exit(close(con));readBin(con,'double',n,size=8,endian='little')}
RNGkind("L'Ecuyer-CMRG","Inversion");set.seed(2026110281L);stream<-.Random.seed;records<-list()
for(n in c(500L,1000L)) for(r in 1:20) {
 sampleid<-sprintf('n%d_r%02d',n,r);saved<-readRDS(file.path(input,sampleid,'primitives.rds'))
 stopifnot(identical(saved$before,stream));set_stream(stream);pr<-generate_kappa_primitives(n,100L)
 stopifnot(identical(pr,saved$primitives),identical(.Random.seed,saved$after));substate<-parallel::nextRNGSubStream(stream)
 dd<-design[design$n==n & design$replication==r & design$arm=='A',]
 for(j in seq_len(nrow(dd))) {
  a<-dd[j,];af<-file.path(input,paste0(a$pair_id,'_A'));bf<-file.path(input,paste0(a$pair_id,'_B'));A<-readRDS(file.path(af,'task.rds'));B<-readRDS(file.path(bf,'task.rds'))
  stopifnot(identical(A$dat,make_kappa_dataset(pr,a$kappa,7L)),identical(A$dat$primitives,B$dat$primitives),identical(A$dat$X,B$dat$X),identical(A$dat$Z,B$dat$Z),identical(A$dat$d,B$dat$d))
  stopifnot(identical(B$dat$D,.05+.90*pnorm(A$dat$d)),all(B$dat$D>=.05),all(B$dat$D<=.95))
  b<-matrix(c(rep(5,7),rep(0,93)));stopifnot(identical(B$dat$y,1+B$dat$D+B$dat$X%*%b+pr$u*B$dat$D))
  stopifnot(identical(A$penalty_state,substate),identical(A$lambda,B$lambda),identical(A$post_penalty_state,B$post_penalty_state))
  set_stream(substate);lambda<-lambda_BC_author(pr$X,R=1000,tau=a$tau,c=2,alpha=.1)
  stopifnot(identical(lambda,A$lambda),identical(.Random.seed,A$post_penalty_state))
  for(arm in c('A','B')) {
   task<-if(arm=='A')A else B;f<-if(arm=='A')af else bf
   stopifnot(identical(task$alpha,alpha_true(a$tau)+a$offset),identical(task$ystar,drop(task$dat$y-task$alpha*task$dat$D)),identical(task$ystar,getbin(file.path(f,'response.bin'),n)),identical(as.numeric(lambda),getbin(file.path(f,'lambda.bin'),101)))
   residual<-drop(task$dat$y-alpha_true(a$tau)*task$dat$D-(1+task$dat$X%*%b));direct<-task$dat$D*(pr$u-qnorm(a$tau))
   stopifnot(max(abs(residual-direct))<1e-12,identical(residual<=0,pr$u<=qnorm(a$tau)))
  }
  records[[length(records)+1]]<-data.frame(pair_id=a$pair_id,primitive_replay='PASS',paired_primitives='PASS',treatment_outcome_truth='PASS',penalty_rng_replay='PASS',binary_inputs='PASS')
  substate<-parallel::nextRNGSubStream(substate)
 }
 stream<-parallel::nextRNGStream(stream);cat('VERIFIED',sampleid,'\n');flush.console()
}
write.csv(do.call(rbind,records),file.path(base,'input_validation.csv'),row.names=FALSE)
