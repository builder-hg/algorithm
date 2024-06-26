import sys
import copy
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)
      
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))
"""
[1, 100, 2, 1, 50]
답은 101
"""