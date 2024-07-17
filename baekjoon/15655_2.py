import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == M:
        print(*ans)
        return
    
    for i in range(start, N):
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = arr[i]
        recur(cur + 1, i + 1)

        visited[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0 for _ in range(M)]
visited = [False for _ in range(N)]
recur(0, 0)