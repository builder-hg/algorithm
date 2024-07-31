import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def recur(cur, use):
    global cnt 

    if cnt == (N // 2):
        return 0

    if cur >= N:
        return 0
    
    if dp[cur][use] != -1:
        return dp[cur][use]
    
    cnt += 1
    ret = recur(cur + 2, use) + raw[cur]           # 밑장빼기를 사용하지 않는 경우
    cnt -= 1
    if not use:
        cnt += 1
        ret = max(ret, recur(cur + 1, 1) + raw[-1])       # 내가 밑장빼기를 사용하는 경우
        cnt -= 1
    if not use:                                 # 상대가 밑장뺴기를 사용한 경우
        cnt += 1
        ret = max(ret, recur(cur + 1, 1) + raw[cur])
        cnt -= 1

    dp[cur][use] = ret
    return dp[cur][use]

N = int(input())
raw = list(map(int, input().split()))
cnt = 0
dp = [[-1, -1] for _ in range(N)]
ans = recur(0, 0)
print(ans)