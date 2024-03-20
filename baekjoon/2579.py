# 탑다운 DP
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(cur, cnt):
#     if cur > N:
#         return -(1 << 60)
    
#     if cnt >= 3:
#         return -(1 << 60)

#     if cur == N:
#         return arr[N]
    
#     if dp[cur][cnt] != -1:
#         return dp[cur][cnt]

#     ret = max(recur(cur + 1, cnt + 1) + arr[cur], recur(cur + 2, 1) + arr[cur])
#     dp[cur][cnt] = ret

#     return dp[cur][cnt]

# N = int(input())
# arr = [0]
# for _ in range(N):
#     num = int(input())
#     arr.append(num)
# dp = [[-1 for _ in range(5)] for _ in range(310)]
# ans = recur(0, 0)
# print(ans)

# 바텀업 DP ===========================================================================
import sys
input = sys.stdin.readline
N = int(input())
arr = [0]
for _ in range(N):
    num = int(input())
    arr.append(num)
dp = [[-(1 << 60) for _ in range(5)] for _ in range(310)]
for i in range(3):
    dp[N][i] = arr[N]

for cur in range(N)[::-1]:
    for cnt in range(3)[::-1]:
        dp[cur][cnt] = max(dp[cur + 1][cnt + 1] + arr[cur], dp[cur + 2][1] + arr[cur])

print(dp[0][0])