import sys
sys.setrecursionlimit(1500010)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [-(1 << 60) for _ in range(1500010)]
dp[N] = 0

for i in range(N)[::-1]:
    if i + arr[i][0] > N:
        dp[i] = max(0, dp[i + 1])
        continue
    dp[i] = max(dp[i + arr[i][0]] + arr[i][1], dp[i + 1])

print(dp[0])
