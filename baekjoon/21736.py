import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def getStartPosition():
    for i in range(N):
        for j in range(M):
            if raw[i][j] == 'I':
                return i, j

def dfs(x, y):
    global ans

    visited[x][y] = True
    if raw[x][y] == 'P':
        ans += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if visited[nx][ny]:
            continue

        if raw[nx][ny] == 'X':
            continue

        dfs(nx, ny)

N, M = map(int, input().split())
raw = [list(map(str, input().strip())) for _ in range(N)]

sx, sy = getStartPosition()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(M)] for _ in range(N)]

ans = 0
dfs(sx, sy)

if ans:
    print(ans)
else:
    print("TT")