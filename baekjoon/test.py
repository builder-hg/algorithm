import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0
init_value = 0

def recur(cur, start, val, K):
    global cnt

    if cur > K:
        return

    if cur == K and val == S:
        cnt += 1
        return
    elif cur == K and val != S:
        return
    
    for i in range(start, N):
        recur(cur + 1, i + 1, val+arr[i], K)

for i in range(1, N+1):
    recur(0,0,init_value,i)
print(cnt)