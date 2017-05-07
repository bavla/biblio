NETBEGIN 1
CLUBEGIN 1
PERBEGIN 1
CLSBEGIN 1
HIEBEGIN 1
VECBEGIN 1

Msg *** Determine the matrix of citations between authors
Msg *** by Vladimir Batagelj, March 2008
Msg Reading Network   ---  Cite.net
N 1 RDN "?" (72281)
Msg Reading Network   ---   WA.net
N 2 RDN "?" (107082)
N 3 TRAN2M 2 (107082)
N 4 1MODE2MODE 1 (144562)
N 1 DN  (72281)
Msg Multiplying matrices  AtC = At * C
N 5 MULTIPLYNET 3 4 22 (107082)
N 4 DN  (144562)
Msg Multiplying matrices  AtCA = AtC * A
N 6 MULTIPLYNET 5 2 21 (34801)
N 2 DN  (107082)
N 3 DN  (107082)
N 5 DN  (107082)
N 6 NETNAME AtCA  [1-Mode]