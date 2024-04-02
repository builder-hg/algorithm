import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    dist[0][0] = arr[0][0]
    heapq.heappush(pq, [arr[0][0], 0, 0])
    while len(pq) > 0:
        cost = pq[0][0]
        x = pq[0][1]
        y = pq[0][2]
        heapq.heappop(pq)

        if x == N - 1 and y == N - 1:
            print(f"Problem {T}: {dist[N - 1][N - 1]}")
            return

        if visited[x][y]: continue

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            nd = cost + arr[nx][ny]

            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, [nd, nx, ny])

            


T = 0
while True:
    T += 1
    N = int(input())

    if N == 0: sys.exit()

    arr = [list(map(int, input().split())) for _ in range(N)]
    pq = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    dist = [[(1 << 30) for _ in range(N)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dijkstra()