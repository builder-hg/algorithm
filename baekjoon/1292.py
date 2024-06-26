"""
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7 
"""
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

arr = [0]
for i in range(1, B + 1):
    for _ in range(i):
        arr.append(i)

ans = 0
for i in range(A, B + 1):
    ans += arr[i]

print(ans)