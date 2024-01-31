import sys
input = sys.stdin.readline

N, M = map(int, input().split())
raw = [[0 for _ in range(M+2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0 for _ in range(M+2)]]
prefix = [[0 for _ in range(M+2)] for _ in range(N+2)]
ans = -(1 << 60)

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + raw[i][j] - prefix[i-1][j-1]

        for row in range(i):
            for col in range(j):
                ans = max(ans, prefix[i][j] - prefix[row][j] - prefix[i][col] + prefix[row][col])

print(ans)