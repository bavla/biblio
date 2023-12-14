# bibmat - Derived bibliographic networks
# Vladimir Batagelj, November 2023
# source("https://raw.githubusercontent.com/bavla/biblio/master/code/bibmat.R")

normalize <- function(M) t(apply(M,1,function(x) x/max(1,sum(x))))
newman <- function(M) t(apply(M,1,function(x) x/max(1,sum(x)-1)))
D0 <- function(M) {diag(M) <- 0; return(M)}
binary <- function(M) {B <- t(apply(M,1,function(x) as.integer(x!=0)))
  colnames(B) <- colnames(M); return(B)}
wod <- function(M) apply(M,1,sum)
wid <- function(M) apply(M,2,sum)
od <- function(M) wodeg(binary(M))
id <- function(M) wideg(binary(M))
wd <- wodeg
Co <- function(M) t(M)%*%M
Cn <- function(M) Co(normalize(M))
Ct <- function(M) D0(t(normalize(M))%*%newman(M))
through <- function(M,S) t(M)%*%S%*%M
arit <- function(a,b) mean(c(a,b))
amin <- function(a,b) min(c(a,b))
amax <- function(a,b) max(c(a,b))
geom <- function(a,b) sqrt(a*b)
harm <- function(a,b) ifelse(a*b==0,0,2/(1/a+1/b))
jacc <- function(a,b) ifelse(a*b==0,0,1/(1/a+1/b - 1))
symm <- function(A,M) {n <- nrow(M); S <- M
  for(i in 1:(n-1)) for(j in (i+1):n) S[i,j] <- S[j,i] <- A(M[i,j],M[j,i])
  return(S)}
ltxArray <- function(M){
  S <- paste("\\begin{array}{r|",paste(rep("r",ncol(M)),collapse=""),"}\n",
    paste(c("",colnames(M)),collapse=" & "),"\\\\\\hline\n",sep="")
  for(i in 1:nrow(M)) 
    S <- paste(S,rownames(M)[i],paste(" &",M[i,],collapse=""),"\\\\\n")
  return(paste(S,"\\hline\n\\end{array}\n",sep=""))
}
ltxMatrix <- function(M){
  S <- paste("\\kbordermatrix{\n",paste(c("",colnames(M)),collapse=" & "),
    "\\\\\n",sep="")
  for(i in 1:nrow(M)) 
    S <- paste(S,rownames(M)[i],paste(" &",M[i,],collapse=""),"\\\\\n")
  return(paste(S,"}\n",sep=""))
}

