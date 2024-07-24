import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(x, y):
    ret = 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if visited[nx][ny]:
            continue

        if not raw[nx][ny]:
            visited[nx][ny] = True
            continue

        ret += dfs(nx, ny)

    return ret


M, N, K = map(int, input().split())
raw = [[1 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            raw[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
arr = []
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        if not raw[i][j]:
            visited[i][j] = True
            continue

        cnt += 1
        size = dfs(i, j)
        arr.append(size)

print(cnt)
print(*sorted(arr))