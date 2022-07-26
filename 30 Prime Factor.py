import math
a = int(input())
count = []
result = []


def primefactors(n):
    while n % 2 == 0:
        count.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while (n % i == 0):
            count.append(i)
            n = n / i

    if n > 2:
        count.append(int(n))


primefactors(a)
i = 0
while i < len(count):
    r = count[i]
    c = count.count(r)
    if c < 2:
        result.append(f"{r}")
    else:
        result.append(f"{r}^{c}")
    i += c
# print(result)
prime = "*".join(str(i) for i in result)
print(f"{a}={prime}")
