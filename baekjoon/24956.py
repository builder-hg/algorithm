"""
0. 문제이해
- WHEE :유사휘파람문자열
- WHEE + E : 유사휘파람 문자열
- WHEE가 떨어져있어도 유사휘파람문자열
- 유사휘파람문자열의 부분수열의 개수 구하기

1. 완전탐색
- 전체 문자열을 순회한다.
- 순회하면저 WHEE가 나온다면 cnt를 증가시킨다.

2. 테스트케이스/관찰
WWAHEWH
- index = 1에서 재시작한다. (휘파람 순서가 어긋났으며 W로 재시작한다.)

3. 구현/설계
순회하는 문자열이 유사휘파람 문자열에 속한다면 스택에 쌓는다.
1) W가 들어올 때 시작한다.
2) 휘파람 순서에 맞게 체크한다.
    - W가 나왔다면 H가 나와야 한다. 
    - H가 나올 때 다음으로 E가 나오는 지 체크한다.
    - 유사휘파람문자열에 속하지 않는 문자가 나올 경우 초기화된다.
3) 순서가 틀어지는 경우 초기화된다.
4) 일치하는 문자열이 있는경우 cnt를 1 증가시키고 초기화시킨다.
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip())
whistle = ["W","H","E","E"]
stack = [-1] # -1은 초깃값이다.
cnt = 0

for i in range(N):
    print(arr[i])
    if stack[-1] == -1:
        if arr[i] == 'W':
            stack.append('W')
        elif arr[i] != 'E' and arr[i] != 'H':
            continue
    elif stack[-1] == 'W':
        if arr[i] == 'H':
            stack.append('H')
        elif arr[i] != 'E' and arr[i] != 'W':
            continue
        else:   
            if arr[i] == 'W':
                stack = [-1, 'W']
            else: stack = [-1] # 초기화
    elif stack[-1] == 'H':
        if arr[i] == 'E':
            stack.append('E')
        elif arr[i] != 'H' and arr[i] != 'W':
            continue
        else:   
            if arr[i] == 'W':
                stack = [-1, 'W']
            else: stack = [-1] # 초기화
    elif stack[-1] == 'E':
        if arr[i] == 'E':
            stack.append('E')
        elif arr[i] != 'H' and arr[i] != 'W':
            continue
        else:   
            if arr[i] == 'W':
                stack = [-1, 'W']
            else: stack = [-1] # 초기화

    if len(stack) == 5:
        cnt += 1
        stack = [-1]
    
    print('stack', stack)

print(cnt)