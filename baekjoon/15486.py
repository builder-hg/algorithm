import sys
sys.setrecursionlimit(1500010)
input = sys.stdin.readline

def recur(cur):
    if cur > N:
        return -(1 << 64)

    if cur == N:
        return 0
    
    if dp[cur] != -1:
        return dp[cur]

    ret = recur(cur + arr[cur][0]) + arr[cur][1]
    ret = max(ret, recur(cur + 1))

    dp[cur] = ret
    return dp[cur]

N = int(input())
arr = []
for _ in range(N):
    t, p = map(int, input().split())
    arr.append([t, p])
dp = [-1 for _ in range(N)]

print(recur(0))