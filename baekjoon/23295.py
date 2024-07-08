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
_sum[0] = prefix[0]
_sum[1] = prefix[1]
_sum[2] = prefix[2]
_sum[3] = prefix[3]