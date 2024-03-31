import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
que = deque()
cnt = 0
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que.append([0, 0])
visited[0][0] = True
