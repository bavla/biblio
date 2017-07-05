#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################################################################
#
#   WoS2Pajek - Transforming WoS bibliographies into Pajek
#
#   Wos2Pajek.run(MLdir,project,bibfile,maxvert,listep,ISIn,makeClean,keywSel,
#                 listTitles,vtxIndex)
#
#   open in IDLE and Run Module and enter the data in Tk window, or in IDLE
#
#   import sys; wdir = r'c:\users\Batagelj\work\Python\WoS'; sys.path.append(wdir)
#   MLdir = r'c:\Python27\Lib\site-packages\MontyLingua-2.1\Python'
#   import os; os.chdir(wdir); sys.path.append(MLdir)
#   import WoS2Pajek
#
#   Vladimir Batagelj, 23. February 2017 /  23-30. March 2007 
#
#   1. 12-14. August 2007  add Journals and Keywords (ID+DE+TI)
#   2. 24. August 2007     add number of pages
#   3. 6. December 2007    add Abstracts (AB) and lemmatization, timestamps
#   4. 27. December 2007   remove DOI info; consider ARTN/AR and UNSP in ISIname
#   5. 17-24. June 2008    file without duplicates
#   6. 29. December 2008   types partition *T
#      12. February 2009   problem with the name:    KULHAVY, , W
#      19. February 2009   problem with the name: AU BENSON, , C
#      8. March 2009       multiple types - sets, timer
#      2. April 2009       problem with the name: AU SCHONEMA.PH
#   7. 22-23. August 2009  Tkinter interface, select keywords fields (DE,ID,TI,AB)
#   8. 27. February 2010   output of authors to WA doesn't depend on CRlist empty;
#                          errors in ISI names
#   9. 16. December 2010   try on the main loop
#  10. 24. October 2011    name.upper() in nameG inserted
#  11. 12. May 2013        correction of *vertices for Keywords
#                          error in names - double spaces (see sn9/first/sn9.log)
#                            de  SOUZA Francoise Jean Oliveira,
#                            Van  Dijck J
#                            Stewart  TA
#  12. 19-23. August 2013  works index and titles list added
#  13. 9. September 2013   journals, write.out ime1 ****
#                          journals --> uppercase
#  14. 20-22. May 2015     DOI, improvement of nameG
#                          names in CR: GRANOVET.MS 1973
#      15. July 2016       problems with names:
#                            Hansen . T., 1978, THESIS YALE U NEW HA
#                            Weinberg . E., 2014, NAT CHEM BIOL, V11, P9
#                            Faradzev . I. A., 1994, INVESTIGATIONS ALGEB, P1
#  15. 23. February 2017   split keyword phrases,
#                          use last part of DI if BP is missing,
#                          ensure that PY info is numeric.
#   To do: cite -> self, other
#          remove authors of only cited works
###########################################################################

import string, os, shutil, sys, re, datetime, csv
import Tkinter as T
import tkFileDialog as Tf
from Tkinter import *

def lemmatize(ML,ab,stopwords):
  sLto = [ML.tokenize(st) for st in ML.split_sentences(ab.lower())]
  sLta = [ML.tag_tokenized(t) for t in sLto]
  lem = [ML.lemmatise_tagged(t) for t in sLta]
  lemas = [s.split('/')[2] for s in string.join(lem).split(' ')]
  return list(set(dropList(lemas,stopwords)))

def dropList(mylist, rmlist):
  def testfun(somestring, checklist=rmlist):
    return somestring not in checklist
  mylist = filter(testfun, mylist)
  return mylist

def ISIname(AU,PY,J9,VL,BP,AR):
# from work description produces its ISI name
  if "." in AU: AU=AU.replace('.',', ')
  name = AU.upper().replace(' ','').replace(',',' ')
  if PY != '': name = name+', '+PY
  if J9 != '': name = name+', '+J9[:20]
  if VL != '': name = name+', V'+VL
  if AR != '': name = name+', ARTN '+AR
  elif BP != '': name = name+', P'+BP
  return name

