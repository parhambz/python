0 setn r15 50
1 setn r11 50
2 read r1
3 setn r3 10
4 mod r2 r1 r3
5 div r1 r1 r3
6 storer r2 r15
7 addn r15 1
8 jgtzn r1 4

9 addn r15 -1
10 loadr r2 r15
11 loadr r4 r11
12 addn r11 1
13 sub r5 r4 r2
14 sub r6 r15 r11
15 addn r6 -2
16 jltzn r6 21
17 jeqzn r5 9

18 setn r13 0
19 write r13
20 halt
21 jeqzn r5 23
22 jumpn 18
23 setn r13 1
24 write r13
25 halt




