import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def getFruit():
    ret = 0
    for i in range(N):
        divider = False
        for j in range(M):
            if visited[i][j]:  # 김상근의 경계선
                divider = True  
                continue

            if divider: # 바나나만 고려한다.
                if arr[i][j][0] == 'B':
                    ret += int(arr[i][j][1:])
            else:       # 사과만 고려한다.
                if arr[i][j][0] == 'A':
                    ret += int(arr[i][j][1:])

    return ret

def dfs(x, y):
    global ans

    visited[x][y] = True

    if x == (N - 1) and y == (M - 1):
        ans = max(ans, getFruit())
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): 
            continue

        if visited[nx][ny]:
            continue

        dfs(nx, ny)
        visited[nx][ny] = False

N, M = map(int, input().split())
arr = []
for _ in range(N):
    lst = list(map(str, input().split()))
    arr.append(lst)

visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 1, 1]  # 아래, 오른쪽, 대각선 아래
dy = [1, 0, 1]

ans = 0
dfs(0, 0)
print(ans)