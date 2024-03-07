import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = []
visited = [False for _ in range(2 * N + 1)]
range_lst = [i for i in range(1, 2 * N + 2)]
for _ in range(M):
    lst.append(list(map(int, input().split())))
arr = [0 for _ in range(N)]
ans = 0

def get_cnt():
    cnt = 0
    for i in range(M):
        flag = True
        for j in (lst[i]):
            if not (j in arr): 
                flag = False
                break
        if flag:
            cnt += 1

    return cnt

def recur(cur, cnt):
    global ans

    if cnt == N:
        ans = max(ans, get_cnt())
        return 

    if cur == (2*N + 1):
        return 
    
    # for i in range(1, (2 * N) + 1):
    #     if visited[i]:continue

    #     visited[i] = True
    #     arr[cur] = i
    #     recur(cur + 1)
    #     visited[i] = False
    
    arr[cnt] = range_lst[cur]
    recur(cur + 1, cnt + 1)
    recur(cur + 1, cnt)

recur(0, 0)
print(ans)


# 1 2 3 , 2 3 1, 1 3 2 => 이렇게 보게 된다
# 