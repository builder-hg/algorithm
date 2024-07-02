import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]
backtracking = [-1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                backtracking[i] = j

count = max(dp)
index = dp.index(count)
ans = []
while index != -1:
    ans.append(arr[index])
    index = backtracking[index]

print(count)
print(*ans[::-1])