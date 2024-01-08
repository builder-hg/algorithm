"""
[문제풀이전략]

1. 문제이해 및 정리
- 양의 정수 A, B (1<= B <= A <= 500)
- A^2 = B^2 + N (1<=N<=1000)

2. 문제풀이방향
1) 반복문으로 A, B의 수를 늘려가며 확인해본다.
2) 조건을 만족할 때마다 쌍의 개수를 1씩 증가시킨다.
"""
import sys

N = int(input())
cnt = 0
for numberA in range(1, 501):
    for numberB in range(1, 501):
        if numberA < numberB:
            continue
        if numberA ** 2 != numberB ** 2 + N:
            continue
        cnt += 1
print(cnt)