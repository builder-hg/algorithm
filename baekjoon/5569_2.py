"""
0. 인자
- 위치 인자 2개, x, y
- 이전에 어디서 왔는지 0, 1, 0은 왼쪽에서, 1은 아래에서 왔다.
- 같은 방향에서 왔다면 0, 다른 방향에서 왔다면 1이며
    같은 방향으로 발걸음을 옮긴다면 해당 네번째 인자의 값이 1 줄어든다.
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(x, y, dir, step):
#     if x > W or y > H:
#         return 0
    
#     if step > 1:
#         return 0
    
#     if x == W and y == H:
#         return 1
    
#     if dp[x][y][dir][step] != -1:
#         return dp[x][y][dir][step]

#     ret = 0
#     if dir == 2:
#         ret += recur(x + 1, y, 0, 0)
#         ret += recur(x, y + 1, 1, 0)
#     elif dir == 0:
#         # 왼쪽에서 왔고, 오른쪽으로 가는 경우
#         ret += recur(x + 1, y, 0, 0)
#         # 왼쪽에서 왔고, 위로 가는 경우
#         ret += recur(x, y + 1, 1, step + 1)
#     elif dir == 1:
#         # 아래쪽에서 왔고, 오른쪽으로 가는 경우
#         ret += recur(x + 1, y, 0, step + 1)
#         # 아래쪽에서 왔고, 위로 가는 경우
#         ret += recur(x, y + 1, 1, 0)

#     dp[x][y][dir][step] = ret
#     dp[x][y][dir][step] %= 100000

#     return dp[x][y][dir][step]
    

# W, H = map(int, input().split())
# dp = [[[[-1 for _ in range(3)] for _ in range(3)] for _ in range(101)] for _ in range(101)]
# ans = recur(1, 1, 2, 0)
# print(ans)

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

W, H = map(int, input().split())
dp = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(110)] for _ in range(110)]

for x in range(101):
    for y in range(101):
        for dir in range(3):
            for step in range(3):
                if x == W and y == H:
                    if step != 2:
                        dp[x][y][dir][step] = 1

for x in range(1, W + 1)[::-1]:
    for y in range(1, H + 1)[::-1]:
        if x == W and y == H:
            continue
        for dir in range(3)[::-1]:
            if x != 1 or y != 1:
                if dir == 2:
                    continue
            for step in range(3)[::-1]:
                ret = 0

                if step > 1:
                    dp[x][y][dir][step] = 0
                    continue
                
                if dir == 2:
                    ret += (dp[x + 1][y][0][0] % 100000)
                    ret += (dp[x][y + 1][1][0] % 100000)
                elif dir == 0:
                    # 왼쪽에서 왔고, 오른쪽으로 가는 경우
                    ret += (dp[x + 1][y][0][0] % 100000)
                    # 왼쪽에서 왔고, 위로 가는 경우
                    ret += (dp[x][y + 1][1][step + 1] % 100000)
                elif dir == 1:
                    # 아래쪽에서 왔고, 오른쪽으로 가는 경우
                    ret += (dp[x + 1][y][0][step + 1] % 100000)
                    # 아래쪽에서 왔고, 위로 가는 경우
                    ret += (dp[x][y + 1][1][0] % 100000)

                dp[x][y][dir][step] = (ret % 100000)

print(dp[1][1][2][0])