import sys
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))
T, P = map(int, input().split())

pack_t = 0
for val in raw:
    if val % T == 0:
        pack_t += (val // T)
    else:
        pack_t += (val // T) + 1

pack_p = pack_p = (N // P)
unit_p = 0
if N % P != 0:
    unit_p = (N % P)

print(pack_t)
print(pack_p, unit_p)