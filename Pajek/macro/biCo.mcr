NETBEGIN 2
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 1

% Network Transpose
N 2 TRAN 1 (3994)
% Multiplying networks
N 3 MULTIPLYNET 1 2 1 (3994)
% Removing loops
N 4 DLOOPS 3 (3994)
% Converting bidirectional Arcs to Edges
N 4 BATOEMIN 4 (3994)
