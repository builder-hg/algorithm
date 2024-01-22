import sys

height = []
for _ in range(9):
    num = int(input())
    height.append(num)
height.sort()
goal = sum(height) - 100

s = 0
e = 8
while s < e:
    if height[s] + height[e] < goal:
        s += 1
    elif height[s] + height[e] > goal:
        e -= 1
    else:
        numA = height[s]
        numB = height[e]
        height.remove(numA)
        height.remove(numB)
        break
height.sort()
for item in height:
    print(item)