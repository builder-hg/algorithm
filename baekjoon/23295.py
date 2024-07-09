import sys
input = sys.stdin.readline

N, T = map(int, input().split())

raw = [0 for _ in range(100002)]
for i in range(N):
    Q = int(input())
    for _ in range(Q):
        s, e = map(int, input().split())
        raw[s] +=1
        raw[e] -= 1

cnt = [0 for _ in range(100001)]
for i in range(1, 100001):
    cnt[i] = cnt[i - 1] + raw[i - 1]

prefix = [0 for _ in range(100001)]
for i in range(1, 100001):
    prefix[i] = prefix[i - 1] + cnt[i]

prv = prefix[T] - prefix[0]
ans = [0, T]
for i in range(T, 100001):
    cur = prefix[i] - prefix[i - T]
    if prv < cur:
        prv = cur
        ans = [i - T, i]

print(*ans)
