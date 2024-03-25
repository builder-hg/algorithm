import sys
input = sys.stdin.readline

N = int(input())
forward_arr = list(map(int, input().split()))
reverse_arr = forward_arr[::-1]

forward_dp = [1 for _ in range(N)]
reverse_dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        # 정방향
        if forward_arr[i] > forward_arr[j]:
            forward_dp[i] = max(forward_dp[i], forward_dp[j] + 1)
        # 역방향
        if reverse_arr[i] > reverse_arr[j]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j] + 1)

ans = [0 for _ in range(N)]
for i in range(N):
    ans[i] = forward_dp[i] + reverse_dp[N - i - 1] - 1

print(max(ans))