import sys
input = sys.stdin.readline

dp = [-1 for _ in range(110)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    print(dp[N])