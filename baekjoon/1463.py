import sys
input = sys.stdin.readline

N = int(input())
dp = [-1 for _ in range(1000010)]
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, 1000001):
    # 2의 배수인 경우
    if i % 2 == 0 and i % 3 != 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
    # 3의 배수인 경우
    elif i % 2 != 0 and i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    # 2의 배수이며, 3의 배수인 경우
    elif i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i // 3] + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[N])