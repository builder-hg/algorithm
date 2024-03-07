import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
arr = [0 for _ in range(10)]
N = len(lst)
ans = 0

def recur(cur, cnt):
    global ans

    if cur == N:
        if cnt >= 5:
            ans += 1
        return
    
    if arr[cur] == lst[cur]:
        cnt += 1
    
    for i in range(1, 6):
        arr[cur] = i
        recur(cur + 1, cnt)


recur(-1, 0)