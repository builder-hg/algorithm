import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1

    N = int(input())
    raw = list(map(int, input().split()))
    res = [raw[0]]
    for i in range(1, N):
        res.append(max(res[i - 1] + raw[i], raw[i]))

    print(max(res))