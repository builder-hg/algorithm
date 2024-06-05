import sys
input = sys.stdin.readline

dp = [[-1, -1] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

def fibonacci(n):
    if dp[n] != [-1, -1]:
        return dp[n]

    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    
    dp[n] = [fibonacci(n - 1)[0] + fibonacci(n - 2)[0], fibonacci(n - 1)[1] + fibonacci(n - 2)[1]]
    return dp[n]

Q = int(input())
while Q:
    Q -= 1

    N = int(input())
    fibonacci(N)
    print(*dp[N])