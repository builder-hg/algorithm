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
    
    
    dis = lst[cur]
    if dis == 0:
        return -(1 << 64)

    ret = -(1 << 60)
    if reverse < 2:
        if dir == 1:
            ret = max(recur(cur - dis, 0, reverse + 1) + 1, recur(cur + dis, 1, reverse) + 1)
        else:
            ret = max(recur(cur - dis, 0, reverse) + 1, recur(cur + dis, 1, reverse + 1) + 1)
    else:
        if dir == 1:
            ret = max(ret, recur(cur + dis, 1, reverse) + 1)
        else:
            ret = max(ret, recur(cur - dis, 0, reverse) + 1)

    dp[cur][dir][reverse] = ret

    return dp[cur][dir][reverse] 

N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(N + 1)]
ans = recur(1, 1, 0)
if ans > 0: print(ans)
else: print(-1)
