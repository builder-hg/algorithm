"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 수열의 크기 N(1<=N<=10000), 구간의 합 M(1<=M<=300000000), 원소의 크기 < 30,000
- 인접한 원소들의 합이 구간의 합과 일치하는 경우의 개수를 출력한다.

2. 문제 풀이 방향
"""
import sys
N, goal = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split())) + [0]

s = 0
e = 0
cnt = 0
total = listA[0]
while e < N:
    if total < goal:
        e += 1
        total += listA[e]
    elif total > goal:
        total -= listA[s]
        s += 1
    else:
        cnt += 1
        total -= listA[s]
        s += 1
        e += 1
        total += listA[e]
print(cnt)