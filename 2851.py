"""
[문제풀이전략]

1. 문제 이해 및 정리
- 특정 인덱스에 위치한 버섯을 먹지않는다면 이후 인덱스에 위치한 버섯들도 먹을 수 없다.
- 먹은 버섯들의 합 중에 100과 최대한 가까운 합을 출력한다. 앞뒤로 동일하다면 더 큰 값을 택한다.

2. 문제 풀이 방향
1) 주어진 버섯들의 점수를 리스트에 담는다.
2) 리스트를 순회하며 각각의 점수를 더한 합이 100보다 커질 때 멈추며 이때의 인덱스와 합을 기억한다.
3) 100을 초과하는 인덱스에서 1을 뺀 인덱스까지의 누적합을 구한다.
4) 2)에 해당하는 합과 3)에 해당하는 누적합 중 100과의 차이값 중 적은 값을 구해 출력한다.
"""
import sys

point = []
for _ in range(10):
    point.append(int(input()))
prefix = 0
prevPrefix = 0 
overIndex = 0

if point[0] > 100:
    print(prefix)
    sys.exit()

for idx in range(len(point)):
    prefix += point[idx] # 현재까지의 누적합
    if idx != 0: # 이전까지의 누적합 구하기
        prevPrefix = prefix - point[idx]
    if prefix > 100 :
        break
    elif prefix == 100:
        print(100)
        sys.exit()

diffNext = abs(100 - prefix)
diffPrev = abs(100 - prevPrefix)
if diffNext > diffPrev:
    print(prevPrefix)
elif diffNext <= diffPrev:
    print(prefix)
