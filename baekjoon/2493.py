import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [0 for _ in range(N)]
for i in range(N):
    while stack:
        if stack[-1][1] >= arr[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    
    stack.append([i, arr[i]])

print(*ans)