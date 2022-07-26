a = int(input())
result = []

for i in range(a):
    n, m = list(map(int, input().strip().split()))
    count = [0 for c in range(m)]
    dna = []
    for f in range(m):
        dna.append(list(input().strip()))

    for j in range(m):
        for k in range(n-1):
            for l in range(k+1, n):
                if ord(dna[j][k]) > ord(dna[j][l]):
                    count[j] = count[j] + 1

    for d in range(m-1):
        for b in range(m-d-1):
            if count[b] > count[b+1]:
                s1 = count[b]
                count[b] = count[b+1]
                count[b+1] = s1

                s2 = dna[b]
                dna[b] = dna[b+1]
                dna[b+1] = s2
    print(' ')
    for x in range(m):
        print("".join(str(i) for i in dna[x]))
    if i != a-1:
        print(' ')


# #me

# a = int(input())
# print('\n')
# result = []


# for i in range(a):
#     n, m = list(map(int, input().strip().split()))

#     count = [0 for c in range(m)]
#     dna = []
#     for f in range(m):
#         dna.append(list(input().strip()))

#     for j in range(m):
#         for k in range(n-1):
#             for l in range(k+1, n):
#                 if ord(dna[j][k]) > ord(dna[j][l]):
#                     count[j] = count[j] + 1

#     for d in range(m-1):
#         for b in range(m-d-1):
#             if count[b] > count[b+1]:
#                 s1 = count[b]
#                 count[b] = count[b+1]
#                 count[b+1] = s1

#                 s2 = dna[b]
#                 dna[b] = dna[b+1]
#                 dna[b+1] = s2

#     print('\n')
#     for i in range(m):
#         result.append(dna[i])
#         if i == m-1:
#             result.append('\n')

# for i in range(len(result)):
#     print("".join(str(x) for x in result[i]))
