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