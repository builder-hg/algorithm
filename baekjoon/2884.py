"""
구현 - 분기처리
1. 45<=M<=59, 
    - 출력: H, M - 45
2. 0<=M<45,
    1-1) 1<=H:
    - 출력: H - 1, 60 - (45 - M)
    1-2) H = 0:
    - 출력: 23, 60 - (45 - M)

"""
import sys
input = sys.stdin.readline

H, M = map(int, input().split())
if 45 <= M <= 59:
    print(H, M - 45)
else:
    if 1 <= H:
        print(H-1, 60 - (45 - M))
    else:
        print(23, 60 - (45 - M))