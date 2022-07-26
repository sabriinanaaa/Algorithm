a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    f1 = 0
    f2 = 1
    if n == 0:
        result[i] = f1
    elif n == 1:
        result[i] = f2
    for j in range(n-1):
        result[i] = f1 + f2
        f1 = f2
        f2 = result[i]

for i in range(a):
    print(result[i])
