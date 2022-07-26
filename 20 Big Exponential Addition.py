a = int(input())
result = [0 for i in range(a)]


def exponential(x, y):

    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (exponential(x, int(y / 2)) *
                exponential(x, int(y / 2)))
    else:
        return (x * exponential(x, int(y / 2)) *
                exponential(x, int(y / 2)))


for i in range(a):
    m, n = list(map(int, input().strip().split()))
    result[i] = exponential(2, m)+exponential(2, n)

for i in range(a):
    print(result[i])
