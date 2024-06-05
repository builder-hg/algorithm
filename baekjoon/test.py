"""
입력
- 테스트 케이스의 수
- 출발점과 도착점(x, y)
- 행성계의 수
- 행성계의 좌표(x, y)와 반지름(r)

x가 출발점과 도착점을 포함한다면, y를 비교한다. 
y가 출발점과 도착점을 포함한다면 카운팅한다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    sx, sy, ex, ey = map(int, input().split())
    N = int(input())
    arr = []
    ans = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        arr.append([a, b, c])

    for i in range(N):
        nx, ny, r = arr[i][0], arr[i][1], arr[i][2]
        dist_start = (sx - nx) ** 2 + (sy - ny) ** 2
        dist_end = (ex - nx) ** 2 + (ey - ny) ** 2

        if (dist_start < r ** 2 and dist_end > r ** 2) or (dist_start > r ** 2 and dist_end < r ** 2):
            ans += 1

    print(ans)