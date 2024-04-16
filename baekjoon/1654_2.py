import sys
input = sys.stdin.readline

def check(mid):
    val = 0
    for i in range(K):
        val += arr[i] // mid

    return val >= N

def binary_search():
    ans = 0
    s = 1
    e = max(arr)

    while s <= e:
        mid = (s + e) // 2

        if check(mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

print(binary_search())