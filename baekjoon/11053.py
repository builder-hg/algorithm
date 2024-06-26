import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            print("dp[i]: ", dp[i])
            print("dp[j] + 1: ", dp[j] + 1)
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))