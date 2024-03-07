import sys
input = sys.stdin.readline

def recur(cur, w):
    if w > K:
        return -(1 << 64)

    if cur == N:
        return 0
    
    if dp[cur][w] != -1:
        return dp[cur][w]

    ret = recur(cur + 1, w + arr[cur][0]) + arr[cur][1]
    ret = max(ret, recur(cur + 1, w))

    dp[cur][w] = ret
    return ret

N, K = map(int, input().split())
arr = []
for _ in range(N):
    w, v = map(int, input().split())
    arr.append([w, v])
dp = [[-1 for i in range(100100)] for _ in range(N)]

print(recur(0, 0))