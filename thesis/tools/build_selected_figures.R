# Presentation-only: python validate_selected_figures.py, then Rscript this file.
# Base R 3.4.3 + Cairo; no estimation, simulation or random-number generation.
options(stringsAsFactors=FALSE)
arg <- grep('^--file=',commandArgs(),value=TRUE)
root <- dirname(dirname(dirname(normalizePath(sub('^--file=','',arg)))))
source(file.path(root,'thesis_extension/config/extension_config.R'))
cfg <- extension_config
stopifnot(capabilities('cairo'), cfg$R_MC==500,
          identical(cfg$sample_sizes,c(500L,1000L)),
          identical(cfg$tau,c(.1,.25,.5,.75,.9)),
          identical(cfg$kappa,c(1,.5,.25,.1)),
          identical(cfg$alpha_grid,seq(-1,3,by=.1)),
          identical(cfg$power_delta,c(-1,-.5,-.25,.25,.5,1)),
          abs(pchisq(cfg$critical_value,2)-.95)<1e-12)
out <- file.path(root,'thesis/figures/generated')
s <- read.csv(file.path(out,'selected_heatmap_values.csv'))
pw <- read.csv(file.path(out,'selected_power_values.csv'))
stopifnot(nrow(s)==120,nrow(pw)==168,all(s$R==500),all(pw$R==500))
# Do not accept stale/edited validation tables: compare every plotted value
# with the frozen final summaries again at rendering time.
key <- function(z) paste(z$n,z$tau,z$kappa,z$estimator)
final <- do.call(rbind,lapply(cfg$sample_sizes,function(n)
  read.csv(file.path(root,paste0('thesis_extension/final/output/n',n,'/summary.csv')))))
fp <- do.call(rbind,lapply(cfg$sample_sizes,function(n)
  read.csv(file.path(root,paste0('thesis_extension/final/output/n',n,'/power_summary.csv')))))
ix <- match(key(s),key(final))
stopifnot(!anyNA(ix),max(abs(s$coverage-final$Coverage[ix]))<1e-12,
          max(abs(s$full_domain-final$all_41_acceptance_rate[ix]))<1e-12)
