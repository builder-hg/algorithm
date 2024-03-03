import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
common_red, common_green, common_blue = map(int, input().split())
ans = 1 << 64

def get_diff(cur, cnt, r, g, b):
    global common_red
    global common_green
    global common_blue

    if cnt <= 1:
        return 1 << 64

    diff = abs(common_red - (r//cnt)) + abs(common_green - (g//cnt)) + abs(common_blue - (b//cnt))
    return diff

def recur(cur, cnt, r, g, b):
    global ans 

    if cnt > 7:
        return

    ans = min(ans, get_diff(cur, cnt, r, g, b))

    if cur == N:
        return
    
    choice_red = lst[cur][0]
    choice_green = lst[cur][1]
    choice_blue = lst[cur][2]
    recur(cur + 1, cnt + 1, r + choice_red, g + choice_green, b + choice_blue)
    recur(cur + 1, cnt, r, g, b)
    


recur(0, 0, 0, 0, 0)
print(ans)