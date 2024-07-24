import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

que = deque()
v = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

for i in range(1, N + 1):
    v[i].sort()

visited = [False for _ in range(N + 1)]
dist = [0 for _ in range(N + 1)]
mySize = 1

que.append(R)
visited[R] = True
while len(que) > 0:
    cur = que[0]
    que.popleft()

    dist[cur] = mySize
    mySize += 1

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True

for val in dist[1:]:
    print(val)