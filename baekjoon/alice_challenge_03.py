import sys
input = sys.stdin.readline

arr = list(input().strip())
N = len(arr)

stack = []
for i in range(N):
    if arr[i] != ')':
        stack.append(arr[i])
    else:
        tmp = ''
        while stack[-1] != '(':
            tmp += stack.pop()

        _init = tmp[::-1]
        cur = ''
        stack.pop() # 여는 괄호제거
        k = int(stack.pop()) # 반복횟수
        for _ in range(k):
            cur += _init
        
        stack.append(cur)

ans = ''
for i in range(len(stack)):
    ans += stack[i]

print(len(ans))