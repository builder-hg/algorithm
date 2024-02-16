import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0 for _ in range(K)]

def recur(cur):
    if cur == K:
        print(*ans)
        return
    
    for i in range(N):
        ans[cur] = arr[i]
        recur(cur + 1)

recur(0)