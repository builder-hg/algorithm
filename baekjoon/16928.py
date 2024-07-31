import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que.append([0, 0])
    visited[0][0] = True
    dist[0][0] = 0
    while len(que) > 0:
        x, y = que[0][0], que[0][1]
        que.popleft()

        if x == 9 and y == 9:
            print(dist[9][9])

        if VL[x][y]:
            nx, ny = VL[x][y][0], VL[x][y][1]
            que.appendleft([nx, ny])
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y]
            continue

        if VS[x][y]:
            nx, ny = VS[x][y][0], VS[x][y][1]
            que.appendleft([nx, ny])
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y]
            continue

        for i in range(1, 7):
            nx = x
            ny = y + i

            if ny > 9:
                nx = x + 1
                ny %= 10

            if not (0 <= nx < 10 and 0 <= ny < 10):
                continue

            if visited[nx][ny]:
                continue

            que.append([nx, ny])
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1



L, S = map(int, input().split())                                # 사다리의 개수 L, 뱀의 수 S
VL = [[[] for _ in range(10)] for _ in range(10)]
VS = [[[] for _ in range(10)] for _ in range(10)]
for _ in range(L):
    a, b = map(int, input().split())
    sx, sy = a // 10, a % 10 - 1
    if not a % 10:
        sx -= 1
        sy = 9

    ex, ey = b // 10, b % 10 - 1
    if not b % 10:
        ex -= 1
        ey = 9

    VL[sx][sy] = [ex, ey]

for _ in range(S):
    a, b = map(int, input().split())
    sx, sy = a // 10, a % 10 - 1
    if not a % 10:
        sx -= 1
        sy = 9

    ex, ey = b // 10, b % 10 - 1
    if not b % 10:
        ex -= 1
        ey = 9

    VS[sx][sy] = [ex, ey]

visited = [[False for _ in range(10)] for _ in range(10)]          
dist = [[-1 for _ in range(10)] for _ in range(10)]

que = deque()
bfs()