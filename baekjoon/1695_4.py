# 탑다운 DP ===============================================
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(s, e):
#     if s >= e:
#         return 0
    
#     if dp[s][e] != -1:
#         return dp[s][e]

#     ret = 1 << 64
#     if arr[s] == arr[e]:
#         ret = min(ret, recur(s + 1, e - 1))
#     else:
#         ret = min(recur(s + 1, e) + 1, recur(s, e - 1) + 1)

#     dp[s][e] = ret

#     return dp[s][e]

# N = int(input())
# arr = list(map(int, input().split()))
# dp = [[-1 for _ in range(N)] for _ in range(N)]
# ans = recur(0, len(arr) - 1)
# print(ans)

# 바텀업 DP ===============================================
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
for s in range(N)[::-1]:
    for e in range(N):
        if s >= e:
            dp[s][e] = 0
            continue

        if arr[s] == arr[e]:
            dp[s][e] = dp[s + 1][e - 1]
        else:
            dp[s][e] = min(dp[s + 1][e] + 1, dp[s][e - 1] + 1)

print(dp[0][len(arr) - 1])