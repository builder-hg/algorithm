import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    if not raw[x][y]:
        return
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < N and 0 <= ny < M):
            continue

        if visited[nx][ny]:
            continue

        dfs(nx, ny)

while True:
    M, N = map(int, input().split())

    if N == 0 and M == 0:
        break

    raw = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]   
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited = [[False for _ in range(M)] for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            visited[i][j] = True
            if not raw[i][j]:
                continue

            ans += 1
            dfs(i, j)

    print(ans)

