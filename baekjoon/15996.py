"""
[문제풀이전략]
1. 문제 이해 및 정리
2. 문제 풀이 방향
"""
import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0
temp = K
while temp <= N:
    cnt += N // temp
    temp *= K

print(cnt)