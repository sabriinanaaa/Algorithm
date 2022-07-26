
def solve(m, n):
    dp = []
    for i in range(m):
        dp1 = []
        dp.append(dp1)
        for j in range(n):
            dp[i].append(0)

    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for k in range(1, m):
        for l in range(1, n):
            dp[k][l] = dp[k-1][l] + dp[k][l-1]

    return int(dp[m-1][n-1])


a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    m, n = list(map(int, input().strip().split()))
    result[i] = solve(m, n)

for i in range(a):
    print(result[i])
