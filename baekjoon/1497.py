'''
연주가능한 곡이 기존에 구한 개수보다 커질 때 마다 
답에 해당하는 악기 수를 갱신한다.
'''

import sys
input = sys.stdin.readline

def get_now_play():
    cnt = 0
    visited = [False for _ in range(M)]

    for i in range(N):
        if choice[i]:
            for j in range(len(lst[i][1])):
                if lst[i][1][j] == 'Y':
                    if visited[j]:
                        continue

                    visited[j] = True
                    cnt += 1

    return cnt

def recur(cur, cnt): # cur: 위치, cnt: 선택한 악기개수
    global play
    global ans

    if cur == N:
        temp = get_now_play()
        
        if temp > play:
            play = temp
            ans = cnt
        elif temp == play:
            ans = min(ans, cnt)

        return
    
    choice[cur] = True
    recur(cur + 1, cnt + 1)
    choice[cur] = False
    recur(cur + 1, cnt)

N, M = map(int, input().split())
lst = []
for _ in range(N):
    guitar, possibility = input().split()
    lst.append([guitar, possibility])
choice = [False for _ in range(N)]
play = 0
ans = 1 << 64

recur(0, 0) 
if ans == 0:
    print(-1)
else:
    print(ans)