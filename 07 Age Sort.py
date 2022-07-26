count = 0
result = []

while True:
    n = int(input())

    if n == 0:
        break
    else:
        s = list(map(int, input().strip().split(" ")))[:n]
        ss = sorted(s)
        sss = " ".join(str(i) for i in ss)
        result.append(sss)
        count = count + 1

for i in range(count):
    # x = " ".join(result[i])
    print(result[i])
