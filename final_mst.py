
def cal_dis(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def dis(lst, data):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if(i == j):
                data[i][j] = 0
            else:
                data[i][j] = cal_dis(lst[i], lst[j])


def check(record, data):
    min = 10000000
    index = 0
    for i in range(0, len(record)):
        if(record[i] == -1):
            continue
        else:
            for j in range(0, len(data[0])):
                if(data[i][j] < min and record[j] == -1):
                    min = data[i][j]
                    index = j
    record[index] = 0
    if(min != 10000000):
        return min
    return 0


N1 = int(input())
result = []

for i in range(N1):
    N2 = int(input())
    sum = 0
    D = []
    data = [[0 for column in range(N2)]
            for row in range(N2)]
    for j in range(0, N2):
        ID = input()
        ID = ID.split(" ")
        ID = [eval(K) for K in ID]
        D.append(ID)
    dis(D, data)
    record = [-1 for column in range(N2)]
    record[0] = 0
    for i in range(N2):
        sum += check(record, data)
    result.append(sum)

for i in range(N1):
    print(result[i])
