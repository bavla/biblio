# WoS2Pajek - Extracting subnetworks and listing their titles
# V. Batagelj, May 1st, 2017
# ------------------------------------------------------

listSubNets <- function(net,clu,subdir,T){
  cat("WoS2Pajek - Extracting subnetworks and listing their titles\n",
    "V. Batagelj, May 2017\n\n",date(),"\n",sep="")
  dir.create(paste(".",subdir,sep=""),showWarnings=FALSE)
  t <- table(read.csv(clu,head=FALSE,skip=1)$V1)
  if(names(t)[1]=="0") t <- t[2:length(t)]
  cluA <- paste(getwd(),"/",clu,sep=""); netA <- paste(getwd(),"/",net,sep="")
#  L <- readLines("getSubnet.txt",n=-1)
  L <- c("NETBEGIN 1", "CLUBEGIN 1", "PERBEGIN 1", "CLSBEGIN 1", 
    "HIEBEGIN 1", "VECBEGIN 1", "", "N 1 RDN \"network\" (477)", 
    "C 1 RDC \"partition\" (477)", "N 2 EXT 1 1 [cluster] 1 (15)", 
    "N 2 WN \"subnet\" 0 (15)", "EXIT")                        
  L <- gsub("partition",cluA,gsub("network",netA,L))
  for(i in 1:length(t)) {
    cl <- names(t)[i]; cat("Subnetwork:",cl,t[i],"\n"); flush.console()
    sub <- paste("subNet",cl,".net",sep="")
    subA <- paste(getwd(),subdir,sub,sep="")
    N <- gsub("subnet",subA,gsub("cluster",cl,L))
    writeLines(N,con="Pajek.log")
    system("C:/programi/pajek/pajek.exe",invisible=TRUE,wait=TRUE)
    if(!file.exists(subA)) {
      cat(subA,"*** problems\n"); flush.console(); next
    } else {
      csv <- paste(".",subdir,"List",cl,".csv",sep="")
      d <- description(subA,csv,T)
    }
  }
}

# listSubNets("Jislands.net","Jislands.clu","/Jislands/",T)


