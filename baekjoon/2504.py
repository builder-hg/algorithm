import sys
input = sys.stdin.readline

arr = list(map(str, input().strip()))
cntA = 0    # (의 개수
cntB = 0    # [의 개수

stack = []
for i in range(len(arr)):
    if arr[i] == '(':
        cntA += 1
        stack.append('(')
    elif arr[i] == '[':
        cntB += 1
        stack.append('[')
    elif arr[i] == ')':
        if cntA == 0:
            print(0)
            sys.exit()

        cntA -= 1
        
        if stack[-1] == '(':
            stack.pop()
            stack.append(2)
            continue

        tmp = 0
        while stack:
            if stack[-1] == '[':
                print(0)
                sys.exit()

            if stack[-1] == '(':
               stack.pop()
               stack.append(tmp)
               break
            else:
                tmp += stack.pop() * 2 
    else:
        if cntB == 0:
            print(0)
            sys.exit()

        cntB -= 1
        
        if stack[-1] == '[':
            stack.pop()
            stack.append(3)
            continue

        tmp = 0
        while stack:
            if stack[-1] == '(':
                print(0)
                sys.exit()

            if stack[-1] == '[':
               stack.pop()
               stack.append(tmp)
               break
            else:
                tmp += stack.pop() * 3

ans = 0
for i in range(len(stack)):
    if type(stack[i]) is not int:
        print(0)
        sys.exit()

    ans += stack[i]

print(ans)