def nameG(name,DOI):
# transforms an ISI name into a short name
# if the name is 'non-standard' it takes it
# as a short name and reports a warning
  s = name.upper().split(", ")
  if len(s) == 1: return(name)
  y = 0; v = ''; p = ''; n = ''
  if s[0][0] == '*' : n = s[0]
  else:
    q = s[0].replace(' . ',' ').replace('.',' ').replace('  ',' ').strip().split(' ')
    n = q[0][:8]; lq = len(q)
    if   lq == 1: pass
    elif lq == 2: n = n+'_'+q[1][0]
    else:
      if q[0] in ['DE', 'VAN', 'VON']:
        n = (q[0]+q[1])[:8]+'_'+q[2][0]
      else: n = n+'_'+q[1][0]
  if len(s) >= 2 :
    try: y = eval(s[1])
    except: pass
  if len(s) >= 4 :
    if s[3][0] == 'V' :
      v = s[3][1:]
      if len(s) >= 5 :
        if s[4][0] == 'P' : p = s[4][1:]
        elif s[4].startswith('ARTN'): p = s[4][5:]
        elif s[4].startswith('UNSP'): p = s[4][5:]
    elif s[3][0] == 'P' : p = s[3][1:]
    elif s[3].startswith('ARTN'): p = s[3][5:]
    elif s[3].startswith('UNSP'): p = s[3][5:]
  if (y == 0) and (len(s) > 1):
    try:
      y = eval(s[0])
      n = '$'+s[1].replace(' ','_')
    except: pass
  if (p == '') and (len(DOI) > 0):
    if DOI.endswith(']'): DOI = DOI[:-1]
    q = DOI.split('/'); p = q[-1]
    i = p.rfind('.')
    if i > 0: p = p[i+1:]
    else:
      i = p.rfind('-')
      if i > 0: p = p[i+1:]      
  if (v == '') and (p == '') and (y == 0) and (len(s) > 1) :
    p = s[1].replace(' ','_')
  if n != '' : return n+'('+str(y)+')'+v+':'+p
# non-standard
  print "--> ", name
  return name

def Gname(AU,PY,VL,BP,AR):
# from work description produces its short name
  if "." in AU: AU=AU.replace('.',', ')
  name = AU.upper()
  s = name.split(", ")
  name = (s[0].replace(' ',''))[:8]+'_'
  try:
    if len(s) > 1: name = name + s[1][0]
  except: name = name + "*"
  if BP != '': return name+'('+str(PY)+')'+VL+':'+BP
  else: return name+'('+str(PY)+')'+VL+':'+AR

def infVertex(name):
# determines the Pajek's number of a vertex with a given
# name; if the name contains the character " a warning
# is reported
   global nver, vert, maxver, nodes, years, ISI, step, linecnt, test, vtxInd, numbib
   if vert.has_key(name):
#     print 'Old vertex(', vert[name], '): ' + name
     return vert[name]
   else:
     if ISI :
       s = name.split(", ")
       try:  year = eval(s[1])
       except: year = 0
     else:
       z = name.find('(')+1; k = name.find(')')
       year = name[z:k]
     nver = nver + 1;
     if nver >= maxver :
       try:
         input("\n*** max vertex number "+str(maxver)+
           " exceeded\n*** program exited\n\nPress Enter")
       except: pass
       exit(0)
     vert[name] = nver
#     if (nver % 1000) == 0:
#       print 'New vertex(', nver, '): ' + name
     nodes.write(str(nver)+' "'+name+'"\n')
     years.write(str(year)+'\n')
     if vtxInd:
       test.write(str(nver)+' '+name+' > '+str(numbib)+' '+str(linecnt)+'\n')
     if name.find('"') >= 0:
       print '***** Bad label ',nver,' : ',name
     return nver

def infAuthor(name):
# determines the Pajek's number of an author
   global naut, aut, authors
   if aut.has_key(name):
     return aut[name]
   else:
     naut = naut + 1;
     aut[name] = naut
     authors.write(str(naut)+' "'+name+'"\n')
     return naut

def infJournal(name):
# determines the Pajek's number of a journal
   global njr, jour, journals
   name = name.upper()
   if jour.has_key(name):
     return jour[name]
   else:
     njr = njr + 1;
     jour[name] = njr
     journals.write(str(njr)+' "'+name+'"\n')
     return njr

