n = int(input())
result = [0 for i in range(n)]
case = 1
for i in range(n):
    m = int(input())
    a = list(input())

    total = 0
    for j in range(len(a)):
        if a[j] == ".":
            total += 1
            if j+1 < len(a):
                a[j+1] = "#"
            if j+2 < len(a):
                a[j+2] = "#"
    result[i] = total
    case += 1

for i in range(n):
    print("Case {}: {}".format(i+1, result[i]))
