"""
문제풀이전략
1. 주어진 좌표의 개수(N)가 홀수/짝수인지 구분한다.
2. x 좌표들과 y 좌표들을 리스트(listX, listY)에 담아 정렬한다.
3. N이 짝수라면 최소거리의 합이 되는 좌표는 listX[N//2 - 1], listY[N//2 - 1]이다. (추가로 더 있으나 생략한다.)
4. N이 홀수라면 최소거리의 합이 되는 좌표는 listX[N//2], listY[N//2]이다. 
5. listX와 listY를 순회하며 목표 좌표와의 절댓값을 구하여 합산한다.
"""
import sys
N = int(input())
listX = []
listY = []
minSum = 0
for _ in range(N):
    xi, yi = map(int, sys.stdin.readline().split())
    listX.append(xi)
    listY.append(yi)
listX.sort()
listY.sort()

if N % 2:
    # N이 홀수일때
    dx = listX[N//2]
    dy = listY[N//2]
else:
    # N이 짝수일때
    dx = listX[N//2 - 1]
    dy = listY[N//2 - 1]
    
for i in range(N):
    minSum += abs(dx - listX[i])
    minSum += abs(dy - listY[i])

print(minSum)