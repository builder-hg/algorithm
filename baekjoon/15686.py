"""
1. 치킨집을 M개 고른다.
2. 각각의 경우마다 치킨 거리를 모두 구해본다.
    - 각 집마다 치킨집 전체를 순회하며 치킨 거리를 구한다.
"""
import sys
input = sys.stdin.readline

def getDistance():
    ret = 0
    for i in range(N):
        for j in range(N):
            if raw[i][j] != 1:
                continue
            
            tmp = 1 << 60
            for k in range(M):
                nx, ny = chic[k]
                tmp = min(tmp, abs(i - nx) + abs(j - ny))
            ret += tmp

    return ret

def recur(cur, cnt):
    global ans 

    if cnt > M:
        return
    
    if cur == len(position):
        if cnt != M:
            return
        
        tmp = getDistance()
        ans = min(ans, tmp)
        return

    chic[cnt] = position[cur]
    recur(cur + 1, cnt + 1)
    recur(cur + 1, cnt)

N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]

position = []                       # 치킨집 위치 배열
for i in range(N):
    for j in range(N):
        if raw[i][j] == 2:
            position.append([i, j]) # 행, 열을 저장한다.

chic = [[] for _ in range(250)]
ans = (1 << 60)
recur(0, 0)
print(ans)
