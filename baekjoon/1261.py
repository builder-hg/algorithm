import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que.append([0, 0])
    visited[0][0] = True
    dist[0][0] = [0, 0]

    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue

            if arr[nx][ny] == '1':
                dist[nx][ny] = [dist[x][y][0] + 1, dist[x][y][1] + 1]
                que.append([nx, ny])
            else:
                dist[nx][ny] = [dist[x][y][0] + 1, dist[x][y][1]]
                que.appendleft([nx, ny])
            visited[nx][ny] = True


M, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
que = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
dist = [[[-1, 0] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
print(dist[N - 1][M - 1][1])