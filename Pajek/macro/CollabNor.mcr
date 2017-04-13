NETBEGIN 1
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1

Msg Determine the normalized collaboration network for a given WA network
Msg --- by V. Batagelj, June 2011 ---------------------------------------
Msg Reading Network  WA.net
N 1 RDN "?"
Msg Output degree centrality of  WA.net
C 1 DEGC 1 [1]
V 1 DV
V 2 MVEC 1
C 2 TWOMODEC 1
V 3 EXTV 2 2 [1]
V 4 INV1VEC 3
V 2 DV
V 3 DV
N 2 VEC2MNET1 4 1
N 3 TRAN2M 1
Msg Multiplying matrices  AW * nor(WA)
N 4 MULTIPLYNET 3 2 21
N 2 DN
N 3 DN
V 5 GETLOOPS 4
Msg Removing loops
N 4 DLOOPS 4
N 4 BATOEMAX 4
Msg Sorting lines - in ascending order of line values
N 4 SORTLINEASC 4
C 1 DC
C 2 DC
V 4 DV
N 4 NETNAME Normalized collaboration network
V 5 VECNAME Self-collaboration
Msg --- end CollabNor ----------------------------------------------------
