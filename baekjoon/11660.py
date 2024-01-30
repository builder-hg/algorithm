"""
"""
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())    # 정사각형의 크기 N, 쿼리 수 Q
arr = [[0 for _ in range(N+2)]] + [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] + [[0 for _ in range(N+2)]]
prefix = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i][j]

while Q:
    Q -= 1
    xs, ys, xe, ye = map(int, input().split())
    ans = prefix[xe][ye] - prefix[xe][ys-1] - prefix[xs-1][ye] + prefix[xs-1][ys-1]
    print(ans)