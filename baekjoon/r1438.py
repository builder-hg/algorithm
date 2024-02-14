import sys
input = sys.stdin.readline

N = int(input())
points = []
coordinatesX = set()
coordinatesY = set()
min_area = 1 << 64
for i in range(N):
    x, y = map(int, input().split())
    coordinatesX.add(x)
    coordinatesY.add(y)
    points.append([x, y])

coordinatesX = sorted(coordinatesX)
coordinatesY = sorted(coordinatesY)
checkpoint = [[0] * len(coordinatesY) for _ in range(len(coordinatesX))]

for i in range(len(coordinatesX)):
    for j in range(i + 1, len(coordinatesX)):
        for k in range(len(coordinatesY)):
            for l in range(k + 1, len(coordinatesY)):
                # 직사각형의 넓이 계산
                area = (coordinatesX[j] - coordinatesX[i]) * (coordinatesY[l] - coordinatesY[k])
                # 내부에 있는 점의 개수 카운트
                cnt = 0
                for x, y in points:
                    if coordinatesX[i] <= x <= coordinatesX[j] and coordinatesY[k] <= y <= coordinatesY[l]:
                        cnt += 1
                # 내부에 있는 점의 개수가 N/2 이상인 경우만 고려
                if area < min_area and cnt >= N / 2:
                    min_area = area  # 최소 넓이 갱신


# print(points)
# for x, y in points:
#     tx = coordinatesX.index(x)
#     ty = coordinatesY.index(y)
#     checkpoint[tx][ty] += 1

print(min_area)