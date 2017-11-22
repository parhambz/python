0 read r1
1 setn r8 1
2 read r3
3 addn r2 10
4 mod r6 r1 r2
5 sub r7 r6 r3
6 jgtzn r7 10
7 div r1 r1 r2
8 jgtzn r1 4
9 jumpn 12
10 write r0
11 halt
12 write r8
13 halt