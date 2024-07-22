"""
01. 각 열마다 합을 구하여 저장한다. (최대 4,000,000)
02. 구간별로 합한 값을 비교하며 큰 값을 구한다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

arr = [[] for _ in range(M)]
for i in range(N):
    for j in range(M):
        arr[j].append(raw[i][j])

col = []
for i in range(M):
    col.append(sum(arr[i]))

K = int(input())
ans = 0
for i in range(M - K + 1):
    tmp = sum(col[i: i + K])
    ans = max(ans, tmp)

print(ans)