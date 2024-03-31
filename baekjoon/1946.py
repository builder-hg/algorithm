T = int(input())

while T:
    T -= 1
    N = int(input())
    standard = 1 << 60
    ans = 0
    v = []

    for i in range(N):
        a, b = map(int, input().split())
        v.append([a, b])

    v.sort(key=lambda x:x[0])

    for cur in v:
        if cur[1] < standard:
            ans += 1
            standard = cur[1]

    print(ans)