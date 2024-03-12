import sys
sys.setrecursionlimit(10 ^ 6)
input = sys.stdin.readline

def recur(total):
    global ans

    if total > N:
        return 1 << 64

    if total == N:
        return 0
    
    if dp[total] != -1:
        return dp[total]

    ret = 1 << 64    
    for i in range(1, N + 1):
        ret = min(ret, recur(total + (i ** 2)) + 1)
        
    dp[total] = ret

    return ret

N = int(input())
dp = [-1 for _ in range(N)]
ans = recur(0)
print(ans)

# import sys
# sys.setrecursionlimit(10 ^ 6)
# input = sys.stdin.readline

# def recur(cur, total):
#     global ans

#     if total > N:
#         return

#     if total == N:
#         ans = min(ans, cur)
#         return
    
#     for i in range(1, N + 1):
#         recur(cur + 1, total + (i * i))

# N = int(input())
# ans = 1 << 64
# recur(0, 0)
# print(ans)