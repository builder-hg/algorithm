import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-(1 << 60) for _ in range(200101)] for _ in range(N + 1)]
for i in range(K + 1):
    dp[N][i] = 0

for i in range(N)[::-1]:
    for j in range(K + 1)[::-1]:
        dp[i][j] = max(dp[i + 1][j + arr[i][0]] + arr[i][1], dp[i + 1][j])

print(dp[0][0])