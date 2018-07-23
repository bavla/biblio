# R procedures

## description

The function description produces a csv file csvFile containing a table with columns (name, WoSline, author, title, journal, year, code)  for vertices of a subnetwork from file netFile. The titles for all (DC>0) vertices are stored in the table T. Since for vertices with DC=0 the title is not available it takes '***'.

```
source("C:\\Users\\..path..\\WoS\\R\\description.R")  
T <- read.csv('titles.csv',sep=";",colClasses="character")  
T$code <- 1  
d <- description("mainpath.net","mainpath.csv",T)  
head(d)  
```

## listSubNets

We first prepare the right environment: load R functions description and listSubNets, set the working directory and read in a data frame T the information about works from the file titles.csv produced by WoS2Pajek:

```
source("C:/Users/batagelj/work/Python/WoS/peere1/description.R")   
source("C:/Users/batagelj/work/Python/WoS/BM/listSubNets.R")   
setwd("C:/Users/batagelj/work/Python/WoS/BM/results/jaccard")   
T <- read.csv('../../titles.csv',sep=";",colClasses="character"); T$code <- 1   
listSubNets("Jislands.net","Jislands.clu","/Jislands/",T)   
```

## readCluRC 

Reads in R a hierarchy produced by hierarchical clustering with relational constraints in Pajek (stored as a partition/clustering) and creates an R hierarchy description.

> <- function(cling){

```
wdir <- "C:/Users/batagelj/work/Python/WoS/BM/results/Acite"
setwd(wdir)
source("https://raw.githubusercontent.com/bavla/biblio/master/Pajek/R/readCluRC.R")
RM <- readCluRC("MaxLeader.clu")
n <- RM$n; nm <- n-1; np <- n+1
HM <- read.csv("MaxLeaderHeig.vec",header=FALSE,skip=np)[[1]]
RM$height <- HM
RM$method <- "Maximum/Tolerant"
RM$dist.method <- "nACiA"
class(RM) <- "hclust"
RM$call <- "Pajek.data"
size <- read.csv("MaxLeaderSize.vec",header=FALSE,skip=np)[[1]]
RM$labels <- read.csv("nACIA.net",header=FALSE,skip=1,sep="",colClasses="character",nrows=n)$V2
```

## orderClu

```
orDendro <- function(m,i){if(i<0) return(-i)
  return(c(orDendro(m,m[i,1]),orDendro(m,m[i,2])))}
 
orSize <- function(m,i){if(i<0) return(1)
  s[i] <<- orSize(m,m[i,1])+orSize(m,m[i,2])
  return(s[i])}

RM$order <- orDendro(RM$merge,nm)
pdf("DendroMaxTol.pdf",width=58.5,height=41.5)
plot(RC,hang=-1,cex=0.08,main="Maximum/Tolerant",lwd=0.01)
dev.off()
```



