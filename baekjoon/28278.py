import sys
input = sys.stdin.readline

Q = int(input())
stack = []
while Q:
    Q -= 1

    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if not len(stack):
            print(-1)
            continue

        lastest = stack.pop()
        print(lastest)
    elif query[0] == 3:
        print(len(stack))
    elif query[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if not len(stack):
            print(-1)
            continue

        print(stack[-1])