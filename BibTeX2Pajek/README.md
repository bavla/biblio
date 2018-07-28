# BibTeX2Pajek

BiBTeX -> Pajek converter, programmed in Python 2 by Vladimir Batagelj, April 2006. Adapted for Python 3 by Vladimir Batagelj, July 2017.

BibTeX2Pajek converts a given BibTeX bibliography into a collection of temporal Pajek's files.
<pre><code>>>> wdir = r'C:\Users\batagelj\work\Python\BibTeX'
>>> import os; os.chdir(wdir)
>>> import BibTeX2Pajek
Module BibTeX2Pajek imported.
To run, type: BibTeX2pajek.run(WorkDir,BibTeXfile,instant)
where BibTeXfile is your input BibTeX file, and
instant is a switch 0-instantaneous, 1-cumulative
>>> BibTeX2Pajek.run('','intbib.bib',1)
instant   =  1
bibFile   =  intbib.bib
networkFile =  bib.net
titleFile =  bibWork.nam
yearFile =  bibYear.clu
typeFile =  bib.clu
authorsFile =  bibAut.nam
bad year in record 834 : int:Tomlin1
Unknown head, line= 11914 
# of lines=11914, records=993, authors=497
 
BibTeX2Pajek - done
>>>
</code></pre>

[Sredin seminar](http://vlado.fmf.uni-lj.si/seminar/05apr06/)

[The Collection of Computer Science Bibliographies](https://liinwww.ira.uka.de/bibliography/index.html)

## BibTeX to RIS and WoS

See [citation resources](http://vladowiki.fmf.uni-lj.si/doku.php?id=pro:bib:citr).

We can use JabRef to convert BibTeX bibliography into RIS format that is very similar to WoS format. For example, for the file [test.bib](test.bib) we get the corresponding converted file [test.ris](test.ris). It contains several empty lines. They can be easily removed in R:
<pre><code>> setwd("C:/Users/batagelj/Documents/books/BM2/chapters/cluster")
> ris <- readLines("test.ris")
> T <- ris[nchar(ris)>0]
> writeLines(T,"testC.ris")
</code></pre>
The condensed RIS file [testC.ris](testC.ris) can be further converted into WoS file [test.WoS](test.WoS) by sequence of substitutions:
<pre><code>> T <- gsub("^T1","TI",gsub("^Y1","PY",gsub("^PB","PU",gsub("^KW","DE",gsub("^TY","PT",gsub("  -","",T))))))
> T <- gsub("^JO","SO",gsub("^AD","PI",gsub("^SP","BP",T)))
> Encoding(T) <- "UTF-8"
> writeLines(T,"test.WoS")
</code></pre>
The obtained file test.WoS needs some additional manual corrections. For example:
<pre><code>PU John Wiley and Sons, New York
</code></pre>
has to be split into
<pre><code>PU John Wiley and Sons
PI New York
</code></pre>
We can add also some missing information.

The above lines of R code can be wraped into a function [ris2wos](ris2wos.R). Then we can run the test
<pre><code>source("https://raw.githubusercontent.com/bavla/biblio/master/BibTeX2Pajek/ris2wos.R")
ris2wos("https://raw.githubusercontent.com/bavla/biblio/master/BibTeX2Pajek/test.ris",stdout())
</code></pre>
