import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = [0 for _ in range(K)]

def recur(cur, start):
    if cur == K:
        print(*ans)
        return
    
    for i in range(start, N+1):
        ans[cur] = i
        recur(cur + 1, i)

recur(0, 1)