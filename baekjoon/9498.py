# 분기처리
import sys
input = sys.stdin.readline

N = int(input())
if 90 <= N:
    print("A")
elif 80 <= N:
    print("B")
elif 70 <= N:
    print("C")
elif 60 <= N:
    print("D")
else:
    print("F")