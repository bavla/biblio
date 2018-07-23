  varCutree <- function(R,var,vmin,vmax){
    mark <- function(t,c){
      if(t<0) part[-t] <<- c else {mark(R$merge[t,1],c); mark(R$merge[t,2],c)}
    }
    n <- length(var); part <- rep(999999,n); nclust <- 0
    value <- cbind(var,rep(0,n))
    for(i in 1:(n-1)){
      j <- R$merge[i,1]; if(j==0) next 
      a <- ifelse(j<0,value[-j,1],value[j,2])
      j <- R$merge[i,2]; if(j==0) next 
      b <- ifelse(j<0,value[-j,1],value[j,2])
      value[i,2] <- a+b
    }
    value[n,2] <- 0
    for(i in 1:(n-1)){
      if(value[i,2]<=vmax) next
      l <- R$merge[i,1]; r <- R$merge[i,2] 
      if(l==0) a <- 0 else a <- ifelse(l<0,value[-l,1],value[l,2])
      if(r==0) b <- 0 else b <- ifelse(r<0,value[-r,1],value[r,2])
      if(min(a,b)>vmax) next
      if(a<=vmax) if(a>=vmin) {nclust <- nclust+1; mark(l,nclust)} else mark(l,0)
      if(b<=vmax) if(b>=vmin) {nclust <- nclust+1; mark(r,nclust)} else mark(r,0)    
    }  
    return(list(part=part,value=value))
  }