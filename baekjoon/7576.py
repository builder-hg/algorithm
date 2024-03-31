import sys
from collections import deque
input = sys.stdin.readline

def find():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                que.append([i, j])

def bfs():
    while len(que) > 0 :
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or arr[nx][ny] == -1 or arr[nx][ny] == 1:
                continue
            
            arr[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
            que.append([nx, ny])

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
que = deque()
ans = 0
dist = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

find()
bfs()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            sys.exit()

    ans = max(ans, max(dist[i]))

if ans == 0: print(0)
else:
    print(ans + 1)