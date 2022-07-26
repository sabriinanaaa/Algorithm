a = int(input())
result = [0 for i in range(a)]

def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a


def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0


def getNthUglyNo(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


for i in range(a):
    n = int(input())
    result[i] = getNthUglyNo(n)

for i in range(a):
    print(result[i])
