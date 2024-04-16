import sys
sys.setrecursionlimit(10 ** 4 + 10)
input = sys.stdin.readline

def dfs(cur, prv, dis):
    global mx, idx

    if mx < dis:
        mx = dis
        idx = cur

    for nxt, nd in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt, cur, dis + nd)


N = int(input())
v = [[] for _ in range(N + 1)]
arr = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())

    v[a].append([b, c])
    v[b].append([a, c])

mx = -1
idx = 0
dfs(1, 0, 0)

mx = -1
dfs(idx, 0, 0)

print(mx)