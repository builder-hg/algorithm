import sys
input = sys.stdin.readline

arr = list(map(str, input().strip()))

ans = 0
stack = []
step = 0
for i in range(len(arr)):
    if arr[i] == '(':
        step = 1
        stack.append(0)
    else:       # ')'
        step -= 1
        stack.pop()
        if step == 0:   # 레이저에 해당한다.
            ans += len(stack)   # 현재 스택개수만큼 분할횟수를 더한다.

            continue
        
        ans += 1

print(ans)