def infKeyword(name):
# determines the Pajek's number of a keyword
   global nkw, keyw, keywords
   if keyw.has_key(name):
     return keyw[name]
   else:
     nkw = nkw + 1;
     keyw[name] = nkw
     keywords.write(str(nkw)+' "'+name+'"\n')
     return nkw

def run(MLdir,project,bibfile,maxvert,listep,ISIn,makeClean,keywSel,
        listTitles,vtxIndex):
   try:
     wdir = os.path.dirname(__file__)
   except NameError:
     wdir = r'C:\Users\batagelj\work\Python\WoS'
   if True:
     print "WoS2Pajek parameters"
     print "WoS  dir: ", wdir
     print "ML   dir: ", MLdir
     print "Proj dir: ", project
     print "WoS file: ", bibfile
     print "MaxNum  : ", maxvert
     print "step    : ", listep
     print "ISI name: ", ISIn
     print "clean   : ", makeClean
     print "keywords: ", keywSel
     print "titles  : ", listTitles
     print "index   : ", vtxIndex
   keyDE = keywSel[0]; keyID = keywSel[1]; keyTI = keywSel[2]; keyAB = keywSel[3]
   import MontyLingua
   global nver, vert, maxver, nodes, ISI, aut, naut, years, authors, numbib
   global step, comlin, jour, njr, nkw, keyw, keywords, journals, linecnt, test, vtxInd
   ML = MontyLingua.MontyLingua()
   maxver = maxvert; ISI = ISIn; vtxInd = vtxIndex
   step = 1000000
   if listep > 0: step = listep
   t1 = datetime.datetime.now()
   if not comlin: print "\n***", version, "\n"+copyR+"\n"
   print "started: "+t1.ctime()+"\n"
   workdir = project+'\\'
   vertype = [ 0 for i in range(maxver) ]
   numpages = [ 0 for i in range(maxver) ]
   try:
     bib = open(bibfile, 'r')
   except:
     print 'wrong WoS file'
     exit()
   resrc = os.path.join(wdir, "resources/")
   stopwords = open(resrc+'StopWords.dat', 'r').read().lower().split()
