"""
A. 배열을 순회하며 각각의 도형별 너비 중 큰 값으로 갱신한다.
    - dfs를 통해 도형별 합을 구한다.
    - visited를 통해 방문처리한다.

a. 2개
b. 1개
c. 8개
d. 4개
e. 4개
"""
import sys
input = sys.stdin.readline

def dfs(x, y, type):
    ret = raw[x][y]

    for i in range(3):
        nx = x + dir[type][i][0]
        ny = y + dir[type][i][1]

        if not (0 <= nx < N and 0 <= ny < M):
            return 0

        ret += raw[nx][ny]

    return ret

N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

dir = [
    [[0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [1, 0], [1, 1]],
    [[1, 0], [2, 0], [2, 1]],
    [[1, 0], [2, 0], [2, -1]],
    [[-1, 0], [-2, 0], [-2, 1]],
    [[-1, 0], [-2, 0], [-2, -1]],
    [[-1, 0], [-1, 1], [-1, 2]],
    [[-1, 0], [-1, -1], [-1, -2]],
    [[1, 0], [1, 1], [1, 2]],
    [[1, 0], [1, -1], [1, -2]],
    [[1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [2, -1]],
    [[0, -1], [1, -1], [1, -2]],
    [[0, 1], [1, 1], [1, 2]],
    [[0, 1], [0, 2], [1, 1]],
    [[0, 1], [0, 2], [-1, 1]],
    [[1, 0], [1, 1], [2, 0]],
    [[1, 0], [1, -1], [2, 0]]
]

ans = 0
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for type in range(19):
            ans = max(dfs(i, j, type), ans)

print(ans)