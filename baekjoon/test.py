# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     dp = [[[0 for _ in range(2)] for _ in range(110)] for _ in range(110)]
    
#     dp[n][k][0] = 0
#     dp[n][k][1] = 0

#     for i in range(n)[::-1]:
#         for j in range(k)[::-1]:
#             for l in range(2)[::-1]:
#                 dp[i][j][l] = dp[i+1][j][0] + dp[i+1][j + k][1]
                
       
#     print(dp[0][0][0])
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[[0 for _ in range(2)] for _ in range(110)] for _ in range(110)]

dp[n][k][0] = 1
dp[n][k][1] = 1

for i in range(n)[::-1]:
    for j in range(k + 1)[::-1]:
        for k in range(2)[::-1]:
            ret = dp[i+1][j][0]
            ret += dp[i+1][j + (k*k)][1]
            dp[i][j][k] = ret

print(dp[0][0][0])