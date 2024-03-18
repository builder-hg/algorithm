"""
인자
- 연속해서 뛰어넘은 횟수
- 뛰어넘은 선인장의 높이 합
- 2인 선인장의 개수
- 위치
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
dp = [[[[0 for _ in range(2)] for _ in range(3)] for _ in range(4)] for _ in range(1010)]

for cur in range(N+1):
    for jump in range(4):
        for total in range(3):
            for high in range(2):
                if cur == N and high == 1:
                    if jump > 2 or total >= 2:
                        continue
                    dp[cur][jump][total][high] = 1


for cur in range(N-1, 0, -1):
    for jump in range(3)[::-1]:
        for total in range(2)[::-1]:
            for high in range(2)[::-1]:
                ret = 0
                ret += dp[cur + 1][0][0][high]
                ret += dp[cur + 1][jump + 1][0][high]
                ret += dp[cur + 1][jump + 1][total + 1][1]

                dp[cur][jump][total][high] = ret % 1000000007
                

print(dp[1][0][0][0])


