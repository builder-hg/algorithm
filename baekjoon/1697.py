import sys
from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(200100)]
que = deque()
dis = 0

plus = [-1, 1, 0]
mul = [1, 1, 2]

que.append(N)
visited[N] =  True
while len(que) > 0:
    sz = len(que)
    for _ in range(sz):
        cur = que[0]
        que.popleft()

        if cur == K:
            print(dis)

        for i in range(3):
            nxt = cur * mul[i] + plus[i]

            if nxt >= 0 and nxt <= 100000 and not visited[nxt]:
                que.append(nxt)
                visited[nxt] = True

    dis += 1