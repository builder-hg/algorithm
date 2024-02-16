"""
0. 특징파악
- a**2 + b**2 = c**2 이거나
- b**2 + c**2 = a**2 이거나
- a**2 + c**2 = b**2 이면 직각삼각형이다.
"""
import sys
input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())

    if A == 0 and B == 0 and C == 0:
        break

    powA = A ** 2
    powB = B ** 2
    powC = C ** 2

    if powA + powB == powC or powA + powC == powB or powB + powC == powA:
        print("right")
    else:
        print("wrong") 