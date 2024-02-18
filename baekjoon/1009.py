# 10
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    N, K = map(int, input().split())
    temp = N % 10
    for _ in range(1, K):
        temp *= (N % 10)
        temp %= 10

    if temp == 0:
        print(10)
    else:
        print(temp)