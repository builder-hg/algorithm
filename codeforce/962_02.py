import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1

    N, K = map(int, input().split())
    raw = [list(map(str, input().strip())) for _ in range(N)]

    for i in range(0, N, K):
        for j in range(0, N, K):
            print(raw[i][j], end="")
        print("")