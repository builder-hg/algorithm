# 탑다운 DP
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(cur, prv, val):
#     if cur == N:
#         if val == K:
#             return 1
#         return 0
    
#     if dp[cur][prv][val] != -1:
#         return dp[cur][prv][val]
    
#     ret = recur(cur + 1, 0, val)
#     ret += recur(cur + 1, 1, prv * 1 + val)

#     dp[cur][prv][val] = ret
#     return dp[cur][prv][val]

# Q = int(input())

# while Q:
#     Q -= 1

#     N, K = map(int, input().split())
#     dp = [[[-1 for _ in range(110)] for _ in range(2)] for _ in range(110)]
#     ans = recur(0, 0, 0)
#     print(ans)

# 바텀업 DP
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    N, K = map(int, input().split())
    dp = [[[0 for _ in range(110)] for _ in range(2)] for _ in range(110)]

    for i in range(2):
        dp[N][i][K] = 1

    for i in range(N)[::-1]:
        for j in range(2)[::-1]:
            for k in range(K+1)[::-1]:
                dp[i][j][k] = dp[i + 1][0][k]
                dp[i][j][k] += dp[i + 1][1][j * 1 + k]

    print(dp[0][0][0])