import sys
input = sys.stdin.readline

def check(K):
    total = 0

    for i in arr:
        if (i % K) == 0:
            total += (i // K)
        else:
            total += (i // K) + 1

    return total <= N

def binary_search():
    ans = 0
    s = 1
    e = max(arr)

    while s <= e:
        mid = (s + e) // 2

        if check(mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans

N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(int(input()))

print(binary_search())