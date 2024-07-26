import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(cur, prv):
    sz[cur] = 1
    for nxt in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt, cur)
        sz[cur] += sz[nxt]
        cnt.append(sz[nxt] * (N - sz[nxt]))

N = int(input())
v = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

weight = sorted(list(map(int, input().split())))
sz = [0 for _ in range(N + 1)]  # 루트를 i로 하는 서브트리의 크기가 저장된다.
cnt = [] # 간선이 몇 번 쓰이는 지 기록한다.

dfs(1, 1)
cnt.sort(reverse=True)

ans = 0
for i in range(len(weight)):
    ans += (cnt[i] * weight[i]) % (10 ** 9 + 7)

print(ans % (10 ** 9 + 7))