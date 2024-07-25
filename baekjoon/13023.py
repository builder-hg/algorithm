import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(cur, depth):
    global chk

    if depth == 4:
        chk = True
        return

    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt, depth + 1)

    visited[cur] = False

N, M = map(int, input().split())
v = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    v[a + 1].append(b + 1)
    v[b + 1].append(a + 1)


visited = [False for _ in range(N + 1)]
chk = False
for i in range(1, N + 1):
    dfs(i, 0)

    if chk:
        break

if chk:
    print(1)
else:
    print(0)