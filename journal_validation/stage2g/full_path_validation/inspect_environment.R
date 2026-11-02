source('thesis_extension/environment/check_author_environment.R')
assert_author_environment('thesis_extension',write_outputs=FALSE)
out<-'journal_validation/stage2g/full_path_validation'
for(name in c('rlasso.default','LassoShooting.fit','lambdaCalculation')) {
 fun<-get(name,asNamespace('hdm'))
 writeLines(capture.output(fun),file.path(out,paste0('historical_',name,'.txt')))
}
