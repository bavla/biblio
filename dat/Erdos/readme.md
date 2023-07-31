# The Erdös Number Project network (version August, 2020) 

The network data are available at Jerry Grossman's site [The Erdös Number Project](https://sites.google.com/oakland.edu/grossman/home/the-erdoes-number-project).
People with Erdös number 1 are shown in ALL CAPS;  people with Erdös number 2 are shown with Normal Capitalization. 

The Grossman's data in HTML files (see `Erdos2020.zip`) were converted to Pajek format by Vladimir Batagelj on Sun Jul 30, 2023.
The conversion was done using the following short program in R
```
> # Conversion of The Erdös Number Project data from HTML to Pajek format
> # by Vladimir Batagelj, July 30, 2023
> wdir <- "C:/data/erdos"
> setwd(wdir)
> library(XML)
> caps <- function(s) return(s==toupper(s))
>
> E0 <- htmlParse(file="grossman - Erdos0p.html")
> A0 <- xpathSApply(doc = E0, path = "//p//span",xmlValue)
> E1 <- htmlParse(file="grossman - Erdos1.html")
> A1 <- xpathSApply(doc = E1, path = "//p//span",xmlValue)
> Ea <- htmlParse(file="grossman - ErdosA.html")
> Aa <- xpathSApply(doc = Ea, path = "//p//span",xmlValue)
>
> # Aa[7911]  [1] "MOSER, LEO*                             1964:  3"
> A1[19510] <- "SWART, HENDRIKA CORNELIA SCOTT (HENDA)*     1993"
>
> lev <- unname(sapply(Aa[5:length(Aa)],function(s) ifelse(caps(s),trimws(substr(s,1,nchar(s)-8)),s)))
> lev <- append(lev,"Paul Erdös"); n <- length(lev)
> lev[11129] <- "SWART, HENDRIKA CORNELIA SCOTT (HENDA)*"
> C <- 2-caps(lev); C[n] <- 0
> B <- substr(A1[6:length(A1)],1,1)
> I <- c(which(B!=" "),length(B)+1)+5
> net <- file("Erdos.net","w"); clu <- file("Erdos.clu","w")
> cat("%",date(),"\n*vertices",n,"\n",file=net)
> cat("%",date(),"\n*vertices",n,"\n",file=clu)
> for(i in 1:n) cat(i,' "',lev[i],'"\n',sep='',file=net)
> cat("*edgeslist\n",file=net)
> for(i in 1:(length(I)-1)){
+   L <- A1[I[i]:(I[i+1]-1)]
+   L[1] <- trimws(substr(L[1],1,nchar(L[1])-8))
+   N <- as.integer(factor(trimws(L),level=lev))
+   T <- which(is.na(N))
+   if(length(T)>0) cat("error",i,L[1],":",L[T],"\n")
+   cat(N,"\n",file=net)
+ }
> cat(c(n,which(C==1)),"\n",file=net)
> cat(C,sep="\n",file=clu)
> close(net); close(clu)
```
To get rid in Aa of the info attached to the Erdos number 1 authors we truncated the last 8 characters. This caused a problem with the entry `SWART, HENDRIKA CORNELIA SCOTT (HENDA)* 1993` which was treated separately.

Finally, the network file `Erdos.net` and partition file `Erdos.clu` were manually combined using a text editor into a Pajek project file `Erdos2020.paj` and saved in UTF-8 with BOM.
