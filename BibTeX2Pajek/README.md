# BibTeX2Pajek

<pre><code>
>>> wdir = r'C:\Users\batagelj\work\Python\BibTeX'
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
