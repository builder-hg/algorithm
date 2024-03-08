import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y):
    if x > W or y > H:
        return 0

    if x == W and y == H:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ret = recur(x + 1, y)
    ret += recur(x, y + 1)
    dp[x][y] = ret
    dp[x][y] //= 100000
    return dp[x][y]

W, H = map(int, input().split())
dp = [[-1 for _ in range(H + 1)] for _ in range(W + 1)]
print(recur(1, 1))