import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y, prv, mode):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < N): continue
        if visited[nx][ny]: continue

        if mode == 1:
            if prv != raw[nx][ny]: continue
            else:
                dfs(nx, ny, raw[nx][ny], mode)
        else:
            if (prv == raw[nx][ny]) or (prv == 'R' and raw[nx][ny] == 'G') or (prv == 'G' and raw[nx][ny] == 'R'):
                dfs(nx, ny, raw[nx][ny], mode)



N = int(input())
raw = [list(map(str, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 적록색약이 아닌 경우 구역의 개수
ansA = 0 
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue

        ansA += 1
        dfs(i, j, raw[i][j], 1)

# 적록색약인 경우 구역의 개수
ansB = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue

        ansB += 1
        dfs(i, j, raw[i][j], 2)

print(ansA, ansB)