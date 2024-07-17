import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        print(*ans)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = arr[i]
        recur(cur + 1)

        visited[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0 for _ in range(M)]
visited = [0 for _ in range(N)]

recur(0)