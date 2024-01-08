"""
[문제풀이전략(24.01.03)]
* 모든 좌표 혹은 사람을 보는게 오래 걸리니 불필요한 좌표 혹은 사람을 걸러내보자
* 맨하탄 거리체계에 한해서 2차원에서 주어진 좌표들이 최소로 이동할 지점은 주어진 x 좌표들의 중앙값, 주어진 y 좌표들의 중앙값이다.
* 따라서 주어진 N개의 x, y 좌표들이 답이될 수 있는 좌표들이다. => 시간복잡도는 N * N
"""
import sys
N = int(input())
listX = []
listY = []
prefixDistanceWrap = []
answerList = []

for _ in range(N):
    xi, yi = map(int, sys.stdin.readline().split())
    listX.append(xi)
    listY.append(yi)
for i in listX:
    for j in listY:
        baseX = i
        baseY = j
        distanceList = []
        alignedDistanceList = []
        prefixDistanceList = []
        prefixSum = 0
        for k in range(N):
            distanceX = abs(baseX - listX[k])
            distanceY = abs(baseY - listY[k])
            distanceList.append(distanceX + distanceY)
        alignedDistanceList = sorted(distanceList)
        for item in alignedDistanceList:
            prefixSum += item
            prefixDistanceList.append(prefixSum)
        prefixDistanceWrap.append(prefixDistanceList)

for listIndex in range(N):
    comparativeValue = 100000000
    for prefixIndex in range(len(prefixDistanceWrap)):
        if prefixDistanceWrap[prefixIndex][listIndex] < comparativeValue:
            comparativeValue = prefixDistanceWrap[prefixIndex][listIndex]
    answerList.append(comparativeValue)    
    
print(*answerList)