import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 탑다운 DP
"""
def recur(cur, dir, cnt):
    if cnt > W:
        return -(1 << 60)

    if cur == T:
        return 0
    
    if dp[cur][dir][cnt] != -1:
        return dp[cur][dir][cnt]
    
    val = 0
    if arr[cur] == dir:
        val = 1

    if dir == 1:
        ret = max(recur(cur + 1, 1, cnt) + val, recur(cur + 1, 2, cnt + 1) + val)
    elif dir == 2:
        ret = max(recur(cur + 1, 1, cnt + 1) + val, recur(cur + 1, 2, cnt) + val)

    dp[cur][dir][cnt] = ret
    return dp[cur][dir][cnt]

T, W = map(int, input().split())
arr = []
for _ in range(T):
    temp = int(input())
    arr.append(temp)
dp = [[[-1 for _ in range(W+1)] for _ in range(3)] for _ in range(1010)]
ans = max(recur(0, 1, 0), recur(0, 2, 1))
print(ans)
"""

# 바텀업 DP
T, W = map(int, input().split())
arr = []
for _ in range(T):
    temp = int(input())
    arr.append(temp)
dp = [[[-(1 << 60) for _ in range(W+10)] for _ in range(3)] for _ in range(1010)]

for i in range(1010):
    for j in range(3):
        if j == 0: continue
        for k in range(W + 1):
            if i == T:
                dp[i][j][k] = 0

for i in range(T)[::-1]:
    for j in range(3)[::-1]:
        for k in range(W + 1)[::-1]:
            val = 0
            if arr[i] == j:
                val = 1

            if j == 1:
                ret = max(dp[i + 1][1][k] + val, dp[i + 1][2][k + 1] + val)
            elif j == 2:
                ret = max(dp[i + 1][1][k + 1] + val, dp[i + 1][2][k] + val)

            dp[i][j][k] = ret


print(max(dp[0][1][0], dp[0][2][1]))