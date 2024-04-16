import sys
input = sys.stdin.readline

def check(K):
    total = 0

    if K == 0:
        return True

    for i in arr:
        total += (i // K)

    return total >= M

def binary_search():
    ans = 0
    s = 0
    e = max(arr)

    while s <= e:
        mid = (s + e) // 2

        if check(mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(binary_search())
