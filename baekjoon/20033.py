import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

s = 0
e = N
ans = 0

def check(mid, arr):
    cnt = 0

    for i in range(len(arr)):
        val = arr[i]
        if val >= mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= mid:
            return True
        
    return False

while s <= e:
    mid = (s + e) // 2

    if check(mid, arr):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)