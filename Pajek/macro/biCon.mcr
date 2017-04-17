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
% Vector # Network
N 2 VECNET1 4 1 (3994)
N 2 NETNAME n(Cite)
% Multiplying networks
N 3 MULTIPLYNET 2 1 1 (3994)
% Removing loops
N 3 DLOOPS 3 (3994)
N 3 NETNAME biC
% Converting bidirectional Arcs to Edges
N 4 BATOESUM 3 (3994)
% Multiplying
N 5 MULLINVAL 4 by 0.5000 1 (3994)
% Disposing Network...
N 4 DN  (3994)
N 5 NETNAME biCon
