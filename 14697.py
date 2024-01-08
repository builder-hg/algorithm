"""
[문제풀이전략]

1. 문제 이해 및 정리
- 침대 수를 기준으로 세가지 타입의 방이 있다.
- 같은 타입의 방들이 여러 개 있다.
- A인실 방, B인실 방, C인실 방과 전체 학생수 N이 주어진다. 
- 배정된 모든 방에 빈 침대가 없도록 할 수 있는지 여부를 판단한다. 가능 시 1을, 없을 시 0을 출력한다.
- 1 ≤ A < B < C ≤ 50, 전체 학생 수를 나타내는 자연수 N (1 ≤ N ≤ 300)

2. 문제 풀이 방향
1) A방의 개수(ax) 범위를 구한다.
1-1) A가 가장 작을때, A=1일 때 ax는 0부터 300까지이다.
2) B방의 개수(bx) 범위를 구한다.
2-1) B가 가장 작을때, B=2일 때 bx는 0부터 150까지이다.
3) C방의 개수(cx) 범위를 구한다. 
3-1) C가 가장 작을때, C=3일 때 cx는 0부터 100까지이다.
4) ax와 bx와 cx의 범위를 순회하며 아래의 식을 성립한다면 1을, 아니라면 0을 출력한다.
4-1) A*ax = N
4-2) A*ax + B*bx = N
4-3) A*ax + B*bx + C*cx = N
4-4) B*ax = N
4-5) B*ax + C*bx = N
4-6) C*ax = N
"""
import sys

A, B, C, N = map(int, sys.stdin.readline().split())
isPossible = 1
for ax in range(0, 301):
    if A*ax == N:
        print(isPossible) #4-1
        sys.exit()
    for bx in range(0, 151):
        if A*ax + B*bx == N: #4-2
            print(isPossible)
            sys.exit()
        if B*bx == N: #4-4
            print(isPossible)
            sys.exit()
        for cx in range(0, 101):
            if C*bx == N: #4-6
                print(isPossible)
                sys.exit()
            if A*ax + B*bx + C*cx == N: #4-3
                print(isPossible)
                sys.exit()
            if B*ax + C*bx == N: #4-5
                print(isPossible)
                sys.exit()

print(0)