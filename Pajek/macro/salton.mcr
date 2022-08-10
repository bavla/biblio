NETBEGIN 4
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 3

% Getting Loops
V 1 GETLOOPS 3 (3)
% Abs + Sqrt Vector
V 2 SQRT1VEC 1 (3)
% Vector with Inverse Values
V 3 INV1VEC 2 (3)
% Vector # Network
N 4 VECNET1 3 3 (3)
% Vector # Network
N 5 VECNET0 3 4 (3)
N 5 NETNAME Salton
