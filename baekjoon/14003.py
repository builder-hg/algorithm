import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[-1, 0] for _ in range(N)]    # 이전에 왔던 index와 현재 값을 저장한다.

LIS = [arr[0]]
for i in range(1, N):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
    else:
        