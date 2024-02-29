"""
0. 풀이설계, 로직
- 1에서 N까지의 경우의 순서쌍을 구한다.
- 순서쌍을 고를 때 가능한 일정과 불가능한 일정을 고려한다.
    불가능한 일정이란 할당받은 태스크의 일정들 중 최소 한 개가 퇴사일을 넘기는 경우다.
- 구한 순서쌍들이 가지는 가치(value)를 비교하며 가장 큰 값으로 갱신한다.

1. 풀이설계, 코드
1) 변수
- N: 경우의 수
- arr
    : 소요시간과 금액이 담긴 배열
- ans
    : 최대금액   

2) 조건
2-1) 가지치기
- 전달받은 cur가 N을 초과하는 경우 return한다.
- 해당 지점에서 지금까지 구한 수익과 ans를 비교하여 큰 값으로 갱신한다.

2-2) 기저조건
- cur == N
    : 재귀함수를 빠져나온다(return)

3) 인자
- cur: 현재의 위치/인덱스
- profit: 각각의 경우에서 구한 수익들의 합이다.

4) 재귀호출
- 1부터 N까지의 경우쌍을 구한다.
- 다음 재귀 호출 시, cur은 cur + arr[i][0], profit 은 profit + arr[i][1]
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = -(1 << 64)
visited = [False for _ in range(N)]

def check(cur, profit):
    global ans

    if cur > N:
        return False
    
    if ans < profit:
        ans = profit

    return True

def recur(cur, profit):
    global ans

    # 가지치기
    if not check(cur, profit):
        return
    
    # 기저조건
    if cur == N:
        return
    
    # 재귀호출
    for i in range(cur, N):
        visited[i] = True
        recur(i + arr[i][0], profit + arr[i][1])
        visited[i] = False

recur(0, 0)
print(ans)