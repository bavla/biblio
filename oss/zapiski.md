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

## 
