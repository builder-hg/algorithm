"""
A팀 인원을 한명씩 고른다.(N)
고른 사람의 능력치로 몇명을 이기고 몇명에게 지고 몇명과 비기는지 확인한다.
(= 해당 능력치가 정렬된 B 집단내에서 몇번째 인덱스에 속하는지, 그 크기를 비교하면서 인덱스를 확인한다.)

lower_bound, upper_bound 개념을 사용한다.
1. 고른 사람의 능력치가 몇명을 이기느냐. => upper_bound
2. 고른 사람의 능력치가 몇명에게 지냐. => lower_bound

* 참고
lower_bound(arr, val): 정렬된 배열 arr에서 val보다 크거나 같은 값 중 가장 앞의 인덱스를 찾는다.
upper_bound(arr, val): 정렬된 배열 arr에서 val보다 큰 값들 중 가장 앞의 인덱스를 찾는다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = sorted(list(map(int, input().split())))

win = 0
lose = 0
draw = 0
# win/lose/draw는 arrA 기준이다.
# 출력순서 win, lose, draw

def lower_bound(arr, val):
    s = 0
    e = M - 1 
    ans = M

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] >= val:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    
    return ans 

def upper_bound(arr, val):
    s = 0
    e = M - 1
    ans = M

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] > val:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


for i in range(N):
    lower = lower_bound(arrB, arrA[i])
    upper = upper_bound(arrB, arrA[i])

    win += lower
    lose += (M - upper)
    draw += (upper - lower)
    
print(win, lose, draw)