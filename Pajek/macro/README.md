# Macros

Pajek's macros for analysis of bibliographic networks
https://github.com/bavla/biblio/wiki/macros

## norm1

Normalized 1-mode network N given as First network.

## norm2

Normalized 2-mode network N given as First network. As data enter # of rows of given 2-mode network.

## norm2p

Newman's normalization of a 2-mode network N given as First network.  As data enter # of rows of given 2-mode network.

## jaccard

For a selected co-appearance network Co (projection of a two-mode network) computes the corresponding Jaccard similarity network with weights
J[u,v] = Co[u,v]/(Co[u,u]+Co[v,v]-Co[u,v])

## salton

For a selected matching network Co (projection of a two-mode network) computes the corresponding Salton cosine similarity network with weights
S[u,v] = Co[u,v]/sqrt(Co[u,u]*Co[v,v])

## saltoni

Same as salton, but takes care of possible null rows in Co.

## biCo

Bibliographic coupling network of a given citation network N

## biCon

Normalized bibliographic coupling network of a given citation network N. Jaccard similarity and normalized Hamming distance between nodes.


