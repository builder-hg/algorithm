import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def recur(cur, cnt, total):  # cur 위치/인덱스/지점, cnt 사용개수
    global ans

    if cur == N:
        if cnt != 0 and total == S:
            ans += 1
        return
    
    recur(cur + 1, cnt + 1, total + arr[cur])
    recur(cur + 1, cnt, total)

recur(0, 0, 0)

print(ans)