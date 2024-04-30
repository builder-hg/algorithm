import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    
    N = int(input())
    par = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        par[b] = a
        
    x, y = map(int, input().split())
    par_x = [x]
    while par[x] != 0:
        x = par[x]
        par_x.append(x)
        
    par_y = [y]
    while par[y] != 0:
        y = par[y]
        par_y.append(y)

    par_x = par_x[::-1]
    par_y = par_y[::-1]

    lca_idx = 0

    for i in range(min(len(par_x), len(par_y))):
        if par_x[i] != par_y[i]:
            break

        lca_idx = i

    print(par_x[lca_idx])