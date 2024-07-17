import sys
input = sys.stdin.readline

def recur(cur):
    if cur == N:
        print(*log)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        log[cur] = raw[i]
        recur(cur + 1)

        visited[i] = False

N = int(input())
raw = []
for i in range(1, N + 1):
    raw.append(i)
visited = [False for _ in range(N)]
log = [0 for _ in range(N)]
recur(0)

