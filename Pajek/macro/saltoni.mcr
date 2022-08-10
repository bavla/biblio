NETBEGIN 8
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 7
NETPARAM 3
VECPARAM 6

% Getting Loops
V 7 GETLOOPS 3 (3)
% Constant Vector
V 8 CONSTANTVEC 1.0000 (3)
% Min/Max of two Vectors
V 9 MAXV 8 7 (3)
% Abs + Sqrt Vector
V 10 SQRT1VEC 9 (3)
% Vector with Inverse Values
V 11 INV1VEC 10 (3)
% Vector # Network
N 8 VECNET1 11 3 (3)
% Vector # Network
N 9 VECNET0 11 8 (3)
N 9 NETNAME Salton (isolates)
