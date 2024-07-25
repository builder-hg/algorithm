import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if visited[nx][ny]:
            continue

        if not raw[nx][ny]:
            if raw[x][y] >= 1:
                raw[x][y] -= 1

            continue

        dfs(nx, ny)


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 1
while True:
    tmp = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            if visited[i][j]:
                continue

            if not raw[i][j]:
                continue
            
            tmp += 1
            dfs(i, j)

    if tmp > 1:
        break
    elif tmp == 0:
        cnt = 1
        break
    
    cnt += 1

print(cnt - 1)

