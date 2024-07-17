import sys
input = sys.stdin.readline

def recur(cur):
    if cur == M:
        print(*ans)
        return
    
    for i in range(N):
        ans[cur] = arr[i]
        recur(cur + 1)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0 for _ in range(M)]
recur(0)