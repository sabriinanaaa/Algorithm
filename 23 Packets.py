def calculate(size, num, grid):
    for i in range(0, 6, size):
        for j in range(0, 6, size):
            if num != 0:
                flag1 = True
                if 6-i >= size and 6-j >= size:
                    for k in range(i, i+size):
                        for l in range(j, j+size):
                            if grid[k][l] != 0:
                                flag1 = False
                    if flag1 == True:
                        for a in range(i, i+size):
                            for b in range(j, j+size):
                                grid[a][b] = 1
                        num = num - 1


count = 0
result = []
while True:
    # n = list(input().split())
    n = list(map(str, input().strip().split()))
    # print(n)
    if n == ['0', '0', '0', '0', '0', '0']:
        break
    else:
        grid = [[0]*6 for i in range(6)]
        box = 0
        flag = True
        while(flag == True):
            box = box + 1
            flag = False
            print(box)
            for i in range(5, -1, -1):
                print("i=", i)
                if int(n[i]) != 0:
                    size = i+1
                    num = int(n[i])
                    for s in range(0, 6, size):
                        for t in range(0, 6, size):
                            if num != 0:
                                flag1 = True
                                if 6-s >= size and 6-t >= size:
                                    for u in range(s, s+size):
                                        for v in range(t, t+size):
                                            if grid[u][v] != 0:
                                                flag1 = False
                                    if flag1 == True:
                                        for u in range(s, s+size):
                                            for v in range(t, t+size):
                                                grid[u][v] = 1
                                        num = num - 1
                    # calculate(i+1, int(n[i]), grid)
                    print("end of calculate", n[i])
                    if int(n[i]) != 0:
                        flag = True
            for j in range(6):
                for k in range(6):
                    grid[j][k] = 0
            print(flag)
        result.append(box)
        count = count + 1

for i in range(count):
    print(result[i])
