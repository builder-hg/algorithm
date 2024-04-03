import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    dist[1] = 0
    heapq.heappush(pq, [0, 1])
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
                ans[nxt] = cur
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])

N, M = map(int, input().split())
v = [[] for _ in range(N + 1)]
dist = [(1 << 30) for _ in range(N + 1)]
ans = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
pq = []
for _ in range(M):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])

dijkstra()

print(N - 1)
for i in range(2, N + 1):
    print(i, ans[i])