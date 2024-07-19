"""
N: 1,
1 
N: 2,
10
N: 3,
101 <- dp[n - 1][0]
100 <- dp[n - 1][1] + dp[n - 1][0]
N: 4,
1000
1010
1001

1뒤에 올 수 있는 수는 0이다.
0뒤에 올 수 있는 수는 0, 1이다.

k는 0과 1이다.
dp[n][k]
"""
import sys 
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(2)] for _ in range(N + 1)]
dp[1] = [0, 1]  # 한 자리에서 0이 오는 경우는 0개, 1이 오는 경우는 1개이다.
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]
print(sum(dp[N]))