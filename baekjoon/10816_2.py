# 해당 숫자카드의 제일 오른쪽 인덱스에서 - 제일 왼쪽 인덱스 + 1 을 구한다.

import sys
input = sys.stdin.readline

def binary_search(K, dir):
    global _exist

    s = 0
    e = N - 1
    ans = 0

    while s <= e:  
        mid = (s + e) // 2

        if own_arr[mid] < K:
            s = mid + 1
        elif own_arr[mid] > K:
            e = mid - 1
        else:
            _exist = True
            ans = mid

            if dir == 'right':
                s = mid + 1
            elif dir == 'left':
                e = mid - 1

    return ans

N = int(input())
own_arr = sorted(list(map(int, input().split())))
M = int(input())
chk_arr = list(map(int, input().split()))

for i in range(M):
    _exist = False

    diff = binary_search(chk_arr[i], 'right') - binary_search(chk_arr[i], 'left')
    if _exist:
        print(diff + 1, end=" ")
    else:
        print(0, end=" ")