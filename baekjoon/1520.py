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