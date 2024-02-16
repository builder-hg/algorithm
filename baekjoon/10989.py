import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(10002)]
for i in range(N):
    num = int(input())
    arr[num] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    cnt = arr[i]
    while cnt:
        cnt -= 1
        print(i)
