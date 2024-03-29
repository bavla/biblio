# Workshop outline

## Info

Netglow [programme](http://ngw.spbu.ru/programme)

4.7.2018, 10:00-12:00, 12:30-14:30

**Analysis of bibliographic networks**

**Teachers:**<br>
*Vladimir Batagelj*, IMFM Ljubljana and AMI UP Koper <br>
*Daria Maltseva*, International laboratory for
Applied Network Research, Moscow


Bibliographic networks consider different types of relations between publications and their authors, 
thus underlying different patterns of collaboration in science (co-authorship, co-citation, citing). 
Data for such networks can be quite easily obtained from special bibliographies (BibTEX) and 
bibliographic services (Web of Science, Scopus, SICRIS, CiteSeer, Zentralblatt MATH, Google Scholar, 
DBLP Bibliography, US patent office, IMDb, and others). Besides names of authors and titles of their
works, more detailed information about them can be obtained: institution, country, time of the first
work, time of the last work – for authors; publisher, journal, editor/s, number, volume, pages, 
key words, time of submission, language, classification/s – for works. With different procedures 
of networks transformation we can get many different kinds of mostly two-mode networks and study 
relations between different entities included in data bases (works, authors, journals, key words, 
institutions, countries, etc.).

## Outline

See the Upsala slides - bibnet.pdf.

### 1. Transforming bibliographic data into networks

Goals, research questions, theory

Sources of data

Typical data
- (semi) structured from data bases
- data from bibliographies

Problem 1: detail of description (list of attributes); completnes of description (all authors?)

Problem 2: different cultures in different disciplines
- examples of diverse citation practices

Problem 3: entity identification/resolution
- synonyms, homonyms
  - normalization - at data entry
  - standardization use standards whenever possible
    - [ORCID](https://orcid.org/)
    - [DOI](https://www.doi.org/)
    - [ISBN](https://isbnsearch.org/)
    - [ISSN](http://www.issn.org/) standard abreviations: [JAS](https://www.abbreviations.com/jas.php), [LTWA](http://www.issn.org/services/online-services/access-to-the-ltwa/), [WoS](https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html),[Caltech](https://www.library.caltech.edu/journal-title-abbreviations),    
  - "dictionaries"
    - [keywords](https://www.wordstream.com/keywords) [lemmatization lists](https://github.com/michmech/lemmatization-lists)

Problem 4: non-Latin alphabets
- Russian (Unicode, automatic transcription)

Boundary problem when extracting subset of data
- preliminary citation network analysis; manually completing the important data 

Tools for collection and mantainance of bibliographic data

Conversion to networks

**Note:** examples from WoS and eLibrary.

### 2. Analyzing bibliographic networks

Methods for analysis of bibliographic networks

Global properties, distributions

Citation network analysis
- main path analysis

Derived networks
- Co-authorship network and fractional approach
- Author citations
- Bibliographic coupling and co-citation
- Author-keywords
- Keywords-journals

Temporal bibliographic networks

Tools
- Pajek
  - macros
- R
  - packages
- VOS




