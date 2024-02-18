"""
0. 문제이해하기
1) 새로운 물감 R만들기
(AR1 + AR2 + ... + ARN) // N -> 새로운 물감 R 
2) 곰두리색의 R,G,B 각각의 차이값이 최소가 되는 색 구하기

1. 풀이방향, 템플릿3
0) 공통변수
- 물감리스트, 물감개수, 답을 저장할 변수(전역선언)
1) 기저조건
- cur은 내가 설정한 K이다 (2<=K<=7)
- 구한 최소값과 기존 값을 비교하여 갱신한다. (더 작은 값으로 대체한다.)
2) 가지치기
- K가 7보다 크다면 재귀를 빠져나간다
3) 재귀호출
- cur, 시작지점, R물감의합, G물감의합, B물감의합, 넘겨야할 값 K(섞을 물감의 개수)
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
base = list(map(int, input().split()))
ans = 1 << 64
total_red = 0
total_green = 0
total_blue = 0

# total -> global 
# 시간초과
# 인자 -> 복사 => 메모리 차지 (따라서, 전역변수로 관리)

def recur(cur, start):
    global ans
    global total_red
    global total_green
    global total_blue

        # 기저조건
    if cur > 7 or cur == N+1:
        return

    if cur >= 2:
        new_red = total_red // cur
        new_green = total_green // cur
        new_blue = total_blue // cur
        val = abs(new_red - base[0]) + abs(new_green - base[1]) + abs(new_blue - base[2])
        if val < ans:
            ans = val


    # 재귀호출
    for i in range(start, N):
        total_red += arr[i][0]
        total_green += arr[i][1] 
        total_blue += arr[i][2]
        recur(cur+1, i+1)
        total_red -= arr[i][0]
        total_green -= arr[i][1] 
        total_blue -= arr[i][2]

recur(0, 0)

print(ans)