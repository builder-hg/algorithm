import sys
input = sys.stdin.readline

def dfs(x, y):
    global my_size

    visited[x][y] = True
    my_size += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '0': continue

        if visited[x + dx[i]][y + dy[i]]: continue

        dfs(x + dx[i], y + dy[i])

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
my_cnt = 0
size_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '0': continue

        if visited[i][j]:
            continue
        
        my_cnt += 1
        my_size = 0

        dfs(i, j)
        size_lst.append(my_size)

size_lst.sort()
print(my_cnt)
for i in size_lst: print(i)

