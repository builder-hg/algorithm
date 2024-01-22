"""
[문제풀이전략]
1. 문제 이해 및 정리
- 조약돌 개수 N (1 <= N <= 300,000)
- 0<= 까만색 조약돌의 개수 <= B, 흰색 조약돌의 개수 >= W
- 조건을 만족하는 구간이 없다면 집으로 간다. (출력 0)
- 조건을 만족하는 가장 긴 구간의 길이를 구한다.
- B: 검은색, W: 흰색, B + W <= N

2. 아이디어
- 이것도 이전에 푼 알파벳 담기와 같은 방식으로 풀면 어떨까?
- 까만색 조약돌이 B보다 작고 e += 1
- 까만색 조약돌이 B보다 크다면 s += 1
- 흰색 조약돌의 개수가 W보다 커지는 지점의 값을 이전 값과 비교한다.

3. 문제 풀이 방향
10 1 2
1)
W B B W W B W W B W
s
e


"""
import sys

N, B, W = map(int, sys.stdin.readline().split())
lst = list(input())
s = 0
e = 0
rock = {'B':0,'W':0}        # 조약돌 종류와 개수가 기록된다.
rock[lst[0]] += 1             # 초기값을 설정한다. 첫 지점의 조약돌의 종류에 1을 증가시킨다.
ans = 0
cnt = 1 
while e < N:
    if rock['B'] <= B:
        e += 1

        if e == N:
            if rock['W'] >= W:  # 흰 조약돌을 만족할만큼 담았는지 체크한다.
                ans = max(ans, cnt)
            break

        cnt += 1 
        rock[lst[e]] += 1
    else:                   # 검은 조약돌을 더 담을 수 없는 경우
        if rock['W'] >= W:  # 흰 조약돌을 만족할만큼 담았는지 체크한다.
            ans = max(ans, cnt-1)

        rock[lst[s]] -= 1
        s += 1 
        cnt -= 1
print(ans)