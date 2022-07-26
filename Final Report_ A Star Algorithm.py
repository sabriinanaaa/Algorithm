# define three nodes in order to graph the route
# because the graph is fixed with 3 node in each stage
class node:
    def __init__(self, n="", V=0, n1=None, n2=None, n3=None, d1=0, d2=0, d3=0):
        self.Name = n
        self.Value = V
        self.next1 = n1
        self.next2 = n2
        self.next3 = n3
        self.dis1 = d1
        self.dis2 = d2
        self.dis3 = d3


# define a fuction to find the minimum
def minimum(a, b, c):
    if(a < b and a < c):
        return a
    if(b < a and b < c):
        return b
    if(c < a and c < b):
        return c


# define a function to calculate the value of f(n) according to the concept of A* algorithm
# f(n) = g(n) + h(n)
# devide into two situation: before update and after update
def cal(n1, n2):
    if(n1.next1 == n2):
        if(n1.Value == 1000):
            return n1.dis1 + minimum(n2.dis1, n2.dis2, n2.dis3)
        else:
            return minimum(n2.dis1, n2.dis2, n2.dis3) + n1.Value - minimum(n1.dis1, n1.dis2, n1.dis3) + n1.dis1
    if(n1.next2 == n2):
        if(n1.Value == 1000):
            return n1.dis2 + minimum(n2.dis1, n2.dis2, n2.dis3)
        else:
            return minimum(n2.dis1, n2.dis2, n2.dis3) + n1.Value - minimum(n1.dis1, n1.dis2, n1.dis3) + n1.dis2
    if(n1.next3 == n2):
        if(n1.Value == 1000):
            return n1.dis3 + minimum(n2.dis1, n2.dis2, n2.dis3)
        else:
            return minimum(n2.dis1, n2.dis2, n2.dis3) + n1.Value - minimum(n1.dis1, n1.dis2, n1.dis3) + n1.dis3


# define a function to update the default node value (1000) by the calculated f(n) value
# "n1.next1 != None" is used to avoid occur stage 5
# because each node will extend to three new node respectively
# three cases (next1, next2, next3) defined are needed
def renew(n1):
    if(n1.next1.Value > cal(n1, n1.next1) and n1.next1 != None):
        n1.next1.Value = cal(n1, n1.next1)
    if(n1.next2.Value > cal(n1, n1.next2) and n1.next1 != None):
        n1.next2.Value = cal(n1, n1.next2)
    if(n1.next3.Value > cal(n1, n1.next3) and n1.next1 != None):
        n1.next3.Value = cal(n1, n1.next3)


# input number of test data
n = int(input())
# make a list for result
result = []

# main code
for i in range(n):
    # input the cost of 24 branches
    a = []
    for j in range(24):
        data = int(input())
        a.append(data)
    # input the required stage number
    b = int(input())

    # build empty node as node list
    Node = []
    A = node()
    B = node()
    C = node()
    D = node()
    E = node()
    F = node()
    G = node()
    H = node()
    I = node()
    T = node()
    S = node()

    # import value, name and the connected nodes of each node
    # in order to graph the full route
    I = node(I, 1000, T, None, None, a[23], 1000, 1000)
    H = node(H, 1000, T, None, None, a[22], 1000, 1000)
    G = node(G, 1000, T, None, None, a[21], 1000, 1000)
    F = node(F, 1000, G, H, I, a[18], a[19], a[20])
    E = node(E, 1000, G, H, I, a[15], a[16], a[17])
    D = node(D, 1000, G, H, I, a[12], a[13], a[14])
    C = node(C, 1000, D, E, F, a[9], a[10], a[11])
    B = node(B, 1000, D, E, F, a[6], a[7], a[8])
    A = node(A, 1000, D, E, F, a[3], a[4], a[5])
    S = node(S, 1000, A, B, C, a[0], a[1], a[2])

    # append all node, finish the graph
    Node.append(S)
    Node.append(A)
    Node.append(B)
    Node.append(C)
    Node.append(D)
    Node.append(E)
    Node.append(F)
    Node.append(G)
    Node.append(H)
    Node.append(I)

    # according to the input stage number,
    # decide what stage the calculation have to stop
    ans = []
    if(b == 2):
        ans.append(S.next1.Name)
        ans.append(S.next2.Name)
        ans.append(S.next3.Name)
    if(b == 3):
        ans.append(A.next1.Name)
        ans.append(A.next2.Name)
        ans.append(A.next3.Name)
    if(b == 4):
        ans.append(D.next1.Name)
        ans.append(D.next2.Name)
        ans.append(D.next3.Name)
    if(b == 5):
        ans.append(G.next1.Name)
        ans.append(G.next2.Name)
        ans.append(G.next3.Name)

    # start the calculation
    # append the first node "S" as the start
    tra = []
    tra.append(Node[0])

    # use while-loop to calculate and renew the value of f(x)
    while(len(tra) != 0):
        mini = 100000
        index = -1
        for i in range(0, len(tra)):
            # if the node value < currently smallest node value,
            # then update the smallest node value
            if(tra[i].Value < mini):
                mini = tra[i].Value
                index = i

        # renew the node
        renew(tra[index])

        # append the node's updated f(n) value
        if(ans.count(tra[index].next1.Name) == 0):
            tra.append(tra[index].next1)
            tra.append(tra[index].next2)
            tra.append(tra[index].next3)

        # delete the initial f(n) value of the node
        del tra[index]

        if(len(tra) == 0):
            break
    # according to the input stage number,
    # decide which stage's minimum f(n) value is required to output
    if(b == 2):
        result.append(minimum(A.Value, B.Value, C.Value))
    if(b == 3):
        result.append(minimum(D.Value, E.Value, F.Value))
    if(b == 4):
        result.append(minimum(G.Value, H.Value, I.Value))
    if(b == 5):
        result.append(T.Value)

# print out the result
for i in range(n):
    print(result[i])
