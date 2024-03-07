'''
3번 물약을 샀어
3번물약 할인정보, 3->1
만약 내가 다음에 살 물약이 할인정보 안에 있는 거라면
expense = 초기리스트[i+1] - discount
이때 초기리스트 <= discount면 expense = 1
'''

import sys
import copy
input = sys.stdin.readline

def get_min_price():
    expense = 0
    copy_arr = copy.deepcopy(price)

    for i in range(N):
        now = arr[i]
        expense += copy_arr[now]
        for elem in info[now]:
            if copy_arr[elem[0] - 1] <= elem[1]:
                copy_arr[elem[0] - 1] = 1
            else:
                copy_arr[elem[0] - 1] -= elem[1]
    return expense

def recur(cur):
    global ans

    if cur == N:
        ans = min(ans, get_min_price())
        return
    
    for i in range(N):
        if visited[i] == True:
            continue

        visited[i] = True
        arr[cur] = i

        recur(cur + 1)
        visited[i] = False

N = int(input())
price = list(map(int, input().split()))
info = [[] for _ in range(N)]
for i in range(N):
    cnt = int(input())
    for j in range(cnt):
        no, discount = map(int, input().split())
        info[i].append([no, discount])
ans = 1 << 64
arr = [0 for _ in range(N)]
visited = [False for _ in range(N)]

recur(0)
print(ans)
