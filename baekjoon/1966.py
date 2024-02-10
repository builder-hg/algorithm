"""
0. 특징파악하기
- 현재 위치한 문서보다 중요도가 높은 문서가 존재한다면, 해당 문서들을 먼저 출력한다.
- 중요도별 문서의 개수는 딕셔너리로 관리한다.
- 2차원 배열로 문서들을 관리한다. 인덱스 0 에는 문서의 고유번호, 1에는 문서의 중요도가 들어간다.

1. 설계
- 딕셔너리에 중요도별 문서개수를 기록한다.
- 문서를 스택에 넣어 관리한다. 
- 원하는 문서를 출력할 때까지 해당 스택에 다시 추가하거나 빼는 행위를 반복한다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    N, idx = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    stack = []
    dd = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for i in range(len(lst)):
        dd[lst[i]] += 1
        elem = [i, lst[i]]
        stack.append(elem)
    
    while True:
        now = stack[0][1]   # 출력가능한 문서의 중요도를 파악한다.
        show = True
        for i in range(now + 1, 10):
            if dd[i] > 0:
                stack.append(stack[0])
                stack.pop(0)
                show = False
                break

        if not show: continue

        if stack[0][0] == idx:
            cnt += 1
            print(cnt)
            break
        else:
            cnt += 1
            dd[now] -= 1
            stack.pop(0)


