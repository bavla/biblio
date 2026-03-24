# Opisi


Projektna spletna stran [https://github.com/bavla/biblio/blob/master/J5-4596/README.md](https://github.com/bavla/biblio/blob/master/J5-4596/README.md)

[Obrazec](https://digitalforms.arrs.si/forms/group-list/rep?PageNumber=0&PageSize=25&SortDirection=0&FormStatus=99&ShowEnded=False&EntityType=99999&RO=2790&FormSignature=2&SearchSelectedGroup=)


Napišite kratko vsebinsko poročilo, kjer boste predstavili raziskovalno hipotezo, opis raziskovanja, ugotovljene rezultate, uporabo rezultatov in sodelovanje s tujimi partnerji (mednarodno sodelovanje). Poročilo naj sledi v predlogu projekta zastavljenim ciljem (oz. nalogam), kjer o vsakem cilju poročate v ločenem razdelku. Razdelek naj se prične z oznako cilja, kot ste jo uporabili v predlogu, in eno-stavčnim opisom cilja. Sledijo naj eden do trije odstavki opisa rezultatov, kjer se pri vseh rezultatih skličete na reference (npr. [1] ali [1, 2]). Po odstavkih z opisom rezultatov za posamezen cilj v alinejah navedite reference za ta cilj (članki, referati, vabljena predavanja, patenti, ipd.). Alineje naj se pričnejo z ustrezno številko (npr. [1]). Rezultatov brez ustreznih referenc pri opisu rezultatov cilja ne navajajte. Če je le možno, navedbo posamezne reference zaključite z ustrezno šifro COBISS. Pri člankih je navedba šifre COBISS obvezna, navedite pa samo članke, kjer ste navedli podatke o sofinancerju (ARRS/ARIS) ali sofinancerjih ter številko ARIS projekta/programa, za katerega pišete poročilo. Celotni razdelek naj vsebuje največ 12.000 znakov, vključno s presledki (velikost pisave 11).

## WP1. Project management, coordination and dissemination

### T1.1 – Coordination.
O delu na projektu smo poročali in se dogovarjali na [Sredinem seminarju](https://www.fmf.uni-lj.si/sl/obvestila/agregator/152/seminar-sreda/). Naslednji seminarji se ukvarjajo s temami projekta J5-4596

  * 2022: 1327, 1329, 1331, 1332;
  * 2023: 1333, 1336, 1337, 1338, 1339, 1340, 1341;
  * 2024: 1343, 1344, 1345, 1346, 1348, 1351, 1352, 1353, 1354, 1355, 1356, 1357;
  * 2025: 1358, 1359, 1363,	1365, 1366, 1367, 1369, 1371, 1375;
  * 2026: 1377, 1379.


### T1.2 – Reporting. 
Done on a yearly basis, as required by the financer (SRA/ARRS).  Financial reporting and funds
monitoring was performed by the accounting departments of the partners.

### T1.3 – Dissemination. 
The obtained results were reported on international scientific conferences and published in scientific journals. The developed software, its documentation and
example data sets are made available on GitHub as open-source.

## WP2. Identification of higher order services and implementation of prototype solutions

The main goal of the project is the identification of potential higher order services and development
of some prototype solutions, based on investigation of actual needs and contexts
of different interest groups. To support this goal we have to provide high quality data often
obtained by combining data from different databases. We also have to develop new algorithms
for some analytical problems.

Za preprostejša vprašanja (kje objaviti članek, pomembna dela ali avtorji na izbrano temo, itd.

selecting appropriate reviewers, evaluation of reviewers, quality of data evaluation, automatic suggestion
of keywords, keyword suggestions, journal suggestions, possible partners for research collaboration, papers to read for selected topics.

) dobimo pogosto zadovoljive odgovore z uporabo orodij UI. Zato smo pozornost preusmerili na zahtevnejše analize podatkov iz bibliografskih podatkovnih baz:

  * soavtorstva med evropskimi državami skozi čas
  * analiza člankov objavljenih v izbrani reviji
  * analiza značilnosti novih univerz
  * analiza izmenjav Erasmus



## WP3. Methods and tools for the identification of units (entity resolution) 

replaced by 
Development of support for obtaining networks from OpenAlex

V R-ju smo razvili knjižnico [OpeAlex2Pajek](https://github.com/bavla/OpenAlex/tree/main/OpenAlex2Pajek). Opisana je bila v članku []. In uporabljena za pridobivanje omrežij v člankih [] [] [] [].


## WP4. Theoretical research in bibliographic network analysis

An important tool in analysis of collections of linked networks (bibliographic networks are
a special case) is network multiplication (Batagelj and Cerinšek, 2013) which enables us to
compute derived networks. In order to consider each unit equally in the analysis of bibliographic
networks, the fractional approach is used. Its theoretical background was proposed in our recent
paper (Batagelj 2020). In papers Batagelj and Praprotnik (2016) and Batagelj and Maltseva
(2020) we proposed a longitudinal approach to temporal network analysis and showed how it
can be applied in analysis of temporal bibliographic networks. We will continue to explore the
possibilities provided by these three approaches in the bibliographic network analysis. 



The main tasks in this WP include:
### T4.1 – New derived networks based on normalization and multiplication; extension to weighted networks

On weighted two-mode network projections [COBISS.SI-ID 216955651]

Weighted degrees and truncated derived bibliographic networks [COBISS.SI-ID 216973315]


Multiway  - Cores in multiway networks [COBISS.SI-ID 217014531]

### T4.2 – Temporal versions of derived networks

Časovna bibliografska omrežja se običajno ukvarjajo z leti. V projektu smo razvili metode časovne analize, ki uporabljajo časovno omrežje razslojeno na časovne rezine.
Običajno so časovne rezine precej zapletena utežena omrežja. Ta poenostavimo tako, da jih nadomestimo s pripadajočimi skeleti izbrane vrste. V skeletu ohranimo le (glede na vprašanje) pomembne sestavine (vozlišča/povezave). Primeri skeletov so: vpeta drevesa, vozliščni/povezavni izrezi, k-naj povezave do sosedov, (posplošene) sredice.

### T4.3 – New temporal quantities describing temporal bibliographic networks

Razvili smo tudi metode za analizo trajektorij. 

Uporabili smo jih za analizo podobnosti slovenskih politikov Oštro.  [COBISS.SI-ID 186331907] [COBISS.SI-ID 202923011]

### T4.4 – Clustering in temporal networks

[COBISS.SI-ID 197238275] [COBISS.SI-ID 182243075] konference

## WP5. Development of new methods for bibliographic network analysis in a new Julia package

preklopili na R

Bibliographic networks can be large (some hundred thousands or even millions of nodes). The
developed software support should provide solutions that can deal also with such data efficiently
– in a range of some seconds or minutes. The core of this WP will be implementation of the new
library in the Julia programming language, that is interoperable with Python, R and Pajek.
The library will be based on experiences gained from Python libraries Nets, TQ and Biblio.
We will also develop direct data imports/exports from JSON based formats and direct and
rich network visualization methods leveraging modern Javascript/HTML/CSS based libraries
(vis.js, vis-network, d3.js, NetworkD3). An important part of the library will be data structures
and analytic algorithms to support data cleaning in WP3. The tasks in this WP include:

### T5.1 – Implementation and optimization of basic data structures and algorithms from Nets and TQ in Julia. 

[TQ](https://github.com/bavla/TQ)
[netsWeight](https://github.com/bavla/Nets/tree/master/netsWeight) 

### T5.2 – Implementation of advanced algorithms.

Advanced algorithms will be implemented based on methods developed in WP4.

Balassa normalization.

### T5.3 – Visualization methods. Integrations with selected Javascript/HTML/CSS visualization libraries.

Visualization 3-way

Balassa


### T5.4 – Testing, optimization and documenting the library.


## WP6. Demonstration of applications

nekatere primere prepustimo UI.

The prototype demonstrations will be developed with selected end users, considering their
needs and use cases. We will work with editors of selected journals (e.g. Ars Mathematica
Contemporanea, Acta Chimica Slovenica). The use cases we may consider include: selecting
appropriate reviewers, evaluation of reviewers, quality of data evaluation, automatic suggestion
of keywords, etc. We will also consider use cases from the “consumer” side, namely authors,
researchers and students. This may include keyword suggestions, journal suggestions, possible
partners for research collaboration, papers to read for selected topics. Demonstrations will be
focused on selected research fields (e.g. mathematics, social network analysis, etc.). The work
package will be divided into the following tasks.

### T6.1 – Bibliometric analysis in selected research fields with demonstration of the newly developed methods
### T6.2 – Applications for journal managers
### T6.3 – Applications for authors, researchers and students

  * soavtorstva med evropskimi državami skozi čas  [COBISS.SI-ID 260663299]
  * analiza člankov objavljenih v izbrani reviji  [COBISS.SI-ID 272388867]
  * analiza značilnosti novih univerz  [COBISS.SI-ID 272423427]
  * analiza izmenjav Erasmus [ArXiv ]


To demonstrate the power of bibliographic (temporal) network analysis we will construct some
collections of large networks on selected scientific fields and analyze them providing an insight
into development and structure of the field.

Social networks [COBISS.SI-ID 217252611], Handball

Smo člani (program Pajek) združenja Network Analysis Software Collective (NASCol) https://www.nascol.net/ . Sodelujemo pri pripravi “Guidelines for Reporting About Network Data” (GRAND) https://grand-statement.org/.
Sodelujemo pri projektu COST HiTeC https://www.hitecaction.org/ .

