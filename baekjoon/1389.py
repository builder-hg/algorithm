import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dist = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    que.append(start)
    visited[start] = True
    while len(que) > 0:
        cur = que[0]
        que.popleft()

        for nxt in v[cur]:
            if visited[nxt]: continue

            visited[nxt] = True
            dist[nxt] = dist[cur] + 1
            que.append(nxt)

    return sum(dist)

N, M = map(int, input().split())
v = [[] for _ in range(N + 1)]
que = deque()
ans = []
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

for i in range(1, N + 1):
    ans.append(bfs(i))

print(ans.index(min(ans)) + 1)