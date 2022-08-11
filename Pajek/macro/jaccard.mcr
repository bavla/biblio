NETBEGIN 18
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 18
NETPARAM 3
VECPARAM 17

Msg Jaccard network from co-appearance network Co
Msg by Vladimir Batagelj, August 11, 2022
Msg ---------------------------------------------
% Getting Loops
V 18 GETLOOPS 3 (3)
% Setting all Line Values to 1
N 18 SETLINEVAL1 3 1 (3)
% Vector # Network
N 19 VECNET1 18 18 (3)
% Vector # Network
N 20 VECNET0 18 18 (3)
% Disposing Network...
N 18 DN  (3)
% Disposing Vector...
V 18 DV  (3)
% Cross-Intersection of Networks
N 21 CROSSINTERSECT 19 20 1 (3)
% Disposing Network...
N 19 DN  (3)
% Disposing Network...
N 20 DN  (3)
% Cross-Intersection of Networks
N 22 CROSSINTERSECT 21 3 2 (3)
% Disposing Network...
N 21 DN  (3)
% Cross-Intersection of Networks
N 23 CROSSINTERSECT 3 22 4 (3)
N 23 NETNAME Jaccard
% Disposing Network...
N 22 DN  (3)
Msg ---------------------------------------------
