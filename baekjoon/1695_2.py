import sys
sys.setrecursionlimit(5000 ** 2 + 10)
input = sys.stdin.readline

def recur(x, y):
    if y == 0:
        x -= 1
        y = N - 1

    if x < -1:
        return -(1 << 64)

    if x == 0:
        return 0
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    if reverse[x] == arr[y]:
        ret = recur(x - 1, y - 1) + 1
    else:
        ret = max(recur(x, y - 1), recur(x - 1, y))

    dp[x][y] = ret
    return dp[x][y]

N = int(input())
arr = list(map(int, input().split()))
reverse = arr[::-1]
dp = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    if arr[i] == reverse[0]:
        dp[0][i] = 1
    else:
        dp[0][i] = 0
for i in range(N):
    if reverse[i] == arr[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = 0
ans = recur(N - 1, N - 1)
print(ans)
