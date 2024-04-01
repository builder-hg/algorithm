import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dis = 0
que = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que.append([0, 0])
visited[0][0] = True
while len(que) > 0:
    sz = len(que)
    for _ in range(sz):
        x, y = que[0][0], que[0][1]
        que.popleft()

        if x == N - 1 and y == M - 1:
            print(dis + 1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if arr[nx][ny] == '0' or visited[nx][ny]:
                continue

            que.append([nx, ny])
            visited[nx][ny] = True

    dis += 1


