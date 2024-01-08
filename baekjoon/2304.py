"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- 막대기둥 개수: N (1<= N <= 1000)
- X좌표와 Y좌표가 N개씩 주어진다. (1 <= X, Y <= 1000)

2. 문제 풀이 방향
- X 좌표를 오름차순으로 정렬하여 따로 리스트(listX)에 저장한다.
- 창고 리스트를 생성한다 (1000)
- 리스트[X]지점의 height 값을 한 번 더 더해준다.
- x가 특정 지점(i)에 도달할 때마다 이후의 값들(warehouse[j+1], warehouse[j+2], ..)을 순회한다. 
    - 처음 j = i, 이며 반복될 때마다 j가 1씩 증가한다.
- warehouse[i] >= 이후의 값(warehouse[j])이라면 
    - height += warehouse[i]를 더해준다.
- warehouse[i] < 이후의 값(warehouse[j])이라면 
    - height += warehouse[j]를 더해준다.
    - i = j를 대입해준다. 
- 이 과정은 계속 반복되다가 i == N + 2면 멈춘다.
- 합산한 height에 warehouse[N+1]을 더해주고 출력한다.
"""
import sys

N = int(input())
warehouse = [0 for _ in range(1010)]
height = warehouse[1]
listX = []
idx = 1
skip = False
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if warehouse[x] != 0:
        warehouse[x+1] = max(warehouse[x], y)
    else:
        warehouse[x] = y
    warehouse[x+1] = y    
    listX.append(x)
listX.sort()

while idx < N:
    for j in range(idx+1, N+1):
        print('idx, j', idx, j)
        if warehouse[idx] > warehouse[j]:
            idx = j
            continue
        else:
            idx += 1
            break
    height += warehouse[idx]
height += warehouse[N+1]
print(height)