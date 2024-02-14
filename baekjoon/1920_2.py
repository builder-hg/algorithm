import sys
input = sys.stdin.readline

N = int(input())
rawN = list(map(int, input().split()))
dictN = {}
for i in range(N):
    val = rawN[i]
    dictN[val] = dictN.get(val, 0) + 1

M = int(input())
rawM = list(map(int, input().split()))

for i in range(M):
    val = rawM[i]
    res = dictN.get(val, 0)
    if res != 0:
        print(1)
    else:
        print(0)