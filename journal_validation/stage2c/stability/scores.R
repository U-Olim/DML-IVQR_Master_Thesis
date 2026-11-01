# Saved fits only. No estimator source, quantile regression or RNG calls.
args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==3L)
src<-normalizePath(args[1],winslash="/",mustWork=TRUE)
out<-normalizePath(args[2],winslash="/",mustWork=TRUE);phase<-args[3]
stopifnot(phase%in%c("baseline","probes"))
folders<-list.dirs(src,recursive=FALSE,full.names=TRUE)
folders<-folders[grepl("/(pilot|validation)_[0-9]{3}$",gsub("\\\\","/",folders))]
cutoff<-qchisq(.95,2);allrows<-list()
put<-function(x,path){stopifnot(!file.exists(path));c<-file(path,"wb");writeBin(as.double(x),c,size=8,endian="little");close(c)}
stat<-function(e,psi) {
 s<-.9-as.numeric(e<=0);obs<-s*t(psi);g<-colSums(obs);S<-crossprod(obs)
 W<-drop(t(g)%*%solve(S,g))
 list(s=s,g=g,S=S,W=W,condition=kappa(S))
}
if(phase=="baseline") {
 writeLines(capture.output(sessionInfo()),file.path(out,"R_sessionInfo.txt"))
 put(cutoff,file.path(out,"historical_cutoff.bin"))
}
for(folder in folders) {
 name<-basename(folder);d<-readRDS(file.path(folder,"details.rds"));Xt<-cbind(1,d$dat$X)
 ystar<-drop(d$dat$y-(1+qnorm(.9))*d$dat$D)
 target<-file.path(out,name)
 if(phase=="baseline") {
  stopifnot(!dir.exists(target));dir.create(target)
  put(d$psi,file.path(target,"psi_observation_row_major.bin"))
  put(d$f,file.path(target,"density.bin"))
  put(ystar,file.path(target,"y_candidate.bin"))
 }
 for(arm in c("P11","P01","P10","P00")) {
  b<-d$arms[[arm]]$beta;base<-drop(ystar-Xt%*%b);reference<-d$arms[[arm]]
  af<-file.path(target,arm)
  if(phase=="baseline") {
   dir.create(af);z<-stat(base,d$psi)
   ediff<-max(abs(base-reference$e));rankdiff<-sum((base<=0)!=(reference$e<=0))
   gdiff<-max(abs(z$g/1000-reference$statistic$moment))
   Sdiff<-max(abs(z$S/1000-reference$statistic$second_moment))
   Wdiff<-abs(z$W-reference$statistic$W)
   row<-data.frame(dataset=name,arm=arm,residual_max_difference=ediff,rank_differences=rankdiff,
    score_moment_max_difference=gdiff,second_moment_max_difference=Sdiff,W_difference=Wdiff,
    W=z$W,saved_W=reference$statistic$W,cutoff=cutoff,accepted=z$W<=cutoff,
    saved_accepted=reference$statistic$W<=cutoff,score_sum_1=z$g[1],score_sum_2=z$g[2],
    S11=z$S[1,1],S12=z$S[1,2],S22=z$S[2,2],condition=z$condition,
    mean_rank_score=mean(z$s),intercept=b[1],cutoff_distance=z$W-cutoff)
   stopifnot(ediff==0,rankdiff==0,gdiff<=1e-9,Sdiff<=1e-9,Wdiff<=1e-9,
    (z$W<=cutoff)==(reference$statistic$W<=cutoff))
   put(base,file.path(af,"baseline_residual.bin"));put(z$s,file.path(af,"baseline_score.bin"))
   put(b,file.path(af,"baseline_beta.bin"))
   allrows[[length(allrows)+1L]]<-row
  } else {
   for(exponent in c(-40L,-30L,-20L,-10L))for(sign in c(-1L,1L)) {
    candidate<-b;candidate[1]<-b[1]+sign*2^exponent
    e<-drop(ystar-Xt%*%candidate);z<-stat(e,d$psi)
    id<-paste0("exp",exponent,"_sign",sign)
    put(e,file.path(af,paste0(id,"_residual.bin")))
    put(z$s,file.path(af,paste0(id,"_score.bin")))
    put(candidate,file.path(af,paste0(id,"_beta.bin")))
    allrows[[length(allrows)+1L]]<-data.frame(dataset=name,arm=arm,id=id,exponent=exponent,sign=sign,
     intercept=candidate[1],rank_changes=sum((e<=0)!=(base<=0)),mean_rank_score=mean(z$s),
     score_sum_1=z$g[1],score_sum_2=z$g[2],S11=z$S[1,1],S12=z$S[1,2],S22=z$S[2,2],
     W=z$W,accepted=z$W<=cutoff,condition=z$condition,cutoff_distance=z$W-cutoff)
   }
  }
 }
 cat("RECONSTRUCTED",phase,name,"\n")
}
write.csv(do.call(rbind,allrows),file.path(out,paste0(phase,"_R.csv")),row.names=FALSE)
if(phase=="baseline")writeLines("PASS: all 92 historical residuals/ranks/moments/W/decisions",file.path(out,"BASELINE_PASS.txt"))
