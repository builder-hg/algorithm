import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(cur, cnt):
    global ans 

    if cnt > 2:
        return

    if cur == N:    # 종료조건
        if cnt != 2:
            return
        
        tmp = 1
        for i in range(cnt):
            tmp *= res[i]
        
        ans += tmp
        return
    
    res[cnt] = arr[cur]
    recur(cur + 1, cnt + 1)
    recur(cur + 1, cnt)


N = int(input())
arr = list(map(int, input().split()))
ans = 0
res = [0 for _ in range(N)]
recur(0, 0)
print(ans)