import sys
from collections import deque

# N: 세로, M: 가로     
N, M = map(int, input().split())   
# arr: 지도                                    
arr = [list(input().strip()) for _ in range(N)]
que = deque()
# ans, 보물이 묻힌 두 곳의 최단 거리
ans = 0                                                         

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for sx in range(N):
    for sy in range(M):
        visited = [[False for _ in range(M)] for _ in range(N)] 
        dis = 0
        
        if arr[sx][sy] == 'W': continue

        que.append([sx, sy])
        visited[sx][sy] = True
        while len(que) > 0:
            sz = len(que)
            for _ in range(sz):
                x = que[0][0]
                y = que[0][1]
                que.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue

                    if visited[nx][ny] or arr[nx][ny] == 'W':
                        continue

                    que.append([nx, ny])
                    visited[nx][ny] = True

            dis += 1 

        ans = max(ans, dis - 1)

print(ans)