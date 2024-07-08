import sys
input = sys.stdin.readline

# 스택을 활용한 문제풀이

N = int(input())
arr = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
stack = []

stack.append(0)
for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)

"""
# 역추적을 활용한 문제풀이, (정답)
N = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(N)]
for i in range(N)[::-1]:
    if i == (N - 1):
        dp[i] = [arr[i], -1]
    else:
        idx = i + 1
        while True:
            if idx == -1:
                dp[i] = [arr[i], -1]
                break

            prv = dp[idx][0]
            cur = arr[i]
            if cur < prv:
                dp[i] = [arr[i], idx]
                break

            idx = dp[idx][1]

for i in range(len(dp)):
    idx = dp[i][1]

    if idx == -1:
        print(-1, end=" ")
    else:
        print(arr[idx], end=" ")

"""