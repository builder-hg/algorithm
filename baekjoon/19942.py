'''
1. 설계
- 각각의 재료에 대하여 두가지옵션, 선택 O/X
- 선택된 재료에 대하여 조건을 만족하는지 상시체크
    - 조건 만족시 비용을 더 작은 값으로 갱신

'''
import sys
input = sys.stdin.readline

def recur(cur, cnt, a, b, c, d, expense):
    global ans
    global isTrue
    global flag_index

    if cnt > 0 and a >= required[0] and b >= required[1] and c >= required[2] and d >= required[3]:
        isTrue = True
        if ans > expense:
            ans = expense
            flag_index = cnt
            for i in range(cnt):
                copy_arr[i] = arr[i]
        return

    if cur == N:
        return
    
    arr[cnt] = cur
    recur(cur + 1, cnt + 1, a + graph[cur][0], b + graph[cur][1], c + graph[cur][2], d + graph[cur][3], expense + graph[cur][4])
    recur(cur + 1, cnt, a, b, c, d, expense)

N = int(input())
required = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
arr = [0 for _ in range(N)]
copy_arr = [0 for _ in range(N)]
isTrue = False
flag_index = -1
ans = 1 << 64

recur(0, 0, 0, 0, 0, 0, 0)

if not isTrue:
    print(-1)
else:
    print(ans)
    for i in range(0, flag_index):
        print(copy_arr[i] + 1, end=" ")