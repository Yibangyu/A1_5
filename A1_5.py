#!/usr/bin/bash

shulie = input()
L = [int(n) for n in shulie.split()]
L.pop(0)
L1, L2, L3, L4, L5 = [],[],[],[],[]

for value in L:
    y = value % 5
    locals()["L"+str(y+1)].append(value)

L1 = list(filter(lambda x: x%2 == 0, L1))

A1 = (sum(L1), "N")[ len(L1) == 0 ]

A2 = (sum([ (-1) ** i * value for i,value in enumerate(L2) ]), "N")[ len(L2) == 0 ]

A3 = (len(L3), "N")[ len(L3) == 0 ]

if len(L4) == 0:
    A4 = "N"
else:
    A4 = round(sum(L4)/len(L4), 1)

if len(L5) == 0:
    A5 = "N"
else:
    A5 = max(L5)

print(A1,A2,A3,A4,A5)

