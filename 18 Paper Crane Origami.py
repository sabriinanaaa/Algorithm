import math
count = 0
result = []

while True:

    allsize = []
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            w, h = list(map(int, input().strip().split()))
            size = math.sqrt((w * h) / 4)
            allsize.append(size)
        max = 0
        for j in range(n-1):
            if allsize[j+1] > allsize[j]:
                max = j+1
        result.append(max+1)
        count = count + 1

for i in range(count):
    print(result[i])
