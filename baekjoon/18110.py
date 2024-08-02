import sys
input = sys.stdin.readline

N = int(input())
if N >= 1:
    raw = []
    for _ in range(N):
        a = int(input())
        raw.append(a)
    raw.sort()

    if (N * 0.15) % 1 < 0.5:
        rm = (N * 0.15) // 1
    else:
        rm = (N * 0.15) // 1 + 1

    rm = int(rm)
    if (sum(raw[rm:N - rm]) / (N - 2 * rm)) % 1 < 0.5:
        ans = (sum(raw[rm:N - rm]) / (N - 2 * rm)) // 1
    else:
        ans = (sum(raw[rm:N - rm]) / (N - 2 * rm)) // 1 + 1

    ans = int(ans)
    print(ans)
else:
    print(0)