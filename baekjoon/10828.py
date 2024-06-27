import sys
input = sys.stdin.readline

T = int(input())
stack = []

while T:
    T -= 1
    
    query = list(map(str, input().split()))
    
    if query[0] == 'push':
        stack.append(int(query[1]))
    elif query[0] == 'top':
        if not len(stack):
            print(-1)
            continue

        print(stack[-1])
    elif query[0] == 'size':
        print(len(stack))
    elif query[0] == 'pop':
        if not len(stack):
            print(-1)
            continue

        last = stack.pop()
        print(last)
    else:
        if len(stack):
            print(0)
        else:
            print(1)