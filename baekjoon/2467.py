"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- (+1) <= 산성용액 특성값 <= 1,000,000,000
- (-1,000,000,000) <= 알칼리성 특성 값 <= -1
- 두 값의 합이 0에 가장 가까운 용액을 만든다.

2. 문제 풀이 방향
"""
import sys

N = int(input())    # 용액싀 수 (2<=N<=100,000)
lst = list(map(int, sys.stdin.readline().split())) + [0]
# 특성 값은 모두 서로 다르다.
ans = 1 << 64
s = 0
e = N-1 
possible = [0,0]
while s < e:
    if abs(lst[s]+lst[e]) < ans :
        ans =  abs(lst[s]+lst[e])
        possible[0]= lst[s]
        possible[1]= lst[e]
    if lst[s]+lst[e] < 0:
        s += 1
    else:
        e -= 1
print(*possible)