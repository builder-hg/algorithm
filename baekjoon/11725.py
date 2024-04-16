import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur, prv):
    for nxt in v[cur]:
        if nxt == prv:
            continue

        par[nxt] = cur
        dfs(nxt, cur)

N = int(input())
v = [[] for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

dfs(1, 0)
for i in range(2, N + 1):
    print(par[i])