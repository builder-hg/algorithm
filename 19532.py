"""
[문제풀이전략]

1. 문제 이해 및 정리
- 근 x, 근 y 는 정수로 하나 존재한다.
- 근 x, 근 y의 범위는 -999이상 999이하이다.
- -999 <= a, b, c, d, e, f <= 999

2. 문제 풀이 방향
1) 이중 반복문을 돌며 근을 찾아 출력한다.(시간제한에 걸리지 않는다. 2000 * 2000 = 4,000,000)

"""
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            sys.exit()