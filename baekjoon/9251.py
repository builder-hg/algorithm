import sys
input = sys.stdin.readline

text_one = list(input().strip())
text_two = list(input().strip())
W = len(text_one)
H = len(text_two)
dp = [[0 for _ in range(H + 1)] for _ in range(W + 1)]

for i in range(1, W + 1):
    for j in range(1, H + 1):
        if text_one[i - 1] == text_two[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[W][H])