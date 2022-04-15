wdir = "C:/Users/markb/OneDrive/Vlado/handball"
#wdir = "C:/Users/vlado/work2/mark/scopus"

import sys; sys.path.append(wdir)
import os; os.chdir(wdir)
import re, datetime

def ISIname(AU,PY,J9,VL,BP,AR):
# from work description produces its ISI name
#LEFKOVITCH LP, 1985, THEOR APPL GENET, V70, P585
  if "." in AU: AU=AU.replace('.',', ')
  name = AU.upper().replace(' ','').replace(',',' ')
  if PY != '': name = name+', '+PY
  if J9 != '': name = name+', '+J9  # [:20] # for Scopus data
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
  print(" --> ", name)
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

def sco2ISI(r):
  YEAR = r"(\b\d{4}|n\.d\.)"
  # AUTHOR = r"\S+, (\S\.)+,"
  # AUTHOR = r"\S+, \S+,"
  # AUTHOR = r"\S+, (\S(\.| | |\S)+,"
  AUTHOR = r"\S+, (\S+|\S+ \S+|\S+ \S+ \S+),"
  AU = ""; PY = ""; TI = ""; VL = ""; BP = ""
  J9 = ""; IS = ""; EP = ""; Er = ""  #; AR = ""
  stand = False
  my = re.search(r"\("+YEAR+r"\)",r)
  if my is None: # nonstandard PY format
    iy = re.search(YEAR,r)
    if not(iy is None): PY = iy.group()
    k = r.find(", ,")
    beg = r[:k]; end = r[k+3:]
    form = 0
  else: # standard format
    PY = my.group()[1:-1]
    j = my.span()[0]
    beg = r[:j]; end = r[j+7:]
    form = 1   
  la = list(re.finditer(AUTHOR,beg))
  n = len(la)
  if n > 1:
    for i in range(n-1):
      if la[i].span()[1]+1 != la[i+1].span()[0]: break
    n = i+1
  la = la[:n]
  AUs = [ a.group()[:-1] for a in la ]
  OK = True
  for a in AUs: OK = OK and (re.search("[a-z]",a.split(", ")[1]) is None)
  # if not OK: print("irregular name in:\n",beg)
  if len(AUs)>0: AU = AUs[0]
  else:
    AU = "ANON"; AUs.append(AU)
  if form == 0: # nonstandard format
    i = la[-1].span()[1]+1
    TI = beg[i:k] 
  else: # standard format
    if AU == "ANON": i = j = 1
    else:
      i = la[-1].span()[1]+1; j = my.span()[0]
    if j>i: # AUs TI (PY)
      TI = beg[i:j]
    else: # AUs(PY) TI, , 
      k = end.find(", ,")
      TI = r[:k]; end = end[k+4:]
# for a in AUs: print(a)
  L = end.split(", ")
  if len(L) > 0: J9 = L[0]
  if len(L) > 2:
    if ("pp." in L[2]) or ("p." in L[2]):
      ii = re.search(r"\(\S+\)",L[1])
      if ii is None: VL = L[1]
      else:
        VL = L[1][:ii.span()[0]].strip()
        IS = ii.group()[1:-1]
      pp = L[2][3:].strip().split("-")
      BP = pp[0]; stand = True
      if len(pp)>1: EP = pp[1]
    else: stand = False   
  if stand: end = ""
  return {"AUs": AUs, "PY": PY, "TI": TI, "J9": J9, "VL": VL, 
          "IS": IS, "BP": BP, "EP": EP, "XY": end, "OK": OK }

def WoSrec(p,short):
  wosR = "PT J\n"; cmd = "AU "
  wosR += "SN " + short + "\n"
  for a in p["AUs"]:
    wosR += cmd + a + "\n"
    cmd = "   "
  if p["TI"] != "": wosR += "TI " + p["TI"] + "\n"    
  if p["J9"] != "": wosR += "SO " + p["J9"] + "\n"    
  if p["PY"] != "": wosR += "PY " + p["PY"] + "\n"    
  if p["VL"] != "": wosR += "VL " + p["VL"] + "\n"    
  if p["IS"] != "": wosR += "IS " + p["IS"] + "\n"    
  if p["BP"] != "": wosR += "BP " + p["BP"] + "\n"    
  if p["EP"] != "": wosR += "EP " + p["EP"] + "\n"
  if p["XY"] != "": wosR += "XY " + p["XY"] + "\n"
  wosR += "ER \n \n"
  return wosR

