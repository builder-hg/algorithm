import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    global tmp

    visited[x][y] = True
    tmp += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M) or arr[nx][ny] == 0: continue

        if visited[nx][ny]: continue

        dfs(nx, ny)

N, M, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1

ans = 0
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: continue

        if visited[i][j]: continue

        tmp = 0
        dfs(i, j)
        ans = max(ans, tmp)

print(ans)