import sys
input = sys.stdin.readline

def binary_search():
    ans = 0
    s = 0
    e = max(arr)

    while s <= e:
        mid = (s + e) // 2

        val = 0
        for i in range(N):
            if (arr[i] - mid) > 0:
                val += (arr[i] - mid)

        if val >= M:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans
            


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
print(binary_search())