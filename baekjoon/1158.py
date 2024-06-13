import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
ans = []
idx = 0

for _ in range(N):
    idx += (K - 1)
    
    if idx >= len(arr):
        idx = (idx % len(arr))

    ans.append(arr.pop(idx))

print("<", end="")
print(*ans, sep=', ', end="")
print(">", end="")

"""
# 시간초과 풀이
N, K = map(int, input().split())
visited = [False for _ in range(N)]
ans = []
move = K
idx = 0

while True:
    # 종료조건
    if len(ans) == N:
        break

    if visited[idx]: 
        idx = (idx + 1) % 7
        continue

    move -= 1
    if move == 0:
        ans.append(idx + 1)
        visited[idx] = True
        move = K

    idx = (idx + 1) % 7

print("<", end="")
print(*ans, sep=', ', end="")
print(">", end="")"""