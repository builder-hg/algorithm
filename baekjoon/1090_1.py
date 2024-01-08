"""
[문제풀이전략(24.01.02)]
- 기준이 되는 좌표 선택, x를 0부터 1000001까지 y를 0부터 1000001까지 순회한다.
- 주어진 좌표와 기준점간의 거리를 담은 리스트를 정렬한다.
	- 해당 리스트의 첫번째 값은 한 개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수이다
	- 해당 리스트의 첫번째 값부터 k개까지의 합은 k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수
- 위에서 구한 리스트의 누적합을 담은 리스트를 새로 생성한다.
- N개의 리스트를 순회하며 누적합을 담은 리스트들의 각 인덱스 중 가장 작은 값을 골라 담는다. 
- 골라담은 리스트를 하나씩 출력한다.
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
for i in range(1000001):
    for j in range(1000001):
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