"""


"""
import sys

c =2

lst = []
for i in range(100000):
    square = i * i
    if square > (2 ** 31 - 1):
        break

    lst.append(square)
    lst.append(square)
lst.sort()

s = 0
e = len(lst) - 1
while s < e:
    if lst[s] + lst[e] > c:
        e -= 1
    elif lst[s] + lst[e] < c:
        s += 1
    else:
        print("yes")
        sys.exit()

print("no")
sys.exit()

