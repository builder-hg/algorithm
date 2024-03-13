import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(x, y):
    if x > len_x or y > len_y:
        return -(1 << 60)

    if x == len_x and y == len_y:
        return 0

    if dp[x][y] != -(1 << 60):
        return dp[x][y]
    
    ret = -(1 << 60)

    if x < len_x and y < len_y:
        if arr_x[x] == arr_y[y]:
            ret = max(ret, recur(x + 1, y + 1) + A)
        else:
            ret = max(ret, recur(x + 1, y + 1) + C)

    ret = max(ret, recur(x + 1, y) + B)
    ret = max(ret, recur(x, y + 1) + B)

    dp[x][y] = ret
    return dp[x][y]    



A, B, C = map(int, input().split())
arr_x = list(input().strip())
arr_y = list(input().strip())
len_x = len(arr_x)
len_y = len(arr_y)
dp = [[-(1 << 60) for _ in range(len_y + 1)] for _ in range(len_x + 1)]
ans = recur(0, 0)
print(ans)

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def recur(cur_x, cur_y, choice_x, choice_y, total):
#     global ans

#     if choice_x == 0 and choice_y == 0:
#         return

#     if cur_x > len(arr_x) - 1:
#         return 
    
#     if cur_y > len(arr_y) - 1:
#         return
    
#     if cur_x == len(arr_x) - 1 and cur_y == len(arr_y) - 1:
#         ans = max(ans, total)
#         return
    
#     temp = 0
#     if choice_x:
#         if choice_y:
#             if arr_x[cur_x] == arr_y[cur_y]:
#                 temp += A
#             else:
#                 temp += C
#         else:
#             temp += B
#     else:
#         if choice_y:
#             temp += B

#     if choice_x == 1:
#         recur(cur_x, cur_y, 1, 0, total + temp)
#     recur(cur_x + 1, cur_y, 1, 0, total + temp)


# A, B, C = map(int, input().split())
# arr_x = list(input().strip())
# arr_y = list(input().strip())
# ans = 0