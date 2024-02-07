import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().strip()))
total = 0
for i in range(N):
    total += int(arr[i])
print(total)