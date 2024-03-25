import sys
input = sys.stdin.readline

S = list(input().strip())
P = list(input().strip())
M = len(S)
N = len(P)

dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
prv = [[[-1, -1] for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if S[i - 1] == P[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            prv[i][j] = [i - 1, j - 1]
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1]
                prv[i][j] = [i, j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
                prv[i][j] = [i - 1, j]

print(dp[M][N])
x, y = M, N
ans = ''
while True:
    if x == 0 or y == 0:
        break

    if S[x - 1] == P[y - 1]:
        ans += S[x - 1]

    x, y = prv[x][y]

print(ans[::-1])



# ==============================================================================
"""import sys
input = sys.stdin.readline
text_one = list(input().strip())
text_two = list(input().strip())
W = len(text_one)
H = len(text_two)
dp = [[0 for _ in range(H + 1)] for _ in range(W + 1)]
backtrack = [[(-1, -1)] * (H + 1) for _ in range(W + 1)]
for i in range(1, W + 1):
    for j in range(1, H + 1):
        if text_one[i - 1] == text_two[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            backtrack[i][j] = (i - 1, j - 1)
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1]
                backtrack[i][j] = (i, j - 1)
            else:
                dp[i][j] = dp[i - 1][j]
                backtrack[i][j] = (i - 1, j)
print(dp[W][H])
x, y = W, H
ans = ""
while True:
    if x == 0 or y == 0:
        break
    if text_one[x - 1] == text_two[y - 1]:
        ans += text_two[y - 1]
    x, y = backtrack[x][y]
print(ans[::-1])"""