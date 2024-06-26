"""
1. 완전탐색
1-1) 사대를 순회한다 (M, 100,000)
1-2) 동물을 순회한다.(N, 100,000)
    - 각각의 사대에서 해당 동물들이 사정거리 내에 있는 지 카운팅한다.

2. 이진탐색
1-1) 동물을 순회한다. (N, 100, 000)
1-2) 해당 동물의 위치에서 사정거리내에 있는 사대를 이진탐색으로 찾아본다. (log M, 5)
"""
import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
targets = sorted(list(map(int, input().split())))
animals = []
for _ in range(N):
    a, b = map(int, input().split())
    animals.append([a, b])

ans = 0
for i in range(N):
    positionX = animals[i][0]
    positionY = animals[i][1]

    s = 0
    e = len(targets) - 1
    while s <= e:
        mid = (s + e) // 2

        if targets[mid] < positionX:
            s = mid + 1
        elif targets[mid] > positionX:
            e = mid - 1
        else:
            s = mid
            break

    if s < M and abs(targets[s] - positionX) + positionY <= L:
        ans += 1
    elif e < M and abs(targets[e] - positionX) + positionY <= L:
        ans += 1


print(ans)