import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    d, N = map(int, input().split())
    raw = [0] + list(map(int,input().split()))
    prefix = [0 for _ in range(N+1)]
    나머지사전 = {}
    ans = 0

    for i in range(1, N+1):
        prefix[i] = (prefix[i-1] + raw[i])

    for i in range(1, N+1):
        나머지 = prefix[i] % d
        ans += 나머지사전.get(나머지, 0)
        나머지사전[나머지] = 나머지사전.get(나머지, 0) + 1

    ans += 나머지사전.get(0,0)
    print(ans)