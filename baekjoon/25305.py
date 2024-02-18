import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break

    ans = arr[i]
    K -= 1

print(ans)