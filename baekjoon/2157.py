import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())                                         # 도시의 개수 N, 방문 가능 횟수 M 이하, 노선 개수 K

point = [[0 for _ in range(N + 1)] for _ in range(N + 1)]                   # point[i, j]는 i에서 j지점까지 가는데 얻는 기내식의 최댓값
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]                      # dp[i, j]는 j번 (방문)횟수로 1번 도시에서 i번 도시로 갈 때 얻는 기대식의 최댓값
for _ in range(K):                                                          # 얻을 수 있는 기내식 점수의 최댓값 채우기
    a, b, c = map(int, input().split())

    if a >= b:
        continue

    point[a][b] = max(point[a][b], c)
for i in range(2, N + 1):                                                   # dp 초깃값 설정
    dp[i][2] = point[1][i]                                                  # 1번 도시에서 i번 도시까지 가는데 얻을 수 있는 기내식 점수

for cur in range(2, N + 1):                                                   # 1번 도시에서 2번, 3번, ..., N번 도시까지 살펴본다.
    for cnt in range(3, M + 1):                                                 # 방문횟수 cnt는 M이하여야 한다. 
        for prv in range(1, cur):
            if not point[prv][cur]:
                continue

            if not dp[prv][cnt - 1]:
                continue

            dp[cur][cnt] = max(dp[cur][cnt], dp[prv][cnt - 1] + point[prv][cur])

print(max(dp[N]))