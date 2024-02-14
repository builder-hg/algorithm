"""
0. 예제이해
1. 구현
1) 전체를 다 곱한 뒤 뒤에서부터 숫자를 살핀다.
"""
import sys
input = sys.stdin.readline

N = int(input())
total = 1
ans = 0

for i in range(1, N+1):
    total *= i
arr = list(str(total))

for i in range(len(arr) - 1, -1, -1):
    if arr[i] == '0':
        ans += 1
    else:
        break

print(ans)