import sys
input = sys.stdin.readline

N, M = map(int, input().split())
raw = [[0 for _ in range(M + 1)]]
for _ in range(N):
    tmp = [0] + list(map(int, input().split()))
    raw.append(tmp)

prefix = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + raw[i][j]

Q = int(input())
while Q:
    Q -= 1
    sx, sy, ex, ey = map(int, input().split())
    ans = prefix[ex][ey] - prefix[ex][sy - 1] - prefix[sx - 1][ey] + prefix[sx - 1][sy - 1]
    print(ans)
