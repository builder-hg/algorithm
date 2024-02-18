"""
하얀색(0, 0) 다음에 검정칸이 주어진다.
1 번째 줄 : 하양, 검정
2 번째 줄 : 검정, 하양
...
8 번째 줄 ; 검정, 하양
"""
import sys
input = sys.stdin.readline

arr = [[-1] * 9] + [[-1]+list(input().strip()) for _ in range(8)]
ans = 0

for i in range(1, 9):
    for j in range(1, 9):
        if i % 2 == 1 and j % 2 == 1:
            if arr[i][j] == 'F': ans += 1
        if i % 2 == 0 and j % 2 == 0:
            if arr[i][j] == 'F': ans += 1

print(ans)