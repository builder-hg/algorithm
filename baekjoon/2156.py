import sys
input = sys.stdin.readline

# 바텀업 DP
N = int(input())
raw = [0]
for _ in range(N):
    tmp = int(input())
    raw.append(tmp)

dp = [0 for _ in range(N + 1)]
dp[1] = raw[1]
if N > 1:
    dp[2] = raw[1] + raw[2]
if N > 2:
    dp[3] = max(raw[3] + raw[1], raw[3] + raw[2], dp[2])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], raw[i] + raw[i - 1] + dp[i - 3], raw[i] + dp[i - 2])

print(dp[N])

"""
#탑다운 DP
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(cur, choice):
    if choice >= 3:
        return -(1 << 60)

    if cur == N:
        return 0
    
    if dp[cur][choice] != -1:
        return dp[cur][choice]
    
    ret = 0
    ret = max(ret, recur(cur + 1, choice + 1) + raw[cur])
    ret = max(ret, recur(cur + 1, 0))

    dp[cur][choice] = ret
    return dp[cur][choice]

N = int(input())
raw = []
for _ in range(N):
    tmp = int(input())
    raw.append(tmp)

log = [0 for _ in range(N)]
dp = [[-1 for _ in range(4)] for _ in range(N + 1)]
ans = recur(0, 0)
print(ans)
"""