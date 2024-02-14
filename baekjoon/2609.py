import sys
input = sys.stdin.readline

A, B = map(int, input().split())
numA = A
numB = B
while numB:
    numA, numB = numB, numA % numB

gcd = numA
lcd = (A * B) // gcd
print(gcd)
print(lcd)