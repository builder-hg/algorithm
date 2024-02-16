import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    val = int(input())
    lst.append(val)

lst.sort()
for i in range(N):
    print(lst[i])