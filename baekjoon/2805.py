"""
1. 완전탐색으로 푼다면,
    - 가장 높은 나무의 높이값부터 -1 씩 높이값을 세팅한다. (n)
    - 해당 높이값에서 얻어갈 수 있는 나무의 크기를 구한다. (n)
    => n * n = 1,000,000,000 * 1,000,000
    => 높이값 세팅하는 작업을 줄여보자.

2. 매개변수 탐색문제로 전환
    - 높이값은 이진탐색으로 선택한다. 
    - 해당 높이값에서 M개의 나무를 가져갈 수 있는지 없는지 체크한다.(True/False)
    - 가져갈 수 있다면 s = mid + 1
    - 가져갈 수 없다면 e = mid - 1
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# s, e, mid 높이값의 범위와 관련된 변수.
s = 0
e = 1000000000
ans = 0

def check(height):
    value = 0

    for i in arr:
        if i > height:
            value += i - height
    
    if value >= M:
        return True
    else:
        return False

while s <= e:
    mid = (s + e) // 2

    if check(mid):  # 해당 높이값으로 설정시 원하는 나무를 가져갈 수 있다면
        ans = mid   # 답으로 설정한다.
        s = mid + 1 # 범위를 옮긴다.
    else:
        e = mid - 1

print(ans)