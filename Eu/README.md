# Scientific co-authorship between European countries

Visualizations of time slices of temporal network describing the co-authorship between authors from European countries for the years 2000-2022.

Let P be the set of scientific papers from Web of Science co-authored by authors from at least two different European countries. The nodes of the network are European countries. The weight of the edge (A:B) is counting the number of papers from P that were co-authored by at least one author from country A and at least one author from country B in the year y.

The list of European countries is available [here](https://www.worldometers.info/geography/how-many-countries-in-europe/) and [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) their ISO alpha 2 codes.

Because the largest weight is 17282 I **divided the weights by 1000**.

```
==============================================================================
Lowest value of line:               1.00000000
Highest value of line:          17282.00000000

         Line Values                                   Frequency       Freq%      CumFreq  CumFreq%
---------------------------------------------------------------------------------------------------
 (                       ...               10.0000]         4387     25.9647         4387   25.9647
 (               10.0000 ...               50.0000]         3474     20.5611         7861   46.5258
 (               50.0000 ...              100.0000]         1487      8.8009         9348   55.3267
 (              100.0000 ...              500.0000]         4686     27.7344        14034   83.0611
 (              500.0000 ...             1000.0000]         1291      7.6409        15325   90.7019
 (             1000.0000 ...             5000.0000]         1392      8.2386        16717   98.9406
 (             5000.0000 ...            10000.0000]          153      0.9055        16870   99.8461
 (            10000.0000 ...            17282.0000]           26      0.1539        16896  100.0000
---------------------------------------------------------------------------------------------------
```

* [Pictures with levels](level)
* [Pictures of the strongest neighbor networks](one)
