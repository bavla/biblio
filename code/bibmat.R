# bibmat - Derived bibliographic networks
# Vladimir Batagelj, November 2023
# source("https://raw.githubusercontent.com/bavla/biblio/master/code/bibmat.R")

normalize <- function(M) t(apply(M,1,function(x) x/max(1,sum(x))))
newman <- function(M) t(apply(M,1,function(x) x/max(1,sum(x)-1)))
D0 <- function(M) {diag(M) <- 0; return(M)}
binary <- function(M) {B <- t(apply(M,1,function(x) as.integer(x!=0)))
  colnames(B) <- colnames(M); return(B)}
wodeg <- function(M) apply(M,1,sum)
wideg <- function(M) apply(M,2,sum)
odeg <- function(M) wodeg(binary(M))
ideg <- function(M) wideg(binary(M))
wdeg <- wodeg

