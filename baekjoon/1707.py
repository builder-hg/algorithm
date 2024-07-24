import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(cur, prv):
    visited[cur] = True

    if prv == 0:        # 기존이 0이었다면
        if arr[cur] == -1:
            arr[cur] = 1
        else:           # 기존에 채워져 있고
            if arr[cur] != 1:
                return False
    elif prv == 1:      # 기존에 1이었다면
        if arr[cur] == -1:
            arr[cur] = 0
        else:
            if arr[cur] != 0:
                return False
    elif prv == -1:               # 초깃값 세팅
        arr[cur] = 1
    else:
        pass

    for nxt in v[cur]:
        if visited[nxt]:
            if arr[cur] == arr[nxt]:
                return False
        else:
            ret = dfs(nxt, arr[cur])
            if not ret:
                return False

    return True

T = int(input())
while T:
    T -= 1

    V, E = map(int, input().split())
    
    v = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)

    arr = [-1 for _ in range(V + 1)]
    chk = True
    visited = [False for _ in range(V + 1)]
    for i in range(1, V + 1):
        if arr[i] != -1:
            _init = 99
        else:
            _init = arr[i]
        chk = dfs(i, _init)
        if not chk:
            break

    if not chk:
        print("NO")
    else:
        print("YES")

