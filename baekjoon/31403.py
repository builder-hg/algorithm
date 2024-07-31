import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
C = int(input())
print(int(A) + int(B) - C)

AB = A + B
print(int(AB) - C)