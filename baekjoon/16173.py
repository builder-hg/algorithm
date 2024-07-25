import sys
from collections import deque
input = sys.stdin.readline

que = deque()

N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

fin = False
que.append([0, 0])
visited[0][0] = True
while len(que) > 0:
    x, y = que[0][0], que[0][1]
    que.popleft()

    jump = raw[x][y]

    if x == N - 1 and y == N - 1:
        fin = True
        break

    for step in [[0, jump], [jump, 0]]:
        nx = x + step[0]
        ny = y + step[1]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        if visited[nx][ny]:
            continue

        que.append([nx, ny])
        visited[nx][ny] = True

if fin:
    print("HaruHaru")
else:
    print("Hing")