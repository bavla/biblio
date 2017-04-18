NETBEGIN 2
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 1

% Output degree centrality of 1. C:\Users\batagelj\work\Python\WoS\BM\results\cluster\citeMain.net (3994)
V 1 DEGV 1 [1] (3994)
% Constant Vector
V 2 CONSTANTVEC 1.0000 (3994)
% Min/Max of two Vectors
V 3 MAXV 2 1 (3994)
% Vector with Inverse Values
V 4 INV1VEC 3 (3994)
% Network Transpose
N 2 TRAN 1 (3994)
% Multiplying networks
N 3 MULTIPLYNET 1 2 1 (3994)
N 3 NETNAME biCo
% Vector # Network
N 4 VECNET1 4 3 (3994)
N 4 NETNAME Rows of N3 "multiplied" by V4
% Removing loops
N 4 DLOOPS 4 (3994)
N 4 NETNAME biC
% Powering Line Values
N 5 POWERLINVAL 4 to -1.0000 1 (3994)
% Converting bidirectional Arcs to Edges
N 5 BATOESUM 5 (3994)
% Adding Constant to Line Values
N 6 ADDLINVAL 5 -1.0000 1 (3994)
% Powering Line Values
N 7 POWERLINVAL 6 to -1.0000 1 (3994)
N 7 NETNAME Jaccard
% Multiplying
N 8 MULLINVAL 7 by -1.0000 1 (3994)
% Adding Constant to Line Values
N 9 ADDLINVAL 8 1.0000 1 (3994)
N 9 NETNAME Hammond
% Disposing Network...
N 8 DN  (3994)
% Disposing Network...
N 6 DN  (3994)
% Disposing Network...
N 5 DN  (3994)
