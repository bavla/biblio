
library(stringi)
library(stringr)
library(readxl)
wdir <- "C:/Mail.Ru Cloud/ANR HSE/ANR Projects/Citation analysis (Russian Scientists)/eLibraryProject (Slovenia)/Network analysis/cited"
setwd(wdir)

urlP <- " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)"
E <- c(
"Левин М.И., Цирик М.Л. Математическое моделирование коррупции//Экономика и математические методы. 1998. Т. 34. Вып. 4.",
"Fleurbaey M. Beyond GDP: The Quest for a Measure of Social Welfare. Journal of Economic Literature, 2009, vol. 47, no. 4, pp. 1029-1046.",
"Cooren, F. Acting and organizing: How speech acts structure organizational interactions. Concepts and Transformation, 2001a, 6(3), 275–293.",
"Bian, Y. Bringing strong ties back in: Indirect ties, network bridges, and job searches in China. American Sociological Review, 1997, 62, 366–385.",
"Denis, J.-L., Langley, A. & Cazale, L.   Leadership and strategic change under ambiguity. Organization Studies, 1996, 17, 673-699.",
"Ingram, Paul, Jeffrey Robinson, and Marc L. Busch. 2005. The intergovernmental network of world trade: IGO connectedness, governance and embeddedness. American Journal of Sociology 111 (3): 824-58.",
"Leeds, Brett Ashley, Andrew G. Long, and Sara McLaughlin Mitchell. 2000. Reevaluating alliance reliability: Specific threats, specific promises. Journal of Conflict Resolution 44 (5): 686-99.",
'W. Chen, Y. Wang, and S. Yang, "Efficient influence maximization in social networks," in KDD 2009.',
"Alexander Fischer. Blog. URL: http://blog.alexander-fischer.org/kategorie/persoenlich/(дата обращения 04.02.2012).",
"Холмогорова, Н.Г. Гаранян, Г.А. Петрова//Социальная и клиническая психиатрия. -2003. -Т. 13. -№ 2. -С. 15-24.",
'Snijders, T.A.B. & Bosker, R.J. (1994) `Modeled Variance in Two-level Models", Sociological Methods and Research 22: 342-363.',
'Erikson, Robert; John Goldthorpe and Lucienne Portocarero. 1979. `International Class Mobility in Three Western European Societies: England, France and Sweden."British Journal of Sociology 30: 415-441."',
"Ирина Голицына. Информационно-коммуникационные технологии в современном образовании. Некоторые аспекты информатизации образования. -LAP LAMBERT Academic Publishing. -2012.-134 с."
)

auName <- function(au){
   if(str_detect(au,"\\.")) return(au)
   a <- strsplit(au," ")[[1]]
   n <- length(a)
   if(n<2) return(au)
   i <- which(nchar(a)>3)
   if(length(i)>0)j <- i[1] else j <- 1 
   if(j<n) return(paste(a[1:j],paste(substr(a[(j+1):n],1,1),collapse=""),sep=", "))
   return(au)
}

toLatin <- function(S)
    gsub('"',"'",gsub(intToUtf8(697),"'",
    stri_trans_general(gsub("ъ","ʹ",S),
    "cyrillic-latin;nfd;[:nonspacing mark:] remove;nfc")))

ISIname <- function(s) {
#   s <- gsub("\\.","\\.",s)  # cyrillic . -> .
   s <- gsub("–","-",s) # cyrillic – -> -
   z <- as.integer(regmatches(s,gregexpr("\\d{4}",s,perl=TRUE))[[1]])
   z <- z[(1800<=z)&(z<=2018)]
   au <- NA; vl <- NA; is <- NA; bp <- NA; ep <- NA; py <- 0; so <- "work" 
   urlN <- regmatches(s,regexpr(urlP,s))
   if(length(z)>0){
      s <- gsub("  "," ",s)      
      y <- regmatches(s,gregexpr("\\(\\d{4}\\)", s, perl=TRUE))[[1]]
      if(length(y)>0){ py <- as.integer(substr(y,2,5))
      } else { py <- z[length(z)] }
      p <- regmatches(s,gregexpr("\\d+-\\d+", s, perl=TRUE))[[1]]
      np <- length(p)
      if(np>0){
         s <- gsub(p[np],"",s)
         pg <- as.integer(unlist(strsplit(p[np],"-")))
         bp <- pg[1]; ep <- pg[2]
      }
      s <- gsub("№ (\\d+)","№\\1",s,perl=TRUE)
      s <- gsub("Т. (\\d+)","№\\1",s,perl=TRUE) # cyrillic Т  !!!
      s <- gsub("vol. (\\d+)","№\\1",s,perl=TRUE)
      p <- regmatches(s,gregexpr("№\\d+",s,perl=TRUE))[[1]]
      np <- length(p)
      if(np>0){ q <- p[np]
         vl <- as.integer(substr(q,2,nchar(q)))
         s <- gsub(q," ",s)
      }
      a <- gsub("(\\D)\\. (.)\\.","\\1.\\2\\. ",s,perl=TRUE)
      a <- strsplit(a," & ",perl=TRUE)[[1]][1]
      a <- strsplit(a," and ",perl=TRUE)[[1]][1]
      L <- strsplit(gsub(",","",a),"\\. ")[[1]]
      if(length(L)>1){ sec <- substr(L[1],2,2)
         if(sec==".") au <- paste(trimws(L[2]),L[1])
         else au <- paste(L[1],trimws(L[2]))
      } else au <- ifelse(nchar(L[1])<30,L[1],substr(L[1],1,30))
      L <- strsplit(au," ",perl=TRUE)[[1]]
      if(length(L)>1){
         if(str_detect(L[2],".")) au <- paste(L[1],L[2])
         else if(length(L)>2) au <- paste(L[1],L[2],L[3])
      }
   }
   if(is.na(au)){if(length(urlN)>0){U <- strsplit(urlN[1],"//")[[1]]
      au <- substr(U[2],1,20)
   } else au <- "*unknown"}
   au <- auName(toLatin(au))
   return(list(au=au,py=py,so=so,vl=vl,is=is,bp=bp,ep=ep))
}

