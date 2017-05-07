NETBEGIN 2
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1
NETPARAM 1

Msg Three collaboration networks from WA network
Msg by Vladimir Batagelj, August 11, 2012
Msg ---------------------------------------------
Msg -- Normalization
V 1 DEGV 1 [1] (269306)
C 1 TWOMODEC 1 (269306)
V 2 EXTV 1 1 [1] (193376)
V 3 INV1VEC 2 (193376)
N 2 VEC2MNET1 3 1 (269306)
N 2 NETNAME Normalized
V 3 DV  (193376)
V 1 DV  (269306)
V 2 VECNAME # of authors
Msg -- Collaboration 1
N 3 AFFILMULT 1 FALSE FALSE (75930)
N 3 NETNAME Collaboration 1
Msg -- Collaboration 2
N 4 TRAN2M 1 (269306)
N 5 MULTIPLYNET 4 2 21 (75930)
N 5 NETNAME Collaboration 2
N 4 DN  (269306)
Msg -- Collaboration 3
N 6 AFFILMULT 2 FALSE FALSE (75930)
N 6 NETNAME Collaboration 3
Msg -- Analysis of Collaboration 2
Msg ---- Self-contribution, Total # of works, Collaborativeness
V 4 GETLOOPS 5 (75930)
V 4 VECNAME Self-contribution
V 5 DEGV 1 [0] (269306)
V 6 EXTV 5 1 [2] (75930)
V 6 VECNAME Author&#39;s total # of works
V 7 DIVV 4 6 (75930)
V 7 VECNAME Self-sufficiency
V 8 CONSTANTVEC 1.0000 (75930)
V 9 SUBV 8 7 (75930)
V 9 VECNAME Collaborativeness
P 1 MAKEVECPERM 4 (75930)
P 2 MIRRORPERM 1 (75930)
Msg ---- Reordering by Self-contribution
N 7 REOR 5 2 (75930)
N 7 NETNAME Reordered Collaboration 2
V 10 REORVECT 4 2 (75930)
V 10 VECNAME Reordered Self-contribution
V 11 REORVECT 6 2 (75930)
V 11 VECNAME Reordered Total
V 12 REORVECT 9 2 (75930)
V 12 VECNAME Reordered Collaborativeness
V 5 DV  (269306)
V 8 DV  (75930)
P 2 PERNAME Order
P 1 DP  (75930)
Msg ---------------------------------------------
