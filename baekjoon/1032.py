import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    _str = input().strip()
    arr.append(_str)
ans = ['' for _ in range(len(arr[0]))]

for i in range(len(ans)):
    mark = True
    for j in range(1, N):
        if arr[j][i] != arr[j-1][i]:
            ans[i] = '?'
            mark = False
            break

    if mark:
        ans[i] = arr[0][i]

print(*ans, sep="")