a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    n = int(input())

    h = list(map(int, input().split()))

    avg = sum(h) // n
    m = 0
    for j in range(0, n):
        if h[j] > avg:
            m += h[j] - avg
    result[i] = m

for i in range(a):
    print(result[i])

