import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    A, B = map(int, input().split())
    print(A + B)