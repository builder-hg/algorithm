"""
x, y가 주어질 때 방향도 주어진다면,
ex)
dir == 0이면 오른쪽 칸이 어딘지 출력한다.
dir == 1이면 아랫칸이 어딘지 출력한다.
dir == 2이면 윗쪽으로,
dir == 3이면 윗칸으로.

x, y = map(int, input().split())
dir = int(input())

if dir == 0:
    print(x+1, y)
elif dir == 1:
    ....

이렇게 접근할 수도 있지만,
간결하게 다음처럼 접근하도록 하자.

x, y = map(int, input().split())
dir = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# =>
# if dir == 0:
#     print(x+1, y+0) # 1,0
# elif dir == 1:
#     print(x + 0, y-1)# 0, -1
# elif dir ==2:   # -1, 0
#     print(x - 1, y + 0)
# else:
#     print(x + 0, y + 1) # 0, 1
print(x + dx[dir], y + dy[dir])


2. 응용. 회전하기
1) 입력, x, y, dir, rotate
우회전, dir = (dir + 1) % 4
반대방향, dir = (dir + 2) % 4
좌회전, dir = (dir + 3) % 4
"""
# 적용, 감시문제
import sys
input =sys.stdin.readline

N, M = map(int, input().split())
arr # 입력
camera = []
cnt = [[0 for i in range(M)] for i in range(N)]
# cnt는 해당 위치에 몇개의 카메라한테 감시당하고 있는지에 대한 값이 저장되어있다.
ans = 1 << 64

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_lst = [[], [0], [0, 2], [0, 3], [0, 2, 3], [0,1,2,3]]
def check(x, y, camera_type, dir, add) # 위치, 카메라종류, 어딜 바라볼 지 방향(dir은 기준방향)
    for i in range(len(dir_lst[camera_type]))    # 기준선기준으로 봐야할 다른 방향에 대해서 생각해본다.
        d = (dir + dir_lst[camera_type][i]) % 4

        nx, ny = x + dx[d], y + dy[d]
        while 0 <= nx < n and 0<= ny < m and arr[nx][ny] != 6:
            cnt[nx][ny] += add
            nx += dx[d]
            ny += dx[d]

def recur(cur): # cur카메라의 방향을 결정한다.
                # 각각의 방향에 대해 중복상관없이 모두 살펴보기로 한다.
    if cur == camera:
        cnt2 = 0
        # #이 아닌부분 카운팅한다.
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0 and cnt[i][j] == 0:
                    cnt2 += 1
        ans = min(ans, cnt2)
        return

    for i in range(4):  # 카메라 종류에 상관없이 방향을 4가지로 설정한다.
        check(camera[cur][0], camera[cur][1], camera[cur][2], i , 1)
        recur(cur+1)
        check(camera[cur][0], camera[cur][1], camera[cur][2], i , -1)

for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            camera.append(i, j, arr[i][j])