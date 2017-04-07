NETBEGIN 5
CLUBEGIN 2
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 10
NETPARAM 1
CLUPARAM 1
VECPARAM 1

% Normalized 2-mode network N'
% by Vladimir Batagelj, April 4, 2017
% Output degree centrality of 1. WK.net [2-Mode] (15964)
V 10 DEGV 1 [1] (15964)
% Partition into Two Modes
C 2 TWOMODEC 1 (15964)
% Extracting SubVector
V 11 EXTV 10 2 [1] (5695)
% Constant Vector
V 12 CONSTANTVEC 1.0000 (5695)
% Subtracting Vectors
V 13 SUBV 11 12 (5695)
% Min/Max of two Vectors
V 14 MAXV 13 12 (5695)
% Vector with Inverse Values
V 15 INV1VEC 14 (5695)
% Vector # Network
N 5 VEC2MNET1 15 1 (15964)
N 5 NETNAME Normalized 2-mode network N&#39;
% Disposing Vector...
V 10 DV  (15964)
% Disposing Vector...
V 11 DV  (5695)
% Disposing Vector...
V 12 DV  (5695)
% Disposing Vector...
V 13 DV  (5695)
% Disposing Partition...
C 2 DC  (15964)
