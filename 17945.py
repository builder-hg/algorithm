"""
[문제풀이전략]

1. 문제이해 및 정리
- 이차방정식 근 구하기
- 근은 항상 정수이다.
- (-1000 ≤ A, B ≤ 1000)

2. 문제풀이방향
-1000 <= b <= 1000
-1000 <= a <= 1000
-1000 * 20000 <= 20000a <= 20000* 1000
-20,000,000 <= 20000a <= 20,000,000
-20,000,000 - 1000 <= 20000a + b <= 20,000,000 + 1000
x^2에 20000a + b를 더했을 때 0이 되어야 한다. 
이를 고려하여 x의 범위를 산정할 수 있다.

x에 1000을 넣는다면 ,
1,000,000 이 나오고 이는 20000a + b의 범위를 생각했을 때 놓치는 범위가 있을 수 있다.
x에 10000을 넣는다면,
100,000,000 이 나오고 이는 20000a + b의 범위를 생각했을 때 놓치는 범위가 없으므로 x를(근을) -10000 부터 10000까지 돌린다.

"""
import sys

answerLlist = []
A, B = map(int, sys.stdin.readline().split())
for i in range(-10000, 10001):
    if i**2 + 2*A*i + B == 0:
        answerLlist.append(i)

print(*sorted(set(answerLlist)))