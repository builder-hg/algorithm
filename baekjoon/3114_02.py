import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(x, y, val):
    global ans

    visited[x][y] = True

    if x == (N - 1) and y == (M - 1):
        divider = False
        alpha = 0
        for j in range(M):
            if visited[x][j]:  # 김상근의 경계선
                divider = True  
                continue

            if divider: # 바나나만 고려한다.
                if arr[x][j][0] == 'B':
                    alpha += int(arr[x][j][1:])
            else:       # 사과만 고려한다.
                if arr[x][j][0] == 'A':
                    alpha += int(arr[x][j][1:])

        ans = max(ans, val + alpha)
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): 
            continue

        if visited[nx][ny]:
            continue

        alpha = 0
        if i == 0 or i == 2:
            divider = False
            for j in range(M):
                if visited[x][j]:  # 김상근의 경계선
                    divider = True  
                    continue

                if divider: # 바나나만 고려한다.
                    if arr[x][j][0] == 'B':
                        alpha += int(arr[x][j][1:])
                else:       # 사과만 고려한다.
                    if arr[x][j][0] == 'A':
                        alpha += int(arr[x][j][1:])

        dfs(nx, ny, val + alpha)
        visited[nx][ny] = False

N, M = map(int, input().split())
arr = []
for _ in range(N):
    lst = list(map(str, input().split()))
    arr.append(lst)

visited = [[False for _ in range(M)] for _ in range(N)]
dx = [1, 0, 1]  # 아래, 오른쪽, 대각선 아래
dy = [0, 1, 1]

ans = 0
dfs(0, 0, 0)
print(ans)