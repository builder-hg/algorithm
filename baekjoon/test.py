import sys
input = sys.stdin.readline

n = int(input())
dp = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(4)] for _ in range(n+1000)]
for j in range(4):
    for k in range(3):
            if j > 2 or k >= 2:
                continue
            
            dp[n][j][k][1] = 1

for i in range(1,n)[::-1]:
        for curCnt in range(3)[::-1]:
                for twoCnt in range(2)[::-1]:
                        for two in range(2)[::-1]:
                                num = dp[i+1][0][0][two] + dp[i+1][curCnt+1][0][two] + dp[i+1][curCnt+1][twoCnt+1][1]
                                dp[i][curCnt][twoCnt][two] = num % 1000000007
print(dp[1][0][0][0])