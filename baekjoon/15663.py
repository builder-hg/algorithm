import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        log.append(ans[:M])
        return
    
    for i in range(N):
        if visited[i]: continue

        visited[i] = True
        ans[cur] = raw[i]
        recur(cur + 1)

        visited[i] = False

N, M = map(int, input().split())
raw = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
ans = [0 for _ in range(N)]
log = []
recur(0)

print(type(log))