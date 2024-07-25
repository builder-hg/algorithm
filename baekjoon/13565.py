import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    que = deque()
    que.append([x, y])
    visitied[x][y] = True
    while len(que) > 0:
        x, y = que[0][0], que[0][1]
        que.popleft()

        if x == N - 1:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visitied[nx][ny]:
                continue

            if raw[nx][ny] == '1':
                continue

            que.append([nx, ny])
            visitied[nx][ny] = True

    return False



N, M = map(int, input().split())
raw = [list(map(str, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

chk = False
for i in range(M):
    if raw[0][i] == '1':
        continue

    visitied = [[False for _ in range(M)] for _ in range(N)]
    chk = bfs(0, i)

    if chk:
        break

if chk:
    print("YES")
else:
    print("NO")