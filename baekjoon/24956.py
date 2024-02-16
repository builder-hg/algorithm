"""
1. H 기준으로 보자.
2. 앞에 W개가 몇개인지, 뒤에 E가 몇개인지 빨리 찾아내면 계산식이 나오지 않을까?
3. 계산식 알아내기.

풀이. H를 기준으로 문제를 본다.
1. H를 중앙으로 본다. 해당 H를 유사휘파람으로 지닌 문자열의 개수를 카운팅한다.
2. 앞에 W 2개, E 4개라면,
cnt_w * (cnt_e C 2 + cnt_e C 3 + cnt_e C + 5 ... cnt_E C cnt_E)
= cnt_w * (nC2 + nC3 + ... + nCn)
= cnt_w * (nC0 + nC1 + nC2 + nC3 + ... + nCn - nC0 - nC1)
= cnt_w * (2**n - nC0 - nC1)
"""




"""
(24.02.12)
0. 완전탐색
- 문자열을 순회하며 W가 나온다면 해당 W로 만들 수 있는 모든 경우를 순회하며 확인한다.
=> 시간초과

1. 다른 접근
가능한 휘파람의 개수를 구할 때, 
E는 H로 만들 수 있는 가능성의 개수에 영향을 받고,
H는W로 만들 수 있는 가능성의 개수에 영향을 받는다.

ex. W가 3개라면 H가 1증가할 때 현재의 H로 만들 수 있는 가능성의 개수는 += W의 개수

E를 고려하는게 머리아팠는데 다음처럼 정리가 되는 것 같다!
E가 하나 추가될 때마다 기존에 E로 만들 수 있는 경우에서 * 2,
왜냐면 새로 들어온 E를 붙이거나 붙이지 않거나 하기 때문에.

그리고 새로들어온 E를 가지고 답을 만들 수 있는 경우는 기존 H로 만들 수 있는 가능성의 개수이기에

따라서 현재의 E로 만들 수 있는 가능성의 개수는 
기존에 E로 만들 수 있는 가능성 * 2 + 기존 H로 만들 수 있는 가능성의 개수
import sys
input = sys.stdin.readline

N = int(input())
text = input().strip()
cnt_w = 0 # W의 개수
possible_h = 0  # 현재 H로 가능한 경우, W의 개수, h가 한번씩 들어올때마다 가능성은 cnt_w 만큼 증가한다.
possible_e = 0  # 현재 E로 가능한 경우 
cnt_e = 0  # E의 개수
ans = 0     # 답, 기존 답의 *2,기존 e로 되는 경우

for i in range(N):
    if text[i] == 'W':
        cnt_w += 1
    elif text[i] == 'H':
        possible_h += cnt_w 
    elif text[i] == 'E':
        if cnt_e == 0:
            cnt_e += 1
            possible_e = 1
            continue
        else:
            ans += possible_e
            possible_e = possible_e * 2 + possible_h
    
    ans %= 1000000007

print(ans)

"""

"""if s[i] == 'W':
    cnt_w += 1
elif s[i] == 'H':
    cnt_h += 1
elif s[i] == 'E':
    # cnt_e1, WHE를 만들 수 있는 개수
    # cnt_e2, WHEE를 만들 수 있는 개수

    cnt_e2 += cnt_e2 + cnt_e1
    cnt_e1 += cnt_h

print(cnt_e2)"""

import sys
input = sys.stdin.readline

N = int(input())
text = input().strip()
cnt_w = 0 # W를 만들 수 있는 개수
cnt_h = 0 # WH를 만들 수 있는 개수
cnt_e1 = 0  # WHE를 만들 수 있는 개수
cnt_e2 = 0  # WHEE를 만들 수 있는 개수

for i in range(len(text)):
    if text[i] == 'W':
        cnt_w += 1
    elif text[i] == 'H':
        cnt_h += cnt_w
    elif text[i] == 'E':
        cnt_e2 += (cnt_e2 + cnt_e1)
        cnt_e1 += cnt_h
        cnt_e2 %= 1000000007

print(cnt_e2)





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

"""