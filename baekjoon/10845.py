import sys
from collections import deque
input = sys.stdin.readline

Q = int(input())
que = deque()
while Q:
    Q -= 1
    query = list(map(str, input().split()))
    
    if query[0] == 'push':
        que.append(query[1])
    elif query[0] == 'front':
        if len(que) > 0:
            cur = que[0]
            print(cur)
        else:
            print(-1)
    elif query[0] == 'back':
        if len(que) > 0:
            cur = que[-1]
            print(cur)
        else:
            print(-1)
    elif query[0] == 'pop':
        if len(que) > 0:
            cur = que[0]
            print(cur)
            que.popleft()
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(que))
    elif query[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
