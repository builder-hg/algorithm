import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def recur(x, y):
    if x >= N or y >= M or x < 0 or y < 0:
        return -(1 << 60)
    
    if x == (N-1) and y == (M-1):
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ret = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N or ny >= M or nx < 0 or ny < 0:
            continue

        if arr[x][y] <= arr[nx][ny]:
            continue

        ret += max(0, recur(nx, ny))  

    dp[x][y] = ret
    return dp[x][y]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(recur(0, 0))

























"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y, prev):
    global ans

    if x >= N or y >= M or x < 0 or y < 0:
        return
    
    if arr[x][y] >= prev:
        return

    if x == N - 1 and y == N - 1:
        ans += 1
        return

    recur(x + 1, y, arr[x][y])
    recur(x - 1, y, arr[x][y])
    recur(x, y + 1, arr[x][y])
    recur(x, y - 1, arr[x][y])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0, 0, 1e9)
print(ans)
"""