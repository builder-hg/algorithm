import sys
input = sys.stdin.readline

def checkOper(k):
    if k == '+' or k == '-' or k == '*' or k == '/':
        return True
    
    return False

def calc(mode):
    b = stack.pop()
    a = stack.pop()

    if mode == '+':
        return a + b
    elif mode == '-':
        return a - b
    elif mode == '*':
        return a * b
    else:
        return a / b

dic = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,
        'H':7,'I':8, 'J':9, 'K':10, 'L':11, 'M': 12,
        'N': 13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S': 18,
        'T':19, 'U':20, 'V':21, 'W':22, 'X':23,'Y':24, 'Z': 25}

N = int(input())
arr = list(map(str, input().strip()))
num = []
for _ in range(N):
    a = int(input())
    num.append(a)

stack = []
for i in range(len(arr)):
    if not checkOper(arr[i]):
        index = dic[arr[i]]
        stack.append(num[index])
        continue

    val = calc(arr[i])
    stack.append(val)

ans = f'{stack[0]:.2f}'
print(ans)