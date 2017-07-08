#!/usr/bin/python
#------------------------------------------------------------------------------
#
#   BiBTeX -> Pajek converter
#
#   Vladimir Batagelj, April 2006
#
#   adapted for Python 3 by Vladimir Batagelj, July 2017
#------------------------------------------------------------------------------

# from string import strip, split, replace, lower, index
from sys import argv, exit, modules
import re, time
global  nam, numRec, links, aTab, wTab, yMax

def processRecord(bibRec,bibType):
   global  nam, numRec, links, aTab, wTab, yMax
   numRec += 1
   parts = bibRec.split('=')
   desKeys = ['head']; desVals = []
   for i in range(len(parts)):
      part = parts[i].strip(); j = part.rfind(',')
      if j < 0: j = len(part)-1
      desVal = part[:j].strip(); s = desVal[0]
      if (s == '"' or s == '{'): desVal = desVal[1:-1]
      desVals.append(desVal)
      desKeys.append(part[j+1:].strip().lower())
   work = desVals[0] = desVals[0].split('{')[1].strip()
   try:
      i = desKeys.index('title'); title = desVals[i].replace('"',"''")
   except ValueError: title = 'UNKNOWN'
   nam.write('%s  "%s"\n' % (numRec,title))
   try: i = desKeys.index('year'); year = desVals[i]
   except ValueError: year = 'UNKNOWN'
   m = re.search('\D',year)
   if m: year = year[:m.start()]
   try: year = int(year)
   except ValueError:
      print('bad year in record %s : %s' % (numRec,work))
      year = 0
   yMax = max(yMax,year)
   if work in wTab: work = 'DUP-'+str(numRec)
   wTab[work]=[numRec,bibType,year,work]
   try: i = desKeys.index('author'); authors = desVals[i]
   except ValueError: authors = 'UNKNOWN'
   authors = authors.split(' and ')
   links[work]=[]
   for author in authors:
      author = author.strip()
      if author in aTab:
         aVal = aTab[author]; numAut = aVal[0]
         aTab[author] = [numAut,min(aVal[1],year),max(aVal[2],year),author]
      else:
         numAut = len(aTab)
         aTab[author] = [numAut,year,year,author]
      links[work].append(numAut)

def run(workdir,input,inst):
   global nam, numRec, links, aTab, wTab, yMax
   pubs=['article','book','booklet','inbook','incollection',
         'inproceedings','manual','mastersthesis','misc','phdthesis',
         'proceedings','techreport','unpublished']
   try: # open input BiBTeX file
      bib = open(workdir+input,'r')
   except IOError as e:
      print("I/O error(%s): %s" % e)
      exit()
   print('instant   = ', inst)
   print('bibFile   = ', workdir+input)
   net = open(workdir+'bib.net','w')
   print('networkFile = ', workdir+'bib.net')
   nam = open(workdir+'bib.nam','w')
   print('titleFile = ', workdir+'bib.nam')
   nam.write('*vertices\n')
   vec = open(workdir+'bib.vec','w')
   print('yearFile = ', workdir+'bib.vec')
   clu = open(workdir+'bib.clu','w')
   print('typeFile = ', workdir+'bib.clu')
   aut = open(workdir+'bib.aut','w')
   eqv = open(workdir+'bibeqv.clu','w')
   links = {}; wTab = {'0':['0']}; aTab = {'0':['0']}
   numRec = 0; bibRec = ''; bibType = -1
   numLine = 0; last = 0; yMax = 0
   while not last:
      line = bib.readline()
      if not line:
         line = '@'; last = 1
      else:
         line = line.strip(); numLine += 1
      if line != '':
         if line[0] == '@':     # start of record
            if bibType >= 0:
               processRecord(bibRec,bibType)
               bibRec = ''
            head = line.split('{')
            head = head[0].replace('@','')
            try: bibType = pubs.index(head.lower())
            except ValueError:
               bibType = -1
               print('Unknown head, line=',numLine, head)
         if bibType >= 0: bibRec += line+' '
   del wTab['0']; del aTab['0'];
   numAut = len(aTab); numVer = numRec+numAut
   print('# of lines=%s, records=%s, authors=%s\n' % (numLine,numRec,numAut))
   net.write('% BibTeX2Pajek converter: BibTex -> Pajek\n')
   net.write('% by Vladimir Batagelj, April 2006 / July 2017\n')
   net.write('% BibTeX File = '+workdir+input+'\n% ')
   net.write('%s\n' % time.ctime(time.time()))
   if inst==0: net.write('% instantaneous\n')
   else: net.write('% cumulative\n')
   net.write('*vertices %s %s\n' % (numVer,numRec))
   vec.write('*vertices %s \n' % numRec)
   clu.write('%  0 - author\n')
   for i in range(len(pubs)):
      clu.write('% '); clu.write('%2i - %s\n' % (i+1,pubs[i]))
   clu.write('*vertices %s \n' % numVer)
   L=sorted(wTab.values())
   for t in L:
      if inst==0: net.write('%6i  \"%s\" [%i]\n' % (t[0],t[3],t[2]))
      else: net.write('%6i  \"%s\" [%i-%i]\n' % (t[0],t[3],t[2],yMax))
      clu.write('%s\n' % (1+t[1]))
      vec.write('%s\n' % t[2])
   L=sorted(aTab.values())
   for t in L:
      if inst==0: net.write('%6i \"%s\" [%i-%i]\n' % (numRec+t[0],t[3],t[1],t[2]))
      else: net.write('%6i \"%s\" [%i-%i]\n' % (numRec+t[0],t[3],t[1],yMax))
      clu.write('%s\n' % 0)
   nam.close(); vec.close(); clu.close();
   net.write('*Edges\n')
   for w in links.keys():
      t = wTab[w]
      for a in links[w]:
         if inst==0: net.write('%5i %5i 1 [%4i]\n' % (t[0],numRec+a,t[2]))
         else: net.write('%5i %5i 1 [%i-%i]\n' % (t[0],numRec+a,t[2],yMax))
   L = sorted(L, key=lambda x: x[3][x[3].rfind(' '):].lower())
   for t in L: aut.write('%6i \"%s\"\n' % (numRec+t[0],t[3]))
   eqv.write('*vertices %s \n' % numVer)
   for i in range(numVer): eqv.write('%s\n' % (i+1))
   bib.close(); net.close();  aut.close(); eqv.close()
   print('BibTeX2Pajek - done')

#
# run BibTeX2Pajek
#
if __name__ == '__main__': # run it from command line
   if len(argv) == 4:
      run(argv[1],argv[2],argv[3])
   else:
      print("Module BibTeX2Pajek")
      if "idlelib" in modules:
         wDir = input("Working directory = ")
         bibFile = input("BibTeX file = ")
         inst = int(input("0-instantaneous, 1-cumulative = "))
         run(wDir,bibFile,inst)
      else:
         print("Three arguments (WorkDir, BibTeXfile, instant) required to run !")
   print()
else: # it is imported
   print("Module BibTeX2Pajek imported.")
   print("To run, type: BibTeX2pajek.run(WorkDir,BibTeXfile,instant)")
   print("where bibFile is your input BibTeX file, and")
   print("instant is a switch 0-instantaneous, 1-cumulative")
#- End -------------------------------------------------------------------------------

