"""
[문제풀이전략]

1. 문제 이해 및 정리
- 도화지의 크기 : 가로 100, 세로 100
- 색종이의 크기 : 가로 10, 세로 10
- 색종이 수 N(100이하), 순서대로 도화지의 x, y 좌표의 시작점이, 주어진다. (0<=x<=100, 0<=y<=100)

2. 문제 풀이 방향
2-1.
1) x리스트의 좌표와, y리스트의 좌표를 담는다.
2) 0으로만 이루어진 2차원 배열(도화지)을 만든다. (100 * 100)
3) N만큼 순회하면서 다음을 계산한다. (주어진 색종이들을 순회하는 개념)
4) i번의 색종이의 x좌표와 y좌표 범위에 해당하는 경우 1을 넣는다.
5) 도화지의 값을 계산해서 출력한다.

2-2. 반례해결하기
N=4, K=1
1 1 1
2 2 2
3 3 3
4 4 4
가 주어졌을 때 실제 답은 3이다.
"""
import sys

N = int(input())
positionX = [] # 시작지점만 담는다.
positionY = [] # 시작지점만 담는다.
for _ in range(N):
    tempX, tempY = map(int, sys.stdin.readline().split())
    positionX.append(tempX)
    positionY.append(tempY)
paper = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N): # 어떤 색종이인가
    for j in range(positionX[i], positionX[i] + 10): # 1이 들어가야할 x 좌표들
        for k in range(positionY[i], positionY[i] + 10): # 1이 들어가야할 y 좌표들
            paper[j][k] = 1

print(sum(sum(paper, [])))
