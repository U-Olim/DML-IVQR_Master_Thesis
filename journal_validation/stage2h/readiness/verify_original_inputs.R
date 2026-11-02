source('thesis_extension/environment/check_author_environment.R')
invisible(capture.output(assert_author_environment('thesis_extension',write_outputs=FALSE)))
source('thesis_extension/src/dgp_kappa.R');source('thesis_extension/src/author_bc_dml_wrapper.R')
source('journal_validation/stage2b/diagnostics.R')
base<-'journal_validation/stage2h/readiness';input<-file.path(base,'inputs')
getbin<-function(p,n){c<-file(p,'rb');on.exit(close(c));readBin(c,'double',n,size=8,endian='little')}
RNGkind("L'Ecuyer-CMRG","Inversion")
for(n in c(500L,1000L)) {
 saved<-readRDS(file.path(input,paste0('primitives_n',n,'.rds')))
 set_stream(saved$before);repeated<-generate_kappa_primitives(n,100L)
 stopifnot(identical(repeated,saved$primitives),identical(.Random.seed,saved$after))
}
design<-read.csv(file.path(base,'DESIGN.csv'),stringsAsFactors=FALSE);rows<-list()
for(k in seq_len(nrow(design))) {
 a<-design[k,];folder<-file.path(input,a$id);task<-readRDS(file.path(folder,'task.rds'))
 saved<-readRDS(file.path(input,paste0('primitives_n',a$n,'.rds')))
 stopifnot(identical(make_kappa_dataset(saved$primitives,a$kappa,7L),task$dat))
 set_stream(task$penalty_state)
 repeated<-lambda_BC_author(task$dat$X,R=1000,tau=task$tau,c=2,alpha=.1)
 stopifnot(identical(repeated,task$lambda),identical(.Random.seed,task$post_penalty_state),
   identical(as.numeric(task$lambda),getbin(file.path(folder,'lambda.bin'),101)),
   identical(task$ystar,getbin(file.path(folder,'response.bin'),a$n)),
   identical(as.vector(t(cbind(1,task$dat$X))),getbin(file.path(folder,'X_row_major.bin'),a$n*101)))
 rows[[k]]<-data.frame(id=a$id,primitive_replay='PASS',original_DGP_reconstruction='PASS',original_penalty_replay='PASS')
}
write.csv(do.call(rbind,rows),file.path(base,'results/original_input_verification.csv'),row.names=FALSE)
cat('PASS: original primitives, datasets, penalties and RNG replay for all 12 cells\n')
