a = int(input())
result = []

for i in range(a):
    n = list(input().split())

    odd = 0
    even = 0
    for j in n:
        for k in range(4):
            if k % 2 > 0:
                odd += int(j[k])
            else:
                t = int(j[k]) * 2
                while t > 0:
                    even += t % 10
                    t //= 10  # ex: 9//2=4

    if (odd+even) % 10 > 0:
        result.append("Invalid")
    else:
        result.append("Valid")

for i in range(a):
    print(result[i])
