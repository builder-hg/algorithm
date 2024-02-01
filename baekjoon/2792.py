"""
0. 보석의 개수를 제일 작게 가지도록 하는 문제.(최대값을 최소화 => 이진탐색 고려)


1. 완전탐색으로 한다면,
    - 아이가 다섯, 보석 종류(A, B, C)가 셋이라면,
    - A를 5명 중에 몇 명에게 할당할지(최소 한명에게는 줘야한다.) 고른다.
    - A를 나눠줄 학생들에게 몇개씩 나누어줄 지 고른다.
A, B, B, B, C
A, B, B, C, C
A, B, C, C, C
A, A, B, B, C
-> 보석 A를 1번, 2번학생에게 몇개씩 나누어 줄 지 고른다.
A, A, B, C, C
A, A, A, B, C
    => 나눠주는 케이스를 일일이 다 구하면 시간초과가 나려나.

답이 될 수 있는 범위는 1부터 보석의 최대개수다. 
N명의 학생에게 다음 수만큼 보석을 쥐어준다면 조건을 만족하며 분배되는가를 확인한다.
1 2 3 4 5 6 7 8 9 10
x x o o o o o o o o 
보석A를 인당 x개만큼 분배한다고 했을 때 A / x 가 필요한 인원이고
보석B를 x개만큼 분배한다고 했을 때 B / x 가 필요한 인원인데 
이 두 인원이 주어진 인원보다 작으면 조건을 만족하며 분배된다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(M):
    elem = int(input())
    arr.append(elem)

s = 1
e = 10 ** 9
ans = 0

def check(x):
    total = 0
    
    for i in arr:
        if i % x == 0:
            total += (i // x)
        else:
            total += (i // x) + 1

    if total <= N:
        return True
    else:
        return False

while s <= e:
    mid = (s + e) // 2
    
    if check(mid):  # 나눠주는 최대의 보석수가 mid일 때 학생들에게 모두 보석을 분배할 수 있는가 True/False 판별
        ans = mid
        e = mid - 1 # 더 작은 경우를 찾으러 떠난다.
    else:
        s = mid + 1

print(ans)