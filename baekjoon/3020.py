import sys
input = sys.stdin.readline

N, H = map(int, input().split())
raw = [0 for _ in range(500001)]
prefix = [0 for _ in range(500001)]

for i in range(N):
    unit = int(input())
    if i % 2 == 0:
        raw[1] += 1
        raw[unit + 1] -= 1
    else:
        raw[H - unit + 1] += 1

for i in range(1, H+1):
    prefix[i] = prefix[i-1] + raw[i]

minV = 1 << 64
for i in range(1, H+1):
    minV = min(minV, prefix[i])

cnt = 0
for i in range(1, H+1):
    if prefix[i] == minV:
        cnt += 1

print(minV, cnt)