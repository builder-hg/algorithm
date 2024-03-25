import sys
input = sys.stdin.readline

K = int(input())
v = [500, 100, 50, 10, 5, 1]
cnt = 0
idx = 0
val = 1000 - K

while idx < 6:
    isDivide = val // v[idx]
    if isDivide != 0:
        cnt += isDivide
    val %= v[idx]
    idx += 1 

print(cnt)