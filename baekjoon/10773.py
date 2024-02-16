import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    
    if num == 0:
        lst.pop()
        continue

    lst.append(num)

if len(lst) == 0:
    print(0)
else:
    print(sum(lst))