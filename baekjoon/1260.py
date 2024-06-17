import sys
from collections import deque
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True
    ansA.append(cur)

    for nxt in v[cur]:
        if visited[nxt]: continue

        dfs(nxt)

N, M, START = map(int, input().split())
v = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

for i in range(len(v)):
    v[i] = sorted(v[i])

ansA = []
ansB = []

visited = [False for _ in range(N + 1)]
visited[START] = True

dfs(START)

que = deque()

que.append(START)
ansB.append(START)
visited = [False for _ in range(N + 1)]
visited[START] = True

while len(que) > 0:
    cur = que[0]
    que.popleft()

    for nxt in v[cur]:
        if visited[nxt]: continue

        que.append(nxt)
        visited[nxt] = True
        ansB.append(nxt)

print(*ansA)
print(*ansB)