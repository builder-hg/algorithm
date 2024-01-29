"""
* 누적합으로 풀어보기
"""
import sys
input = sys.stdin.readline

N = int(input())
lst = [0 for _ in range(1002)]
ans = 0
maxX = -1
maxY = -1
prefix_front = [0 for _ in range(1002)]
prefix_back = [0 for _ in range(1002)]
for _ in range(N):
    x, y = map(int, input().split())
    lst[x] = y
    if maxY <= y:
        maxX = x
        maxY = y
for i in range(1, 1001):
    if lst[i] > prefix_front[i-1]:
        prefix_front[i] = lst[i]
    else: 
        prefix_front[i] = prefix_front[i-1]
for i in range(1000, 0, -1):
    if lst[i] > prefix_back[i+1]:
        prefix_back[i] = lst[i]
    else: 
        prefix_back[i] = prefix_back[i+1]
for i in range(1, maxX+1):
    ans += prefix_front[i]
for i in range(1000, maxX, -1):
    ans += prefix_back[i]
print(ans)