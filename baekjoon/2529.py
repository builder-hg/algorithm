"""
0. 문제특징이해
- 중복 X
- 조건을 만족해야 한다. (가지치기)
"""

import sys
import copy
input = sys.stdin.readline

N = int(input())
arr = list(input().split())
ans = [0 for _ in range(N+1)]
wrap = []
visited = [0 for _ in range(10)]
fin = False

def check(cur):
    if cur <= 1:
        return True
    
    if arr[cur-2] == '<' and ans[cur - 2] > ans[cur - 1]:
        return False
    if arr[cur-2] == '>' and ans[cur - 2] < ans[cur - 1]:
        return False
    
    return True

def recur(cur, dir):
    global fin
    if fin:
        return

    if not check(cur):  # 가지치기
        return

    if cur == (N+1):

        temp = ''
        for i in range(len(ans)):
            temp += str(ans[i])
        # wrap.append(temp)
        print(temp)

        fin = True
        return

    if dir == -1:
        leng = range(9, -1, -1)
    elif dir == 1:
        leng = range(10)

    for i in leng:
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = i
        recur(cur+1, dir)
        visited[i] = False


recur(0,-1)
fin = False
recur(0,1)
# print(wrap[-1])
# print(wrap[0])