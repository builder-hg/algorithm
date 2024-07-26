import sys
input = sys.stdin.readline

def preorder(cur):
    global ansA

    if cur == -1:
        return
    
    ansA += alpha[cur]
    preorder(v[cur][0])
    preorder(v[cur][1])

def inorder(cur):
    global ansB

    if cur == -1:
        return
    
    inorder(v[cur][0])
    ansB += alpha[cur]
    inorder(v[cur][1])

def postorder(cur):
    global ansC

    if cur == -1:
        return
    
    postorder(v[cur][0])
    postorder(v[cur][1])
    ansC += alpha[cur]

N = int(input())
idx = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,
        'H':7,'I':8, 'J':9, 'K':10, 'L':11, 'M': 12,
        'N': 13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S': 18,
        'T':19, 'U':20, 'V':21, 'W':22, 'X':23,'Y':24, 'Z': 25}
alpha = {value:key for key, value in idx.items()}
v = [[-1, -1] for _ in range(N)]
for _ in range(N):
    a, b, c = map(str, input().split())
    
    par = idx[a]
    if idx.get(b, -1) >= 0:
        v[par][0] = idx[b]
    if idx.get(c, -1) >= 0:
        v[par][1] = idx[c]

ansA = ''
preorder(0)
print(ansA)

ansB = ''
inorder(0)
print(ansB)

ansC = ''
postorder(0)
print(ansC)