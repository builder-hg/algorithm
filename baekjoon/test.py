N = 6
arr = [10, 20, 10, 30, 20, 50]

dp = [1 for _ in range(N)]
prv = [-1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] >= arr[i]: continue

        if dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prv[i] = j

ans = 0
idx = 0
for i in range(N):
    if ans < dp[i]:
        ans = dp[i]
        idx = i

while idx != -1:
    print(arr[idx])
    idx = prv[idx]
