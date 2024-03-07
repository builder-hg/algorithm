import sys
import copy
input = sys.stdin.readline

def check(cnt):
    global ans
    temp = cnt
    copy_arr = copy.deepcopy(arr)

    for i in range(cnt):
        index = change_list[i]
        for k in [[0, -1], [0, 1], [0, 0], [1, 0]]:
            if index + k[1] == 10 or index + k[1] == -1: continue
            if copy_arr[0 + k[0]][index + k[1]] == '#':
                copy_arr[0 + k[0]][index + k[1]] = 'O'
            else:
                copy_arr[0 + k[0]][index + k[1]] = '#'

    for i in range(1, 10):
        for j in range(10):
            if copy_arr[i-1][j] == 'O':
                temp += 1
                for k in [[0, -1], [0, 1], [0, 0], [-1, 0], [1, 0]]:
                    if j + k[1] == 10 or j + k[1] == -1: continue
                    if i + k[0] == 10: continue
                    if copy_arr[i + k[0]][j + k[1]] == '#':
                        copy_arr[i + k[0]][j + k[1]] = 'O'
                    else:
                        copy_arr[i + k[0]][j + k[1]] = '#'
    
    for i in range(10):
        if copy_arr[9][i] == 'O':
            return False

    ans = min(ans, temp)

    return True

def recur(y, cnt):
    global ans

    if y == 10:
        if not check(cnt):
            return False
        return

    change_list[cnt] = y
    recur(y + 1, cnt + 1)
    recur(y + 1, cnt)

arr = [list(input().strip()) for _ in range(10)]
change_list = [0 for _ in range(10)]
ans = 1 << 64
recur(0, 0)

if ans == 1 << 64:
    print(-1)
else:
    print(ans)