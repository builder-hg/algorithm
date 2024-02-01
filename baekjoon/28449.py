"""
1. 완전탐색으로 접근한다면,
    - 모든 경우를 다 고려한다. (a팀 인원 전체와 b팀 인원전체를 비교한다.)
    -> (N * M => 시간초과)

4 3
1000 90 3 20000
1 3 100000
    
2. 
능력치: 1이상 100,000 이하
세팅된 능력치가 3일때,
a 그룹에서는 해당 능력치 미만인 경우가 2개
b 그룹에서는 해당 능력치 초과인 경우가 2개
능력치가 같은 경우가 1개

세팅된 능력치가 6일때,
a 그룹에서 해당 능력치 미만인 경우가 5개
b 그룹에서 해당 능력치 초과인 경우가 0개
능력치가 같은 경우 0
조건을 부합한다. e를 세팅된 능력치(mid) - 1로 수정한다.

세팅된 능력치가 2 일때,
a 그룹에서 해당 능력치 미만인 경우가 1개
b 그룹에서 해당 능력치 초과인 경우가 3개
능력치가 같은 경우 0

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = sorted(list(map(int, input().split())))
a, b, c = 0, 0, 0

def lower_bound(arr, val):
    s = 0
    e = len(arr) - 1
    idx = len(arr)

    while s <= e:    
        mid = (s + e) // 2

        if arr[mid] >= val:
            idx = mid 
            e = mid - 1
        else:
            s = mid + 1
    
    return idx

def upper_bound(arr, val):
    s = 0
    e = len(arr) - 1
    idx = len(arr)

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] > val:
            idx = mid
            e = mid - 1
        else:
            s = mid + 1

    return idx


for i in range(N):
    l = lower_bound(arrB, arrA[i])
    u = upper_bound(arrB, arrA[i])

    a += l
    b += u - l
    c += M - u

print(a, c, b)

"""
lower_bound(arr, val) # 정렬된 배열 arr에서 val보다 크거나 같은 값 중 가장 앞의 인덱스를 찾는다.
1 2 3 3 3 5 6 7 8

lower_bound(5)

"""