"""
0. 특징파악
1. 케이스
((())
[[]]]
- 괄호의 개수가 서로 다르다면 잘못된 케이스
([(]))
- 이전 괄호가 ( 일때 ]가 나온다면 잘못된 케이스
- 이전 괄호가 [ 일때 )가 나온다면 잘못된 케이스

2. 구현/설계
- 문자열을 순회한다.
- 괄호가 나오면 별도의 리스트에 담는다.
- 새로운 괄호가 나온다면 가장 최근에 담은 괄호와 비교한다.
- 어긋나게 나오지 않는다면 계속 담는다. 이때 종류에 따라 딕셔너리에 카운팅한다.
"""
import sys
input = sys.stdin.readline

while True:
    text = list(input())[:-1]
    stack = []

    if len(text) == 1 and text[-1] == '.':
        break

    for i in text:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")



"""
import sys
input = sys.stdin.readline

while True:
    text = list(input()[:-1])
    flag = True
    dd = {'(': 0, ')': 0, '[': 0, ']': 0}
    lst = []
    types = ['(', ')', '[', ']']
    
    if text[0] == '.':
        break

    for word in text:
        if not (word in types):
            continue
        if word == '.':
            break

        if len(lst) == 0:
            if word == ']':
                flag = False
                break
            
            if word == ')':
                flag = False
                break

            lst.append(word)
            dd[word] += 1
            continue

        if lst[-1] == '(' and word == ']':
            flag = False
            break
        
        if lst[-1] == '[' and word == ')':
            flag = False
            break

        if word == ')':
            if dd.get('[') != dd.get(']'):
                flag = False
                break

        if word ==']':
            if dd.get('(') != dd.get(')'):
                flag = False
                break

        lst.append(word)
        dd[word] += 1

    if dd.get('(') != dd.get(')'):
        flag = False
    
    if dd.get('[') != dd.get(']'):
        flag = False

    # print(lst)
    # print(dd)

    if not flag:
        print("no")
    else:
        print("yes")
"""