"""
문제풀이전략

1.
2.
"""
import sys
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))
upside = 0
idx = 0
cnt = 0

for i in range( N-1):
    if raw[i] > raw[i + 1]:
        idx = i 
        upside += 1

if upside == 0:
    print(N)
    sys.exit()
if upside == 1:
    if idx == N-2:
        if raw[idx-1] <= raw[idx+1]:
            print(2)
        else:
            print(1)
        sys.exit()
    elif idx == 0:
        if raw[idx] <= raw[idx + 2]:
            print(2)
        else:
            print(1)
        sys.exit()
    else:
        if (raw[idx-1] <= raw[idx+1]):
            cnt += 1
        if (raw[idx] <= raw[idx+2]):
            cnt += 1
        print(cnt)
        sys.exit()
else:
    print(0)