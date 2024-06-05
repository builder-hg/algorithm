import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    global ans

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        if visited[nx][ny]: continue

        visited[nx][ny] = True
        if arr[nx][ny] == 1:
            dfs(nx,ny)

    return

Q = int(input())
while Q:
    Q -= 1

    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0 

    for i in range(N):
        for j in range(M):
            if not arr[i][j]: 
                visited[i][j] = True
                continue

            if visited[i][j]: continue

            visited[i][j] = True
            ans += 1
            dfs(i, j)

    print(ans)