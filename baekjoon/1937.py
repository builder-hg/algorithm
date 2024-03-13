import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y, prev, cnt):
    global ans

    if x >= N or y >= N or x < 0 or y < 0:
        return

    if arr[x][y] < prev:
        return

    ans = max(ans, cnt)

    recur(x - 1, y, arr[x][y], cnt + 1)
    recur(x, y - 1, arr[x][y], cnt + 1)
    recur(x, y + 1, arr[x][y], cnt + 1)
    recur(x + 1, y, arr[x][y], cnt + 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        recur(i, j, -1, 1)

print(ans)