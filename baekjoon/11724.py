import sys
input = sys.stdin.readline

N, M = map(int, input().split())
v = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
visited[0] = True
ans = 0

for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

for i in range(N + 1):
    if visited[i]:
        continue

    ans += 1
    dfs(i)

print(ans)