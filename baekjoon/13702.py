import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    elem = int(input())
    arr.append(elem)

s = 1
e = max(arr)
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for i in range(N):
        cnt += (arr[i] // mid)

    if cnt >= K:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)