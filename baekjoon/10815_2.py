import sys 
input = sys.stdin.readline

def binary_search(K):
    s = 0
    e = N - 1

    while s <= e:
        mid = (s + e) // 2

        if own_arr[mid] == K:
            return 1
        elif own_arr[mid] < K:
            s = mid + 1
        elif own_arr[mid] > K:
            e = mid - 1

    return 0

N = int(input())
own_arr = sorted(list(map(int, input().split())))
M = int(input())
check_arr = list(map(int, input().split()))

for i in range(M):
    print(binary_search(check_arr[i]), end=" ")
