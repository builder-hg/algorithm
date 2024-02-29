import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1 << 64

def recur(cur, cnt, a, b):
    global ans

    if cur == N:
        if cnt == 0:
            return
        ans = min(ans, abs(a - b))
        return
    
    recur(cur + 1, cnt + 1, a * arr[cur][0], b + arr[cur][1])
    recur(cur + 1, cnt, a, b)

recur(0, 0, 1, 0)
print(ans)