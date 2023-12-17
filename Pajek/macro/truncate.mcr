NETBEGIN 3
CLUBEGIN 3
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 8
NETPARAM 2
CLUPARAM 2
VECPARAM 7

Msg Truncated coappearance network of network N
Msg by Vladimir Batagelj, December 5, 2023
Msg ---------------------------------------------
% Scalar - Sum
V 8 SUMSCALAR 7 (1)
V 8 VECNAME T(WAn)
% Transforming Vector to Partition
Msg Enter threshold value t
C 3 MAKEVECPAR 7 [?] (28108)
% Extracting SubVector
V 9 EXTV 7 3 [2] (1799)
V 9 VECNAME wid_WAn/one
% Constant Partition
Msg Enter number of rows
C 4 CONSTANTC 0 (9225)
% Fusing Partitions
C 5 FUSEP 4 3 (37333)
% Extracting Subnetwork according to Partition
N 3 EXT 2 5 [0,2] 1 (11024)
% Partition into Two Modes
C 7 TWOMODEC 3 (11024)
% Binarizing Partition
C 8 BIN 7 [2] (11024)
% Output degree centrality of 3. Extracting N2 according to C5 [0,2] (11024)
C 9 DEGC 3 [1] (11024)
% Adding Partitions
C 10 ADDP 9 8 (11024)
% Extracting Subnetwork according to Partition
N 4 EXT 3 10 [1-*] 1 (10315)
N 4 NETNAME WAn1
% Generating 1-mode network from 2-mode network
N 5 AFFILMULT 4 FALSE TRUE 1 (1799)
N 5 NETNAME Truncated Cn
% Weighted Degree
V 10 LINESUM 5 [1] (1799)
V 10 VECNAME alpha
% Scalar - Sum
V 11 SUMSCALAR 10 (1)
V 11 VECNAME T11
% Subtracting Vectors
V 12 SUBV 9 10 (1799)
V 12 VECNAME beta
% Scalar - Sum
V 13 SUMSCALAR 12 (1)
V 13 VECNAME T10
% Subtracting Vectors
V 14 SUBV 8 11 (1)
% Subtracting Vectors
V 15 SUBV 14 13 (1)
% Subtracting Vectors
V 16 SUBV 15 13 (1)
V 16 VECNAME T00
% Disposing Vectors ...
V 14 DV  (1)
V 15 DV  (1)
% V 6 DV  (37333)
V 7 DV  (28108)
% Disposing Partitions ...
C 3 DC  (28108)
C 4 DC  (9225)
C 5 DC  (37333)
C 6 DC  (11024)
C 7 DC  (11024)
C 8 DC  (11024)
C 9 DC  (11024)
C 10 DC  (11024)
C 11 DC  (10315)
% Disposing Networks ...
N 3 DN  (11024)
N 4 DN  (10315)
Msg ---------------------------------------------

