# 10만보다 커진다면 바텀업 DP를 생각해보자.
import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
raw = []
for _ in range(N):
    tmp = int(input())
    raw.append(tmp)
raw.sort()

dp = [0 for _ in range(K + 1)]
dp[0] = 1
for coin in raw:
    for i in range(coin,  K + 1):
        dp[i] += dp[i - coin]

print(dp[K])
"""
# 탑다운 DP
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(cur, val):
    if val > K:            
        return 0
    
    if val == K:
        return 1

    if cur == N:            # 더이상 사용할 동전이 없다면 return 한다.
        return 0
    
    if dp[cur][val] != -1:
        return dp[cur][val]
    
    ret = 0
    for i in range(100001): # 내가 위치한 지점의 값을 여러번 쓸 수 있기에 반복문을 돌렸다.
        tmp = raw[cur] * i
        if val + tmp > K:
            break

        ret += recur(cur + 1, val + tmp)

    dp[cur][val] = ret
    return dp[cur][val]


N, K = map(int, input().split())
raw = []
for _ in range(N):
    tmp = int(input())
    raw.append(tmp)
dp = [[-1 for _ in range(10010)] for _ in range(101)]
ans = recur(0, 0)
print(ans)
"""