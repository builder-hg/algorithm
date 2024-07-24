import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
raw = [0] + list(map(int, input().split()))
v = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    s = i + 1
    for j in range(s, s + raw[i]):
        if j > N:
            continue

        v[i].append(j)

que = deque()
visited = [False for _ in range(N + 1)]
dist = [(1 << 30) for _ in range(N + 1)]

que.append(1)
visited[1] = True
dist[1] = 0
while len(que) > 0:
    cur = que[0]
    que.popleft()

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1

if dist[N] != (1 << 30):
    print(dist[N])
else:
    print(-1)