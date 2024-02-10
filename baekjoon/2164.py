import sys
input = sys.stdin.readline

N = int(input())
pow_index = 2

if N == 1 or N == 2:
    print(N)
    sys.exit()

while True:
    pow_index *= 2
    if N <= pow_index:
        ans = (N - (pow_index//2)) * 2
        print(ans)
        break