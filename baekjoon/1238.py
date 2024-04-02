import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end):
    visited = [False for _ in range(N + 1)]
    dist = [(1 << 30) for _ in range(N + 1)]
    pq = []

    dist[start] = 0
    heapq.heappush(pq, [0, start])
    while len(pq) > 0:
        mn = pq[0][0]
        cur = pq[0][1]
        heapq.heappop(pq)

        if visited[cur]: continue

        visited[cur] = True

        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = v[cur][i][1] + mn

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])
    
    return dist[end]

N, M, X = map(int, input().split())
v = [[] for _ in range(N + 1)]
ans = -1
for _ in range(M):
    a, b, c = map(int, input().split())

    v[a].append([b, c])

for i in range(1, N + 1):
    ans = max(dijkstra(i, X) + dijkstra(X, i), ans)

print(ans)