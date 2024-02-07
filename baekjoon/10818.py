import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
minV = 10000010
maxV = -10000010

for i in range(N):
    if arr[i] <= minV:
        minV = arr[i]
    if arr[i] >= maxV:
        maxV = arr[i]

print(minV, maxV)