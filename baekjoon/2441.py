import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    print(' ' * i + '*' * (N - i))
