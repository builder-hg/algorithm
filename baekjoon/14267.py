import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline

def dfs(cur):
    for nxt in v[cur]:
        ans[nxt] += ans[cur]
        dfs(nxt)

N, M = map(int, input().split())
v = [[] for _ in range(N + 1)]
arr = list(map(int, input().split()))
ans = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if arr[i - 1] == -1:
        continue

    v[arr[i - 1]].append(i)

for _ in range(M):
    a, b = map(int, input().split())
    ans[a] += b

dfs(1)

ans = ans[1::]
print(*ans)