<img src="https://github.com/bavla/biblio/blob/master/J5-4596/ARISLogoSlo.svg?sanitize=true" width=300pt>
<img src="https://github.com/bavla/biblio/blob/master/J5-4596/ARISLogoSlo.svg?sanitize=true" width=300pt>

# J5-4596 - Višjestopenjske bibliografske storitve

J5-4596 je projekt ARIS (od 1. 10. 2022 do 30. 09. 2025) usmerjen v razvoj višjestopenjskih bibliografskih storitev. Na njem sodelujejo
Univerza na Primorskem, Fakulteta za matematiko, naravoslovje in informacijske tehnologije, Inštitut za matematiko, fiziko in mehaniko in
Univerza v Ljubljani, Filozofska fakulteta.

## Povzetek iz prijave projekta

Bibliografske storitve, kot so Web of Science/Knowledge, Scopus, CiteSeer, Zentralblatt
Math, Google Scholar, COBISS in druge, nudijo podatke o znanstvenih delih (članki, knjige,
poročila, itd.). Posameznik jih običajno uporablja za iskanje del na izbrano tematiko,
ustanove pa jih uporabljajo za ovrednotenje in načrtovanje raziskovalnega dela.
Uporabljajo se tudi kot vir podatkov za bibliometrične in scientometrične raziskave. Ze te
namene se podatki na izbrano tematiko pogosto pretvorijo v zbirko sklopljenih bibliografskih
omrežij, ki povezujejo raznovrstne enote (dela, avtorje, urednike, revije, ključne besede,
ustanove, države, jezike, itd.).

Podatki, pridobljeni iz uveljavljenih bibliografskih storitev, se nanašajo predvsem na
recenzirana in že objavljena znanstvena dela in so običajno dobro strukturirani in
kakovostni. Zaradi postopkov recenziranja in objave takšni podatki odražajo "preverjeni rob
znanosti" z zaostankom 3 mesecev ali običajno veliko več. Na hitro razvijajočih se
raziskovalnih področjih (npr. umetna inteligenca, raziskave Covid 19, ...) so ti podatki že
"stare novice".

Primarni viri najnovejših rezultatov raziskav so preprinti. Obstaja več uveljavljenih javnih
arhivov predobjav (Arxiv, BioRxiv, ...). Velik izziv predstavlja že pridobitev (s “strganjem” po
spletu in razčlenjevanjem PDF-jev) in identificikacija istih enot (napredno razvrščanje) vseh
teh objav in zagotavljanje vsaj nekakšne osnovne standardizacije. Na srečo je to delo že
opravljeno in rezultati so dostopni prek Semantic Scholar Open Research Corpus-a (SSORC)
in njegovih prečiščenih izpeljank S2ORC in CORD-19, s spletišča Allen Institute of AI.
Bistven korak pri izgradnji bibliografskih omrežij je določitev enot (entity resolution)
(razrešitev sinonimnih / homonimnih imen/oznak enot). To vprašanje je zelo pomembno tudi
pri združevanju podatkov iz različnih virov. Visoka natančnost pri določanju enot je
predpogoj za izgradnjo visoko kakovostnih omrežij. Razvili bomo nove, zelo natančne
postopke določanja enot za posebne vrste enot, ki upoštevajo medsebojne odnose med
enotami. Izdelali bomo tudi programsko podporo za pretvorbo med različnimi zapisi
bibliografskih podatkov.

Ustvarjena bibliografska omrežja so pogosto velika (na tisoče ali tudi milijone enot). Za
njihovo analizo je potrebno razviti zelo učinkovite (podkvadratične) algoritme, ki običajno
temeljijo na dejstvu, da je večina velikih omrežij redka (število povezav je istega reda kot
število vozlišč).

Pomembno orodje pri analizi zbirk sklopljenih omrežij so izpeljana omrežja, ki jih dobimo s
prepletanjem normalizacije (deležni (fractional) pristop) in množenja usklajenih omrežij.
Pred kratkim smo razdelali teoretično ozadje deležnega pristopa in pokazali kako lahko
časovna omrežja, ki temeljijo na časovnih količinah, uporabimo v biblimetričnih analizah. V
projektu nameravamo raziskati nove možnosti, ki jih odpirata oba pristopa. Novorazvite
metode bomo uporabili pri analizi izbranih bibliografskih podatkovij.

Obdelana in prečiščena bibliografska omrežja bi lahko uporabili tudi za izgradnjo višjestopenjskih storitev za različne vrste uporabnikov. Poiskali bomo nekaj primerov tovrstnih storitev in izdelali zanje prototipne rešitve.
Glavni cilji projekta so torej:
  - Razvoj metod in algoritmov za kakovostno določitev bibliografskih enot na podlagi
analize bibliografskih omrežij.
  - Nadaljnji razvoj metodologij in algoritmov za analizo bibliografskih omrežij, ki temelji na
naših preteklih raziskavah (dvovrstna omrežja, množenje, deležni pristop, časovna
omrežja in časovne količine), motiviranimi s posebnimi vrstami analiz s poudarkom n a
tem, kako se znanost razvija v “v realnem času" in prepoznavanjem "vročih tem" (na
podlagi predobjav).
  - Razvoj odprtokodne knjižnice v programskem jeziku Julia za učinkovito obdelavo
bibliografskih podatkov in analizo omrežij.
  - Izvesti več prototipov bibliografskih analiz in razviti ustrezna orodja, katerih razvoj
izhaja iz potreb izbranih končnih uporabnikov (študentov, upravljalcev revij, urednikov,
znanstvenikov na določenih področjih itd.)

[Podrobni opis projekta v angleščini](http://vladowiki.fmf.uni-lj.si/lib/exe/fetch.php?media=vlado:proj:j5-4596:docs:vsebina_projekta_eng.pdf)
