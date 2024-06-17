import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    print("*" * i, end="")
    print(" " * (2 * (N - i)), end="")
    print("*" * i)
for i in range(N - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (N - i)), end="")
    print("*" * i)