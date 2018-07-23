readCluRC <- function(cling){
  tree <- as.integer(read.csv(cling,header=FALSE,skip=1)$V1)
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
  return(list(merge=merge,n=n))
}

