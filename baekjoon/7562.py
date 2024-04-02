import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        if x == ex and y == ey:
            return dist[x][y] - 1
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1
            que.append([nx, ny])

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]


Q = int(input())
while Q:
    Q -= 1

    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    que = deque()
    dist = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    que.append([sx, sy])
    visited[sx][sy] = True
    dist[sx][sy] = 1
    print(bfs())
    