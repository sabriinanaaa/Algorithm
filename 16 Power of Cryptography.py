a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    m, n = list(map(int, input().strip().split()))
    result[i] = round(n ** (1 / m))

for i in range(a):
    print(result[i])
