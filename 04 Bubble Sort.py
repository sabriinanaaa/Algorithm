a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    data = list(map(int, input().strip().split()))[:n]
    for j in range(n-1):
        for k in range(n-j-1):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]
                result[i] = result[i] + 1

for i in range(a):
    print(f"Optimal swapping takes {result[i]} swaps.")
