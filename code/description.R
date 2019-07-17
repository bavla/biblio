#
# description produces a csv file csvFile containing a table with columns
#   (name, WoSline, author, title, journal, year, code) 
# for vertices of a subnetwork from file netFile.
# The titles for all (DC>0) vertices are stored in the table T.
# Since for vertices with DC=0 the title is not available it takes '***'.
#
# Vladimir Batagelj,  September 7, 2013 / August 19, 2013
#
description <- function(netFile,csvFile,T){
  f <- function(L){
    s <- unlist(strsplit(L,"[[:space:]]+"))
    if(s[1]=="") t <- s[3] else t <- s[2]
    t <- substr(t,2,nchar(t)-1)
    if(substr(t,1,1)=="=") t <- substr(t,2,nchar(t))
    return(t)
  }
  net <- file(netFile,"r")
  L <- readLines(net,n=1)       
  n <- as.integer(unlist(strsplit(L,"[[:space:]]+"))[2])
  S <- readLines(net,n=n);  close(net)
  N <- gsub("&#39;","'",unlist(lapply(S,f)))
  nn <- length(N); tit <- character(nn); aut <- character(nn); jrn <- character(nn);
  cod <- character(nn); wos <- integer(nn); yer <- integer(nn)
  for(k in 1:nn){j <- which(T$name==N[k]); 
    tit[k] <- ifelse(length(j)==0,NA,T$title[j])
    aut[k] <- ifelse(length(j)==0,NA,T$author[j])
    wos[k] <- ifelse(length(j)==0,NA,T$WoSline[j])
    jrn[k] <- ifelse(length(j)==0,NA,T$journal[j])
    cod[k] <- ifelse(length(j)==0,NA,T$code[j])
    yer[k] <- ifelse(length(j)==0,NA,T$year[j])
#    cat(k,yer[k],tit[k],'\n'); flush.console()
    if(is.na(yer[k])){
      l <- regexpr("(",N[k],fixed=TRUE)[1]+1
      r <- regexpr(")",N[k],fixed=TRUE)[1]-1
      yer[k] <- as.integer(substr(N[k],l,r))
    }
  }
  D <- data.frame(name=as.character(N),WoSline=wos,author=as.character(aut),
     title=as.character(tit),journal=as.character(jrn),year=yer,code=as.character(cod))
  write.csv2(D,file=csvFile,fileEncoding="UTF-8",row.names=FALSE,quote=FALSE)
  return(D)
}

# > setwd("E:/Data/Centrality/net")
# > T <- read.csv2("titles.csv")
# >  source("https://raw.githubusercontent.com/bavla/biblio/master/code/description.R")
# > d <- description("./res/island2.net","./res/island2new.csv",T)

