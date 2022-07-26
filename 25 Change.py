a = int(input())
result = []

for i in range(a):
    n, s = list(map(int, input().strip().split()))
    while n == s == 0:
        code = 0
        break
    else:
        code = 1
        arr = list(map(int, input().split()))

        m = [[-1 for i in range(s+1)] for j in range(len(arr))]
        m[len(arr)-1][0] = 0

        x = len(arr) - 1
        while x >= 0:
            y = 0
            while y <= s:
                if y - arr[x] >= 0 and m[x][y - arr[x]] != -1:
                    m[x][y] = m[x][y - arr[x]] + 1
                if x+1 < len(arr) and m[x+1][y] != -1:
                    if m[x][y] == -1:
                        m[x][y] = m[x+1][y]
                    else:
                        if m[x][y] > m[x+1][y]:
                            m[x][y] = m[x+1][y]
                y += 1
            x -= 1
        result.append(m[0][s])

for i in range(a):
    if code == 1:
        print(result[i])
