import sys
input = sys.stdin.readline

N, K = map(int, input().split())
val = 1
for i in range(K):
    val *= (N - i)
for i in range(K, 0, -1):
    val //= i

print(val)