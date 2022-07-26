a = int(input())
result = [0 for i in range(a)]

def kthSmallest(arr, k):
    arr.sort()
    return arr[k-1]

for i in range(a):
    h = list(map(int, input().split()))
    n = int(input())
    result[i] = kthSmallest(h, n)
    
for i in range(a):
    print(result[i])