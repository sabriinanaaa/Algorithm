import queue

class Node:
    def __init__(self, val = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

cflag = True
dflag = True

def build_Tree(current, pos, spos, value):
    global dflag
    #For root
    if pos == "":
        #If somebody is already there
        if current.val != -1: dflag = False
        #else give the value
        else: current.val = value
    
    #spos start from 0
    if spos < len(pos):
        if pos[spos] == 'L':
            
            if current.left == None:
                newLeft = Node()
                #If it is the correct position that the value should be in
                if len(pos) == (spos+1): newLeft.val = value
                current.left = newLeft
            
            else:
                if len(pos) == (spos+1):
                    if current.left.val >= 0: dflag = False
                    else: current.left.val = value
            
            build_Tree(current.left, pos, spos+1, value)
        
        elif pos[spos] == 'R':
            
            if current.right == None:
                newRight = Node()
                if len(pos) == (spos+1): newRight.val = value
                current.right = newRight
            
            else:
                if len(pos) == (spos+1):
                    if current.right.val >= 0: dflag = False
                    else: current.right.val = value

            build_Tree(current.right, pos, spos+1, value)

q = queue.Queue()
def Level_Order(current, output):
    q.put(current)
    #print(q.queue[0].val, end = "")
    output.append(q.queue[0].val)
    if q.queue[0].left != None: q.put(q.queue[0].left)
    if q.queue[0].right != None: q.put(q.queue[0].right)
    q.get()
    while not q.empty():
        #print(" ", end="")
        #print(q.queue[0].val, end = "")
        output.append(q.queue[0].val)
        if q.queue[0].left != None: q.put(q.queue[0].left)
        if q.queue[0].right != None: q.put(q.queue[0].right)
        q.get()
    

def check_Empty(current):
    global cflag
    if (current.val < 0): cflag = False
    if current.left is not None: check_Empty(current.left)
    if current.right is not None: check_Empty(current.right)

N = int(input())
result = []
for i in range(N):
    output = []
    #input preprocessing
    tree_string = list(input().strip().split())
    tree_string_positions = []
    tree_string_values = []
    for i in range(len(tree_string)-1):
        val, pos = tree_string[i].strip('()').split(',')
        tree_string_values.append(int(val))
        tree_string_positions.append(pos)

    root = Node()
    for i in range(len(tree_string_values)):
        build_Tree(root, tree_string_positions[i] ,0, tree_string_values[i])

    check_Empty(root)
    if dflag == False:
        result.append("not complete")
    elif cflag == False:
        result.append("not complete")
    else:
        Level_Order(root, output)
        result.append(output)
    dflag = 1
    cflag = 1
for i in range(N):
    if result[i] == "not complete":
        print(result[i])
    else:
        print(' '.join(map(str,result[i])))