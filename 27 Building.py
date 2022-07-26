a = int(input())
result = []

for i in range(a):
    n = int(input())
    input_tuple = []
    for j in range(n):
        m = int(input())
        if m >= 0:
            input_tuple.append(('+', m))
        else:
            input_tuple.append(('-', abs(m)))
    sort_tuple = sorted(input_tuple, key=lambda x: x[1])

    count = 1
    for k in range(n-1):
        current_sign = sort_tuple[k][0]
        if current_sign != sort_tuple[k+1][0]:
            count += 1
    result.append(count)

for i in range(a):
    print(result[i])
