import sys
input = sys.stdin.readline

def dfs(cur, prv):
    sz[cur] = 1             # 나 자신이 존재하기에 사이즈의 초깃값은 1이다.
    for nxt in v[cur]:
        if nxt == prv or nxt == R:
            continue

        dfs(nxt, cur)
        sz[cur] += sz[nxt]

N = int(input())
par = list(map(int, input().split()))
R = int(input())

v = [[] for _ in range(N)]
for i in range(len(par)):
    if par[i] == -1:
        continue

    v[par[i]].append(i)
    v[i].append(par[i])

S = -1
for i in range(len(par)):
    if par[i] == -1:
        S = i

if R == S:
    print(0)
    sys.exit()

sz = [-1 for _ in range(N)]
v[R] = []
dfs(S, -1)

ans = 0
for i in range(len(sz)):
    if sz[i] == 1:  
        ans += 1

print(ans)