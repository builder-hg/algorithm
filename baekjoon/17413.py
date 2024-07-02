import sys
input = sys.stdin.readline

arr = list(map(str, input().strip()))
ans = []
stack = []
on = False   # 정방향일 때는 True를 역방향일 때는 False
for i in range(len(arr)):
    if arr[i] == '<':   # 정방향 시작
        ans.extend(stack[::-1])
        stack = []
        stack.append(arr[i])

        on = True
        continue
    elif arr[i] == '>': # 정방향 종료
        stack.append(arr[i])
        ans.extend(stack)
        stack = []

        on = False
        continue

    if not on and arr[i] == ' ':
        ans.extend(stack[::-1])
        ans.append(' ')
        stack = []
        continue

    stack.append(arr[i])

if stack:
    ans.extend(stack[::-1])

print(*ans, sep="")