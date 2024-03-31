import sys
input = sys.stdin.readline

def dfs(cur):
    global ans

    visited[cur] = True
    ans += 1

    if cur == B:
        print(ans - 1)
        sys.exit()

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)
    ans -= 1

N = int(input())
A, B = map(int, input().split())
M = int(input())
v = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
ans = 0
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

dfs(A)
print(-1)