# Saved ordinary-QR coefficients ONLY; no package loads, RNG or refitting.
args<-commandArgs(trailingOnly=TRUE);stopifnot(length(args)==2L)
folders<-list.dirs(args[1],recursive=FALSE,full.names=TRUE)
folders<-folders[grepl("/(pilot|validation)_[0-9]{3}$",gsub("\\\\","/",folders))]
for(folder in folders) {
 d<-readRDS(file.path(folder,"details.rds"))
 target<-file.path(args[2],paste0(basename(folder),"_ordinary_beta.bin"))
 stopifnot(!file.exists(target))
 con<-file(target,"wb");writeBin(as.double(d$ordinary$coefficients),con,size=8,endian="little");close(con)
 cat("EXPORTED_SAVED_REFERENCE",basename(folder),"\n")
}
