"""
3
NYY
YNY
YYN

i 1 ~ N까지 순회 (자신)
j (i+1) ~ N까지 순회(다른 요소)
"""
import sys
input = sys.stdin.readline                  

N = int(input())
v = [[False for _ in range(N)] for _ in range(N)]
arr = []
for i in range(1, N + 1):
    tmp = list(input().strip())
    arr.append(tmp)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue

            if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[j][k] == 'Y'):
                v[i][j] = True

ans = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if v[i][j]: 
            tmp += 1

    ans = max(ans, tmp)

print(ans)