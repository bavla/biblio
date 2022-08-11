NETBEGIN 4
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 3

Msg Salton cosine network from matching network Co
Msg by Vladimir Batagelj, August 10, 2022
Msg ---------------------------------------------
% Getting Loops
V 1 GETLOOPS 3 (3)
% Abs + Sqrt Vector
V 2 SQRT1VEC 1 (3)
% Disposing Vector...
V 1 DV  (3)
% Vector with Inverse Values
V 3 INV1VEC 2 (3)
% Disposing Vector...
V 2 DV  (3)
% Vector # Network
N 4 VECNET1 3 3 (3)
% Vector # Network
N 5 VECNET0 3 4 (3)
N 5 NETNAME Salton
% Disposing Vector...
V 3 DV  (3)
% Disposing Network...
N 4 DN  (3)
Msg ---------------------------------------------

