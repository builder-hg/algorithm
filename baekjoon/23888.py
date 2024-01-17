"""
[문제풀이전략]
1. 문제 이해 및 정리
- 입력: 수열의 초항, 공차
- 입력: 쿼리의 개수
- 입력: 1이라면 수열의 합 / 2라면 범위내 숫자들의 최대공약수, 시작지점, 끝지점
2. 문제 풀이 방향
- An = a + (n-1)d 
"""
import sys

a, d = map(int, sys.stdin.readline().split())   # 초항과 공차
query = int(input())                            # 쿼리 수
while query > 0:
    query -= 1
    mode, start, end = map(int, sys.stdin.readline().split())

    if mode == 1:
        ans = 0
        for i in range(start, end + 1):
            ans += (a + (i-1) * d)
    else:
        ans = a + (start - 1) * d
        for i in range(start, end + 1):
            cur = a + (i-1) * d
            while cur:
                ans, cur = cur, ans % cur 
    
    print(ans)