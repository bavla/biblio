#!/usr/bin/python
###########################################################################
#
#   ZB1 - Transforming ZB data into Pajek files
#
#   ZB1.run(words)
#     words=0 keywords are phrases from the ut field
#     words=1 kywords are words from fields ut and ti
#
#   import sys; wdir = r'c:\users\Batagelj\data\ZB1'; sys.path.append(wdir)
#   MLdir = r'c:\Python32\Lib\site-packages\MontyLingua-2.1\Python'
#   sys.path.append(MLdir)
#
#   import ZB1
#
#   Vladimir Batagelj,
#     5. March 2011
#     based on ZB.py:  27-30. December 2010
#
###########################################################################

import string, os, shutil, sys, re, datetime

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

def removeTeX(s):
  s=s.lower().replace('. ','.').replace('\\i ','i').replace('\\l ','l')
  s=re.sub('{|}','',s)
  s=s.replace('\\"u','ue').replace('\\"o','oe').replace('\\"a','ae')
  s=s.replace('\\i','i').replace('\\l','l')
  s=re.sub('\\\\.','',re.sub('\\\\. ','',s))
  return(s)

def standardName(s):
  s = s.strip().lower()
  if s.endswith('.'): s=s[:-1]  
  return(s.replace('.','-').replace(', ','.').replace(' ','-'))

def infVertex(name):
# determines the Pajek's number of a work
  global nver, vert, nodes
  if name in vert:
    return vert[name]
  else:
    nver += 1; vert[name] = nver
    nodes.write(str(nver)+' "'+name+'"\n')
    return nver

def infAuthor(name):
# determines the Pajek's number of an author
  global naut, aut, authors
  if name in aut:
    return aut[name]
  else:
    naut += 1; aut[name] = naut
    authors.write(str(naut)+' "'+name+'"\n')
    return naut

def infKeyword(name):
# determines the Pajek's number of a keyword
  global nkey, key, keys
  if name in key:
    return key[name]
  else:
    nkey += 1; key[name] = nkey
    keys.write(str(nkey)+' "'+name+'"\n')
    return nkey

def infJournal(cont):
# determines the Pajek's number of a journal
  global njr, jour, jourinfo, journame
  selist = cont.split("\t")
  name = selist[0]
  if name in jour:
    return jour[name]
  else:
    njr += 1; jour[name] = njr
    if len(selist)<4: selist.extend(4*['?'])
    journame.write(str(njr)+' "'+name+'"\n')
    jourinfo.write(str(njr)+'\t'+selist[1]+'\t'+selist[2]+\
      '\t'+selist[3]+'\n')
    return njr

def infMSC(name):
# determines the Pajek's number of a MSC
  global nmsc, msc, mscs
  if name in msc:
    return msc[name]
  else:
    nmsc += 1; msc[name] = nmsc
    mscs.write(str(nmsc)+' "'+name+'"\n')
    return nmsc

def makeNet(cols,Wnet,inp,link,ncol):
# works X ??? network
  global wdir
  workdir = wdir+'\\'
  print("works X "+cols+"  network: "+workdir+Wnet+'.net')
  nodes  = open(workdir+'nodes.tmp', 'r')
  tinp  = open(workdir+inp, 'r')
  net   = open(workdir+Wnet+'.net', 'w')
  net.write("% created by "+version+" "+datetime.datetime.now().ctime()+"\n")
  net.write('*vertices '+str(nver+ncol)+' '+str(nver)+'\n')
  shutil.copyfileobj(nodes,net)
  nodes.close()
#  for line in tinp.readlines():
  while True:
    line = tinp.readline()
    if not line: break
    s = line.split(" ",1)
    net.write(str(eval(s[0])+nver)+' '+s[1])
  temp  = open(workdir+link, 'r')
  net.write('*arcs\n')
#  for line in temp.readlines():
  while True:
    line = temp.readline()
    if not line: break
    s = line.split(" ")
    net.write(s[0]+' '+str(eval(s[1])+nver)+'\n')
  temp.close(); net.close(); tinp.close()
  
def run(words=0):
  global comlin, version, copyR, wdir, nver, vert, nodes
  global naut, aut, authors, njr, jour, journals, jourinfo
  global journame, nmsc, msc, mscs, t1
  global nkey, key, keys
  import MontyLingua
  ML = MontyLingua.MontyLingua()
  t1 = datetime.datetime.now()
#  if not comlin: print("\n***", version, "\n"+copyR+"\n")
  print("started: "+t1.ctime()+"\n")
  workdir = wdir+'\\'
#  datfile = workdir+'zentralblatt.dat'
  datfile = workdir+'zentralblatt2.ZB'
