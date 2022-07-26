a = int(input())
sum = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    m = int(input())
    if n % 2 == 0:
        n = n + 1
    if m % 2 == 0:
        m = m - 1
    for h in range(n, m+1, 2):
        sum[i] = sum[i] + h

for i in range(a):
    print(f"Case {i+1}: {sum[i]}")
