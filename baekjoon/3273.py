"""
[문제풀이전략]

1. 문제 이해 및 정리
2. 문제 풀이 방향
"""
import sys
N = int(input())
listA = sorted(list(map(int, sys.stdin.readline().split())))
X = int(input())
start = 0
end = N-1
cnt = 0
while start < end:
    if listA[start] + listA[end] < X:
        start += 1
        continue
    if listA[start] + listA[end] > X:
        end -= 1
        continue
    if listA[start] + listA[end] == X:
        cnt += 1
        start += 1

print(cnt)