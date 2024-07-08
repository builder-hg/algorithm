import sys
input = sys.stdin.readline

N, M = map(int, input().split())
raw = [0] + list(map(int, input().split()))
arr = [0 for _ in range(N + 2)]
for _ in range(M):
    a, b, k = map(int, input().split())
    arr[a] += k
    arr[b + 1] -= k

prefix = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i]

for i in range(1, N + 1):
    prefix[i] += raw[i]

print(*prefix[1:N + 1])