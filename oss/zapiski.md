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

## Logistična krivulja

https://en.wikipedia.org/wiki/Logistic_function

### Absolutna napaka

Δ<sub>x</sub> = f(x,p) - y<sub>x</sub> 
```
> wdir <- "C:/Users/vlado/docs/papers/2025/Biro/Projekt"
> setwd(wdir)
> W <- read.csv2(file="works_year_OA.csv",skip=1,row.names=1)
> tail(W)
> X <- W$year[1:51]; Y <- W$count[1:51]
> plot(X,Y,xlim=c(1950,2050),ylim=c(0,15000000),pch=16)
> i <- 47; x0 <- X[i]; L <- 2*Y[i]; k <- 0.07; y <- 1950:2050 
> # least squares
> f <- function(x,p) {L <- p[1]; k <- p[2]; x0 <- p[3]; L/(1+exp(-k*(x-x0)))}
> E <- function(p){d <- f(X,p) - Y; sum(d**2)}
> # E <- function(p){d <- 1 - Y/f(X,p); sum(d**2)}
> p0 <- c(L,k,x0); best <- optim(p0,E)
> E(p0)
[1] 3.598176e+13
> best
$par
[1] 2.035811e+07 8.340236e-02 2.016878e+03
$value
[1] 8.456562e+12
$counts
function gradient 
     200       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="red",pch=16,cex=0.5)
```
<img src="https://github.com/user-attachments/assets/8d0e61f8-889a-4741-8dd7-ec7896ee367c" width="600" />

## Dvignjena logistična krivulja

y0 + L/(1+exp(-k*(x-x0)))
```
> plot(X,Y,xlim=c(1950,2050),ylim=c(0,21000000),pch=16)
> i <- 47; x0 <- X[i]; y0 <- Y[1]; L <- 2*Y[i]-Y[1]; k <- 0.07; y <- 1950:2050 
> # least squares
> f <- function(x,p) {L <- p[1]; k <- p[2]; x0 <- p[3]; y0 <- p[4]; y0 + L/(1+exp(-k*(x-x0)))}
> E <- function(p){d <- f(X,p) - Y; sum(d**2)}
> # E <- function(p){d <- 1 - Y/f(X,p); sum(d**2)}
> p0 <- c(L,k,x0,y0); best <- optim(p0,E)
> E(p0)
[1] 1.120447e+14
> best
$par
[1] 1.935462e+07 1.048966e-01 2.017273e+03 1.032547e+06
$value
[1] 8.853627e+12
$counts
function gradient 
     337       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="red",pch=16,cex=0.5)
```
<img src="https://github.com/user-attachments/assets/f87aab94-ccf9-4308-a1d5-2b9497f976b6" width="600" />

### Logaritemska napaka, najmanjši kvadrati

Δ<sub>x</sub> = log(y<sub>x</sub>/f(x,p))   

```
> plot(X,Y,xlim=c(1950,2060),ylim=c(0,21000000),pch=16)
> i <- 47; x0 <- X[i]; y0 <- Y[1]; L <- 2*Y[i]-Y[1]; k <- 0.07; y <- 1950:2060 
> # least squares
> f <- function(x,p) p[4] + p[1]/(1+exp(-p[2]*(x-p[3])))
> E <- function(p){d <- log(Y/f(X,p)); sum(d**2)}
> p0 <- c(L,k,x0,y0); best <- optim(p0,E)
> E(p0)
[1] 13.7609
> best
$par
[1] 1.859472e+07 1.064136e-01 2.016000e+03 7.980038e+05
$value
[1] 0.1536802
$counts
function gradient 
     393       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="red",pch=16,cex=0.5)
```
<img src="https://github.com/user-attachments/assets/74cf7e3e-843e-4f65-aedd-d3b5ca451317" width="600" />

### Logaritemska napaka, vsota absolutnih napak

```
> plot(X,Y,xlim=c(1950,2060),ylim=c(0,21000000),pch=16)
> i <- 47; x0 <- X[i]; y0 <- Y[1]; L <- 2*Y[i]-Y[1]; k <- 0.07; y <- 1950:2060 
> # least squares
> f <- function(x,p) p[4] + p[1]/(1+exp(-p[2]*(x-p[3])))
> E <- function(p){d <- log(Y/f(X,p)); sum(abs(d))}
> p0 <- c(L,k,x0,y0); best <- optim(p0,E)
Warning message:
In log(Y/f(X, p)) : NaNs produced
> E(p0)
[1] 23.30731
> best
$par
[1] 1.940282e+07 1.166885e-01 2.015695e+03 9.552365e+05
$value
[1] 2.73447
$counts
function gradient 
     367       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="red",pch=16,cex=0.5)
> 
```
<img src="https://github.com/user-attachments/assets/e0518eef-5b97-4e57-b695-af45125819a2" width="600" />

### Lokalni ekstremi

Zgleda, da ima iskanje priležnic več lokalnih ekstremov. Parameter x0 se (skoraj) ne spreminja. Če ga sami spreminjamo v začetni rešitvi, dobimo npr. naslednje.

```
> p0 <- c(10000000,0.13,2008,950000)
> plot(X,Y,xlim=c(1950,2060),ylim=c(0,15000000),pch=16)
> best <- optim(p0,E)
> E(p0)
[1] 4.332392
> best
$par
[1] 1.162367e+07 1.373500e-01 2.008000e+03 9.321085e+05
$value
[1] 2.764556
$counts
function gradient 
     447       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="red",pch=16,cex=0.5)
 
> p0[3] <- 2007
> best <- optim(p0,E)
> E(p0)
[1] 3.907996
> best
$par
[1] 1.104687e+07 1.437737e-01 2.007000e+03 9.483508e+05
$value
[1] 3.042086
$counts
function gradient 
     483       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="blue",pch=16,cex=0.5)
 
> p0[3] <- 2009
> best <- optim(p0,E)
> E(p0)
[1] 5.742115
> best
$par
[1] 1.242951e+07 1.329896e-01 2.009000e+03 9.204891e+05
$value
[1] 2.575939
$counts
function gradient 
     471       NA 
> pr <- function(x){f(x,best$par)}
> points(y,pr(y),col="green",pch=16,cex=0.5)
```
<img src="https://github.com/user-attachments/assets/e3b704c2-7ac6-4c90-a375-a9879f4f8e99" width="600" />

Število člankov na leto ima vsaj dva "generatorja": rast števila raziskovalcev in temeljitost beleženja objav. Pri zadnjih letih se postavi še vprašanje zapoznelosti beleženja.


