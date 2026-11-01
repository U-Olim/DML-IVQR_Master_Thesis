# Diagnostic evaluation of a rounded representation of the unique rational beta.
# No optimizer, package load, RNG draw or downstream refit.
args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==1L)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE)
source_root<-"journal_validation/stage2e/output/paired_20261029T093009Z"
getbin<-function(path,n){c<-file(path,"rb");x<-readBin(c,"double",n=n,size=8,endian="little");close(c);stopifnot(length(x)==n);x}
put<-function(x,path){stopifnot(!file.exists(path));c<-file(path,"wb");writeBin(as.double(x),c,size=8,endian="little");close(c)}
rows<-list()
for(id in c("pilot_002_minus","pilot_006_truth")) {
 folder<-file.path(out,id)
 if(!file.exists(file.path(folder,"exact_optimum_nearest_binary64_beta.bin")))next
 original<-readRDS(file.path(source_root,id,"historical_task.rds"))
 alternative<-readRDS(file.path(source_root,id,"independent_path.rds"))
 beta<-getbin(file.path(folder,"exact_optimum_nearest_binary64_beta.bin"),101L)
 e<-drop(original$ystar-cbind(1,original$dat$X)%*%beta);s<-.9-as.numeric(e<=0)
 put(e,file.path(folder,"rounded_optimum_R_residual.bin"));put(s,file.path(folder,"rounded_optimum_R_score.bin"))
 stats<-lapply(list(original$projection$psi,alternative$projection$psi),function(psi){
  observations<-s*t(psi);g<-colSums(observations);S<-crossprod(observations)
  W<-drop(t(g)%*%solve(S,g));list(W=W,accepted=W<=qchisq(.95,2))
 })
 rows[[length(rows)+1L]]<-data.frame(id=id,exact_zero_R_residuals=sum(e==0),
  fixed_historical_psi_W=stats[[1]]$W,fixed_historical_psi_accepted=stats[[1]]$accepted,
  fixed_independent_psi_W=stats[[2]]$W,fixed_independent_psi_accepted=stats[[2]]$accepted)
}
if(length(rows))write.csv(do.call(rbind,rows),file.path(out,"rounded_optimum_R_diagnostics.csv"),row.names=FALSE)
cat("REPRESENTATION_DIAGNOSTICS",length(rows),"no fitting\n")
