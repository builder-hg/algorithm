"""
윤년
1. 4의 배수 and 100의 배수가 아님
2. 4의 배수 and 400의 배수
"""
import sys
input = sys.stdin.readline

N = int(input())
if N % 4 != 0:
    print("0")
    sys.exit()

if N % 400 == 0:
    print("1")
    sys.exit()

if N % 100 != 0:
    print("1")
    sys.exit()

print("0")