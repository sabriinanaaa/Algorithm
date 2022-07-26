a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    title = str(input())
    for k in range(len(title)):
        result[i] = result[i] * 26
        result[i] = result[i] + ord(title[k]) - ord("A") + 1

for i in range(a):
    print(result[i])
