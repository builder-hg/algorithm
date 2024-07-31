import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1

    query = list(map(str, input().strip()))
    N = int(input())
    raw = input().strip()[1:-1].split(",")
    
    que = deque()
    for i in range(len(raw)):
        if raw[i] == '':
            continue

        que.append(raw[i])

    error = False
    reverse = 0
    for q in query:
        if q == 'R':
            reverse += 1
        elif q == 'D':
            if len(que) > 0:
                if reverse % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
            else:
                error = True
                break

    if error:
        print('error')
    else:
        if reverse % 2:
            que.reverse()
            
        print("[" + ",".join(que) + "]")

