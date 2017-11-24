0 setn r15 25
1 jumpn 17
2 storer r12 r15
3 addn r15 1
4 setn r13 0
5 setn r12 10
6 storer r1 r15
7 addn r15 1
8 div r1 r1 r12
9 addn r13 1
10 jgtzn r1 8
11 write r13
12 addn r15 -1
13 loadr r1 r15
14 addn r15 -1
15 loadr r12 r15
16 jumpr r14
---------------
17 jumpn 32
18 storer r1 r15
19 addn r15 1
20 storer r2 r15
21 addn r15 1
22 setn r2 10
23 mod r13 r1 r2
24 div r1 r1 r2
25 write r13
26 jgtzn r1 23
27 addn r15 -1
28 loadr r2 r15
29 addn r15 -1
30 loadr r1 r15
31 jumpr r14
----------------
32 jumpn 45
33 setn r8 1
34 read r3
35 mod r6 r1 r12
36 sub r7 r6 r2
37 jgtzn r7 41
38 div r1 r1 r12
39 jgtzn r1 35
40 jumpn 43
41 copy r13 r0
42 jumpr r14
43 copy r13 r8
44 jumpr r14
---------------
45 jumpn 61 
46 setn r11 100
47 copy r3 r2
48 setn r4 1
49 addn r2 -1
50 mul r4 r4 r1
51 addn r3 -1
52 jgtzn r3 50
53 store r4 r11
54 addn r11 1
55 jgtzn r2 47
56 setn r5 1
57 store r5 r11
58 addn r11 1
59 copy r13 r11 
60 jumpr r14
-----------------
read r1
read r2
storer r1 r15
addn r15 1
calln r14 33
jeqzn r13 *






addn r15 -1
loadr r1 r15

