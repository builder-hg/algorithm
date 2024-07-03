"""
a b c d 4 
c d 4

01. arr를 순회하며 stack에 쌓는다.
02. rm의 최신 값과 arr[i]가 같다면 arr[i]에서 arr[i-1]방향으로, rm의 값을 거꾸로 살펴본다.
03. 일치한다면 stack의 전체길이 - rm의 길이 부터 전체길이까지 pop 해준다.
"""
import sys
input = sys.stdin.readline

def check():
    rm_index = len(rm) - 2
    index = len(stack) - 1

    if len(rm) == 1:
        return True

    if not stack:
        return False

    while stack and rm_index >= 0:
        if not stack:
            return False
        
        if stack[index] != rm[rm_index]:
            return False
        rm_index -= 1
        index -= 1
        
    return True

raw = list(map(str, input().strip()))
rm = list(map(str, input().strip()))

stack = []
for i in range(len(raw)):
    if raw[i] == rm[-1]:
        if check():    # 폭발문자열이라면
            cnt = len(rm) - 1
            while cnt:
                stack.pop()
                cnt -= 1
        else:
            stack.append(raw[i])

    else:
        stack.append(raw[i])

if stack:
    print(*stack, sep="")
else:
    print("FRULA")