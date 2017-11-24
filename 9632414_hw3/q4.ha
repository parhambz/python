0 read r1
1 read r2
2 copy r3 r2
3 setn r4 1
4 addn r2 -1
5 mul r4 r4 r1
6 addn r3 -1
7 jgtzn r3 5
8 write r4
9 jgtzn r2 2
10 setn r5 1
11 write r5
12 halt