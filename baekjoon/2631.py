import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    temp = int(input())
    arr.append(temp)
dp = [1 for _ in range(N)]

#가장 긴 증가하는 수열 찾기 
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

#n- 긴 증가하는 부분수열의 길이 
print(N - max(dp))