import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y, dir, step):
    if x > W or y > H:
        return 0

    if x == W and y == H:
        return 1
    
    if dp[x][y][dir][step] != -1:
        return dp[x][y][dir][step]
    
    ret = 0
    if dir == 2:
        ret += recur(x + 1, y, 0, 0)
        ret += recur(x, y + 1, 1, 0)
    elif dir == 0: # 이전에 x축으로 오면서
        if step == 1: # 방향 전환을 했던 상태라면
            ret += recur(x + 1, y, 0, 0)
        else:   # 최소 한 번 이상 왔던 방향으로 더 갔던 경우
            ret += recur(x, y + 1, 1, 1)
            ret += recur(x + 1, y, 0, 0)
    elif dir == 1:   # 이전에 y축으로 오면서
        if step == 1: # 방향 전환을 했던 상태라면
            ret += recur(x, y + 1, 1, 0)
        else:
            ret += recur(x + 1, y, 0, 1)
            ret += recur(x, y + 1, 1, 0)

    dp[x][y][dir][step] = ret
    dp[x][y][dir][step] %= 100000
    return dp[x][y][dir][step]

W, H = map(int, input().split())
dp = [[[[-1 for _ in range(2)] for _ in range(3)] for _ in range(H + 1)] for _ in range(W + 1)]
ans = recur(1, 1, 2, 0)
print(ans)