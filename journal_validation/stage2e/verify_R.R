# Saved-object validation/export only. No fitting, package loading or RNG draws.
args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==1L)
out<-normalizePath(args[1],winslash="/",mustWork=TRUE)
tasks<-read.csv(file.path(out,"task_manifest.csv"),stringsAsFactors=FALSE);checks<-list();penalties<-list()
for(id in tasks$id) {
 folder<-file.path(out,id);h<-readRDS(file.path(folder,"historical_task.rds"))
 if(!file.exists(file.path(folder,"independent_path.rds")))next
 a<-readRDS(file.path(folder,"independent_path.rds"))
 stopifnot(identical(h$post_penalty_state,a$rng_before),identical(a$rng_before,a$rng_after))
 for(side in c("historical","independent")) {
  projection<-if(side=="historical")h$projection else a$projection
  for(j in 1:2) {
   c<-projection$penalty_traces[[j]]
   stopifnot(c$replay_difference<1e-11,c$options$penalty$c==.5,
    abs(c$options$penalty$gamma-.1/log(1000))<1e-15)
   penalties[[length(penalties)+1L]]<-data.frame(id=id,side=side,instrument=j,coordinate=1:100,
    actual_last_penalty=as.numeric(c$last_penalty),reported_next_penalty=as.numeric(c$reported_next_penalty))
   checks[[length(checks)+1L]]<-data.frame(id=id,side=side,instrument=j,
    effective_c=c$options$penalty$c,gamma=c$options$penalty$gamma,replay_difference=c$replay_difference,
    weighted_gram_condition=projection$weighted_gram_condition,rng_paired=TRUE)
  }
 }
}
write.csv(do.call(rbind,checks),file.path(out,"downstream_verification.csv"),row.names=FALSE)
write.csv(do.call(rbind,penalties),file.path(out,"actual_instrument_penalties.csv"),row.names=FALSE)
cat("SAVED_DOWNSTREAM_CHECKS",length(checks),"\n")
