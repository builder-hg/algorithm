import sys
input = sys.stdin.readline

def recur(cntA, cntB, value):
    global ans 

    if value > N:
        return
    
    if value == N:
        ans = min(ans, cntA + cntB)
        return

    recur(cntA + 1, cntB, value + 5)
    recur(cntA, cntB + 1, value + 2)

def recur2(value):
    if value > N:
        return (1 << 60)
    
    if value == N:
        return 0
    
    if dp[value] != 1 << 60:
        return dp[value]
    
    ret = 1 << 60
    ret = min(ret, recur2(value + 5) + 1)
    ret = min(ret, recur2(value + 2) + 1)

    dp[value] = ret
    return dp[value] 

N = int(input())
ans = 1 << 60
dp = [(1 << 60) for _ in range(50010)]
recur2(0)
