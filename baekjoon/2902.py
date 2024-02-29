import sys
input = sys.stdin.readline

arr = list(input().rstrip())
ans = [arr[0]]

for i in range(1, len(arr)):
    if arr[i-1] == '-':
        ans.append(arr[i])

print(*ans,sep="")