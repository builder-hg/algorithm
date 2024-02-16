import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0 for _ in range(K)]
visited = [False for _ in range(N)]

def recur(cur, start):
    if cur == K:
        print(*ans)
        return
    
    for i in range(start, N):
        if visited[i]:
            continue
        visited[i] = True
        ans[cur] = arr[i]
        recur(cur+1, i+1)
        visited[i] = False

recur(0, 0)