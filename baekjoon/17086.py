import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    que = deque()
    que.append([x, y, 1])
    visited[x][y] = True
    while len(que) > 0:
        x, y, dis = que[0][0], que[0][1], que[0][2]
        que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visited[nx][ny]:
                continue

            if raw[nx][ny] == 1:
                return dis
            
            que.append([nx, ny, dis + 1])
            visited[nx][ny] = True

N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

ans = 0
for i in range(N):
    for j in range(M):
        if raw[i][j] != 0:
            continue
        
        visited = [[False for _ in range(M)] for _ in range(N)]
        ans = max(ans, bfs(i, j))

print(ans)
