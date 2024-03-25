import sys
input = sys.stdin.readline

N = int(input())    # 노드개수
M = int(input())    # 간선개수
v = [[] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]
ans = 0

for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)


def dfs(cur):
    global ans
    
    visited[cur] = True
    ans += 1

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

dfs(1)
print(ans - 1)
