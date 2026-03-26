# Opisi


Projektna spletna stran [https://github.com/bavla/biblio/blob/master/J5-4596/README.md](https://github.com/bavla/biblio/blob/master/J5-4596/README.md)

[Obrazec](https://digitalforms.arrs.si/forms/group-list/rep?PageNumber=0&PageSize=25&SortDirection=0&FormStatus=99&ShowEnded=False&EntityType=99999&RO=2790&FormSignature=2&SearchSelectedGroup=)


Napišite kratko vsebinsko poročilo, kjer boste predstavili raziskovalno hipotezo, opis raziskovanja, ugotovljene rezultate, uporabo rezultatov in sodelovanje s tujimi partnerji (mednarodno sodelovanje). Poročilo naj sledi v predlogu projekta zastavljenim ciljem (oz. nalogam), kjer o vsakem cilju poročate v ločenem razdelku. Razdelek naj se prične z oznako cilja, kot ste jo uporabili v predlogu, in eno-stavčnim opisom cilja. Sledijo naj eden do trije odstavki opisa rezultatov, kjer se pri vseh rezultatih skličete na reference (npr. [1] ali [1, 2]). Po odstavkih z opisom rezultatov za posamezen cilj v alinejah navedite reference za ta cilj (članki, referati, vabljena predavanja, patenti, ipd.). Alineje naj se pričnejo z ustrezno številko (npr. [1]). Rezultatov brez ustreznih referenc pri opisu rezultatov cilja ne navajajte. Če je le možno, navedbo posamezne reference zaključite z ustrezno šifro COBISS. Pri člankih je navedba šifre COBISS obvezna, navedite pa samo članke, kjer ste navedli podatke o sofinancerju (ARRS/ARIS) ali sofinancerjih ter številko ARIS projekta/programa, za katerega pišete poročilo. Celotni razdelek naj vsebuje največ 12.000 znakov, vključno s presledki (velikost pisave 11).

## WP1. Vodenje projekta, sodelovanje in objave

### T1.1 – Sodelovanje.
O delu na projektu smo poročali in se dogovarjali na [Sredinem seminarju](https://www.fmf.uni-lj.si/sl/obvestila/agregator/152/seminar-sreda/). Naslednji seminarji se ukvarjajo s temami projekta J5-4596

  * 2022: 1327, 1329, 1331, 1332;
  * 2023: 1333, 1336, 1337, 1338, 1339, 1340, 1341;
  * 2024: 1343, 1344, 1345, 1346, 1348, 1351, 1352, 1353, 1354, 1355, 1356, 1357;
  * 2025: 1358, 1359, 1363,	1365, 1366, 1367, 1369, 1371, 1375;
  * 2026: 1377, 1379.


### T1.2 – Poročanje. 
Letna poročila (SRA/ARRS). Finančna poročila in nadzor so opravljale ustrezne službe partnerjev projekta.


### T1.3 – Objave. 
Pridobljeni rezultati so bili predstavljeni na mednarodnih znanstvenih konferencah in objavljeni v znanstvenih revijah in zbornikih konferenc. Razvita programska oprema, njena dokumentacija in primeri podatkov so na voljo na GitHubu kot odprtokodni viri. Posamezni rezultati so bili vključeni tudi v predavanja na univerzi.

## WP2. Identifikacija višjenivojskih storitev

Za preprostejša vprašanja (kje objaviti članek, pomembna dela ali avtorji na izbrano temo, izbira ustreznih recenzentov, ocenjevanje recenzentov, predlaganje ključnih besed, možni partnerji za raziskovalno sodelovanje, itd.) dobimo pogosto zadovoljive odgovore z uporabo orodij UI. Zato smo pozornost preusmerili na zahtevnejše analize podatkov iz bibliografskih podatkovnih baz:

  * soavtorstva med evropskimi državami skozi čas
  * analiza člankov objavljenih v izbrani reviji
  * analiza značilnosti novih univerz
  * analiza izmenjav Erasmus

Izvedbe teh storitev in dobljeni rezultati na izbranih omrežjih bodo opisani v naslednjih razdelkih.

## WP3. Razvoj podpore za pridobivanje omrežij iz OpenAlexa
Kot je bilo razloženo v Spremembah smo prvotni cilj "Metode in orodja za identifikacijo enot (določanje entitet)" zamenjali s podporo uporabe baze OpenAlex. 

V R-ju smo razvili knjižnico OpeAlex2Pajek [1]. Opisana je bila v članku [2] in predstavljena na srečanjih []. In uporabljena za pridobivanje omrežij v člankih [] [] [] [].

[1] OpeAlex2Pajek: https://github.com/bavla/OpenAlex/tree/main/OpenAlex2Pajek

[2] Batagelj, Vladimir. "OpenAlex2Pajek--an R Package for converting OpenAlex bibliographic data into Pajek networks." COLLNET 2024, Strasbourg, December 12-14. In Jain, Praveen Kumar (ed.), et al. Innovations in webometrics, informetrics, and scientometrics: AI-driven approaches and insights. Delhi: Bookwell, cop. (2025): 66--77. ISBN 978-93-86578-65-5. arXiv preprint arXiv:2501.06656. [COBISS.SI-ID 220027395]

[3] BATAGELJ, Vladimir. OpenAlex2Pajek: an R-library for creating bibliometric networks. V: Applied Statistics 2024 : international conference : program and abstracts : September 23-25, 2024, Koper, Slovenia. [Ljubljana]: [Statistical Society of Slovenija], 2024. Str. 19. https://as.mf.uni-lj.si/uploads/pdf/as2024book.pdf. [COBISS.SI-ID 272600835]


## WP4. Teoretične raziskave v analizi bibliografskih omrežij

Pomembno orodje pri analizi zbirk sklopljenih omrežij (bibliografska omrežja so poseben primer) je množenje omrežij (Batagelj in Cerinšek, 2013 [COBISS-ID: 16739929]), ki nam omogoča izračun izpeljanih omrežij. Da bi pri analizi bibliografskih omrežij enakovredno upoštevali vsako enoto, se uporablja deležni (fractional) pristop. Njegovo teoretično ozadje je bilo predlagano v našem članku (Batagelj, 2020 [COBISS-ID: 18940505]). V člankih Batagelj in Praprotnik (2016 [COBISS-ID: 525752089]) ter Batagelj in Maltseva (2020 [COBISS-ID: 18898009]) smo predlagali longitudinalni pristop k analizi časovnih omrežij in pokazali, kako ga je mogoče uporabiti pri analizi časovnih bibliografskih omrežij. 

### T4.1 – New derived networks based on normalization and multiplication; extension to weighted networks



[1] Batagelj, Vladimir. "On weighted two-mode network projections." Scientometrics 129, no. 6 (2024): 3565-3571. [COBISS.SI-ID 216955651]

[2] Batagelj, Vladimir. "Weighted degrees and truncated derived bibliographic networks." Scientometrics 129, no. 8 (2024): 4863-4883.  [COBISS.SI-ID 216973315]

[3] Batagelj, Vladimir. "Cores in multiway networks." Social Network Analysis and Mining 14, no. 1 (2024): 122. [COBISS.SI-ID 217014531]

[4] Matveeva, Nataliya, Vladimir Batagelj, "Structures of Authors’ Collaboration at Young Universities". In Shushanik Sargsyan, Wolfgang Glänzel, Giovanni Abramo (eds.): Proceedings of 20th International Conference on Scientometrics & Informetrics - ISSI 2025, 23–27 June 2025, Yerevan, Armenia. Volume II (2025): 1630-1653. [COBISS.SI-ID 272423427]

[5] BATAGELJ, Vladimir. Weighted degrees and truncated derived networks. V: HiTEc meeting & workshop on complex data in econometrics and statistics (HiTEc & CoDES 2024) : programme and abstracts : Cyprus University of Technology, Limassol, Cyprus, 23-24 March 2024. [S. l.: CMStatistics], 2024. Str. 9. https://www.cmstatistics.org/hiteccodes2024/docs/HITECCODES2024_BoA.pdf?20240305222439. [COBISS.SI-ID 272593667]
      
[6] BATAGELJ, Vladimir. Truncated two-mode network projections. V: Sunbelt Conference 2024 : 24-30 June 2024. Edinburgh: Heriot-Watt University. https://sunbelt2024.com/event-schedule/. [COBISS.SI-ID 272656643]

[7] BATAGELJ, Vladimir. Analiza večsmernih omrežij. V: LIČEN, Mina (ur.), KASTRIN, Andrej (ur.). NetSlo ’25 : IX. srečanje raziskovalcev s področja analize omrežij : zbornik povzetkov prispevkov : Ljubljana, 23. januar 2025. Ljubljana: Statistično društvo Slovenije, 2025. Str. 9-10. ISBN 978-961-94283-7-5. https://netslo.mf.uni-lj.si/netslo25zbornik.pdf. [COBISS.SI-ID 272561155]

[8] BATAGELJ, Vladimir. On the structure of the network of European airports and airlines. V: HiTEc meeting & workshop on complex data in econometrics and statistics, Limassol, Cyprus, 3-4 April 2023. [Brussels: COST], 2023. 1 spletni vir. http://www.cmstatistics.org/hiteccodes/fullprogramme.php. [COBISS.SI-ID 272689923]


### T4.2 – Časovne različice izpeljanih omrežij

Časovna bibliografska omrežja se običajno ukvarjajo z leti. V projektu smo razvili metode časovne analize, ki uporabljajo časovno omrežje razslojeno na časovne rezine.
Običajno so časovne rezine precej zapletena utežena omrežja. Ta poenostavimo tako, da jih nadomestimo s pripadajočimi skeleti izbrane vrste. V skeletu ohranimo le (glede na vprašanje) pomembne sestavine (vozlišča/povezave). Primeri skeletov so: vpeta drevesa, vozliščni/povezavni izrezi, k-naj povezave do sosedov, (posplošene) sredice, otoki, itd.

   1. BATAGELJ, Vladimir. Longitudinal approach to the analysis of temporal networks based on temporal quantities. V: Workshop Innovation in dynamic network modelling : Lugano, September 11-13, 2024. Lugano: Università della Svizzera Italiana, Institute of Computing; Torun: Bernoulli Society for Mathematical Statistics and Probability. 2024, 1 spletni vir. https://www.ci.inf.usi.ch/innodyn/. [COBISS.SI-ID 272640515]

ARS
COMPSTAT

### T4.3 – New temporal quantities describing temporal bibliographic networks

Razvili smo tudi metode za analizo trajektorij. 

Uporabili smo jih za analizo podobnosti slovenskih politikov Oštro.  [COBISS.SI-ID 186331907] [COBISS.SI-ID 202923011]

### T4.4 – Clustering in temporal networks

[COBISS.SI-ID 197238275] [COBISS.SI-ID 182243075] konference


Ogrodje omrežja je graf. Sodelovali smo pri nekaj člankih iz teorije grafov

[1] POŽAR, Rok, MARTIN, Tim, GIORDANI, Bruno, KAVCIC, Voyko. Enhanced functional brain network integration in mild cognitive impairment during cognitive task performance : a compensatory mechanism or a result of neural disinhibition?. The European journal of neuroscience. 2024, vol. 60, iss. 7, str. 5569-5580,  DOI: 10.1111/ejn.16511. [COBISS.SI-ID 205199107]

[2] POŽAR, Rok. Fast computation of the centralizer of a permutation group in the symmetric group. Journal of symbolic computation. jul./avg. 2024, vol. 123, art. 102287, str. 1-14.  DOI: 10.1016/j.jsc.2023.102287. [COBISS.SI-ID 181181699]

[3] ZUGAN, Dani, POŽAR, Rok, BRODNIK, Andrej. Floyd–Warshall algorithm for sparse graphs. Algorithms. Dec. 2015, vol. 18, iss. 12, [article no.] 766, str. 1-13, DOI: 10.3390/a18120766. [COBISS.SI-ID 262471683]

[4] POŽAR, Rok, MARTIN, Tim, KERLIN, Mary Katherine, MCCOLLIGAN, Aidan, GIORDANI, Bruno, KAVCIC, Voyko. Baseline resting-state network integration modulates task performance and aftereffect. Sensors. Jan.-1 2026, vol. 26, iss. 1, [article no.] 41, str. 1-12, DOI: 10.3390/s26010041. [COBISS.SI-ID 266590979]

[5] MALNIČ, Aleksander, POŽAR, Rok. On reduced Hamilton walks. Applied mathematics and computation. [Print ed.]. 1 Feb. 2026, vol. 510, art. 129695, str. 1-11,  DOI: 10.1016/j.amc.2025.129695. [COBISS.SI-ID 248238083]

[6] HILAIRE, Claire, KRNC, Matjaž, MILANIČ, Martin, RAYMOND, Jean-Florent. Linear colorings of graphs. European journal of combinatorics. May 2026, vol. 135, [article no.] 104374, str. 1-22.  DOI: 10.1016/j.ejc.2026.104374. [COBISS.SI-ID 272926979]

[7] GURVICH, Vladimir, KRNC, Matjaž, MILANIČ, Martin, VYALYI, Mikhail N. Avoidability beyond paths. The Electronic journal of combinatorics. [Online ed.]. 2025, vol. 32, iss. 2, article no. p2.27, str. 1-39 DOI: 10.37236/13023. [COBISS.SI-ID 237137667]

[8] GURVICH, Vladimir, KRNC, Matjaž, VYALYI, Mikhail N. Growing trees and amoebas’ replications. Results in mathematics. 2025, vol. 80, article no. 117, str. 1-17, DOI: 10.1007/s00025-025-02421-6. [COBISS.SI-ID 237096963]

[9] GOTTLIEB, Eric, KRNC, Matjaž, MURŠIČ, Peter. Sprague–Grundy values and complexity for LCTR. Discrete applied mathematics. [Print ed.]. mar. 2024, vol. 346, str. 154-169, DOI: 10.1016/j.dam.2023.11.036. [COBISS.SI-ID 178885891]

[10] CHIARELLI, Nina, KRNC, Matjaž, MILANIČ, Martin, PFERSCHY, Ulrich, SCHAUER, Joachim. Fair allocation algorithms for indivisible items under structured conflict constraints. Computational & Applied Mathematics. Oct. 2023, vol. 42, iss. 7, [article no.] 302, 21 str. DOI: 10.1007/s40314-023-02437-0. [COBISS.SI-ID 164733443]

[11] CHIARELLI, Nina, KRNC, Matjaž, MILANIČ, Martin, PFERSCHY, Ulrich, PIVAČ, Nevena, SCHAUER, Joachim. Fair allocation of indivisible items with conflict graphs. Algorithmica. May 2023, vol. 85, iss. 5, str. 1459-1489.  DOI: 10.1007/s00453-022-01079-8. [COBISS.SI-ID 134381827]

[12] Bašić, Nino, Gévay, Gábor, Pisanski, Tomaž. The Möbius–Kantor graph is a faithful unit-distance graph. The art of discrete and applied mathematics. 2025, vol. , no. , str. 1-6 [COBISS.SI-ID 258543107]

[13] Berman, Leah, Gévay, Gábor, Pisanski, Tomaž. Polycyclic geometric realizations of the Gray configuration. The Australasian journal of combinatorics. 2025, vol. 93, pt. 1, str. 171-197 [COBISS.SI-ID 250814979]

[14] Bonvicini, Simona, Pisanski, Tomaž, Žitnik, Arjana. All generalized rose window graphs are hamiltonian. Graphs and combinatorics. Apr. 2026, vol. 42, iss. 2, [article no.] 27, 20 str. [COBISS.SI-ID 269644547]

[15] Bašić, Nino, Damnjanović, Ivan, Fowler, Patrick W. On the degrees of regular nut graphs and Cayley nut graphs. Ars mathematica contemporanea.  2026, vol. , no. , [article no.], str. 1-15, [COBISS.SI-ID 264594691]

[16] Bašić, Nino, Fowler, Patrick W., Mccarthy, Maxine M., Potočnik, Primož. Nut digraphs. Discrete applied mathematics. 2026, vol. 383, str. 203-226  [COBISS.SI-ID 264177411]

[17] Bašić, Nino, Damnjanović, Ivan. Nut graphs with a prescribed number of vertex and edge orbits. Journal of algebraic combinatorics. Jan. 2026, vol. 63, iss. 1, article no. 9, str. 1-12 [COBISS.SI-ID 264172035]

  1. Pisanski, Tomaž. Zakaj elektronska knjiga?. V: Mulec, Janez. Življenjska pot matematika Iva Laha. Brezplačna elektronska izd. Koper: Založba Univerze na Primorskem, 2026. Str. 1-3. [COBISS.SI-ID 252742659].

## WP5. Razvoj novih metod za analizo bibliografskih omrežij v R-ju

Spočetka smo nameravali analizo bibliografskih omrežij podpreti v programskem jeziku Julia, a smo po ponovnem premisleku spoznali, da je ustreznejši programski jezik R.


### T5.1 – Implementacija in optimizacija osnovnih podatkovnih struktur in algoritmov iz Nets in TQ

[TQ](https://github.com/bavla/TQ)
[netsWeight](https://github.com/bavla/Nets/tree/master/netsWeight) 

### T5.2 – Implementacija algoritmov iz WP4.

Advanced algorithms will be implemented based on methods developed in WP4.

Salton, Balassa normalization, neighbors

### T5.3 – Prikazi

Visualization 3-way

Balassa


### T5.4 – Testiranje, optimizacija in dokumentiranje knjižnic.


## WP6. Uporabe

nekatere primere prepustimo UI.


### T6.1 – Bibliometrična analiza izbranih raziskovalnih področjih z uporabo novo razvitih metod
### T6.2 – Uporabe za urednike revij
### T6.3 – Uporabe za avtorje, raziskovalce in študente

  * soavtorstva med evropskimi državami skozi čas  [COBISS.SI-ID 260663299]
  * analiza člankov objavljenih v izbrani reviji  [COBISS.SI-ID 272388867]
  * analiza značilnosti novih univerz  [COBISS.SI-ID 272423427]
  * analiza izmenjav Erasmus [ArXiv ]



Social networks [COBISS.SI-ID 217252611], Handball

Smo člani (program Pajek) združenja Network Analysis Software Collective (NASCol) https://www.nascol.net/ . Sodelujemo pri pripravi “Guidelines for Reporting About Network Data” (GRAND) https://grand-statement.org/.
Sodelujemo pri projektu COST HiTeC https://www.hitecaction.org/ .

