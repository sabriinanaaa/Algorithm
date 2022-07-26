import math


def solve(eq, var='x'):
    eq1 = eq.replace("=", "-(") + ")"
    eq1 = eq1.replace("x", "*x")
    eq1 = eq1.replace("+*x", "+x")
    eq1 = eq1.replace("-*x", "-x")
    eq1 = eq1.replace("(*x", "(x")
    # print(eq1)
    # print({var: 1j})
    if eq1[0] == "*":
        eq1 = eq1.lstrip("*")
    # print(eq1)
    c = eval(eq1, {var: 1j})
    # print(c)
    # print("c.real", c.real)
    # print("c.imag", c.imag)

    if c.imag == 0:
        if c.real == 0:
            return "IDENTITY"
        else:
            return "IMPOSSIBLE"
    else:
        return (math.floor(-c.real/c.imag))


a = int(input())
result = [0 for i in range(a)]

for i in range(a):
    m = input()
    result[i] = solve(m)

for i in range(a):
    print(result[i])
