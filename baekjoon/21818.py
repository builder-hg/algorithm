"""
0. 문제이해
1) 4~7개의 숫자가 주어진다.
2) 주어진 숫자는 A, B, C, A+B, B+C, A+C, A+B+C 중 하나이다.
3) 가능한 A, B, C의 경우의 수를 구한다.

1. 전략, 템플릿 2
1) 가능한 경우의 수는 7이다.
2) 각각의 경우를 살펴본다. 살펴볼 경우의 개수는 N이다.


# 이차원 배열로 접근해야할까?
"""
import sys
input = sys.stdin.readline

# 테스트케이스의 수는 마지막에 고려한다.
N = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(N)]
visited = [False for _ in range(N)]
cases = {
    0:'A', 1:'B', 2:'C', 3:'A+B',4:'B+C', 5:'A+C', 6:'A+B+C'
}
cnt = 0

def check(cur):
    if cur < N:
        return True
    
    A = 0
    B = 0
    C = 0

    for i in range(N):
        if ans[i] == 0:
            A = 
    


def recur(cur):
    global cnt
    # 가지치기 
    if not check(cur):
        return
    
    # 기저조건
    if cur == N:
        cnt += 1
        return
    
    # 재귀호출
    for i in range(7):  # 경우를 순회한다.
        if visited[i]:
            continue

        visited[i] = True
        ans[cur] = arr[i]
        recur(cur+1)
        visited[i] = False


recur(0)

