import sys
import math
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if dis == 0 and r1 == r2:
        print(-1)
    elif dis == abs(r1 - r2) or dis == (r1 + r2):
        print(1)
    elif dis > abs(r1 - r2) and dis < (r1 + r2):
        print(2)
    else:
        print(0)