"""
테스트 케이스
3 3 
ACA
BCA
ADA
"""
import sys
input = sys.stdin.readline

def dfs(x, y):
    ret = 0
    dic[raw[x][y]] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if dic.get(raw[nx][ny], 0):
            continue

        ret = max(ret, dfs(nx, ny) + 1)
    
    dic[raw[x][y]] = 0
    return ret


N, M = map(int, input().split())
raw = [list(map(str, input().strip())) for _ in range(N)]
dic = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
    'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
    'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
    'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = dfs(0, 0)
print(ans + 1)