def findnth(niz, podniz, n):
    parts= niz.split(podniz, n+1)
    if len(parts)<=n+1:
        return -1
    return len(niz)-len(parts[-1])-len(podniz)

wosfile = open("scopus.wos", "w", encoding="utf-8")
scopus = open("scopus_handball.txt", "r", encoding="latin-1")
scopWoS = open("ScopusRefs.WoS", "w", encoding="utf-8")
trace = open("trace.txt", "w", encoding="utf-8")

print("Scopus to Wos")
t1 = datetime.datetime.now()
print("started: ",t1.ctime(),"\n")

works = set()
ponovi = True
r = 0; np = 0
auprvi = True
keys = ""

while(ponovi): 
    line = scopus.readline()
    if not line:
        print(r," vrstic")
        break
    if r % 5000 == 0: a = sys.stdout.write("\n"+str(r)+" ")
    r += 1
    # if r > 1000: ponovi = False
    if r % 100 == 0: a = sys.stdout.write("."); sys.stdout.flush()
    s = line.strip("\n").split("  - ")
    if len(s)==2:
        ukaz = s[0]
        vre = s[1]
        refs=False
        if ukaz == "EF": ponovi = False
        elif ukaz == "TY":
        #preveri JOUR
            wosfile.write("PT J\n")
        elif ukaz == "TI": wosfile.write("TI "+vre+"\n")
        elif ukaz == "N1":
            if vre[:12]=='References: ':
                refs = True; cmd = "CR "
                T = vre[12:].rstrip(";").split(";")
                for ref in T:
                    if len(ref.strip()) == 0: continue
                    try:
                        p = sco2ISI(ref)
                    except:
                        trace.write("Problem in line "+str(r)+"\n"+ref+"\n")
                        np += 1; continue
                    if not p["OK"]:
                        np += 1
                        trace.write("irregular name in line "+str(r)+"\n")
                    isi = ISIname(p["AUs"][0],p["PY"],p["J9"],p["VL"],p["BP"],"")
                    short = nameG(isi,"")
                    if not(short in works):
                        works.add(short)
                        scopWoS.write(WoSrec(p,short))
                    wosfile.write(cmd+isi+"\n")
                    cmd = "   "
        elif ukaz == "T2": wosfile.write("SO "+vre+"\n")
        elif ukaz == "VL": wosfile.write("VL "+vre+"\n")
        elif ukaz == "IS": wosfile.write("IS "+vre+"\n")
        elif ukaz == "SP": wosfile.write("BP "+vre+"\n")
        elif ukaz == "EP": wosfile.write("EP "+vre+"\n")
        elif ukaz == "PY": wosfile.write("PY "+vre+"\n")
        elif ukaz == "KW":
            if keys == "": keys = vre #posebej obravnavamo začetek, ki nima podpičja
            else: keys += ";" + vre
        elif ukaz == "AU":
            if auprvi:
                wosfile.write("AU "+vre+"\n")
                auprvi = False
            else: wosfile.write("   "+vre+"\n")       
        #print(r, AU)
        elif ukaz == "ER":
            wosfile.write("DE "+keys.lower()+"\n")
            keys=""
            wosfile.write("ER\n")
            auprvi = True
    else:
        if refs:
            T = line.rstrip(";").split(";")
            for ref in T:
                if len(ref.strip()) == 0: continue
                try:
                    p = sco2ISI(ref)
                except:
                    trace.write("Problem in line "+str(r)+"\n"+ref+"\n")
                    np += 1; continue
                if not p["OK"]:
                    np += 1
                    trace.write("irregular name in line "+str(r)+"\n")
                isi = ISIname(p["AUs"][0],p["PY"],p["J9"],p["VL"],p["BP"],"")
                short = nameG(isi,"")
                if not(short in works):
                    works.add(short)
                    scopWoS.write(WoSrec(p,short))
                wosfile.write("   "+isi+"\n")
scopus.close(); wosfile.close(); scopWoS.close(); trace.close()
print("\nDone\n# of problems = ", np)
t2 = datetime.datetime.now()
print("ended: ",t2.ctime(),"\n")
