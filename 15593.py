"""
[문제풀이전략]

1. 문제 이해 및 정리
- 구조원 : N(1 <= N <= 100)
- 0 <= 수영장개장시간 < 1000
- 0 <= 구조원들의 근무 시간 < 1000
- N개 중 N-1개를 골라 구조원들이 근무할 수 있는 최대 근무 시간을 구하라.
- 이때 최대 근무시간을 산정할 때 구조원들의 근무 시간이 끊기면 안된다.

2. 문제 풀이 방향
1) 시작지점과 끝지점리스트를 생성해 담는다.
2) N개중 N-1개의 소들의 근무시간을 담을 리스트를 생성한다.
3) N개 중 제외할 특정 지점(exceptIndex) 한 개를 골라 그 시간대를 제외한 나머지 시간대를 순회한다.
4) 0~999 사이즈의 0으로 채워진 리스트에 소들의 근무시간 첫지점부터 끝지점까지 1로 바꾼다.
"""
import sys

N = int(input())
positionX = []
positionY = []
cntList = []
for _ in range(N):
    tempX, tempY = map(int, sys.stdin.readline().split())
    positionX.append(tempX)
    positionY.append(tempY)
for exceptIdx in range(N):
    officeHours = [0 for _ in range(0, 1000)]
    for i in range(N):
        if i == exceptIdx:
            continue
        for j in range(positionX[i], positionY[i]):
            officeHours[j] = 1
    cntList.append(sum(officeHours))

print(max(cntList))
