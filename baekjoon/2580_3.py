'''
1. 설계
- 비어있는 빈칸에 1부터 9까지 숫자를 넣어본다.
- 스도쿠를 다 채웠다면 0,0에서 8,8까지 순회하며 스도쿠의 조건(가로/세로/대각서)들을 충족하는 지 확인한다.
    - 충족한다면 해당 배열을 출력하고 종료한다.
'''
import sys
import copy
input = sys.stdin.readline

def check(x, y, val):
    # 가로검증
    for j in range(9):
        if j == y: continue
        if copy_arr[x][j] == val:
            return False

    # 세로검증
    for j in range(9):
        if j == x: continue
        if copy_arr[j][y] == val:
            return False
    
    # 3*3 검증
    if y >= 0 and y <= 2:
        ny = 3
    elif y <= 5:
        ny = 6
    else:
        ny = 9

    if x >= 0 and x <= 2:
        nx = 3
    elif x <= 5:
        nx = 6
    else:
        nx = 9

    for i in range(nx - 3, nx):
        for j in range(ny - 3, ny):
            if i == x and j == y: continue
            if copy_arr[i][j] == val:
                return False
    return True

def recur(x, y):
    if y == 9:
        x += 1 
        y = 0
    
    if x == 9:
        for i in range(9):
            for j in range(9):
                print(copy_arr[i][j], end=" ")
            print()
        sys.exit()
    
    if arr[x][y] == 0:
        for i in range(1, 10):
            copy_arr[x][y] = i
            if check(x, y, i): 
                recur(x, y + 1)
            copy_arr[x][y] = 0
    else:
        recur(x, y + 1)


arr = [list(map(int, input().split())) for _ in range(9)]
copy_arr = copy.deepcopy(arr)
recur(0, 0)
