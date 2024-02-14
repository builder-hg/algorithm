import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
total = int(input())

s = 0
e = max(arr)
ans = 0

while s <= e:
    mid = (s + e) // 2  # 상한액
    temp = 0

    for val in arr:
        if val <= mid:
            temp += val
        else:
            temp += mid

    if temp <= total:
        ans = mid
        s = mid + 1
    elif temp > total:
        e = mid - 1

print(ans)
    