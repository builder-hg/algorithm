"""
0. 완전탐색
주어진 N개에서 두 개를 골라서 비교한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
ans = [0 for _ in range(N)]
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    
    ans[i] = cnt + 1

print(*ans)