import sys
import heapq
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1

    N, K, S = map(int, input().split())                                 # 컴퓨터 개수 N, 의존성 개수 K, 감염된 컴퓨터 번호 S
    v = [[] for _ in range(N + 1)]                                      # 의존성 배열 v
    for _ in range(K):
        a, b, t = map(int, input().split())
        v[b].append([a, t])                                             # b가 감염되면 t초 후에 a가 감염됨을 의미한다.

    dist = [(1 << 30) for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    pq = []

    dist[S] = 0                                                         # 시작 노드의 초기값 
    heapq.heappush(pq, [0, S])                                          # 가중치와 위치가 들어간다.
    while len(pq) > 0:
        mn, cur = heapq.heappop(pq)

        if visited[cur]:
            continue

        visited[cur] = True
        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = dist[cur] + v[cur][i][1]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])

    cnt = 0
    time = 0
    for i in range(1, N + 1):
        if dist[i] == (1 << 30):
            continue

        cnt += 1
        time = max(time, dist[i])
    
    print(cnt, time)