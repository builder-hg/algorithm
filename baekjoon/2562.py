import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
maxV = 0
idx = 0

for i in range(9):
    if arr[i] > maxV:
        maxV = arr[i]
        idx = i
print(maxV)
print(idx+1)