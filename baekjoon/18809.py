"""
1. 배양액을 뿌릴 수 있는 땅에 초록색, 빨간색 배양액을 분배한다.
    - 해당 칸에 빨간 배양액을 뿌리거나, 뿌리지 않거나
    - 해당 칸에 초록 배양액을 뿌리거나, 뿌리지 않거나
2. 각각의 경우에서 꽃이 피는 개수를 헤아린다.
    - 빨간
"""
import sys
sys.setrecursionlimit(10010)
from collections import deque
input = sys.stdin.readline

def findFlower():
    global ans

    que = deque()
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if log[i][j] == 1:
                que.append([i, j, -1, -1, 1, 0])                    # x 좌표, y 좌표, 이전 x좌표, 이전 y 좌표, 초록/빨강 배양색 타입, 시간,
            elif log[i][j] == 2:
                que.append([i, j, -1, -1, 2, 0])

    tmp = 0
    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        prvX = que[0][2]
        prvY = que[0][3]
        type = que[0][4]                                        # 초록색 배양액은 1, 빨강색 배양액은 2
        time = que[0][5]
        que.popleft()

        if visited[prvX][prvY] == [99, 99]:
            continue

        if visited[x][y] != [-1, -1]:
            if visited[x][y][0] != type and visited[x][y][1] == time:
                visited[x][y] = [99, 99]
                tmp += 1

            continue

        visited[x][y] = [type, time]

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visited[nx][ny] != [-1, -1]:
                continue

            if raw[nx][ny] == 0:
                continue

            que.append([nx, ny, x, y, type, time + 1])

    ans = max(ans, tmp)

def recur(curX, curY, green, red):                          # 배양액을 알맞게 뿌리는 경우를 구하는 함수.
    if green > G or red > R:
        return

    if curY == M:
        curX += 1
        curY = 0
    
    if curX == N:
        if not (green == G and red == R):
            return
            
        findFlower()
        return
    
    if raw[curX][curY] != 0 and raw[curX][curY] != 1:        # 해당 땅이 배양액을 뿌릴 수 있다면
        log[curX][curY] = 1
        recur(curX, curY + 1, green + 1, red)                   # 초록색 배양액을 뿌리거나
        log[curX][curY] = 2
        recur(curX, curY + 1, green, red + 1)                   # 빨간색 배양액을 뿌리거나
    log[curX][curY] = -1
    recur(curX, curY + 1, green, red)                       # 아무것도 뿌리지 않거나



N, M, G, R = map(int, input().split())                      # 행의 개수, 열의 개수, 초록색 배양액 개수, 빨간색 배양액 개수
raw = [list(map(int, input().split())) for _ in range(N)]   # 정원, 호수 0, 배양액 뿌릴 수 없는 땅 1, 배양액 뿌릴 수 있는 땅 2
log = [[-1 for _ in range(M)] for _ in range(N)]            # 뿌린 배양액 기록, 초록색은 1, 빨간색은 2        

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
recur(0, 0, 0, 0)

print(ans)