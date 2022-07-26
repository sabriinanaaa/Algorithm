import math

a = int(input())
result = [0 for i in range(a)]
total = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    t = math.ceil((math.sqrt((n+1)*8+1)-1)/2)
    total[i] = t
    count = 0
    for j in range(t+1):
        count = count + j
    result[i] = count - n

for i in range(a):
    print(result[i], total[i])
