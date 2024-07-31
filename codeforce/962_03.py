import sys
input = sys.stdin.readline

T = int(input())
while T:                                    # 1개 이상 1000개이하이다.
    T -= 1

    N, Q = map(int, input().split())        # 1이상 2 * (10 ** 5)개이다.
    rawA = list(map(str, input().strip()))
    rawB = list(map(str, input().strip()))
    
    logA = [[0 * 26] for _ in range(N)]
    logB = [[0 * 26] for _ in range(N)]
    while Q:
        Q -= 1

        s, e = map(int, input().split())
