# Zapiski

## Število del v OpenAlexu po letih
```
> library(httr)
> library(jsonlite)
> wdir <- "C:/Users/vlado/docs/papers/2025/Biro/Projekt"
> setwd(wdir)
> res <- GET("https://api.openalex.org/works?filter=publication_year:1970-2024&group_by=publication_year")
> cont <- fromJSON(rawToChar(res$content))
> str(cont)
> C <- cont$group_by
> i <- order(C$key)
> year <- as.integer(C$key[i])[1:51]
> count <- C$count[i][1:51]
> plot(year,count,ylim=c(0,11500000),pch=16,main="OpenAlex - works/year")
> plot(year,log(count),pch=16,main="OpenAlex - log(works)/year")
```

<img src="https://github.com/user-attachments/assets/2aa8b9aa-e4f4-4a55-b24e-a55c448c9cb8" width="600" />

## Podvojitve števila del

```
> W <- data.frame(year=as.integer(C$key[i]),count=C$count[i])
> head(W)
> nrow(W)
[1] 55
> write.csv2(W,file="works_year_OA.csv")

> t <- W$count[2]; J <- c()
> for(j in 1:nrow(W)){
+   if(W$count[j]>=t) {cat(j,W$year[j],t,W$count[j],"\n"); J <- c(J,j); t <- 2*t}
+ } 
 1 1970  881943  955236 
20 1989 1763886 1847109 
32 2001 3527772 3705036 
40 2009 7055544 7275504 
> J
[1]  1 20 32 40
```

## 
