import sys
input = sys.stdin.readline

def dfs(curX, curY, total):
    global ans

    if curY == M:
        curX += 1
        curY = 0

    if curX == N:
        ans = max(ans, total)
        return
    
    if not visited[curX][curY]:
        for i in range(4):
            ax, ay = curX + step[i][0][0], curY + step[i][0][1]
            bx, by = curX + step[i][1][0], curY + step[i][1][1]

            if ax < 0 or ax >= N or ay < 0 or ay >= M:
                continue
            if bx < 0 or bx >= N or by < 0 or by >= M:
                continue
            if visited[ax][ay] or visited[bx][by]:
                continue

            visited[curX][curY] = True
            visited[ax][ay] = True
            visited[bx][by] = True
            dfs(curX, curY + 1, total + arr[curX][curY] * 2 + arr[ax][ay] + arr[bx][by])

            visited[curX][curY] = False
            visited[ax][ay] = False
            visited[bx][by] = False

    dfs(curX, curY + 1, total)

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

if N == 1 or M == 1:
    print(0)
    sys.exit()

step = [
    [[0, -1], [1, 0]],
    [[0, -1], [-1, 0]],
    [[-1, 0], [0, 1]],
    [[1, 0], [0, 1]]
]

visited = [[False for _ in range(M)] for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

if N == 1 or M == 1:
    print(0)
    sys.exit()

dy = [[1, M], [1, M], [0, M - 1], [0, M - 1]]
dx = [[0, N - 1], [1, N], [1, N], [0, N - 1]]
move = [
    [[-1, 0], [0, 1]],
    [[0, -1], [-1, 0]],
    [[0, -1], [1, 0]],
    [[0, 1], [1, 0]]
]

ans = 0
for type in range(4):              # 부메랑 종류 선택
    xs, xe = dx[type][0], dx[type][1]
    ys, ye = dy[type][0], dy[type][1]
    for i in range(xs, xe):
        tmp = 0
        for j in range(ys, ye):
            tmp += arr[i][j] * 2
            
            for k in range(2):
                nx = i + move[type][k][1]
                ny = j + move[type][k][0]

                tmp += arr[nx][ny]
        
            ans = max(ans, tmp)

print(ans)
"""
