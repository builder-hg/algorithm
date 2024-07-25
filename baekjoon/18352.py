import sys
import heapq
input = sys.stdin.readline

N, M, K, R = map(int, input().split())
v = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    v[a].append([b, 1])

visited = [False for _ in range(N + 1)]
dist = [(1 << 30) for _ in range(N + 1)]

pq = []

dist[R] = 0
heapq.heappush(pq, (0, R))  # 두 번째 인자, 가중치와 위치
while len(pq) > 0:
    mn = pq[0][0]
    cur = pq[0][1]
    heapq.heappop(pq)

    if visited[cur]:
        continue

    visited[cur] = True
    for i in range(len(v[cur])):
        nxt = v[cur][i][0]
        nd = dist[cur] + v[cur][i][1]

        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, [nd, nxt])

fin = True
for i in range(1, N + 1):
    if dist[i] == K:
        fin = False
        print(i)

if fin:
    print(-1)