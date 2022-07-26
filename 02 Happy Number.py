a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    n = int(input())
    while n != 1 or n != 4:
        n = (n//100) ** 2 + ((n//10) % 10) ** 2 + (n % 10) ** 2

        if len(str(n)) < 2:
            break
    if n == 1:
        result[i] = 1
    elif n == 4:
        result[i] = 0

for i in range(a):
    if result[i] == 1:
        print("Happy")
    elif result[i] == 0:
        print("Not Happy")
