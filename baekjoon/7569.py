import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global yet 

    while len(que) > 0:
        h, x, y = que[0][0], que[0][1], que[0][2]
        que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visited[h][nx][ny]:
                continue

            if raw[h][nx][ny] == -1:
                continue

            que.append([h, nx, ny])
            visited[h][nx][ny] = True
            yet -= 1
            dist[h][nx][ny] = dist[h][x][y] + 1

        for i in range(2):
            nh = dh[i] + h

            if not (0 <= nh < H):
                continue

            if visited[nh][x][y]:
                continue

            if raw[nh][x][y] == -1:
                continue

            que.append([nh, x, y])
            visited[nh][x][y] = True
            yet -= 1
            dist[nh][x][y] = dist[h][x][y] + 1

M, N, H = map(int, input().split())
raw = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

que = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
dist = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dh = [-1, 1]

yet = H * N * M
for h in range(H):
    for x in range(N):
        for y in range(M):
            if raw[h][x][y] == 0:
                continue

            yet -= 1
            if raw[h][x][y] == 1:
                que.append([h, x, y])
                visited[h][x][y] = True

if not yet:
    print(0)
else:
    bfs()
    if yet:
        print(-1)
    else:
        ans = 0
        for h in range(H):
            for x in range(N):
                ans = max(ans, max(dist[h][x]))

        print(ans)