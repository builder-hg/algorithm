import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = 0
e = N - 1
ans = 0

def get_sum(start, end, val):
    numC = 0
    mid = 0

    while start <= end:
        mid = (start + end) // 2

        if mid == start or mid == end:
            break

        if arr[mid] <= val:
            numC = arr[mid]
            start = mid
        else:
            end = mid

    return numC

for i in range(N):
    for j in range(i+1, N):
        val = arr[i] + arr[j]

        if val > M:
            continue

        C = get_sum(i, j, M - val)

        if C == 0:
            continue

        if ans < (val + C):
            ans = val + C

print(ans)