for(i in seq_len(nrow(pw))) {
  z <- pw[i,]
  expected <- if(z$delta==0) final$Size[match(key(z),key(final))] else
    fp$power[match(paste(key(z),z$delta),paste(key(fp),fp$Delta))]
  stopifnot(length(expected)==1,is.finite(expected),abs(z$rejection-expected)<1e-12)
}
es <- c('Oracle-GMM','Full-GMM','DML-IVQR-BC')
el <- c('Oracle-GMM','Full-GMM','DML-IVQR')
# Match the retained accepted-set figure's estimator identity encoding.
co <- c('#1F77B4','#D62728','#2CA02C');mk <- c(16,15,17);lt <- c(1,2,4)
# Keep the two heatmaps at their approved width; export Figure 2 at the full
# 14.5 cm thesis text width so its plotting type remains 9 pt after inclusion.
heatmap_width <- .72*14.5/2.54
power_width <- 14.5/2.54
power_height <- 6.3
saveplot <- function(name,width,height,draw) {
  cairo_pdf(file.path(out,paste0(name,'.pdf')),width=width,height=height,
            family='Arial',pointsize=9)
  draw();dev.off()
}
heat <- function(metric,lower,barlabel,nominal=FALSE) {
  # Apply the requested reduction once: 7.2 pt * 0.90 = 6.48 pt.
  numeric_cex <- 6.48/9
  values <- 100*s[[metric]]
  stopifnot(all(is.finite(values)),min(values)>=lower,max(values)<=100)
  # Monotone light-to-dark blue sequential palette (common across all panels).
  pal <- colorRampPalette(c('#F7FBFF','#C6DBEF','#6BAED6','#2171B5','#08306B'))(256)
  par(mar=rep(0,4),xpd=NA,cex=1)
  plot.new();plot.window(xlim=c(0,1),ylim=c(0,1),xaxs='i',yaxs='i')
  left <- c(.115,.412,.709); right <- left+.278
  for(j in 1:3)text((left[j]+right[j])/2,.975,el[j],font=2)
  text(.55,.923,expression(n==500),font=2)
  text(.55,.515,expression(n==1000),font=2)
  text(.014,.57,expression(kappa),srt=90)
  text(.55,.157,expression(tau))
  for(i in 1:2)for(j in 1:3) {
    yy <- if(i==1)c(.635,.895) else c(.227,.487)
    par(fig=c(left[j],right[j],yy),new=TRUE,mar=rep(0,4),mgp=c(1,.25,0),xpd=FALSE)
    plot(NA,xlim=c(.5,5.5),ylim=c(.5,4.5),axes=FALSE,xlab='',ylab='',xaxs='i',yaxs='i')
    for(t in 1:5)for(k in 1:4) {
      z <- s[s$n==cfg$sample_sizes[i]&s$estimator==es[j]&s$tau==cfg$tau[t]&s$kappa==cfg$kappa[k],]
      stopifnot(nrow(z)==1)
      v <- 100*z[[metric]];idx <- round((v-lower)/(100-lower)*255)+1
      rect(t-.5,4.5-k,t+.5,5.5-k,col=pal[idx],border='#FFFFFF',lwd=.25)
      rgb <- col2rgb(pal[idx])/255
      lum <- sum(ifelse(rgb<=.04045,rgb/12.92,((rgb+.055)/1.055)^2.4)*c(.2126,.7152,.0722))
      text(t,5-k,sprintf('%.1f',v),family='Arial Narrow',cex=numeric_cex,font=1,
           col=if(lum<.179)'white' else '#101010')
    }
    # Explicit tick text prevents base axis() dropping alternate close labels.
    mtext(sprintf('%.2f',cfg$tau),side=1,at=1:5,line=.35,cex=numeric_cex,
          family='Arial Narrow',font=1,adj=.5)
    if(j==1)axis(2,at=4:1,labels=sprintf('%.2f',cfg$kappa),tick=FALSE,las=1,
                 cex.axis=numeric_cex,font.axis=1)
  }
  par(fig=c(.20,.90,.105,.128),new=TRUE,mar=rep(0,4),xpd=NA,mgp=c(1,.3,0))
  plot(NA,xlim=c(lower,100),ylim=c(0,1),axes=FALSE,xlab='',ylab='',xaxs='i',yaxs='i')
  xs <- seq(lower,100,length.out=257)
  for(k in 1:256)rect(xs[k],0,xs[k+1],1,col=pal[k],border=NA)
  at <- if(lower==0)seq(0,100,25) else c(lower,60,80,100)
  axis(1,at=at,labels=at,tick=FALSE,cex.axis=numeric_cex,font.axis=1)
  mtext(barlabel,side=1,line=1.3,cex=1)
  if(nominal) {
    segments(95,0,95,1.25,col='#111111',lwd=.7)
    text(95,1.45,'95 nominal',adj=c(1,0),cex=numeric_cex,font=1)
  }
}
coverage_lower <- min(40,floor(min(100*s$coverage)/10)*10)
plot_args <- commandArgs(trailingOnly=TRUE)
if (!('--power-only' %in% plot_args)) {
  saveplot('coverage_heatmap',heatmap_width,3.5,function()heat('coverage',coverage_lower,'Coverage (%)',TRUE))
  saveplot('full_domain_acceptance_heatmap',heatmap_width,3.5,function()heat('full_domain',0,'Frequency (%)'))
}
if (!('--heatmaps-only' %in% plot_args)) saveplot('power_median_combined',power_width,power_height,function() {
  par(mar=rep(0,4),xpd=NA);plot.new();plot.window(c(0,1),c(0,1),xaxs='i',yaxs='i')
  text(.305,.978,expression(n==500),font=2)
  text(.745,.978,expression(n==1000),font=2)
  text(.018,.56,'Rejection probability',srt=90)
  text(.525,.086,expression(Delta))
  left <- c(.115,.555);right <- left+.38
  for(k in 1:4) {
    top <- .924-(k-1)*.197;bottom <- top-.155
    text(.525,top+.014,bquote(kappa==.(sprintf('%.2f',cfg$kappa[k]))),cex=1)
    for(i in 1:2) {
      par(fig=c(left[i],right[i],bottom,top),new=TRUE,mar=rep(0,4),xpd=FALSE,mgp=c(1,.3,0))
      plot(NA,xlim=c(-1.06,1.06),ylim=c(0,1),axes=FALSE,xlab='',ylab='',xaxs='i',yaxs='i')
      abline(h=seq(0,1,.25),col='#E5E5E5',lwd=.4)
      axis(1,at=c(-1,-.5,0,.5,1),labels=if(k==4)c('-1','-0.5','0','0.5','1') else FALSE,
           cex.axis=8/9,tck=-.025,col='#888888',lwd=.4)
      axis(2,at=c(0,.5,1),labels=if(i==1)c('0','0.5','1') else FALSE,
           las=1,cex.axis=8/9,tck=-.02,col='#888888',lwd=.4)
      abline(h=.05,lty=2,lwd=.7,col='#777777')
      for(j in 1:3) {
        z <- pw[pw$n==cfg$sample_sizes[i]&pw$kappa==cfg$kappa[k]&pw$estimator==es[j],]
        z <- z[order(z$delta),];stopifnot(nrow(z)==7)
        lines(z$delta,z$rejection,lty=lt[j],col=co[j],lwd=1)
        points(z$delta,z$rejection,pch=mk[j],col=co[j],cex=.65,xpd=NA)
      }
    }
    par(fig=c(0,1,0,1),new=TRUE,mar=rep(0,4),xpd=NA)
    plot.new();plot.window(c(0,1),c(0,1),xaxs='i',yaxs='i')
  }
  legend(.525,.033,xjust=.5,yjust=.5,legend=el,col=co,pch=mk,lty=lt,lwd=1,
         ncol=3,bty='n',cex=1,seg.len=1.3,x.intersp=.55)
})
if ('--power-only' %in% plot_args) {
  cat('Rendered power: 14.5 x 16.002 cm. Heatmaps skipped with --power-only.\n')
} else if ('--heatmaps-only' %in% plot_args) {
  cat('Rendered heatmaps: 10.44 x 8.89 cm. Power skipped with --heatmaps-only.\n')
} else {
  cat('Rendered heatmaps: 10.44 x 8.89 cm and power: 14.5 x 16.002 cm.\n')
}
