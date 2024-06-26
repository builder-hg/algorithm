import sys
input = sys.stdin.readline 

Q = int(input())
count = 1
while count <= Q:
    N = int(input())
    arrX = []
    arrY = []

    for _ in range(N):
        x, y = map(float, input().split())
        arrX.append(x)
        arrY.append(y)

    arrX.sort()
    arrY.sort()

    width = max(arrX) - min(arrX)
    height = max(arrY) - min(arrY)
    area = width * height
    perimeter = 2 * (width + height)
    
    print(f'Case {count}: Area {area}, Perimeter {perimeter}')
    count += 1