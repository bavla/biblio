NETBEGIN 22
CLUBEGIN 27
PERBEGIN 9
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 10
NETPARAM 6
CLUPARAM 26
PERPARAM 8
VECPARAM 9

Msg *** Determine the boundary of citation network
Msg *** by Vladimir Batagelj, January 2008
Msg Input degree centrality of Citation network
C 27 DEGC 6 [0]
Msg Binarize - select the range 1-k (k is a boundary degree)
C 28 BIN 27 ?
Msg Output degree centrality of Citation network
C 29 DEGC 6 [1]
C 30 BIN 29 [0]
C 31 MINP 28 30
Msg Determine the boundary (class=0) Partition
Msg Extracting Subnetwork according to Partition
N 22 EXT 6 31 [0] 1
Msg Delete auxiliary files
C 32 DC
C 30 DC
C 29 DC
C 28 DC
C 27 DC
