# Independent export audit: compare every numerical payload to saved R objects.
base<-Sys.getenv('STAGE2H_RUN');input<-file.path(base,'inputs')
design<-read.csv(file.path(base,'DESIGN.csv'),stringsAsFactors=FALSE)
getbin<-function(p){con<-file(p,'rb');on.exit(close(con));readBin(con,'double',file.info(p)$size/8,size=8,endian='little')}
records<-list()
for(i in seq_len(nrow(design))) {
 a<-design[i,];folder<-file.path(input,a$id);task<-readRDS(file.path(folder,'task.rds'));dat<-task$dat
 expected<-list(X_column_major=cbind(1,dat$X),X_row_major=as.vector(t(cbind(1,dat$X))),Z_row_major=as.vector(t(dat$Z)),Y=dat$y,D=dat$D,response=task$ystar,lambda=task$lambda,parameters=c(task$tau,task$kappa,task$alpha))
 for(name in names(expected))stopifnot(identical(as.numeric(expected[[name]]),getbin(file.path(folder,paste0(name,'.bin')))))
 records[[i]]<-data.frame(id=a$id,numerical_payloads_checked=length(expected),status='PASS')
}
write.csv(do.call(rbind,records),file.path(base,'binary_input_validation.csv'),row.names=FALSE)
cat('PASS: all 1440 candidates, eight binary payloads each\n')
