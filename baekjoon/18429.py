import sys
input = sys.stdin.readline

def recur(cur):
    global weight, ans

    if weight < 500:
        return
    
    if cur == N:
        ans += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        weight += raw[i]
        weight -= K
        recur(cur + 1)

        visited[i] = False
        weight -= raw[i]
        weight += K

N, K = map(int, input().split())
raw = list(map(int, input().split()))
weight = 500
visited = [False for _ in range(N)]
ans = 0
recur(0)

print(ans)