#  datfile = workdir+'test.zb'
  try:
    dat = open(datfile, 'r', encoding='utf-8-sig')
  except:
    print('bad ZB data file:', datfile)
    exit()
  resrc = os.path.join(wdir, "resources/")
  stopwords = open(resrc+'StopWords.dat', 'r').read().lower().split()
  stopwords = ['.',',',';','(',')','[',']','"','=','?','!',':','-','s','']+stopwords

  nodes  = open(workdir+'nodes.tmp', 'w')
  authors = open(workdir+'authors.tmp', 'w')
  keys = open(workdir+'keywords.tmp', 'w')
  authlink  = open(workdir+'authlink.tmp', 'w')
  keylink  = open(workdir+'keylink.tmp', 'w')
  years  = open(workdir+'years.clu', 'w')
  years.write("*vertices ??\n")
  journals  = open(workdir+'journals.tmp', 'w')
  journame  = open(workdir+'journame.tmp', 'w')
  jourinfo  = open(workdir+'jourinfo.tmp', 'w')
  mscs  = open(workdir+'mscs.tmp', 'w')
  msclink  = open(workdir+'msclink.tmp', 'w')

  vert = {}; nver = 0
  aut  = {}; naut = 0
  msc  = {}; nmsc = 0
  jour = {}; njr  = 0
  key  = {}; nkey = 0
  enddat = False; linecnt = 0
  aidef = False
#  for line in dat.readlines():
  while True:
    line = dat.readline()
    if not line: break
    linecnt += 1
    if (linecnt % 100000) == 0: print(linecnt) 
    control = str.lower(line[:2])
    content = str.strip(line[3:-1])
    if control =='an': iver = infVertex(content)
    elif control == 'ai':
      aidef = True
      ailist = content.split("; ")
    elif control == 'au':
      autlist = content.split("; ")
      if not aidef: ailist = ['-']*len(autlist)
      elif len(ailist) != len(autlist):
        dl = len(ailist) - len(autlist)
        print('lengths',iver,linecnt,len(ailist),len(autlist))
        if dl>0: ailist = ailist[:-dl]
      for (i,a) in enumerate(ailist):
        if a.strip()=='-': sa = standardName(removeTeX(autlist[i]))
        else: sa = a
        authlink.write(str(iver)+' '+str(infAuthor(sa))+'\n')
      aidef = False
    elif control == 'cc':
      msclist = content.split(" ")
      for cc in msclist:
        msclink.write(str(iver)+' '+str(infMSC(cc))+'\n')
    elif control == 'ut':
      if words==0: kwlist = removeTeX(content).split("; ")
      if words==1:
        s = re.split('\W+',removeTeX(content))
        kwlist = [w for w in s if (w not in stopwords) and (len(w)>1)]
        wlist = lemmatize(ML,kwlist,stopwords)
      for k in wlist:
        keylink.write(str(iver)+' '+str(infKeyword(k))+'\n')
    elif control == 'ti':
      if words==1:
        kwlist = re.split('\W+',removeTeX(content))
        kwlist = [w for w in kwlist if (w not in stopwords) and (len(w)>1)]
        wlist = lemmatize(ML,kwlist,stopwords)
        for k in wlist:
          keylink.write(str(iver)+' '+str(infKeyword(k))+'\n')
    elif control == 'se':
      journals.write(str(iver)+' '+str(infJournal(content))+'\n')
    elif control == 'py':
      years.write(content+'\n')
# for beseda in re.split(’\W+’,b[i:j].lower()):
  dat.close(); nodes.close(); jourinfo.close()
  journals.close(); journame.close(); authors.close()
  authlink.close(); years.close(); keys.close()
  keylink.close(); msclink.close(); mscs.close()

  print("years partition: "+workdir+'years.clu')
  makeNet('authors','WA','authors.tmp','authlink.tmp',naut)
  makeNet('keywords','WK','keywords.tmp','keylink.tmp',nkey)
  makeNet('MSCs','WM','mscs.tmp','msclink.tmp',nmsc)
  makeNet('journals','WJ','journame.tmp','journals.tmp',njr)

global comlin, version, copyR, wdir, t1
version = "ZB 0.1"
copyR = "by V. Batagelj, March 5, 2011 / December 27-30, 2010"
comlin = False
wdir = r'c:\users\Batagelj\data\ZB1'
sys.path.append(wdir) 
print("Module ZB imported.\n")
print("***", version, copyR+"\n")
MLdir = r'c:\Python32\Lib\site-packages\MontyLingua-2.1\Python'
sys.path.append(MLdir)
run(1)
t2 = datetime.datetime.now()
print("\nfinished: "+t2.ctime())
print("time used: ", t2-t1)
print(40*"*")

#- End -------------------------------------------------------------------------------

