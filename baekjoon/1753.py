import sys
import heapq

N, M = map(int, input().split())
K = int(input())
v = [[] for _ in range(N + 1)]
dist = [1 << 30 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
pq = []

for _ in range(M):
    a, b, c = map(int, input().split())

    v[a].append([b, c])

dist[K] = 0
heapq.heappush(pq, [0, K])
while len(pq) > 0:
    mn = pq[0][0]
    cur = pq[0][1]
    heapq.heappop(pq)

    if visited[cur]: continue

    visited[cur] = True

    for i in range(len(v[cur])):
        nxt = v[cur][i][0]
        nd = v[cur][i][1] + dist[cur]

        if dist[nxt] > nd:
            dist[nxt] = nd 
            heapq.heappush(pq, [nd, nxt])

for i in range(1, N + 1):
    if dist[i] == 1 << 30:
        print('INF')
    else:
        print(dist[i])