"""
[문제풀이전략]

1. 문제 이해 및 정리
- 양, 염소 각각 마리 수 x,y (x>=1)(y>=1) / x+y = n 
- 양, 염소 각각 먹는 사료양 = a, b / a+b = w

2. 풀이방향
1) 양과 염소를 한 마리씩 증가시키며 해를 구해 리스트에 담는다.
2) 각각의 리스트 원소가 2개이상이거나 0이면 -1을 출력한다.
3) 각각의 리스트 원소가 1개라면 해당 원소를 출력한다.
"""
import sys

a, b, n, w = map(int, sys.stdin.readline().split())
sheepList = []
goatList = []

for sheep in range(1, n + 1):
    for goat in range(1, n + 1):
        if (sheep + goat == n) and (sheep * a + goat * b == w):
            sheepList.append(sheep)
            goatList.append(goat)

if len(sheepList) >= 2 or len(sheepList) == 0:
    print(-1)
    sys.exit()

print(sheepList[0], goatList[0])