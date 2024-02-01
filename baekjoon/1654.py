"""
1. 완전탐색으로 푼다면,
    - 가장 긴 랜선길이로부터 -1씩 줄여가며 랜선의 길이를 설정한다. (2^31 - 1)
    - 설정된 길이로부터 얻을 수 있는 랜선의 개수를 구한다. (K)
    => 랜선 길이 설정을 단축한다. 
    => 랜선 길이 설정을 이진탐색으로 줄여가면서 세팅한다.
2. 매개변수 탐색문제로 전환
    - 랜선 길이는 이진탐색으로 선택
    - 해당 랜선길이에서 M개의 랜선을 챙길 수 있는지 판별한다.
    - 챙길 수 있다면 s = mid + 1
    - 챙길 수 없다면 e = mid - 1
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    elem = int(input())
    arr.append(elem)

s = 1
e = 2 ** 31 - 1
ans = 0

def check(leng):
    value = 0

    for i in arr:
        value += (i // leng)

    if value >= M:
        return True
    else:
        return False

while s <= e:
    mid = (s + e) // 2

    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)