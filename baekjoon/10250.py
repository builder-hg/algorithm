"""
1. 분기처리
    - N % H 값이 층에 해당한다.
    - (N // H) + 1값이 호수에 해당한다.
2. 출력
    호수는 십의자리로, 10보다 작다면 앞에 0을붙인다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    H, W, N = map(int, input().split())

    if N % H == 0:
        A = H
        B = (N // H)
    else:
        A = N % H
        B = (N // H) + 1
    if B < 10:
        print(str(A)+'0'+str(B))
    else:
        print(str(A)+str(B))
