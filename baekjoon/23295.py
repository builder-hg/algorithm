import sys
input = sys.stdin.readline

N, T = map(int, input().split())

raw = [0 for _ in range(100002)]
for i in range(N):
    Q = int(input())
    for _ in range(Q):
        s, e = map(int, input().split())
        raw[s] +=1
        raw[e + 1] -= 1

prefix = [0 for _ in range(100001)]
for i in range(100001):
    if i == 0:
        prefix[i] = raw[i]
        continue

    prefix[i] = prefix[i - 1] + raw[i]

_sum = [0 for _ in range(100001)]
for i in range(100001):
    _sum[i] = _sum[i - 1] + prefix[i]

ans = 0
for i in range(T):
    ans += prefix[i]
lst = [0, T]
for i in range(T, 100001):
    if ans < _sum[i] - _sum[i - T + 1]:
        ans = _sum[i] - _sum[i - T + 1]
        lst = [i - T, i]

print(*lst)