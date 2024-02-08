import sys
input = sys.stdin.readline

N = int(input())
points = []
coordinatesX = set()
coordinatesY = set()
for i in range(N):
    x, y = map(int, input().split())
    coordinatesX.add(x)
    coordinatesY.add(y)
    points.append([x, y])

coordinatesX = sorted(coordinatesX)
coordinatesY = sorted(coordinatesY)
print(coordinatesX, coordinatesY)
checkpoint = [[0] * len(coordinatesY) for _ in range(len(coordinatesX))]

print(points)
for x, y in points:
    tx = coordinatesX.index(x)
    ty = coordinatesY.index(y)
    checkpoint[tx][ty] += 1

print(checkpoint)