#   resrc = u"unicode_path/resources/StopWords.dat"  # <<<<<<
#   stopwords = open(resrc, 'r').read().lower().split()
   stopwords = ['.',',',';','(',')','[',']','"','=','?','!',':','-','s','']+stopwords
   nodes  = open(workdir+'nodes.tmp', 'w')
   arcs   = open(workdir+'arcs.tmp', 'w')
   arcs.write('*arcs \n')
   temp  = open(workdir+'works.tmp', 'w')
   authors = open(workdir+'authors.tmp', 'w')
   years  = open(workdir+'years.tmp', 'w')
   journals  = open(workdir+'journals.tmp', 'w')
   jourlink  = open(workdir+'jourlink.tmp', 'w')
   keywords  = open(workdir+'keywords.tmp', 'w')
   keylink  = open(workdir+'keylink.tmp', 'w')
   time     = open(workdir+'timer.dat', 'w')
   trace    = open(workdir+'trace.txt', 'w')
   if listTitles:
     csvfile = open(workdir+'titles.csv', 'wb')
     titles = csv.writer(csvfile, delimiter=';',quotechar='"',
              quoting=csv.QUOTE_MINIMAL)
     titles.writerow(['name', 'WoSline', 'author', 'title', 'journal', 'year'])
   if vtxIndex: test = open(workdir+'vtxIndex.txt', 'w')
   else: test = ""  
   if makeClean:
     clean  = open(workdir+'clean.WoS', 'w')
     copyLine = True; lines = ''
   vert = {}; nver = 0
   aut  = {}; naut = 0
   keyw = {}; nkw  = 0
   jour = {}; njr  = 1
   jour['*****'] = njr
   journals.write(str(njr)+' "*****"\n')
   numbib = 0; endbib = False; numdup = 0; lines = ""; bibTY = 1
   tc = datetime.datetime.now()
   time.write('{0}: {1}\n'.format(numbib,tc))
   linecnt = 0
   try:
     while not endbib:
       line = bib.readline()
       if not line: break
       linecnt = linecnt + 1
       if len(line)<2: line = "SK IP\n"
       lines = lines + line
       control = line[:2]
       if control != '  ': state = control
       content = line[3:-1]
       if control == 'PT':
         numbib = numbib + 1; startline = linecnt
         bibAU = ''; bibCR = ''; bibPT = content; bibPG = ''; bibAR = ''
         bibVL = ''; bibJ9 = '*****'; bibBP = ''; bibEP = ''; bibDI = ''
         bibTI = ''; bibID = ''; bibDE = ''; bibAB = ''; bibPY = '0'
         listCR = []; listAU = []
       elif control == '*T': bibTY = eval(content)
       elif control == 'AU':
         if bibAU == '': bibAU = content
       elif control == 'J9': bibJ9 = content
       elif control == 'PY': bibPY = re.sub('[^0-9]','',content)
       elif control == 'VL': bibVL = content
       elif control == 'BP': bibBP = content
       elif control == 'EP': bibEP = content
       elif control == 'PG': bibPG = content
       elif control == 'AR':
         if content.startswith('e'): content = content[1:]
         bibAR = content
       elif control == 'DI':
         bibDI = content.split('.')[-1]
         if "/" in bibDI: bibDI = bibDI.split('/')[-1]
       elif control == '**': print ">>> ", content
       elif control == 'ER':
         if bibPY == '': bibPY = '0'
         if bibBP == '':
           if bibDI != '': bibBP = bibDI
           elif bibAR != '': bibBP = bibAR
         if ISI : name = ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR)
         else: name = Gname(bibAU,bibPY,bibVL,bibBP,bibAR)
         sind = infVertex(name)
         if (numbib % step) == 0:
           tc = datetime.datetime.now()
           print numbib,':',name,' - ',str(tc)
           time.write('{0}: {1}\n'.format(numbib,tc))
         journal = bibJ9
         ijour = infJournal(journal)
         jourlink.write('{0} {1}\n'.format(sind,ijour))
         try:
           if bibPG != '': numpages[sind] = eval(bibPG)
           else: numpages[sind] = 1 + eval(bibEP) - eval(bibBP)
         except: pass
         for aind in listAU:
           temp.write(str(sind)+' '+str(aind)+'\n')
         if (not vertype[sind]) and listTitles:
           titles.writerow([name,startline,bibAU,bibTI,bibJ9,bibPY])
         if listCR != []:
           if vertype[sind] :
             vertype[sind] = vertype[sind] | (1 << (bibTY-1))
             trace.write("*** duplicate: {0}\n".format(ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR)))
             if vtxIndex: test.write("*** duplicate L: {0} {1} > {2} {3} {4}\n".format(
                        sind,ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR),numbib,linecnt,bibTY))
             numdup = numdup + 1
             if makeClean: copyLine = False
           else:
             if bibTY > 0: vertype[sind] = 1 << (bibTY-1)
             else: vertype[sind] = 0
             for tind in listCR:
               arcs.write('{0} {1}\n'.format(sind,tind))
         else:
           if vertype[sind] :
             vertype[sind] = vertype[sind] | (1 << (bibTY-1))
             trace.write("*** duplicate: {0}\n".format(ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR)))
             if vtxIndex: test.write("*** duplicate E: {0} {1} > {2} {3} {4}\n".format(
                        sind,ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR),numbib,linecnt,bibTY))
             numdup = numdup + 1
             if makeClean: copyLine = False
           else:
             if bibTY > 0: vertype[sind] = 1 << (bibTY-1)
             trace.write("*** no CRs: {0}\n".format(ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR)))
             if vtxIndex: test.write("*** no CRs: {0} {1} > {2} {3} {4}\n".format(
                        sind,ISIname(bibAU,bibPY,bibJ9,bibVL,bibBP,bibAR),numbib,linecnt,bibTY))
         if vtxIndex: test.write("--- {0} {1}\n".format(bibTY,vertype[sind]))
         if not keyTI : bibTI = ''
#         titwords=re.split('\W',bibTI.lower())
#         words = [token for token in titwords if token not in stopwords]
#         kwords = [token.strip() for token in (bibID+';'+bibDE).lower().split(';') if len(token) > 0]
#         words = words + kwords
         ic = bibAB.lower().rfind("(c)")
         if ic > 0: bibAB = bibAB[:ic]
         words = lemmatize(ML,(bibTI+'. '+bibID+';'+bibDE+'. '+bibAB).lower().replace("'"," ").replace("-"," "),stopwords)
         for w in words:
           ikey = infKeyword(w)
           keylink.write('{0} {1}\n'.format(sind,ikey))
         if makeClean:
           if copyLine and (lines != ''): clean.write(lines)
           lines = ''; copyLine = True
