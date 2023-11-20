# Data
## Bibliographic networks - small example

ExNets contains three networks: the citation network ExCi, the authorship network ExWA, and the countryship network ExAC. The file ExNets.ini contains Pajek parameters setting.

![ExNets](https://github.com/bavla/biblio/assets/20244435/86883871-e851-49fe-972c-432fd89cddeb)

```
> wdir <- "C:/Users/vlado/test/biblio"
> setwd(wdir)
> library(jsonlite)
> BL <- fromJSON("https://raw.githubusercontent.com/bavla/biblio/master/Eu/Data/bibList.json")
> str(BL)
> urlEx <- "https://github.com/bavla/biblio/raw/master/Eu/Data/ExNets.RDS"
> download.file(url=urlEx,destfile=paste0(wdir,"/ExNets.RDS",sep=""))
> Ex <- readRDS("ExNets.RDS")
> str(Ex)
> Ci <- Ex$Ci; WA <- Ex$WA; AC <- Ex$AC
```

