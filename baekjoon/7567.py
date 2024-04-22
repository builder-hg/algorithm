"""
1. 이전에 위치한 그릇의 모양과 비교해야 한다.
- 이전에 '('라면, 동일하다면 + 5, 다르다면 + 10
- 이전 값을 갱신한다.
"""
import sys
input = sys.stdin.readline

arr = list(input().strip())
que = []
total = 0

for cur in arr:
    if len(que) == 0:
        que.append(cur)
        total += 10
        continue

    prv = que.pop()
    que.append(cur)
    if prv == cur:
        total += 5
    else:
        total += 10

print(total)