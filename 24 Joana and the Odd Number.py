a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    m3 = ((n + 1) * (n + 1) / 2 - 1)
    m2 = ((n + 1) * (n + 1) / 2 - 3)
    m1 = ((n + 1) * (n + 1) / 2 - 5)
    m = m1 * m2 * m3
    result[i] = int(m)

for i in range(a):
    print(result[i])
