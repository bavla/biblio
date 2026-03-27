<img src="https://github.com/bavla/biblio/blob/master/J5-4596/ARISLogoSlo.svg?sanitize=true" width=300pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/space.svg?sanitize=true" width=100pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/UP-famnit.png" width=150pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/space.svg?sanitize=true" width=50pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/imfm.svg?sanitize=true" width=120pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/space.svg?sanitize=true" width=50pt> <img src="https://github.com/bavla/biblio/blob/master/J5-4596/UL-FF.svg?sanitize=true" width=120pt>

# J5-4596 - Višjestopenjske bibliografske storitve

J5-4596 je projekt ARIS (od 1. 10. 2022 do 30. 09. 2025) usmerjen v razvoj višjestopenjskih bibliografskih storitev. Na njem sodelujejo
Univerza na Primorskem, Fakulteta za matematiko, naravoslovje in informacijske tehnologije, Inštitut za matematiko, fiziko in mehaniko in
Univerza v Ljubljani, Filozofska fakulteta. [Sodelavci](team.md)

## Povzetek iz prijave projekta

Bibliografske storitve, kot so Web of Science/Knowledge, Scopus, CiteSeer, Zentralblatt
Math, Google Scholar, COBISS in druge, nudijo podatke o znanstvenih delih (članki, knjige,
poročila, itd.). Posameznik jih običajno uporablja za iskanje del na izbrano tematiko,
ustanove pa jih uporabljajo za ovrednotenje in načrtovanje raziskovalnega dela.
Uporabljajo se tudi kot vir podatkov za bibliometrične in scientometrične raziskave. Za te
namene se podatki na izbrano tematiko pogosto pretvorijo v zbirko sklopljenih bibliografskih
omrežij, ki povezujejo raznovrstne enote (dela, avtorje, urednike, revije, ključne besede,
ustanove, države, jezike, itd.).

Podatki, pridobljeni iz uveljavljenih bibliografskih storitev, se nanašajo predvsem na
recenzirana in že objavljena znanstvena dela in so običajno dobro strukturirani in
kakovostni. Zaradi postopkov recenziranja in objave takšni podatki odražajo "preverjeni rob
znanosti" z zaostankom 3 mesecev ali običajno veliko več. Na hitro razvijajočih se
raziskovalnih področjih (npr. umetna inteligenca, raziskave Covid 19, ...) so ti podatki že
"stare novice".

Primarni viri najnovejših rezultatov raziskav so preprinti. Obstaja več uveljavljenih javnih arhivov predobjav (Arxiv, BioRxiv, ...). Velik izziv predstavlja že pridobitev (s “strganjem” po spletu in razčlenjevanjem PDF-jev) in identificikacija istih enot (napredno razvrščanje) vseh teh objav in zagotavljanje vsaj nekakšne osnovne standardizacije. Na srečo je to delo že opravljeno in rezultati so dostopni prek Semantic Scholar Open Research Corpus-a (SSORC) in njegovih prečiščenih izpeljank S2ORC in CORD-19, s spletišča Allen Institute of AI. Bistven korak pri izgradnji bibliografskih omrežij je določitev enot (entity resolution) (razrešitev sinonimnih / homonimnih imen/oznak enot). To vprašanje je zelo pomembno tudi pri združevanju podatkov iz različnih virov. Visoka natančnost pri določanju enot je predpogoj za izgradnjo visoko kakovostnih omrežij. Razvili bomo nove, zelo natančne postopke določanja enot za posebne vrste enot, ki upoštevajo medsebojne odnose med enotami. Izdelali bomo tudi programsko podporo za pretvorbo med različnimi zapisi bibliografskih podatkov.

Ustvarjena bibliografska omrežja so pogosto velika (na tisoče ali tudi milijone enot). Za njihovo analizo je potrebno razviti zelo učinkovite (podkvadratične) algoritme, ki običajno temeljijo na dejstvu, da je večina velikih omrežij redka (število povezav je istega reda kot število vozlišč).

