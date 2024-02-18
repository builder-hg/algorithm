import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    star = 2 * i - 1
    rest = (2 * N - star) // 2

    print(' ' * rest + '*' * star )

for i in range(2, N+1):
    star = 2 * i - 1
    rest = (2 * N - star) // 2

    print(' ' * rest + '*' * star)
