import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y, dir, cnt):
    if x >= N or y >= N:
        return 0
    
    if cnt < 0:
        return 0

    if x < N and y < N:
        if arr[x][y] == 'H':
            return 0

    if x == N-1 and y == N-1:
        return 1
    
    if dp[x][y][dir][cnt] != -1:
        return dp[x][y][dir][cnt]

    ret = 0
    if x == 0 and y == 0:
        ret += recur(x + 1, y, 0, cnt)
        ret += recur(x, y + 1, 1, cnt)
    else:
        if dir == 0: # 왼쪽에서 왔다면
            ret += recur(x + 1, y, 0, cnt)
            ret += recur(x, y + 1, 1, cnt - 1)
        if dir == 1: # 위에서 왔다면
            ret += recur(x + 1, y, 0, cnt - 1)
            ret += recur(x, y + 1, 1, cnt)

    dp[x][y][dir][cnt] = ret
    return dp[x][y][dir][cnt]

Q = int(input())
while Q:
    Q -= 1
    N, K = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    dp = [[[[-1 for _ in range(4)] for _ in range(2)] for _ in range(N)] for _ in range(N)]
    ans = recur(0, 0, 0, K)
    print(ans)
