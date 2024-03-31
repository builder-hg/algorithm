import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    remove = []
    que.append([0, 0])
    visited[0][0] = True

    while len(que) > 0:
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]: 
                continue

            visited[nx][ny] = True
            if arr[nx][ny] == 0:
                que.append([nx, ny])
            elif arr[nx][ny] == 1:
                remove.append([nx, ny])

    for i in range(len(remove)):
        x = remove[i][0]
        y = remove[i][1]
        arr[x][y] = 0

    return len(remove)


N, M = map(int, input().split())
que = deque()
arr = []
ans = 0
cheeze = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    cheeze += sum(temp)
    arr.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    visited = [[False for _ in range(M)] for _ in range(N)] 
    remove_cnt = bfs()
    ans += 1 
    cheeze -= remove_cnt

    if cheeze == 0:
        print(ans)
        print(remove_cnt)
        sys.exit()