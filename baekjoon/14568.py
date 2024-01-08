"""
[문제풀이전략]

1. 문제이해 및 정리
- 사탕개수 N
- 택희 사탕개수: A, 영훈 사탕개수: B, 남규 사탕개수: C
- C >= B + 2 
- A != 0, B != 0, C != 0
- A % 2 != 1 

2. 문제풀이방향
1) 3중 반복문을 돌면서 조건을 만족하는 순서쌍의 개수를 구한다.
"""
import sys

N = int(input())
cnt = 0
for A in range(1, N + 1):
    if A % 2:
        continue
    for B in range(1, N + 1):
        for C in range(1, N + 1):
            if A + B + C != N:
                continue
            if C < B + 2:
                continue
            cnt += 1

print(cnt)