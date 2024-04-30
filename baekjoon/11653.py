import sys
input = sys.stdin.readline

N = int(input())
K = N

if N == 1:
    sys.exit()

for i in range(2, N + 1):
    if i * i > N:
        break

    while K % i == 0:
        print(i)
        K //= i

if K != 1:
    print(K)
