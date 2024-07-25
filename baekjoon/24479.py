import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur):
    global cnt

    visited[cur] = True
    dist[cur] = cnt

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        cnt += 1
        dfs(nxt)


N, M, R = map(int, input().split())

v = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)
for i in range(1, N + 1):
    v[i].sort()

visited = [False for _ in range(N + 1)]
dist = [0 for _ in range(N + 1)]

cnt = 1
dfs(R)

for value in dist[1:]:
    print(value)