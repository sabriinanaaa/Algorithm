import math

a = int(input())
nn = []
mm = []
number = []
divisor = []

for i in range(a):
    n, m = list(map(int, input().strip().split()))
    nn.append(n)
    mm.append(m)
    dv = 0
    nb = 0

    for j in range(n, m+1):
        c = 0
        for k in range(1, math.ceil(math.sqrt(j))):
            if j % k == 0:
                if j / k == k:
                    c = c + 1
                else:
                    c = c + 2
        if c > dv:
            nb = j
            dv = c
    number.append(nb)
    divisor.append(dv)

for i in range(a):
    print(
        f"Between {nn[i]} and {mm[i]}, {number[i]} has a maximum of {divisor[i]} divisors.")