#      elif control == 'EF':
#        endbib = True
         lines = ''
       else:
         pass
       if state == 'CR':
         id = content.rfind(', DOI ')
         if id > 0 :
           DOI = content[id+2:]; content = content[:id]
         else: DOI = ""
         if ISI : name = content
         else: name = nameG(content,DOI)
         newWork = not vert.has_key(name)
         work = infVertex(name)
         listCR.append(work)
         if newWork:
           if ISI : author = name[:name.find(',')]
           elif (name[0]=='*') or (name[0]=='$') : author = 'UNKNOWN'
           else: author = name[:name.find('(')]
           iaut = infAuthor(author)
           temp.write('{0} {1}\n'.format(work,iaut))
           ll = content.split(', ')
           journal = '*****'
           if len(ll) == 5 : journal = ll[2]
           ijour = infJournal(journal)
           jourlink.write('{0} {1}\n'.format(work,ijour))
       if state == 'AU':
         if ISI : author = content.upper().replace(' ','').replace(',',' ')
         else:
           name = content.upper()
           s = name.split(", ")
           author = (s[0].replace(' ',''))[:8]+'_'
           try:
             if len(s) > 1: author = author + s[1][0]
           except:
             author = author + "*"
         listAU.append(infAuthor(author))
       if (state == 'TI')          : bibTI = bibTI + ' ' + content
       if (state == 'ID') and keyID: bibID = bibID + ' ' + content
       if (state == 'DE') and keyDE: bibDE = bibDE + ' ' + content
       if (state == 'AB') and keyAB: bibAB = bibAB + ' ' + content
   except:
     trace.write("Error in run\n\n")
     trace.write("in line: "+str(linecnt)+"\n")
     trace.write(line+"\n")
     trace.write(lines+"\n")
     trace.close()
     bib.close(); nodes.close(); arcs.close(); journals.close()
     jourlink.close(); authors.close(); years.close(); temp.close()
     keylink.close(); keywords.close();
     if vtxIndex: test.close();
     if listTitles: csvfile.close()
     sys.exit("WoS2Pajek - abnormal termination")

   tc = datetime.datetime.now()
   print numbib,':',name,' - ',str(tc)
   print ">>> End of processing of WoS file"
   time.write(str(numbib)+': '+str(tc)+'\n')
   time.close()
   if makeClean:
     if  copyLine and (lines != ''): clean.write(lines)
     clean.close()
   bib.close(); nodes.close(); arcs.close(); journals.close()
   jourlink.close(); authors.close(); years.close(); temp.close()
   keylink.close(); keywords.close(); trace.close()
   print "number of works      = ",nver
   print "number of authors    = ",naut
   print "number of journals   = ",njr
   print "number of keywords   = ",nkw
   print "number of records    = ",numbib
   print "number of duplicates = ",numdup
   if makeClean: print "clean WoS data  : clean.WoS"
   if listTitles:
     print "works + titles  : titles.csv"; csvfile.close()
   if vtxIndex:
     print "works index file: vtxIndex.txt"; test.close()


# year of publication partition
   print "\n*** FILES:\nyear of publication partition: "+project+'\\Year.clu'
   yinp  = open(workdir+'years.tmp', 'r')
   years  = open(workdir+'Year.clu', 'w')
   years.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   years.write('*vertices '+str(nver)+'\n')
   shutil.copyfileobj(yinp,years)
   yinp.close(); years.close()

# described / cited only partition
   print "described / cited only partition: "+project+'\\DC.clu'
   part  = open(workdir+'DC.clu', 'w')
   part.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   part.write('*vertices '+str(nver)+'\n')
   for i in range(nver):
     part.write(str(vertype[i+1])+'\n')
   part.close()

# number of pages vector
   print "number of pages vector: "+project+'\\NP.vec'
   vect  = open(workdir+'NP.vec', 'w')
   vect.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   vect.write('*vertices '+str(nver)+'\n')
   for i in range(nver):
     vect.write(str(numpages[i+1])+'\n')
   vect.close()

