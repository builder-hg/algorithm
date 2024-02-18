"""
0. 아이디어
- CCTV 개수: cur
- visited 2차원 배열 선언,
    : CCTV 종류와 경우에 따라서 방문처리
    : 방문하는 함수, 방문하였다가 나가는 함수 두 개를 따로 구현한다.
    : 방문처리 횟수 누적한다.
    : cur == CCTV에 왔을때, 전체 배열의 크기 - 방문처리한 횟수 - CCTV 수를 구한다.
"""
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
visited_count = 0
CCTV = 0
ans = 1 << 64
dir1 = ['U', 'D', 'L', 'R']         # 상, 하, 좌, 우
dir2 = ['UD', 'LR']                 # 상하, 좌우
dir3 = ['UR', 'UL', 'DR', 'DL']     # 상우, 상좌, 하우, 하좌 
dir4 = ['LTR', 'TRD', 'LDR', 'DLU'] # 좌상우, 상우하, 좌하우, 상좌하

# CCTV 개수 구하기
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            CCTV += 1

def come_in(dx, dy, dir):
    global visited_count

    if dir == 'U':
        pass
    elif dir == 'D':
        pass
    elif dir == 'L':
        pass
    elif dir == 'R':
        pass
    elif dir == 'UD':
        pass
    elif dir == 'LR':
        pass
    elif dir == 'UR':
        pass
    elif dir == 'UL':
        pass
    elif dir == 'DR':
        pass
    elif dir == 'DL':
        pass
    elif dir == 'LTR':
        pass
    elif dir == 'TRD':
        pass
    elif dir == 'LDR':
        pass
    elif dir == 'DLU':
        pass
    elif dir == 'UDLR':
        pass
    
    return

def come_out(dx, dy, dir):
    global visited_count

    if dir == 'U':
        pass
    elif dir == 'D':
        pass
    elif dir == 'L':
        pass
    elif dir == 'R':
        pass
    elif dir == 'UD':
        pass
    elif dir == 'LR':
        pass
    elif dir == 'UR':
        pass
    elif dir == 'UL':
        pass
    elif dir == 'DR':
        pass
    elif dir == 'DL':
        pass
    elif dir == 'LTR':
        pass
    elif dir == 'TRD':
        pass
    elif dir == 'LDR':
        pass
    elif dir == 'DLU':
        pass
    elif dir == 'UDLR':
        pass
    
    return

def recur(cur, dx, dy):
    global visited_count

    if cur == CCTV:
        val = N * M - visited_count - CCTV
        if val < ans:
            ans = val
        return
    
    for i in range(dx, N):
        for j in range(dy, M):
            if visited[i][j]:
                continue
            
            mode = arr[i][j]
            if mode == 1:
                dir = ['U', 'D', 'L', 'R']
            elif mode == 2:
                dir = ['UD', 'LR']
            elif mode == 3:
                dir = ['UR', 'UL', 'DR', 'DL']
            elif mode == 4:
                dir = ['LTR', 'TRD', 'LDR', 'DLU']
            else:
                dir = ['UDLR']

            for k in dir:
                come_in(i, j, k)
                recur(cur+1, i+1, j+1)
                come_out(i, j, k)


recur(0,0,0)
"""
0. 아이디어
1) CCTV 별 경우의 수
1: 4개, 좌, 우, 상, 하
2: 2개, 상하, 좌우
3: 4개, (상,우), (상,좌), (하,우), (하,좌)
4: 4개, 좌, 우, 상, 하
5: 1개
[상: U,우:R,하:D,좌:L]
[상하:02, 좌우:13]

1. 풀이방향, 3번 템플릿
1) 답의 개수는 전체배열의 크기 - CCTV의 개수 - #으로 체크한 개수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 행의개수, 열의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
CCTV = 0    # CCTV 개수
HASH = 0    # #의 개수
ans = 1 << 64   # 답
dir1 = ['U', 'D', 'L', 'R'] # 상, 하, 좌, 우
dir2 = ['UD', 'LR']
dir3 = ['UR', 'UL', 'DR', 'DL']
dir4 = ['LTR', 'TRD', 'LDR', 'DLU']

def check(cur_x, cur_y, mode, dir):
    if cur_x == 0 and cur_y == 0:
        return True

    return True

def recur(cur_x, cur_y, mode, dir):
    # 전역변수
    global CCTV
    global HASH
    global wrap

    # 가지치기
    if not check(cur_x, cur_y, mode, dir):
        return

    # 기저조건
    if cur_x == N and cur_y == M:
        return
    
    for dx in range(N):
        for dy in range(N):
            if arr[dx][dy] == 0 or arr[dx][dy] == 6:
                continue
                
            recur(cur_x + 1, cur_y + 1, arr[dx][dy],)

recur(0, 0, -1, -1)

"""