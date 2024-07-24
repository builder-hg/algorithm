"""
조건
01. 2 <= N <= 100, 배열 전체 순회 10,000번
02. 1 <= raw[i] <= 100, 높이 값 각각을 다 보는데 100번
=> 각 높이별로 배열 전체를 순회하는데 1,000,000번

테스트케이스
2
100 100
100 100
=> 1
"""
import sys
sys.setrecursionlimit(1000010)
input = sys.stdin.readline

def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < N and 0 <= ny < N):
            continue
        
        if visited[nx][ny]:
            continue

        if raw[nx][ny] <= h:
            visited[nx][ny] = True
            continue

        dfs(nx, ny, h)

N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
for h in range(101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    tmp = 0     # 안전영역의 개수
    for i in range(N):
        for j in range(N):
            if visited[i][j]:   # 방문한 곳은 살펴보지 않는다.
                continue
            
            visited[i][j] = True    # 방문하지 않은 곳은 방문하였다고 표시한다.
            if raw[i][j] <= h:      # 잠기는 지역은 넘어간다.
                continue

            tmp += 1
            dfs(i, j, h)
    ans = max(ans, tmp)

print(ans)