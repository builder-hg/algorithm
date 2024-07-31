"""
x, y 는 격자단위의 시작점이다.
0번째 행, 0번째 열 -> x + (size - 1 - 0)번째 행, 0번째 열
0번째 행, 1번째 열 -> x + (size - 1 - 1)번째 행, 0번째 열
0번째 행, 2번째 열 -> x + (size - 1 - 2)번째 행, 0번째 열
1번째 행, 1번째 열 -> x + (size - 1 - 1)번째 행, 1번째 열
1번째 행, 2번째 열 -> x + (size - 1 - 2)번째 행, 1번째 열
2번째 행, 1번째 열 -> x + (size - 1 - 1)번째 행, 2번째 열
=>
x + i번째 행, y + j번째 열에는 raw[x + (size - 1 - j)][y + i]가 채워진다.
"""
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def rotateBoard(raw, size):                                         # board를 회전 한다.
    board = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]     # 갱신된 보드판
    for x in range(0, len(board), size):                            # 부분 격자단위로 움직인다.
        for y in range(0, len(board), size):                        # 부분 격자단위로 움직인다.
            for i in range(size):                                   # 행 인덱스 i
                for j in range(size):                               # 열 인덱스 j
                    board[x + i][y + j] = raw[x + (size - 1 - j)][y + i]

    return board

def meltBoard(raw):                                                 # 얼음을 녹인다.
    board = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]     # 갱신된 보드판
    for x in range(len(board)):
        for y in range(len(board)):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < 2 ** N and 0 <= ny < 2 ** N):
                    continue

                if raw[nx][ny] > 0:
                    cnt += 1

            if cnt < 3:
                board[x][y] = raw[x][y] - 1
            else:
                board[x][y] = raw[x][y]

    return board

def dfs(x, y):
    global my_sum

    ret = 1
    visited[x][y] = True
    my_sum += board[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < 2 ** N and (0 <= ny < 2 ** N)):
            continue

        if visited[nx][ny]:
            continue

        if board[nx][ny] < 1:
            continue

        ret += dfs(nx, ny)
    
    return ret



N, Q = map(int, input().split())                                # 격자크기 2 ** N, 쿼리 개수 Q
board = [list(map(int, input().split())) for _ in range(2 ** N)]
query = list(map(int, input().split()))

visited = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(Q):
    board = rotateBoard(board, 2 ** query[i])
    board = meltBoard(board)

my_sum = 0
my_cnt = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        if visited[i][j]:
            continue

        if board[i][j] < 1:
            continue

        my_cnt = max(my_cnt, dfs(i, j))

print(my_sum)
print(my_cnt)