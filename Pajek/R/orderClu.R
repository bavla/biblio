
orDendro <- function(m,i){if(i<0) return(-i)
  return(c(orDendro(m,m[i,1]),orDendro(m,m[i,2])))}

orSize <- function(m,i){if(i<0) return(1)
  s[i] <<- orSize(m,m[i,1])+orSize(m,m[i,2])
  return(s[i])}