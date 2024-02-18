# 6

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(N+1)]

for i in range(K):
    start, end = map(int, input().split())
    cnt = (end - start + 1) // 2

    for j in range(cnt):
        arr[start + j], arr[end - j] = arr[end - j], arr[start + j]

print(*arr[1:])