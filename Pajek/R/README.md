# R procedures

## description

The function description produces a csv file csvFile containing a table with columns (name, WoSline, author, title, journal, year, code)  for vertices of a subnetwork from file netFile. The titles for all (DC>0) vertices are stored in the table T. Since for vertices with DC=0 the title is not available it takes '***'.


> source("C:\\Users\\..path..\\WoS\\R\\description.R")  
> T <- read.csv('titles.csv',sep=";",colClasses="character")  
> T$code <- 1  
> d <- description("mainpath.net","mainpath.csv",T)  
> head(d)  
