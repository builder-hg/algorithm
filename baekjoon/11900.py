import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
v = [[] for _ in range(N + 1)]                  # 노드간 간선과 가중치를 담을 배열

# 노드 간 간선과 간선의 가중치를 저장한다.
for a in range(N):
    for b in range(N):
        if a == b: continue

        if a > b and 1 <= (a - b) and (a - b) <= (N - 1) and arr[a - b] > 0:
            v[a].append([b, arr[a - b]])
        elif a < b and 1 <= (a - b + N) and (a - b + N) <= (N - 1) and arr[a - b + N] > 0:
            v[a].append([b, arr[a - b + N]])

Q = int(input())                                # 쿼리 수

while Q:
    Q -= 1
    S, K = map(int, input().split())            # 시작노드 및 도착노드

    dist = [1 << 30 for _ in range(N + 1)]
    pq = []

    dist[S] = 0                             
    heapq.heappush(pq, [0, S])
    while len(pq) > 0:
        mn = pq[0][0]
        cur = pq[0][1]
        heapq.heappop(pq)

        if dist[cur] != mn: continue

        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = v[cur][i][1] + dist[cur]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])

    if dist[K] != (1 << 30):
        print(dist[K])
    else:
        print(-1)