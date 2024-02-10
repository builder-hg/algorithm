import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
total = 0
for i in range(N):
    total += (arr[i] / max_value) * 100
average = total / N
print(average)