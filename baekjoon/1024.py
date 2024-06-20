"""
S = (org + 1) + (org + 2) + ... + (org + i), 
- i개의 항이 L 이상이어야 한다.
- S는 N과 같아야 한다.

S = org * i + (i * (i + 1)) // 2 = N
org * i = N - ((i * (i + 1)) // 2)
org = (N - ((i * (i + 1)) // 2)) / i => 나머지가 0 이어야 한다.
"""
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

def printFn(s, e):
    for i in range(s, e):
        print(i, end=" ")

    return

for i in range(L, 101):
    organdi = N - ((i * (i + 1)) // 2)
    if (organdi % i) == 0:
        org = organdi // i
        if (org + 1) >= 0:
            printFn(org + 1, org + 1 + i)
            sys.exit()

print(-1)