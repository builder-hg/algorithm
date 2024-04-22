"""
1. 찾고자 하는 값이 K일 때, 주어진 수들 중 K보다 작은 값의 개수는 1부터 N단 중 K를 그 단으로 나눈 값이다.
  - 2단, 2 4 6 ... 200일때 K가 140이라면, 140보다 작은 값의 개수는 140 // 2 => 70
  - 찾고자 하는 값 K가 초기값(A)보다 작다면 K보다 작은 값의 개수는 0이다.
  - 최댓값(C)가 초기값(A)보다 작다면 K보다 작은 값의 개수는 0이다.
2. K 이하의 수가 홀수인 경우 중 가장 왼쪽에 위치한 K를 구한다.
3. K 이하의 개수 - (K - 1) 이하의 개수가 K의 개수이다. 
"""
import sys
input = sys.stdin.readline

def get_cnt(K):
    cnt = 0

    for i in arr:
        _init, _max, _var = i[0], i[1], i[2]

        ref = min(_max, K)
        if K < _init or _max < _init:
            cnt += 0
        else:
            cnt += ((ref - _init) // _var) + 1

    return cnt

def binary_search():
    s = 1
    e = 2147483648
    ans = -1
    while s <= e:
        mid = (s + e) // 2

        if get_cnt(mid) % 2: # 홀수라면,
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    if ans == -1:
        return "NOTHING"
    else:
        return f'{ans} {get_cnt(ans) - get_cnt(ans - 1)}'

N = int(input())
arr = []
for _ in range(N):
    A, C, B = map(int, input().split())
    arr.append([A, C, B])
print(binary_search())