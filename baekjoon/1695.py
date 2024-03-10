import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(cur, dir, reverse):
    if cur < 1 or cur > N:
        return -(1 << 64)
    
    if cur == N:
        return 0
    
    if dp[cur][dir][reverse] != -1:
        return dp[cur][dir][reverse]
    
    if dir == 1:
        dis = lst[cur]
        ch_dir = 0
    else:
        dis = -1 * lst[cur]
        ch_dir = 1

    if reverse < 2:
        ret = max(recur(cur + dis, dir, reverse) + 1, recur(cur - dis, ch_dir, reverse + 1) + 1)
    else:
        ret = recur(cur + dis, dir, reverse) + 1

    dp[cur][dir][reverse] = ret

    return dp[cur][dir][reverse] 

N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(N)]
ans = recur(1, 0, 0)
if ans > 0: print(ans)
else: print(-1)
