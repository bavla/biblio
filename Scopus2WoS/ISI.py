
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
 # if len(beg.strip())==0:   
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
  if not OK: print("irregular name in:\n",beg)
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
  return {"AUs": AUs, "PY": PY, "TI": TI, "J9": J9,
          "VL": VL, "IS": IS, "BP": BP, "EP": EP, "XY": end }

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

S = [""]*39
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

S[17] = "Graves, JE, Pollock, ML, Jones, AE, Colvin, AB, Leggett, SH., Specificity of limited range of motion variable resistance training (1989) Med Sci Sports Exerc, 21, pp. 84-89;"
S[18] = "Farthing, JP, Chilibeck, PD., The effects of eccentric and concentric training at different velocities on muscle hypertrophy (2003) Eur J Appl Physiol, 89, pp. 578-586;"
S[19] = "Ebben, WP, Simenz, C, Jensen, RL., Evaluation of plyometric intensity using electromyography (2008) J Strength Cond Res, 22, pp. 861-868;"
S[20] = "Jimenez-Olmedo, JM, Penichet-Tomas, A, Ortega Becerra, M, Pueo, B, Espina-Agullo, JJ., Relationships between anthropometric parameters and overarm throw in elite beach handball (2019) Hum Mov, 20 (2), pp. 16-24;"
S[21] = "Wagner, H, Finkenzeller, T, Wurth, S, von Duvillard, SP., Individual and team performance in team-handball: a review (2014) J Sports Sci Med, 13 (4), pp. 808-816;"
S[22] = "McNeill, M. C., Fry, J. M., Wright, S. C., Tan, W. K. C., Tan, K. S. S., Schempp, P. G., Â«In the Local ContextÂ»: Singaporean Challenges to Teaching Games on Practicum (2004) Sport, Education and Society, 9 (1), pp. 3-32. , https://doi.org/10.1080/1357332042000175791;"
S[23] = "Hermassi, S, Chelly, MS, Fathloun, M, Shephard, RJ., The effect of heavy â vs. Moderate load training on the development of strength, power, and throwing ball velocity in male handball players (2010) J Strength Cond Res, 24 (9), pp. 2408-2418;"
S[24] = "De Dreu, C. K. W., Weingart, L. R., Task versus relationship conflict, team performance, and team member satisfaction: A meta-analysis (2003) Journal of Applied Psychology, 88, pp. 741-749. , 6;"
S[25] = "MartÃ­nez-RodrÃ­guez, A, MartÃ­nez-Olcina, M, HernÃ¡ndez-GarcÃ­a, M, Rubio-Arias, J, SÃ¡nchez-SÃ¡nchez, J, SÃ¡nchez-SÃ¡ez, JA., Body composition characteristics of handball players: Systematic review (2020) Arch de Medicina del Deporte, 37, pp. 52-61;"
S[26] = "Visscher, CM, Lobbezoo, F, de Boer, W, van der Zaag, J, Naeije, M, Prevalence of cervical spinal pain in craniomandibular pain patients (2001) Eur J Oral Sci, 109, pp. 76-80;"
S[27] = "Hsieh, Y.-L., Yang, S.-A., Yang, C.-C., Chou, L.-W., Dry Needling at Myofascial Trigger Spots of Rabbit Skeletal Muscles Modulates the Biochemicals Associated with Pain, Inflammation, and Hypoxia (2012) Evid.-Based Complement. Altern. Med, 2012, pp. 1-12. , [CrossRef] [PubMed];"

S[28] = "DE FORNEL, M. (1993). Faire parler les objets. Raisons Pratiques, 4, 241-265;"
S[29] = "DEWEY,J. (1922). Human nature and conduct.Carbondale, Southern Illinois University Press;"
S[30] = "DODIER, N. (1993). Les arÃ¨nes des habiletÃ©s techniques. Raisons Pratiques, 4, 115-139;"
S[31] = "Development and Evaluation of a Sport-Specific Measurement Protocol (2015) J Sports Sci Med, 14, pp. 501-506;"
S[32] = "FLEURANCE, P. et F. WINNYKAMEN (1995). Effects of the degree of competence symmetry- assymmetry in the acquisition of a motor skill in a dyad, Journal of Human Movement Studies, 28, 255-273;"
S[33] = "American College of Sports Medicine, (2006) ACSM's Guidelines for Exercise Testing and Prescription, pp. 123-134. , 6th ed. Baltimore: Lippincot, Willians & Wilkins;"
S[34] = "American Dental Association. Bureau of Dental Health Education and Bureau of Economic Research and Statistics: Mouth protectors: 1962 and the future (1963) J Am Dent Assoc, 66, pp. 539-543;"
S[35] = "Declaration of Helsinki. Ethical principles for medical research involving human subjects (2009) Journal of the Indian Medical Association, 107 (6), pp. 403-405. , 59. WMA;"
S[36] = "Declaration of Helsinki: Ethical principles for medical research involving human subjects (2008) WMJ, 54, pp. 122-125;"
S[37] = "(2018) Inventory Survey of Membership 2018, , Accessed 14 Jan 2019;"
S[38] = "(2018) Juventus & Cristiano Ronaldo digital impact, , https://www.facebook.com/ResultSports/posts/2002596436471764, ResultSports. (August 10). [Facebook content];"

# regex emEditor  \u\. \(   ! match cases

for (c,t) in enumerate(S):
  T = t.rstrip(";").split(";")
  for ref in T:
    try:
      p = sco2ISI(ref)
    except:
      print(c,"*****\n",ref)
      continue
    for name in p["AUs"]: print("     ",name)
    isi = ISIname(p["AUs"][0],p["PY"],p["J9"],p["VL"],p["BP"],"")
    short = nameG(isi,"")
    if not(short in works):
      works.add(short)
    #  wosfile.write(WoSrec(p,short))
      print(c, "SN  = ", short)
      print("XY  = ",p["XY"])

# wosfile.close()


 
 

 
