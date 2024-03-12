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
    
    if dir == -1:
        ret = recur(x + 1, y, 0, 0)
        ret += recur(x, y + 1, 1, 0)
    
    if dir == 0:
        ret = recur(x, y + 1, 0, 0)
        ret += recur(x, y + 1, 1, 0)
    else: 
        ret = recur(x + 1, y, 0, 0)
        ret += recur(x, y + 1, 1, 0)


    
W, H = map(int, input().split())
dp = [[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(H+1)] for _ in range(W+1)]
print(recur(1, 1, -1, 0))

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(x, y, a, b, c):
#     global ans
#     if a == 0 and b == 1 and c == 0:
#         return
    
#     if a == 1 and b == 0 and c == 1:
#         return

#     if x > W or y > H:
#         return

#     if x == W and y == H:
#         ans += 1
#         return
    
#     # b -> a, c -> b
#     a = b
#     b = c 
#     recur(x, y + 1, a, b, 1)
#     recur(x + 1, y, a, b, 0)
    

# W, H = map(int, input().split())
# ans = 0
# recur(0, 0, -99, -99, -99)
# print(ans)

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(x, y, cnt_x, cnt_y):
#     if x != 1 and y != 1 and cnt_x == 1 and cnt_y == 1:
#         return 0

#     if x > W or y > H:
#         return 0

#     if x == W and y == H:
#         return 1
    
#     if dp[x][y][cnt_x][cnt_y] != -1:
#         return dp[x][y][cnt_x][cnt_y]
    
#     ret = recur(x + 1, y, cnt_x + 1, cnt_y)
#     ret += recur(x, y + 1, cnt_x, cnt_y + 1)
#     dp[x][y][cnt_x][cnt_y] = ret
#     dp[x][y][cnt_x][cnt_y] %= 100000
#     return dp[x][y][cnt_x][cnt_y]

# W, H = map(int, input().split())
# dp = [[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(H+1)] for _ in range(W+1)]
# print(recur(1, 1, 0, 0))