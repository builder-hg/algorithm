import sys
sys.setrecursionlimit(10 ** 6)
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
            continue

        ret += dfs(nx, ny)

    return ret




N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
size = 0
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        if not (raw[i][j]):
            continue

        cnt += 1
        size = max(size, dfs(i, j))

print(cnt)
print(size)