ris2wos <- function(fris,fwos){
  ris <- readLines(fris) 
  T <- gsub("^JO","SO",
       gsub("^AD","PI",
       gsub("^SP","BP",
       gsub("^A1","AU",
       gsub("^T1","TI",
       gsub("^Y1","PY",
       gsub("^PB","PU",
       gsub("^KW","DE",
       gsub("^TY (\\S)(\\S*)","PT \\1",
       gsub("  -","",ris[nchar(ris)>0]))))))))))
  Encoding(T) <- "UTF-8"
  writeLines(T,fwos)
}
# ris2wos("test.ris","test.WoS")