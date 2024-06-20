"""
N = 5일때, A B C D E가 있고,
dp[N]이 N개의 선물을 상호간에 주고 받는 값이라고 하자.

1) A와 B가 서로 교환했다면,
남은 세 사람 C, D, E끼리 선물을 주고 받는다.
즉, dp[N - 2] * (N - 1)

2) A는 B에게 주었으나 B는 A에게 주지 않았다면,
선물을 받지 못한 남은 네 사람 A, C, D, E이 선물B, 선물C, 선물D, 선물E 네 개의 선물 주고 받아야 한다. 
즉, dp[N - 1] * (N - 1)

점화식
dp[N] = dp[N - 1] * (N - 1) +  dp[N - 2] * (N - 1)

dp[1] = 0
dp[2] = 1
dp[3] = 2
a=>b, b=>c, c=>a
a=>c, b=>a, c=>b
"""
import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(1000001)]
dp[1] = 0
dp[2] = 1
dp[3] = 2

for i in range(4, 1000001):
    dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % 1000000000

print(dp[N])