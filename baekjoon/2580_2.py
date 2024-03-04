import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(9)]

def recur(x, y): # x는 행, y는 열
    # y가 8보다 클 시 행을 이동시킨다.
    if y > 8:
        x += 1
        y = 0

    # 기저조건
    if x > 8:
        for i in range(9):
            for j in range(9):
                print(lst[i][j], end=" ")
            print()
        return


    if lst[x][y] == 0: # 입력받은 스도쿠판을 전체 순회하며 비어있는 항목에 대해서만 다음 작업을 수행한다.
        for i in range(1, 10):
            lst[x][y] = i
            recur(x, y + 1)
    else:
        recur(x, y + 1)


recur(0, 0)