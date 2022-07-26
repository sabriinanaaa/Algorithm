# import sys
import math
inf = math.inf
d = []
for i in range(10):
    d1 = []
    d.append(d1)
    for j in range(10):
        d[i].append(0)

n, m = map(int, input().split(' '))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            d[i][j] = 0
        else:
            d[i][j] = inf


for i in range(1, m+1):
    t1, t2, t3 = map(str, input().split(' '))

    if t1 == "a":
        t1 = 1
    elif t1 == "b":
        t1 = 2
    elif t1 == "c":
        t1 = 3
    elif t1 == "d":
        t1 = 4
    elif t1 == "e":
        t1 = 5
    elif t1 == "f":
        t1 = 6
    elif t1 == "g":
        t1 == 7
    elif t1 == "h":
        t1 = 8
    elif t1 == "i":
        t1 = 9
    elif t1 == "j":
        t1 = 10
    elif t1 == "k":
        t1 = 11
    elif t1 == "l":
        t1 = 12
    elif t1 == "m":
        t1 == 13
    elif t1 == "n":
        t1 = 14
    elif t1 == "o":
        t1 = 15
    elif t1 == "p":
        t1 = 16
    elif t1 == "q":
        t1 = 17
    elif t1 == "r":
        t1 = 18
    elif t1 == "s":
        t1 == 19
    elif t1 == "t":
        t1 == 20
    elif t1 == "u":
        t1 = 21
    elif t1 == "v":
        t1 = 22
    elif t1 == "w":
        t1 = 23
    elif t1 == "x":
        t1 = 24
    elif t1 == "y":
        t1 = 25
    elif t1 == "z":
        t1 == 26

    if t2 == "a":
        t2 = 1
    elif t2 == "b":
        t2 = 2
    elif t2 == "c":
        t2 = 3
    elif t2 == "d":
        t2 = 4
    elif t2 == "e":
        t2 = 5
    elif t2 == "f":
        t2 = 6
    elif t2 == "g":
        t2 == 7
    elif t2 == "h":
        t2 = 8
    elif t2 == "i":
        t2 = 9
    elif t2 == "j":
        t2 = 10
    elif t2 == "k":
        t2 = 11
    elif t2 == "l":
        t2 = 12
    elif t2 == "m":
        t2 == 13
    elif t2 == "n":
        t2 = 14
    elif t2 == "o":
        t2 = 15
    elif t2 == "p":
        t2 = 16
    elif t2 == "q":
        t2 = 17
    elif t2 == "r":
        t2 = 18
    elif t2 == "s":
        t2 == 19
    elif t2 == "t":
        t2 == 20
    elif t2 == "u":
        t2 = 21
    elif t2 == "v":
        t2 = 22
    elif t2 == "w":
        t2 = 23
    elif t2 == "x":
        t2 = 24
    elif t2 == "y":
        t2 = 25
    elif t2 == "z":
        t2 == 26

    t3 = int(t3)
    d[t1][t2] = int(t3)

# Floyd-Warshall algorithm
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # print(d[i][j])
            # print(d[i][k]+d[k][j])
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

                # print("min", k, i, j, d[i][j])

# for i in range(1, n+1):
#     if d[i][j] == 99999999:
#         d[i][j] = "INF"

for i in range(1, n+1):

    result = d[i][1:n+1]
    print(" ".join(str(i) for i in result))
