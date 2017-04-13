# R procedures

## description


> source("C:\\Users\\..path..\\WoS\\R\\description.R")  
> T <- read.csv('titles.csv',sep=";",colClasses="character")  
> T$code <- 1  
> d <- description("mainpath.net","mainpath.csv",T)  
> head(d)  
