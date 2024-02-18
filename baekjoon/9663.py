"""
0. 아이디어
- N = 4일 때, 퀸이 놓일 수 있는 위치는 열의 인덱스에 해당한다.
    ans = [2,0,3,1]

1. 풀이방향
- 2번 템플릿
- 가지치기
1) 대각선에 위치할 경우 False를 반환한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(N)]
visited = [False for _ in range(N)]
cnt = 0

def check(cur):
    if cur <= 1:
        return True
    
    for i in range(cur-1):
        if abs(arr[cur-1] - arr[cur-i-2]) == i + 1:
            return False

    return True

def recur(cur):
    global cnt

    # 가지치기
    if not check(cur):
        return

    # 기저조건
    if cur == N:
        cnt += 1
        # print(*arr)
        return
    
    # 재귀호출
    for i in range(N):
        if visited[i]:
            continue

        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)
print(cnt)