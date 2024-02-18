import sys
input = sys.stdin.readline

N = int(input())
lst = [0 for _ in range(N)]
for i in range(N):
    num = int(input())
    lst[i] = num
lst.sort()
print(*lst)