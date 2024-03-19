import sys
sys.setrecursionlimit(100000) # 재귀 깊이 제한을 늘림
input = sys.stdin.readline

def recur(e, n, dir, block):

    #넘어가면 0
    if e > w or n > h:
        return 0

    #끝까지 돈 경우라서 경우의 수 1
    if e == w and n == h:
        return 1

    if dp[e][n][dir][block] != -1:
        return dp[e][n][dir][block]

    ret = 0
    #맨 처음부분인데, 맨처음엔 무조건 방향전환 안한것이므로 동쪽 북쪽 둘 다 가능.
    #그리고 맨 처음부분은 저장할 필요 없이 꼭 봐야하므로 dp에 저장 안함
    if dir == -1:
        ret+= recur(e+1, n,0,0) + recur(e, n+1,1,0)

    # 방향이 0이면 동쪽방향 봄
    if dir == 0:
        #1이 방향전환 했단건데 안했다면 방향전환도 할 수 있으므로 추가 케이스 더해줌
        if block != 1:
            ret += recur(e,n+1,1,1)
        
        #기본적으로는 방향전환 안하는걸로 감
        ret += recur(e+1,n,0,0)

    #1이면 북쪽 방향에서 봄
    if dir == 1:
        if block != 1:
            ret += recur(e+1,n,0,1)
        ret += recur(e,n+1,1,0)
        
    #메모이제이션
    dp[e][n][dir][block] = ret
    dp[e][n][dir][block] %= 100000
    return dp[e][n][dir][block]

w, h = map(int,input().split())

#4개의 인자 봐야해서 4차원 
dp = [[[[-1 for i in range(2)] for j in range(2)] for k in range(h+1)] for l in range(w+1)]

print(recur(1,1,-1,0))

# 바텀업 DP
import sys
input = sys.stdin.readline

w, h = map(int,input().split())
dp = [[[[0 for i in range(2)] for j in range(2)] for k in range(h+1)] for l in range(w+1)]
for i in range(w + 1):
    for j in range(h + 1):
        for k in range(2):
            for l in range(2):
                if i == w and j == h:
                    dp[i][j][k][l] = 1
