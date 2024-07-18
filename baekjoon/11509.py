import sys
input = sys.stdin.readline

def recur(cur, prv):
    if cur > N:             
        return 0
    
    if cur == N:                # 끝까지 살펴봤다면
        return 0           
    
    if dp[cur][prv] != -1:      # 기존에 구한 값이 있다면 재사용한다.
        return dp[cur][prv]
    
    if prv == -1:               # 첫시작인 경우 raw[0][0]만 살펴본다.
        prv = 0
        ret = recur(cur + 1, prv) + raw[cur][prv]
    else:                       # 그 외에는 raw[cur][prv], raw[cur][prv + 1]만 본다.
        ret = max(recur(cur + 1, prv) + raw[cur][prv], recur(cur + 1, prv + 1) + raw[cur][prv + 1])
    
    dp[cur][prv] = ret
    return dp[cur][prv]

N = int(input())
raw = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    raw.append(tmp)
arr = [-1 for _ in range(500)]
dp = [[-1 for _ in range(501)] for _ in range(501)]
recur(0, -1)
print(dp[0][0])