Pomembno orodje pri analizi zbirk sklopljenih omrežij so izpeljana omrežja, ki jih dobimo s prepletanjem normalizacije (deležni (fractional) pristop) in množenja usklajenih omrežij. Pred kratkim smo razdelali teoretično ozadje deležnega pristopa in pokazali kako lahko časovna omrežja, ki temeljijo na časovnih količinah, uporabimo v biblimetričnih analizah. V projektu nameravamo raziskati nove možnosti, ki jih odpirata oba pristopa. Novorazvite metode bomo uporabili pri analizi izbranih bibliografskih podatkovij.

Obdelana in prečiščena bibliografska omrežja bi lahko uporabili tudi za izgradnjo višjestopenjskih storitev za različne vrste uporabnikov. Poiskali bomo nekaj primerov tovrstnih storitev in izdelali zanje prototipne rešitve. Glavni cilji projekta so torej:
  - Razvoj metod in algoritmov za kakovostno določitev bibliografskih enot na podlagi analize bibliografskih omrežij.
  - Nadaljnji razvoj metodologij in algoritmov za analizo bibliografskih omrežij, ki temelji na naših preteklih raziskavah (dvovrstna omrežja, množenje, deležni pristop, časovna omrežja in časovne količine), motiviranimi s posebnimi vrstami analiz s poudarkom na tem, kako se znanost razvija v “v realnem času" in prepoznavanjem "vročih tem" (na podlagi predobjav).
  - Razvoj odprtokodne knjižnice v programskem jeziku Julia za učinkovito obdelavo bibliografskih podatkov in analizo omrežij.
  - Izvesti več prototipov bibliografskih analiz in razviti ustrezna orodja, katerih razvoj izhaja iz potreb izbranih končnih uporabnikov (študentov, upravljalcev revij, urednikov, znanstvenikov na določenih področjih itd.)

