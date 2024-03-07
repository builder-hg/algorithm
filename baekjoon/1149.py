# import sys
# sys.setrecursionlimit(1010)
# input = sys.stdin.readline

# def recur(cur, y, prev):
#     if y == prev:
#         return 1 << 64
    
#     if cur == N:
#         return 0

#     if y >= 0 and prev >= 0:
#         if dp[cur][y][prev] != -1:
#             return dp[cur][y][prev]
    
#     ret = recur(cur + 1, 0, y) + arr[cur][0]
#     ret = min(ret, recur(cur + 1, 1, y) + arr[cur][1])
#     ret = min(ret, recur(cur + 1, 2, y) + arr[cur][2])

#     dp[cur][y][prev] = ret
#     return dp[cur][y][prev]

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[-1, -1, -1] for _ in range(3)] for _ in range(N)]
# print(recur(0, -1, -2))

import sys
input = sys.stdin.readline

def recur(cur, prv):
    if cur == n:
        return 0
    
    if dp[cur][prv] != -1:
        return dp[cur][prv]
    
    ret = 1 << 60
    for i in range(3):
        if i == prv:
            continue

        ret = min(ret, recur(cur + 1, i) + arr[cur][i])

    dp[cur][prv] = ret
    return ret

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1, -1, -1, -1] for _ in range(n)]
print(recur(0,-1))