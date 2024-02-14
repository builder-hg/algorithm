"""
문제풀이전략

1. 완전탐색으로 접근하자
- x좌표와 y좌표를 1씩 증가시키며 모든 좌표를 살펴본다.
- 해당 좌표에서 규현이의 좌표와의 거리가 r1이며
- 승환이의 좌표와의 거리가 r2인지를 확인한다.
- 조건을 만족하는 좌표의 개수를 카운팅한다.
"""
import sys
import math
input = sys.stdin.readline

Q = int(input())

while Q:
    Q -= 1

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    cnt = 0

    # 범위 커팅
    xe = max(x1 - r1, x1 + r1, x2 - r2, x2 + r2)
    xs = min(x1 - r1, x1 + r1, x2 - r2, x2 + r2)
    ys = min(y1 - r1, y1 + r1, y2 - r2, y2 + r2)
    ye = max(y1 - r1, y1 + r1, y2 - r2, y2 + r2)

    for i in range(xs, xe):
        for j in range(ys, ye):
            distA = math.sqrt((x1 - i)**2 + (y1 - j)**2)
            distB = math.sqrt((x2 - i)**2 + (y2 - j)**2)
            if distA != int(distA): continue
            if distB != int(distB): continue

            if distA == r1 and distB == r2:
                cnt += 1
    print(cnt)


"""
조규현 x1, y1 + r1 => 원 형태로 나온다.
백승환 x2, y2 + r2 => 원 형태로 나온다.
원이 몇개의 점에서 접점을 가지냐는 문제이다.
원 두개가 동일하면 무한대가 된다.
- 원이 3개가 겹치도록 하는 거는 불가능하다.
- 한 원이 다른 원을 포함해버리는 경우, 포함하는데 한점에서 만나는 경우도 있다.
# 보류
"""