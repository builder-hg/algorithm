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
lst = [0, 0, 0]
ans = 1 << 64
leng = range(2, N+1)
if N <= 7:
    leng = range(2, 8)

def check(cur, total_red, total_green, total_blue, K):
    if cur <= 1:
        return True, 0
    
    if cur > 7:
        return False, -1
    
    total_red //= K
    total_green //= K
    total_blue //= K
    val = abs(total_red - base[0]) + abs(total_green - base[1]) + abs(total_blue - base[2])
    if val > ans:
        return False, -1

    return True, val

def recur(cur, start, total_red, total_green, total_blue, K):
    global ans

    fin, res = check(cur, total_red, total_green, total_blue, K)

    if not fin:
        return 

    # 기저조건
    if cur == K:
        total_red //= K
        total_green //= K
        total_blue //= K
        val = abs(total_red - base[0]) + abs(total_green - base[1]) + abs(total_blue - base[2])
        if val < ans:
            ans = val
        return

    # 재귀호출
    for i in range(start, N):
        total_red += arr[i][0]
        total_green += arr[i][1] 
        total_blue += arr[i][2]
        recur(cur+1, i+1, total_red, total_green, total_blue, K)
        total_red -= arr[i][0]
        total_green -= arr[i][1] 
        total_blue -= arr[i][2]

for i in leng:
    recur(0, 0, 0, 0, 0, i)

print(ans)