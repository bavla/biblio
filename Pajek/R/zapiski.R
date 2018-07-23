setwd("C:/Users/batagelj/work/Python/WoS/BM/results/cluster")

tree <- as.integer(read.csv("./MaxTol.clu",header=FALSE,skip=1)$V1)
N <- length(tree); n <- (N+1) %/% 2
merge <- matrix(0,nrow=(n-1),ncol=2)
for(i in 1:n) if(tree[i]>0){
  k <- tree[i]-n
  if(merge[k,1]==0) merge[k,1] <- -i else merge[k,2] <- -i
}
for(i in (n+1):N) if(tree[i]>0){
  k <- tree[i]-n; j <- i-n 
  if(merge[k,1]==0) merge[k,1] <- j else merge[k,2] <- j
}

# ------------------------------------------------------------------------

> RM <- Pajek2R("MaxTol.clu")
> HM <- read.csv("MaxTolHeight.vec",header=FALSE,skip=3111)[[1]]
> RM$height <- HM
> RM$method <- "Maximum/Tolerant"
> RM$dist.method <- "Euclidean"
> RM$labels <- rownames(U)
> class(RM) <- "hclust"
> RM$call <- "Pajek.data"

source("C:\\Users\\batagelj\\work\\Python\\WoS\\BM\\cluster\\Pajek2R.R")
source("C:\\Users\\batagelj\\work\\Python\\WoS\\BM\\cluster\\varCutTree.R")

RM <- Pajek2R("MaxTol.clu")
n <- RM$n; nm <- n-1; np <- n+1
HM <- read.csv("MaxTolHeight.vec",header=FALSE,skip=np)[[1]]
RM$height <- HM
RM$method <- "Maximum/Tolerant"
RM$dist.method <- "Jaccard"
RM$labels <- read.csv("CiteNam.net",header=FALSE,skip=1,sep=" ",colClasses="character",nrows=n)$V2
class(RM) <- "hclust"
RM$call <- "Pajek.data"
> names(RM)
[1] "merge"       "n"           "method"      "dist.method" "labels"     
[6] "call"        "height"  


C <- varCutree(RM,rep(1,n),10,100)
table(C$part)



plot(RC,hang=-1,cex=0.001,main="Max/Tolerant")
for(i in (nm-100):nm) cat(i,RM$merge[i,],"\n")


nam <- read.csv("CiteNam.net",header=FALSE,skip=1,sep="",colClasses=c("integer","character","numeric","numeric","numeric"),nrows=n)nam <- read.csv("CiteNam.net",header=FALSE,skip=1,sep=" ",colClasses="character",nrows=n)

> nam <- read.csv("CiteNam.net",header=FALSE,skip=1,sep="",colClasses=c("integer","character","numeric","numeric","numeric"),nrows=n)
> head(nam)
  V1                      V2     V3     V4  V5
1  1       ALBA_R(1973)3:113 0.4999 0.8867 0.5
2  2   BREIGER_R(1974)53:181 0.4160 0.0500 0.5
3  3   BREIGER_R(1975)12:328 0.5291 0.1014 0.5
4  4 GRANOVET_M(1973)78:1360 0.3582 0.9057 0.5
5  5     WHITE_H(1976)81:730 0.5079 0.1398 0.5
6  6   BRIEGER_R(1976)41:117 0.5541 0.0500 0.5
> nam[1:15,]
   V1                      V2     V3     V4  V5

# ------------------------------------------------------------------------

> setwd("C:\\Users\\batagelj\\work\\Python\\WoS\\BM\\results\\cluster")
> source("C:\\Users\\batagelj\\work\\Python\\WoS\\BM\\results\\cluster\\Pajek2R.R")
> source("C:\\Users\\batagelj\\work\\Python\\WoS\\BM\\results\\cluster\\varCutTree.R")
> 
> RC <- Pajek2R("MaxTol.clu")
> n <- RC$n
> n
[1] 3927
> nm <- n-1; np <- n+1
> rCount <- varCutree(RC,rep(1,n),5,400)
> t <- table(rCount$part)
> t
> out <- file("CMaxTot1.clu","w"); cat(paste("*vertices ",n),rCount$part,sep="\n",file=out); close(out)

> orDendro <- function(m,i){if(i<0) return(-i)
+   return(c(orDendro(m,m[i,1]),orDendro(m,m[i,2])))}
> 
> orSize <- function(m,i){if(i<0) return(1)
+   s[i] <<- orSize(m,m[i,1])+orSize(m,m[i,2])
+   return(s[i])}
> HC <- read.csv("MaxTolHeight.vec",header=FALSE,skip=np)[[1]]

> colT <- c("integer","character","numeric","numeric","numeric") 
> nam <- read.csv("CiteNam.net",header=FALSE,skip=1,sep="",colClasses=colT,nrows=n)
> RC$height <- HC
> RC$method <- "Maximum/Tolerant"
> RC$dist.method <- "Jaccard / Normalized Hamming"
> RC$labels <- nam
> class(RC) <- "hclust"
> RC$call <- "Pajek.data"

> RC$order <- orDendro(RC$merge,nm)
> plot(RC,hang=-1,cex.axis=4,main="Maximum/Tolerant",lwd=0.01,oma=c(5,5,5,5))
