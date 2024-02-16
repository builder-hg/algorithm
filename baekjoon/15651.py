import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = [0 for _ in range(K)]

def recur(cur):
    if cur == K:
        print(*ans)
        return
    
    for i in range(1, N+1):
        ans[cur] = i
        recur(cur+1)

recur(0)