aFile <- "./elib/Articles.xlsx"
atypes <- c("text","text","skip","skip","text",rep("skip",4),rep("text",5),rep("skip",11))
af <- read_excel(aFile,sheet=1,col_types=atypes)
dim(af)
(nb <- nrow(af))
short <- vector(mode="character",length=nb)
Last <- vector(mode="character",length=nb)
Init <- vector(mode="character",length=nb)
S <- strsplit(af[[3]]," ") 

for(i in 1:nb) {Last[i] <- substr(S[[i]][1],1,8); Init[i] <- substr(S[[i]][2],1,1)} 
for(i in 1:nb) short[i] <- paste(Last[i],"_",Init[i],"(",af[i,6],")",af[i,5],":",af[i,7],sep="")
isi <- vector(mode="character",length=nb)
for(i in 1:nb) isi[i] <- paste(af[i,3],", ",af[i,6],", ",substr(af[i,4],1,20),", V",af[i,5],", P",af[i,7],sep="") 

waFile <- "./elib/WA.net"
N <- as.vector(read.table(waFile,sep=" ",skip=4,nrows=9207,stringsAsFactors=FALSE)$V2)
Encoding(N) <- "UTF-8"
links <- read.table(waFile,col.names=c("u","v"),skip=9212)

excel_sheets("cited.xls")
types <- c("numeric","text","skip","text","skip","skip")                                                    
df <- read_excel("cited.xls",sheet=1,col_types=types)
dim(df)
S <- as.vector(unlist(df[,2]))
Encoding(S) <- "UTF-8"
(nc <- length(S))
head(S)
pId <- as.character(as.integer(df[[3]]))

iDic <- new.env(hash=TRUE,parent=emptyenv())
rin <- 0; lin <- 1; cpid <- pId[1]
for(cp in 1:nc) if(cpid==pId[cp]) {rin <- rin+1} else {
   assign(cpid,list(i=lin,j=rin),env=iDic)
   lin <- rin+1; rin <- lin; cpid <- pId[cp]
}
get("16519995",env=iDic,inherits=FALSE)

wos <- file("basic.wos","w"); cit <- file("cited.wos","w")
skip <- file("skiped.txt","w"); cat(date(),"\n")
write(paste("**\n** Conversion of elibrary.ru data into WoS format\n** ",
   date(),"\n*T 1\nFN eLib2WoS\nVR 1.0\n",sep=""),wos)
noref <- 0; k <-1; nl <- nrow(links); ni <- 0; ns <- 0
N <- toLatin(N)
for(i in 1:nb){
   write(paste("PT J",sep=""),wos)
   if(k<=nl){found <- FALSE
      if(links$u[k]==i){found <- TRUE
         writeLines(paste("AU ",auName(N[links$v[k]]),sep=""),wos,useBytes=T) 
         repeat{ 
            k <- k+1
            if(k>nl) break
            if(links$u[k]>i) break
            writeLines(paste("   ",auName(N[links$v[k]]),sep=""),wos,useBytes=T)
         }       
      }
   }
   if(!found && !is.na(af[[3]][i]))writeLines(paste("AU ",auName(toLatin(af[[3]][i])),sep=""),wos,useBytes=T)
   writeLines(paste("TI ",toLatin(af[[2]][i]),sep=""),wos,useBytes=T)
   writeLines(paste("J9 ",toLatin(af[[4]][i]),sep=""),wos,useBytes=T)
   cid <- af[[1]][i]
   if(exists(cid,env=iDic,inherits=FALSE)){
      code <- "CR "
      ij <- as.vector(unlist(get(cid,env=iDic,inherits=FALSE)))
      for(j in ij[1]:ij[2]){
         D <- ISIname(S[j])
         if(D$py==0){ ns <- ns+1
            writeLines(paste(i,j,S[j]),skip,useBytes=T)
         } 
         writeLines(paste(code,D$au,", ",D$py,", ",substr(D$so,1,20),
            ", V",D$vl,", P",D$bp,sep=""),wos,useBytes=T)
#         writeLines(paste("   ",S[j],sep=""),wos,useBytes=T)
         code <- "   "; ni <- ni+1
      }
   } else {
      if((noref %% 10)==0) cat("\n")
      noref <- noref+1; cat(" ",cid)
   }
   write(paste("PY ",af[[6]][i],sep=""),wos)
   write(paste("VL ",af[[5]][i],sep=""),wos)
#  write(paste("IS ",af[[2]][i],sep=""),wos)
   write(paste("BP ",af[[7]][i],sep=""),wos)
   write(paste("EP ",af[[8]][i],sep=""),wos)
   write(paste("UT ELIB:",cid,sep=""),wos)
   writeLines(paste("UT short:",N[i],sep=""),wos,useBytes=T)
   write(paste("ER \n",sep=""),wos)
}
cat("\nnc=",nc,"  ni=",ni,"  ns=",ns,"  ne=",noref,"\n",date(),"\n")
close(wos); close(cit); close(skip)

