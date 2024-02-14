import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    N, M = map(int, input().split())
    arrA = sorted(list(map(int, input().split())))
    arrB = sorted(list(map(int, input().split())))
    ans = 0

    for i in range(N):
        val = arrA[i]
        s = 0
        e = M - 1
        cnt = -1

        while s <= e:
            mid = (s + e) // 2
            
            if val > arrB[mid]:
                cnt = mid
                s = mid + 1
            else:
                e = mid - 1

        ans += (cnt + 1)
    print(ans)