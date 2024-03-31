import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que.append([0, 0, 1])
    visited[0][0][1] = True
    dist[0][0][1] = 0
    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        cnt = que[0][2]
        que.popleft()

        if x == (N - 1) and y == (M - 1):
            return dist[x][y][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny][cnt]:
                continue

            if arr[nx][ny] == '0':
                que.append([nx, ny, cnt])
                visited[nx][ny][cnt] = True
                dist[nx][ny][cnt] = dist[x][y][cnt] + 1
            
            if arr[nx][ny] == '1' and cnt == 1:
                que.append([nx, ny, 0])
                visited[nx][ny][0] = True
                dist[nx][ny][0] = dist[x][y][cnt] + 1


    return -2

    

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
dist = [[[-1, -1] for _ in range(M)] for _ in range(N)]
que = deque()
cnt = 0
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs() + 1)