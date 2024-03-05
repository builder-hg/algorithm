import sys
input = sys.stdin.readline

def recur(cur, cnt):
    global taste

    if cnt == K:
        temp = 0
        for i in range(K):
            for j in range(i+1, K):
                if i == j:
                    continue
                x = ans[i]
                y = ans[j]
                temp += arr[x][y]
                
        taste = max(taste, temp)

        return

    # 기저조건
    if cur == N:
        return
    
    ans[cnt] = cur
    recur(cur + 1, cnt + 1)
    recur(cur + 1, cnt)

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0 for _ in range(K)]
taste = -(1 << 64)

recur(0, 0)
print(taste)
