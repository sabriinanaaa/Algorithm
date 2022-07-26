
a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    s, t = list(map(str, input().strip().split(" ")))  # [:2]
    same = 0
    n = 0
    for j in range(len(s)):
        for k in range(n, len(t)):
            if s[j] == t[k]:
                same = same + 1
                n = k + 1
                break
    if len(s) == same:
        result[i] = 1
    else:
        result[i] = 0

for i in range(a):
    if result[i] == 1:
        print("Yes")
    elif result[i] == 0:
        print("No")
