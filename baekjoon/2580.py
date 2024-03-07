'''
1. 풀이방향 1
1) 가로를 살펴본다.
- 1 ~ 9 중 방문하지 않은 숫자가 답에 해당한다.
- 방문하지 않은 숫자가 2개 이상일 경우 다음 규칙을 살펴본다.
2) 세로를 살펴본다.
- 1 ~ 9 중 방문하지 않은 숫자가 답에 해당한다.
- 방문하지 않은 숫자가 2개 이상일 경우 다음 규칙을 살펴본다.
3) 3 * 3 정사각형을 살펴본다.
- 1 ~ 9 중 방문하지 않은 숫자가 답에 해당한다.
- 방문하지 않은 숫자가 2개 이상일 경우 다음 규칙을 살펴본다.

2. 설계
0)
- 방문배열을 사용한다.
1)
- y를 계속 증가시킨다.
- x가 3보다 작을 때 y가 3이라면 x += 1, y = 0으로 만든다.
- x가 2일 때 y가 3이라면 x = 0, y = y로 만든다.
- x가 2일 때 y가 6이라면 x = 0, y = y로 만든다.
- x가 2일 때 y가 9라면 x = 3, y = 0으로 만든다.
2)
- y를 계속 증가시킨다.
- x가 2보다 크고 6보다 작을 때 y가 3이라면 x += 1, y = 0으로 만든다.
- x가 5일 때 y가 3이라면 x = 0, y = y로 만든다.
- x가 5일 때 y가 6이라면 x = 0, y = y로 만든다.
- x가 5일 때 y가 9라면 x = 6, y = 0으로 만든다.
3)
- y를 계속 증가시킨다.
- x가 5보다 클 때 y가 3이라면 x += 1, y = 0으로 만든다.
- x가 8일 때 y가 3이라면 x = 0, y = y로 만든다.
- x가 8일 때 y가 6이라면 x = 0, y = y로 만든다.
- x가 8일 때 y가 9라면 스도쿠판을 출력하고 return 한다.

'''
import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(9)]

def explore_square(end_x, end_y):
    visited = [False for i in range(10)]
    cnt = 0
    ans = []
    check_x, check_y = 0, 0
    for i in range(end_x - 3, end_x):
        for j in range(end_y - 3, end_y):
            if lst[i][j] == 0: 
                check_x = i
                check_y = j
                continue

            visited[lst[i][j]] = True
    for i in range(1,10):
        if not visited[i]:
            cnt += 1
            ans.append(i)
    if cnt == 1:
        lst[check_x][check_y] = ans[0]
    return 

def check(x, y): # 빈 항목값을 채우기 위해 가로/세로/정사각형을 살펴본다.
    # 가로 검증
    visited = [False for i in range(10)]
    cnt = 0
    ans = []
    for j in range(9):
        if lst[x][j] == 0: continue

        visited[lst[x][j]] = True
    for i in range(1, 10):
        if not visited[i]:
            cnt += 1
            ans.append(i)
    if cnt == 1:
        lst[x][y] = ans[0]
        return 

    # 세로 검증
    visited = [False for i in range(10)]
    cnt = 0
    ans = []
    for j in range(9):
        if lst[j][y] == 0: continue

        visited[lst[j][y]] = True
    for i in range(1, 10):
        if not visited[i]:
            cnt += 1
            ans.append(i)
    if cnt == 1:
        lst[x][y] = ans[0]
        return 

    # 3 * 3 정사각형 검증
    if y >= 0 and y <= 2: # 1) 0<=y<=2
        if x >= 0 and x <= 2: explore_square(3, 3)
        elif x >= 3 and x <= 5: explore_square(6, 3)
        else: explore_square(9, 3)
    elif y >= 3 and y <= 5: # 2) 3<=y<=5
        if x >= 0 and x <= 2: explore_square(3, 6)
        elif x >= 3 and x <= 5: explore_square(6, 6)
        else: explore_square(9, 6)
    else: # 3) 6<=y
        if x >= 0 and x <= 2: explore_square(3, 9)
        elif x >= 3 and x <= 5: explore_square(6, 9)
        else: explore_square(9, 9)

    '''
    feedback)
    차라리,
    if y >= 0 and y <= 2:
    ny = 3
    elif y <= 5:
    ny = 6
    else:
    ny = 9
    if x >= 0 and x <= 2:
    nx = 3
    elif y <= 5:
    nx = 6
    else:
    nx = 9

    explore_square(nx, ny)
    
    feedback, 2)
    nxt = [3, 3, 3, 6, 6, 6, 9, 9, 9]
    nx = nxt[x]
    ny = nxt[y]

    '''
    
    return


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
        sys.exit()
        return

    if lst[x][y] == 0: # 입력받은 스도쿠판을 전체 순회하며 비어있는 항목에 대해서만 다음 작업을 수행한다.
        check(x, y)     
    recur(x, y + 1)

recur(0, 0)