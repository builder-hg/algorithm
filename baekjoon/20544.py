import sys
input = sys.stdin.readline

def recur(cur, fly, prefix_height_2_cnt, exist):
    if fly > 2 or prefix_height_2_cnt >= 2:
        return 0

    if cur == N:
        return exist
    
    if dp[cur][fly][prefix_height_2_cnt][exist] != -1:
        return dp[cur][fly][prefix_height_2_cnt][exist]
    
    ret = recur(cur + 1, 0, 0, exist)
    ret += recur(cur + 1, fly + 1, 0, exist)
    ret += recur(cur + 1, fly + 1, prefix_height_2_cnt + 1, 1)

    dp[cur][fly][prefix_height_2_cnt][exist] = ret
    dp[cur][fly][prefix_height_2_cnt][exist] %= 1000000007
    return dp[cur][fly][prefix_height_2_cnt][exist]


N = int(input())
dp = [[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(3)] for _ in range(N)]
print(recur(0, 0, 0, 0))