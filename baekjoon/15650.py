import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = [0 for _ in range(K)]
visited = [False for _ in range(N+1)]
visited[0] = True

def recur(cur, start):
    if cur == K:
        print(*ans)
        return
    
    for i in range(start, N+1):
        if visited[i]:
            continue
        visited[i] = True
        ans[cur] = i
        recur(cur+1, i+1)
        visited[i] = False

recur(0, 0)