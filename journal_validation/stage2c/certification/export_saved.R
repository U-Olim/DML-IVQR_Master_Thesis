# Read saved RDS objects only. No source(), package loads, RNG draws or fits.
args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==2L)
src<-normalizePath(args[1],winslash="/",mustWork=TRUE)
dest<-normalizePath(args[2],winslash="/",mustWork=TRUE)
folders<-list.dirs(src,recursive=FALSE,full.names=TRUE)
folders<-folders[grepl("/(pilot|validation)_[0-9]{3}$",folders)]
for(folder in folders) {
 d<-readRDS(file.path(folder,"details.rds"));target<-file.path(dest,basename(folder))
 stopifnot(!dir.exists(target));dir.create(target)
 put<-function(x,name){con<-file(file.path(target,paste0(name,".bin")),"wb");writeBin(as.double(x),con,size=8,endian="little");close(con)}
 put(as.vector(t(cbind(1,d$dat$X))),"X_row_major")
 put(drop(d$dat$y-(1+qnorm(.9))*d$dat$D),"y_candidate")
 for(arm in c("P11","P01","P10","P00","KNOWN")) {
  put(d$arms[[arm]]$beta,paste0(arm,"_beta"))
  put(d$arms[[arm]]$e,paste0(arm,"_residual"))
  put(d$arms[[arm]]$penalty,paste0(arm,"_penalty"))
 }
 writeLines("little-endian IEEE754 binary64; X 1000x101 row-major; y/residual 1000; beta/penalty 101",file.path(target,"FORMAT.txt"))
 cat("EXPORTED_SAVED",basename(folder),"\n")
}