[Podrobni opis projekta v angleščini](http://vladowiki.fmf.uni-lj.si/lib/exe/fetch.php?media=vlado:proj:j5-4596:docs:vsebina_projekta_eng.pdf)

## Spremembe

Ob začetku izvajanja projekta je prišlo do dveh pomembnih dogodkov:
- uveljavljati so se začela orodja umetne inteligence (ChatGPT, Claude, DeepSeek, itd.), ki jih lahko tudi uporabimo za iskanje odgovorov na nekatera bibliometrična vprašanja
- delovati je začela odprta in prosto dostopna bibliografska podatkovna baza OpenAlex, ki je vnesla nove razsežnosti v dostopnost bibliografskih podatkov.

Prvi cilj projekta (metode in algoritmi za kakovostno določitev bibliografskih enot) orodja umetne inteligence zelo dobro razrešujejo. Uporablja jih tudi OpenAlex. Še več, za razliko od drugih bibliografskih podatkovnih baz (Web of Science, Scopus, itd.) imajo v OpenAlexu vse bibliografske enote (dela, avtorji, ) identifikatorje, ki so javno dostopni. To bistveno olajša pripravo podatkov za analize. To, da je za identifikacijo poskrbljeno že v podatkovni bazi, je pravi pristop. Ker identifikacija ni vselej pravilna, je v delovanje baze potrebno vgraditi mehanizem za sodelovanje uporabnikov in odpravljanje odkritih napak. Zato smo prizadevanja usmerili v podporo uporabe bibliografske baze OpenAlex pri pridobivanju podatkov za analize.

Pred tem smo kot vir podatkov v glavnem uporabljali tržno bibliografsko bazo Web of Science iz katere smo s pythonskim programom WoS2Pajek ustvarili ustrezna omrežja. Tržna narava baze postavlja omejitve na količino pridobljenih podatkov in na dostopnost ustvarjenih omrežij za druge raziskovalce. Razvili smo tudi programe za pridobivanje omrežij iz baz Scopus in ZBMath ter BibTeXovskih bibliografij. 
 
Standardna shema analize je bila: (1) pridobi datoteko izbranih podatkov (iz izbrane bibliografske baze) (2) predelaj in prečisti podatke v ustrezna omrežja (3) analiziraj omrežja z uporabo programa Pajek in statističnih orodij. Naslonitev na OpenAlex omogoča združitev korakov (1) in (2). Korak (3) zahteva "programiranje" - izvedbo vprašanju ustreznih postopkov. 

V predlogu projekta smo nameravali programsko podporo izvesti v programskem jeziku Julija, ki ustvarja hitrejšo prevedeno kodo. Po ponovnem premisleku se je izkazal za ustreznejši programski jezik R, ki je ustvarjen za podporo analize podatkov (statistike). Prednosti R-ja so izredno bogata zbirka knjižnic za najrazličneje probleme analize podatkov in veliko večja skupnost uporabnikov, ki ga dobro obvlada - je programski jezik privzet na podiplomskem študiju statistike. To omogoči tudi združiti vso analizo pod isto streho. Za predelavo izbranih bibliografskih podatkov iz OpenAlexa v pripadajoča omrežja smo razvili knjižnico OpenAlex2Pajek. Za izognitev preklapljanju med Pajkom in R-jem pa smo začeli z razvojem ustreznih Pajkovskih funkcij v R-ju zbranih v knjižnici netsWeight. S tem bo v R-ju ustvarjeno enovito okolje v katerem bodo lahko uporabniki samostojno razvijali višje bibliografske storitve.
 
## Rezultati

Bibliografski podatki zbrani v bibliografskih bazah omogočajo odgovore na veliko več vprašanj kot pa jih ponujajo vmesniki do storitev teh baz. Osnovni cilj projekta je omogočiti izvedbo analiz, ki omogočajo dobiti te odgovore - višjestopenjske bibliografske storitve.

Pred začetkom projekta smo kot vir podatkov v glavnem uporabljali tržno bibliografsko bazo Web of Science, iz katere smo s pythonskim programom WoS2Pajek ustvarili ustrezna omrežja. V projektu smo se usmerili na razvoj metod za analizo bibliografskih omrežij in izgradnjo programske podpore za pridobivanje omrežij iz baze OpenAlex in analizo bibliografskih omrežij. Pri programiranju le-te smo se odločili za programski jezik R, ki je ustvarjen za podporo analize podatkov (statistike) in ga obvlada večje število uporabnikov. To omogoči tudi združiti vso analizo pod isto streho. Za predelavo izbranih bibliografskih podatkov iz OpenAlexa v pripadajoča omrežja smo razvili knjižnico OpenAlex2Pajek. Za izognitev preklapljanju med Pajkom in R-jem pa smo začeli z razvojem ustreznih Pajkovskih funkcij v R-ju zbranih v knjižnici netsWeight. Obe knjižnici sestavljata enovito okolje, v katerem bodo lahko uporabniki samostojno razvijali višje bibliografske storitve.

Izpeljana omrežja so utežena. V teoretičnem delu projekta smo nadaljevali z razvojem postopkov, ki temeljijo na izpeljanih omrežjih, in razdelali vprašanje neupoštevanja povezav z zelo majhno utežjo. Za vpogled v utežena omrežja jih poenostavimo tako, da jih oklestimo - nadomestimo s pripadajočimi skeleti izbrane vrste. Razvili smo metode časovne analize, ki uporabljajo časovno omrežje razslojeno na časovne rezine - stanja omrežja v izbranih časovnih intervalih. Posamezno rezino analiziramo z metodami analize uteženih omrežij in dobljene rezultate združimo v časovno zaporedje. Pri razumevanju in tolmačenju rezultatov so nam v veliko pomoč ustrezni slikovni prikazi. Za posebej uporabna sta se izkazala pristop 1-sosedov in pri manjših omrežjih (npr. države sveta) Balasseva normalizacija uteži.

Dodatno smo razvili tudi postopke za analizo enot, ki temeljijo na opisih enot s trajektorijami - zaporedji dogodkov. Pojem omrežja smo posplošili na večsmerna omrežja. Za opis omrežij z lastnostmi opisanimi s strukturiranimi vrednostmi smo predlagali obliko zapisa netsJSON, ki jo vgrajujemo v naše programske rešitve.

Rezultati bibliografskih analiz se uporabljajo tudi pri vrednotenjih dela posameznikov, skupin in ustanov. Pri tem se pogosto začuti delovanje Goodhartovega zakona - Ko mera postane cilj, preneha biti dobra mera. Razmišljali smo o njegovi vlogi v odprti znanosti.

Razvite metode in knjižnici smo preizkusili z analizami bibliografskih omrežij na izbrane teme.

Razvita programska oprema, njena dokumentacija in primeri podatkov so na voljo na GitHubu kot odprtokodni viri.

[Objave](pub.md), [Predstavitve](meet.md) in [Opisi](opisi.md)
