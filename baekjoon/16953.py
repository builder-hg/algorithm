import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
dist = {}

que = deque()
que.append(A)
dist[A] = dist.get(A, 0) + 1
while len(que) > 0:
    cur = que[0]
    que.popleft()

    if cur == B:
        break

    for nxt in [cur * 2, cur * 10 + 1]:
        if dist.get(nxt, 0):
            continue

        if nxt > B:
            continue

        que.append(nxt)
        dist[nxt] = dist.get(cur, 0) + 1
        
if dist.get(B, 0):
    print(dist[B])
else:
    print(-1)