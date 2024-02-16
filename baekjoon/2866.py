"""
0. 완전탐색 
1) 각 열별로 문자열을 구한다.
2) 문자열의 제일 앞을 지운다고 가정한다. R만큼 반복한다. N (필수)
3) 가장 앞의 문자가 지워졌을 때 남은 문자열들이 중복되는 지 체크한다.
    - 두 개씩 비교하므로 N * N = 1000 * 1000
=> 1,000 * 1,000 * 1,000 = 1,000,000,000
=> 시간초과

1. 이진탐색
1) 각 열별로 s부터 e까지의 문자열을 구한다.
2) 해당 문자열을 딕셔너리에 저장한다 (없으면 1, 있으면 +1)
3) 딕셔너리에서 구한 개수가 1보다 크다면 s와 e를 조정한다.
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

ans = 0
s = 0
e = R - 1

while s <= e:
    mid = (s + e) // 2

    check = True
    alpha = {}

    for y in range(C):
        temp = ''
        for x in range(mid, R):
            temp += arr[x][y]

        alpha[temp] = alpha.get(temp, 0) + 1

        if alpha[temp] > 1:
            check = False
            break

    if check:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1 

print(ans)