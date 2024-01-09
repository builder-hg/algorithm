"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- 막대기둥 개수: N (1<= N <= 1000)
- X좌표와 Y좌표가 N개씩 주어진다. (1 <= X, Y <= 1000)

2. 문제 풀이 방향
- 제일 큰 y값을 기준으로 좌측에서 향하는 버전이랑 우측에서 향하는 버전으로 나누어 구한다.
"""
import sys

N = int(input())
warehouse = [0 for _ in range(1010)]
answer = 0
maxV = 0
timestampX = 0
timestampY = 0
lastX = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    warehouse[x] = y
    if lastX <= x:
        lastX = x
    if timestampY <= y:
        timestampY = y
        timestampX = x
heightL = warehouse[1]
heightR = warehouse[lastX]
        
for i in range(1, timestampX + 1):
    heightL = max(heightL, warehouse[i])
    maxV = warehouse[i]
    for j in range(i+1, timestampX + 2):
        maxV = max(maxV, warehouse[j])
        if heightL <= warehouse[j]:
            break
        if j == timestampX + 1:
            heightL = maxV
    answer += heightL 

for i in range(lastX, timestampX, -1):
    heightR = max(heightR, warehouse[i])
    maxV = warehouse[i]
    for j in range(i+1, timestampX + 2):
        maxV = max(maxV, warehouse[j])
        if heightR <= warehouse[j]:
            break
        if j == timestampX + 1:
            heightR = maxV
    answer += heightR 
print(answer)