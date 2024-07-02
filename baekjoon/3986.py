import sys
input = sys.stdin.readline

T = int(input())
ans = 0
while T:
    T -= 1
    arr = list(map(str, input().strip()))

    stack = []
    for i in range(len(arr)):
        if not len(stack):
            stack.append(arr[i])
            continue

        if stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])

    if not len(stack):
        ans += 1

print(ans)

"""
반례: abaabaaa

코드:
import sys
input = sys.stdin.readline

T = int(input())
ans = 0
while T:
    T -= 1
    arr = list(map(str, input().strip()))

    flag = True
    stack = []
    dic = {'A': 0, 'B': 0}

    def check(alpha):
        if stack[-1] != alpha:        # 가장 최근에 스택에 넣은 값이 alpha가 아니라면
            if dic[alpha]:            # alpha의 개수가 0인지 확인한다. 아닐 경우, 교차하는 경우이므로 답이 될 수 없다.
                return False
            
            dic[alpha] += 1           
            stack.append(alpha)
        else:                           # 가장 최근에 스택에 넣은 값이 alpha이므로
            dic[alpha] -= 1           # 원소의 개수를 하나 줄이고
            stack.pop()                 # 스택에서 제거한다.

        return True

    for i in range(len(arr)):
        if not len(stack):                  
            dic[arr[i]] += 1                
            stack.append(arr[i])            
        else:
            if not check(arr[i]):
                flag = False
                break

    if len(stack):              # 스택이 비어있지 않다면 답이 될 수 없다.
        flag = False                

    if flag:
        ans += 1

print(ans)
"""

