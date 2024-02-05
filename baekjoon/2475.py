import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
temp = 0
ans = 0
for i in range(len(arr)):
    temp += arr[i] ** 2
ans = temp % 10
print(ans)
