
# https://github.com/keeferrourke/pyapa
# https://www.w3schools.com/python/python_regex.asp
# https://www.w3schools.com/python/python_strings_methods.asp
# razčlenitev referenc na sestavine AU, TI, SO, PY, VL, IS, BP, EP
# april 2022
# wdir = "C:/Users/markb/OneDrive/Vlado/handball"
wdir = "C:/Users/vlado/work2/mark/scopus"

import sys; sys.path.append(wdir)
import os; os.chdir(wdir) # delovno področje je trenutno področje 
import re

def ISIname(AU,PY,J9,VL,BP,AR):
# from work description produces its ISI name
  if "." in AU: AU=AU.replace('.',', ')
  name = AU.upper().replace(' ','').replace(',',' ')
  if PY != '': name = name+', '+PY
  if J9 != '': name = name+', '+J9  #[:20]
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
  print("--> ", name)
  return name

def sco2ISI(r):
  YEAR = r"(\b\d{4}|n\.d\.)"
  AUTHOR = r"\S+, (\S\.)+,"
  AU = ""; PY = ""; TI = ""; VL = ""; BP = ""
  J9 = ""; IS = ""; EP = ""; Er = ""  #; AR = ""
  stand = False
  la = list(re.finditer(AUTHOR,r))
  AUs = [ a.group()[:-1] for a in la ]
  if len(AUs)>0: AU = AUs[0]
  else:
    AU = "ANON"; AUs.append(AU)
  my = re.search(r"\("+YEAR+r"\)",r)
  if my is None: # nonstandard format
    iy = re.search(YEAR,r)
    if not(iy is None): PY = iy.group()
    i = la[-1].span()[1]+1
    k = r.find(", ,",i)
    TI = r[i:k]; q = r[k+4:] 
  else: # standard format
    PY = my.group()[1:-1]
    i = la[-1].span()[1]+1
    j = my.span()[0]
    if j>i: # AUs TI (PY)
      TI = r[i:j]; q = r[j+7:]
    else: # AUs(PY) TI, , 
      k = r.find(", ,",j+7)
      TI = r[j+7:k]; q = r[k+4:]
# for a in AUs: print(a)
  L = q.split(", ")
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
  if stand: q = ""
  return {"AUs": AUs, "PY": PY, "TI": TI, "J9": J9,
          "VL": VL, "IS": IS, "BP": BP, "EP": EP, "XY": q }

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

# wosfile = open("ScopusRefs.WoS", "w", encoding="utf-8")
works = set()

S = [""]*17
S[0] = "MacDougall, J.D., Ward, G.R., Sale, D.G., Biochemical adaptation of human skeletal muscle to heavy resistance training and immobilization (1977) J. Appl. Physiol., 43, pp. 700-703;" 
S[1] = "Mikkelsen, F., Olesen, M.N., (1976) Handbold 82–8884, , (Traening af skudstyrken). Stockholm: Trygg-Hansa;" 
S[2] = "Conover, W.J., (1980) Practical Nonparametric Statistics. 2nd Edn., , New York: John Wiley and Sons;"
S[3] = "LaPrade, R.F., Burnett, Q.M.I.I., Femoral intercondylar notch stenosis and correlation to anterior cruciate ligament injuries. A prospective study (1994) Am J Sports Med, 22, pp. 198-202. , discussion 203;" 
S[4] = "Sale, D.G., Neural adaptation to resistance training (1988) Med Sci Sports Exerc, 20, pp. S135-45;"
S[5] = "Tropp, H., (1985) Functional Instability of the Ankle Joint, , Thesis Linköping University Medical Dissertations (Abstract);" 
S[6] = "Trubestein, Brect, T.H., Ludwig, M., Willfallism, M., Muller, N., Fibrinolytic therapy with streptokinase and urokinase in deep vein thrombosis (1984) Haemostasis, 14, p. 80;"
S[7] = "Mikhelsen, F., Olsen, M.N., (1979) Etude Physiologique du Handball, , Stockholm: Thèse. Ed. Trygg Hansa;"
S[8] = "Cotelle, B., Baudier, F., Nutrition (1999), pp. 69-94. , 'Barometre sante jeunes 97/98 (CFES editions)' Vanves; Dickie, N.H., Bender, A., Breakfast and performance in school children (1982) Brit. J. Nutr., 48, pp. 483-495;"
S[9] = "Smith, A.P., Kendrick, A.M., Meals and performance (1992), pp. 1-23. , 'Handbook of Human Performance (A.P. Smith, D.M. Jones eds)'. Academic press, London;" 
S[10] = "Roy, J., Shephard habitual physical activity and academic performance (1996) Nutr. Rev., 54, pp. 32-36;" 
S[11] = "Testu, F., Variations journalieres et hebdomadaires des performances en milieu scolaire. Nature de la tache (1983), pp. 175-182. , 'Les rythmes de l'enfant et de l'adolescent: ces jeunes en mal de temps et d'espace (H. Montagner ed)'. Stock, Paris; Marcocchi, N., Musse, J.P., Kohler, F., Michaud, C., Michel, F., Schwertz, A., Drouin, P., Mejean, L., Une experience d'enquete nutritionnelle informatisee: 'PEDI' a la foire de NANCY (1987) Cah. Nut. Diet., 22, pp. 185-195;"
S[12] = "Mirbach, A., (1995) Schulsportunfälle an Allgemeinen Schulen in Westfalen-Lippe, , Gemeindeunfallversicherungsverband (GUVV) Westfalen-Lippe, LIT Verlag, Münster;"
S[13] = "Vogt, L., Bernhardt, M., Döring, K., Pfeifer, K., Banzer, W., Inline-Skating in der Schule - Verletzungsrisiken und Körperliche Aktivität, , Hänsel F, Pfeifer K, Woll A: Lifetime-Sport Inline-Skating. Schorndorf. Hofmann 1999;" 
S[14] = "Viru, A., Plasma hormones and physical exercise (1992) International Journal of Sports Medicine, 13 (3), pp. 201-209;"
S[15] = "Guillet, E., Sarrazin, P., (1999) Using survival analysis to determine the moments and the rates of dropout in sport: The example of the female handball, , Unpublished manuscript, University of Grenoble 1, France. (In French.);"
S[16] = "Sarrazin, P., Vallerand, R., Guillet, E., Pelletier, L., Cury, F., Motivation and dropout in female handballers: A 21-month prospective study Eur J Soc Psychol., , in press;"


for (c,t) in enumerate(S):
  T = t.rstrip(";").split(";")
  for ref in T:
    p = sco2ISI(ref)
    isi = ISIname(p["AUs"][0],p["PY"],p["J9"],p["VL"],p["BP"],"")
    short = nameG(isi,"")
    if not(short in works):
      works.add(short)
    #  wosfile.write(WoSrec(p,short))
      print(c, "SN  = ", short)
      print("XY  = ",p["XY"])

# wosfile.close()



 
 

 
