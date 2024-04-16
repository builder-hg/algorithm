import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline

def dfs(cur, prv):
    sz[cur] = 1
    for nxt in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt, cur)
        sz[cur] += sz[nxt]

N, R, Q = map(int, input().split())
v = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)
sz = [0 for _ in range(N + 1)]

dfs(R, 0)
for _ in range(Q):
    root = int(input())

    print(sz[root])