# citation network
   print "citation network: "+project+'\\Cite.net'
   nodes  = open(workdir+'nodes.tmp', 'r')
   net  = open(workdir+'Cite.net', 'w')
   net.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   net.write('*vertices '+str(nver)+'\n')
   shutil.copyfileobj(nodes,net)
   arcs   = open(workdir+'arcs.tmp', 'r')
   shutil.copyfileobj(arcs,net)
   arcs.close(); net.close(); nodes.close()

# works X journals network ***
   print "works X journals network: "+project+'\\WJ.net'
   nodes  = open(workdir+'nodes.tmp', 'r')
   tj  = open(workdir+'journals.tmp', 'r')
   wj  = open(workdir+'WJ.net', 'w')
   wj.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   wj.write('*vertices '+str(nver+njr)+' '+str(nver)+'\n')
   shutil.copyfileobj(nodes,wj)
   nodes.close()
   while True:
     line = tj.readline()
     if not line: break
     s = line.split(" ",1)
     wj.write(str(eval(s[0])+nver)+' '+s[1])
   temp  = open(workdir+'jourlink.tmp', 'r')
   wj.write('*arcs\n')
   while True:
     line = temp.readline()
     if not line: break
     s = line.split(" ")
     wj.write(s[0]+' '+str(eval(s[1])+nver)+'\n')
   temp.close(); wj.close(); tj.close()

# works X keywords network
   print "works X keywords network: "+project+'\\WK.net'
   nodes  = open(workdir+'nodes.tmp', 'r')
   tk  = open(workdir+'keywords.tmp', 'r')
   wk  = open(workdir+'WK.net', 'w')
   wk.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n") 
   wk.write('*vertices '+str(nver+nkw)+' '+str(nver)+'\n')
   shutil.copyfileobj(nodes,wk)
   nodes.close()
   while True:
     line = tk.readline()
     if not line: break
     s = line.split(" ",1)
     wk.write(str(eval(s[0])+nver)+' '+s[1])
   temp  = open(workdir+'keylink.tmp', 'r')
   wk.write('*arcs\n')
   while True:
     line = temp.readline()
     if not line: break
     s = line.split(" ")
     wk.write(s[0]+' '+str(eval(s[1])+nver)+'\n')
   temp.close(); wk.close(); tk.close()

# works X authors network
   print "works X authors  network: "+project+'\\WA.net'
   nodes  = open(workdir+'nodes.tmp', 'r')
   taut  = open(workdir+'authors.tmp', 'r')
   wa  = open(workdir+'WA.net', 'w')
   wa.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
   wa.write('*vertices '+str(nver+naut)+' '+str(nver)+'\n')
   shutil.copyfileobj(nodes,wa)
   nodes.close()
   while True:
     line = taut.readline()
     if not line: break
     s = line.split(" ",1)
     wa.write(str(eval(s[0])+nver)+' '+s[1])
   temp  = open(workdir+'works.tmp', 'r')
   wa.write('*arcs\n')
   while True:
     line = temp.readline()
     if not line: break
     s = line.split(" ")
     wa.write(s[0]+' '+str(eval(s[1])+nver)+'\n')
   temp.close(); wa.close(); taut.close()
   try:
     os.remove(workdir+'works.tmp')
     os.remove(workdir+'authors.tmp')
     os.remove(workdir+'years.tmp')
     os.remove(workdir+'arcs.tmp')
     os.remove(workdir+'nodes.tmp')
     os.remove(workdir+'keywords.tmp')
     os.remove(workdir+'keylink.tmp')
     os.remove(workdir+'journals.tmp')
     os.remove(workdir+'jourlink.tmp')
   except:
     print "unable to delete some temp files"
   t2 = datetime.datetime.now()
   print "finished: "+t2.ctime()
   print "time used: ", t2-t1
   print "***"
# ----------------------------------------------------------------------------------------


