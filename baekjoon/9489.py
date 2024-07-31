import sys
input = sys.stdin.readline

while True:
    N, K = map(int, input().split())            # 노드의 개수, 대상 노드

    if N == 0 and K == 0:
        break

    raw = [-1] + list(map(int, input().split()))
    
    par = [0] * (N + 1)
    par[0] = -1
    index = -1
    for i in range(1, N + 1):
        if raw[i] != raw[i - 1] + 1:
            index += 1

        par[i] = index                          # raw[i]의 부모를 저장한다.

    target = raw.index(K)
    ans = 0
    for i in range(1, N + 1):
        if par[i] != par[target] and par[par[i]] == par[par[target]]:
            ans += 1

    print(ans)