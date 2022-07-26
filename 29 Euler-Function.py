a = int(input())
result = [0 for i in range(a)]


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result


for i in range(a):
    n = int(input())
    result[i] = phi(n)

for i in range(a):
    print(result[i])
