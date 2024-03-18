import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))

if N == 1:
    print(lst[0] * lst[0])
else:
    print(lst[0] * lst[N-1])
    
