import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(21)]
arr[0] = 0
arr[1] = 1

for i in range(2, 21):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[N])