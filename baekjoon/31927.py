import sys 
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))

print(N//2)
for i in range(N//2):
    raw[i] += (10 ** 6) - (5000 * i)
    raw[N - i - 1] -= ((10 ** 6) - (5000 * i))
    print(*raw)