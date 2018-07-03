import sys, os, string
wdir = r'c:\users\Batagelj\data\ZB1'; sys.path.append(wdir)
MLdir = r'c:\Python25\Lib\site-packages\MontyLingua-2.1\Python'
sys.path.append(MLdir)
import MontyLingua
ML = MontyLingua.MontyLingua()

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

def infLemma(name):
# determines the lemma's number
  global nlem, lemmas
  if name in lemmas:
    return lemmas[name]
  else:
    nlem += 1; lemmas[name] = nlem
    return nlem

resrc = os.path.join(wdir, "resources/")
stopwords = open(resrc+'StopWords.dat', 'r').read().lower().split()
stopwords = ['.',',',';','(',')','[',']','"','=','?','!',':','-','s','']+stopwords

test=["go", "went", "skies", "and", "algebraic", "of", "men"]
for w in test: print w,"->",lemmatize(ML,w,stopwords)

# ---------------------------------------------------------
def run():
  global nlem, lemmas

  dat = open(wdir+'\\nets\\WK.net','r')
  clu = open(wdir+'\\nets\\lemmas.clu','w')
  a=dat.readline()
  b=dat.readline()
  V = b.split(" ")
  clu.write(V[0]+' '+V[1]+'\n')
  m=eval(V[2])
  lemmas = {}; nlem = 0
  k=0
  while True:
    k += 1
    if k % 100000 == 0: print(k)
    c=dat.readline()
    if c[0]=="*": break
    if k>m:
      name =c.split(" ")[1][1:-2]
      lema =lemmatize(ML,name,stopwords)
      if len(lema)==0: group=0
      else: group=m+infLemma(lema[0])
    else: group=k
    clu.write(str(group)+'\n')
  dat.close(); clu.close()  
