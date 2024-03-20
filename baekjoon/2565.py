import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    no, val = map(int, input().split())
    arr.append([no, val])
arr.sort(key=lambda x:x[0])

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))