"""
0. 특징
1) 0<= H, M <= 100
2) 2, 5, 8, 0 은 뒤집어도 그대로
    6, 9는 9와 6으로 바뀐다.
3) H와 M의 자리가 다르면 0을 출력한다.

1. 관찰
1)
H = 24, M = 20일 때,
H가 22, M에 00 이 들어온다면
뒤집어진 시계는 00:22를 가리킨다.
- 뒤집어진 시간이 제한범위를 넘어선다면 cnt를 증가시키지 않는다.

2. 완전탐색
- 시간에 대해 0부터 H까지, 분에 대해 0부터 M까지 1씩 증가시키며 순회한다. (전체를 살펴본다)
- 뒤집어졌을 때에도 시간이 유지된다면 cnt를 증가시킨다.
- 뒤집어졌을 때 시간이 유지되지 않는 조건
1) 시간 혹은 분에 1, 3, 4, 7이 하나라도 들어가있는 경우
2) 뒤집어진 분이 H보다 크거나, 뒤집어진 시간이 M보다 큰 경우
3) H와 M의 자릿수가 서로 다른 경우 (str로 바꾸어 len을 사용한다.)
- 순회할때 신경쓸점
1) 자릿수가 같지 않은 경우는 과감하게 넘어간다.
2) 
"""
import sys
input = sys.stdin.readline

H, M = map(int, input().split())
cnt = 0

#시간과 분의 자릿수가 서로 다르다면 답은 0이된다. 
if len(str(H)) != len(str(M)):
    print(0)
    sys.exit()
if H == 10 and M > 10:
    print(0)
    sys.exit()
if H > 10 and M == 10:
    print(0)
    sys.exit()

def check(num):
    for except_num in [1,3,4,7]:
        for raw in list(str(num)):
            if except_num == int(raw):
                return False
    return True

def check_reverse(raw, limited):
    # 28, 60 -> 뒤집으면 82이기때문에 return False
    lst = list(str(raw))[::-1]
    reverse = 0
    for i in range(1, len(lst) + 1):
        val = int(lst[i - 1])
        if val == 6:
            val = 9
        elif val == 9:
            val = 6
        reverse += val * (10 ** (len(lst) - i))
    if reverse >= limited:
        return False
    return True


for h in range(H):
    for m in range(M):
        # case1) 뒤집어질 수 없는 수가 h 혹은 m에 하나라도 나온다면 넘어간다.
        if not check(h) or not check(m):
            continue

        # case2) 일의 자리수라면 앞에 0을 붙인다.
        if h < 10:
            str_h = '0' + str(h)
        if m < 10:
            str_m = '0' + str(m)

        # case3) 뒤집어진 시간이 M보다 크거나 뒤집어진 분이 H보다 크다면 넘어간다.
        if not check_reverse(str_h, M) or not check_reverse(str_m, H):
            continue

        # 조건을 모두 통과한 경우
        print(h, m, cnt)
        cnt += 1

print(cnt)
