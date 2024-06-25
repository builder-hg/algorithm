import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    N = int(input())
    arrA = list(map(int, input().split()))  # 실제 수
    arrA.sort()

    M = int(input())
    arrB = list(map(int, input().split()))  # 확인할 값

    for i in range(M):
        # 확인할 값 arrB[i]
        EXIST = False
        s = 0
        e = N - 1
        while s <= e:
            mid = (s + e) // 2

            if arrA[mid] == arrB[i]:
                EXIST = True
                break
            elif arrA[mid] < arrB[i]:
                s = mid + 1
            else:
                e = mid - 1

        if EXIST:
            print(1)
        else:
            print(0)