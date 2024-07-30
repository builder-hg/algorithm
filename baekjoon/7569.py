import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
raw = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dh = [-1, 1]