class MainWindow(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.grid(row=0, column=0)

        self.OK = False
        self.mlDir = T.StringVar()
        self.mlDir.set(r'c:\Python27\Lib\site-packages\MontyLingua-2.1\Python')
        self.prDir = T.StringVar()
        self.wosFil = T.StringVar()
        self.maxNum = 0
        self.maxNumStr = T.StringVar()
        self.step = T.IntVar()
        self.stepStr = T.StringVar()
        self.useIsi = T.BooleanVar()
        self.clean = T.BooleanVar()
        self.titles = T.BooleanVar()
        self.index = T.BooleanVar()
        self.states = []
        options = ['DE - Author Keywords','ID - Keywords Plus','TI - Title','AB - Abstract']

        mle = T.Entry(self,relief=T.SUNKEN,textvariable=self.mlDir,width=60)
        mlb = T.Button(self, text='browse...')
        mle.bind('<Key-Return>', self.gotitml)
        mlb.config(command=(lambda x=mle: x.insert(0, Tf.askdirectory(
          title="WoS directory"))))
        mlDirLabel = T.Label(self, text="ML  dir:",anchor=T.W, underline=0)

        pre = T.Entry(self,relief=T.SUNKEN,textvariable=self.prDir,width=60)
        prb = T.Button(self, text='browse...')
        pre.bind('<Key-Return>', self.gotitpr)
        prb.config(command=(lambda x=pre: x.insert(0, Tf.askdirectory(
          title="Project directory"))))
        prDirLabel = T.Label(self, text="Pro dir:", anchor=T.W, underline=0)

        wfe = T.Entry(self,relief=T.SUNKEN,textvariable=self.wosFil,width=60)
        wfb = T.Button(self, text='browse...')
        wfe.bind('<Key-Return>', self.gotitwf)
        wfb.config(command=(lambda x=wfe: x.insert(0, Tf.askopenfilename(
          title="WoS file"))))
        wosFilLabel = T.Label(self, text="WoS file:", anchor=T.W, underline=0)
        mnLabel = T.Label(self, text="MaxNum:", underline=0, anchor=T.W)
        mne = T.Entry(self,relief=T.SUNKEN,textvariable=self.maxNumStr,width=10)
        stLabel = T.Label(self, text="Step:", underline=0, anchor=T.W)
        ste = T.Entry(self,relief=T.SUNKEN,textvariable=self.stepStr,width=10)
        isiLabel = T.Label(self, text="names:", underline=0, anchor=T.W)
        chkIsi = T.Checkbutton(self,text="use ISI names", variable=self.useIsi)
        clnLabel = T.Label(self, text="clean:", underline=0, anchor=T.W)
        chkClean = T.Checkbutton(self,text="make clean file", variable=self.clean)
        titLabel = T.Label(self, text="titles:", underline=0, anchor=T.W)
        chkTitles = T.Checkbutton(self,text="make titles file", variable=self.titles)
        idxLabel = T.Label(self, text="index:", underline=0, anchor=T.W)
        chkIndex = T.Checkbutton(self,text="make works index file", variable=self.index)
        keyLabel = T.Label(self, text="keywords:", underline=0, anchor=T.W)
        for i in range(4):
           var = T.IntVar()
           chkKey = T.Checkbutton(self,text=options[i],variable = var)
           chkKey.grid(row=6+i,column=1, padx=2, pady=2, sticky=T.W)
           self.states.append(var)

        runButton = T.Button(self, text='RUN', command=self.start)
        cancelButton = T.Button(self, text='Cancel', command=self.close)

        mlDirLabel.grid(row=1, column=0, padx=2, pady=2, sticky=T.W)
        mle.grid(row=1, column=1, padx=2, pady=2, sticky=T.EW)
        mlb.grid(row=1, column=2, padx=2, pady=2, sticky=T.E)
        prDirLabel.grid(row=2, column=0, padx=2, pady=2, sticky=T.W)
        pre.grid(row=2, column=1, padx=2, pady=2, sticky=T.EW)
        prb.grid(row=2, column=2, padx=2, pady=2, sticky=T.E)
        wosFilLabel.grid(row=3, column=0, padx=2, pady=2, sticky=T.W)
        wfe.grid(row=3, column=1, padx=2, pady=2, sticky=T.EW)
        wfb.grid(row=3, column=2, padx=2, pady=2, sticky=T.E)
        mnLabel.grid(row=4, column=0, padx=2, pady=2, sticky=T.W)
        mne.grid(row=4, column=1, padx=2, pady=2, sticky=T.EW)
        stLabel.grid(row=5, column=0, padx=2, pady=2, sticky=T.W)
        ste.grid(row=5, column=1, padx=2, pady=2, sticky=T.EW)
        keyLabel.grid(row=6, column=0, padx=2, pady=2, sticky=T.W)
        isiLabel.grid(row=10,column=0, padx=2, pady=2, sticky=T.W)
        chkIsi.grid(row=10,column=1, padx=2, pady=2, sticky=T.W)
        clnLabel.grid(row=11,column=0, padx=2, pady=2, sticky=T.W)
        chkClean.grid(row=11,column=1, padx=2, pady=2, sticky=T.W)
        titLabel.grid(row=12,column=0, padx=2, pady=2, sticky=T.W)
        chkTitles.grid(row=12,column=1, padx=2, pady=2, sticky=T.W)
        idxLabel.grid(row=13,column=0, padx=2, pady=2, sticky=T.W)
        chkIndex.grid(row=13,column=1, padx=2, pady=2, sticky=T.W)
        runButton.grid(row=14,column=1, padx=2, pady=2, sticky=T.EW)
        cancelButton.grid(row=14,column=2, padx=2, pady=2, sticky=T.EW)
        self.entml = mle
        self.entpr = pre
        self.entwf = wfe
        wfe.focus_set()

    def gotitml(self,event):
        self.mlDir = self.entml.get()
        self.destroy()

    def gotitpr(self,event):
        self.prDir = self.entpr.get()
        self.destroy()

    def gotitwf(self,event):
        self.wosFil = self.entwf.get()
        self.destroy()

    def start(self):
        try: self.maxNum = eval(self.maxNumStr.get())
        except: self.maxNum = 100000
        try: self.step = eval(self.stepStr.get())
        except: self.step = 0
        self.OK = True
        self.quit()

    def close(self,event=None):
        self.parent.focus_set()
        self.quit()

    def quit(self, event=None):
        self.parent.destroy()

def process():
    application = T.Tk()
#    path = os.path.join(os.path.dirname(__file__), "resources/")
    path = os.path.join(os.path.abspath('.'), "resources/")
    if sys.platform.startswith("win"):
        icon = path + "pajek.ico"
    else:
        icon = "@" + path + "interest.xbm"
#   icon = u"unicode_path/resources/pajek.ico"  # <<<<<<
    application.iconbitmap(icon)
    application.title("WoS2Pajek 1.5 / February 23, 2017")
    window = MainWindow(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()
    sys.path.append(window.mlDir.get())
    if window.OK:
       run(window.mlDir.get(),window.prDir.get(),
         window.wosFil.get(),window.maxNum,window.step,
         window.useIsi.get(),window.clean.get(),[var.get()>0 for var in window.states],
         window.titles.get(),window.index.get())

#
# Run Wos2Pajek
#
global comlin, version, copyR
version = "WoS2Pajek 1.5"
copyR = "by V. Batagelj, February 23, 2017 / March 23, 2007"
if __name__ == '__main__':
   comlin = True
   print "\n***", version, "\n"+copyR+"\n"
#   for (i,x) in enumerate(sys.argv): print i,x
   if len(sys.argv) == 11:
      for x in sys.argv[1:]: print x
      print "------------------------"
      MLdir = sys.argv[1]
      project = sys.argv[2]
      bibfile = sys.argv[3]
      maxvert = eval(sys.argv[4])
      listep = eval(sys.argv[5])
      ISIn = eval(sys.argv[6])
      makeClean = eval(sys.argv[7])
      keywSel = eval(sys.argv[8])
      listTitles = eval(sys.argv[9])
      vtxIndex = eval(sys.argv[10])
      sys.path.append(MLdir)
      run(MLdir,project,bibfile,maxvert,listep,ISIn,makeClean,keywSel,
          listTitles,vtxIndex)
   else:
      process()
   print
   try: a = input("Close console?")
   except: pass
else:
   comlin = False
   print "Module Wos2Pajek imported.\n"
   print "***", version, copyR+"\n"
   process()
   print "\nTo rerun, type:"
   print "  reload(WoS2Pajek)"

#- End -------------------------------------------------------------------------------
