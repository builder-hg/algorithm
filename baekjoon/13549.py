import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    que.append(start)
    visited[start] = True
    dist[start] = 0
    while len(que) > 0:
        cur = que[0]
        que.popleft()

        if cur == K:
            return dist[cur]
        
        for i in range(3):
            nxt = cur * mul[i] + add[i]

            if nxt < 0 or nxt > 100000 or visited[nxt]: continue

            visited[nxt] = True
            if i == 0:
                que.appendleft(nxt)
                dist[nxt] = dist[cur]
            else:
                que.append(nxt)
                dist[nxt] = dist[cur] + 1
            
N, K = map(int, input().split())
que = deque()
dist = [0 for _ in range(100100)]
visited = [False for _ in range(100100)]

add = [0, -1, 1]
mul = [2, 1, 1]

# print(bfs(N))
if N == 0 and K == 0:
    print(0)
elif N == 0 and K != 0:
    print(bfs(1) + 1)
else:
    print(bfs(N))
