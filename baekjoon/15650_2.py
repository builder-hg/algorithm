import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == M:
        print(*arr)
        return
    
    for i in range(start, N + 1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur + 1, i + 1)

        visited[i] = False

N, M = map(int, input().split())
arr = [0 for _ in range(M)]
visited = [False for _ in range(N + 1)]

recur(0, 1)