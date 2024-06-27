import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
T = int(input())
stack = []
while T:
    T -= 1

    query = list(map(str, input().split()))
    if query[0] == 'P':
        arr.append(query[1])
    elif query[0] == 'L':
        if not len(arr):
            continue

        alpha = arr.pop()
        stack.append(alpha)
    elif query[0] == 'B':
        if not len(arr):
            continue

        arr.pop()
    else:           # 'D'
        if not len(stack):
            continue

        alpha = stack.pop()
        arr.append(alpha)

for i in arr[::-1]:
    stack.append(i)
print(*stack[::-1], sep="")
