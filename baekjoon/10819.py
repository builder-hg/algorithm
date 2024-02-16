"""
0. 풀이방향
1) 큰값과 작은 값을 번갈아 정렬한다.
2) 완전탐색한다.

1-1. 완전탐색, 새로운 배열 생성 후 값 도출
1-2. 완전탐색, 백트래킹 => 2번 템플릿
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = []    # 각각의 경우에서 구한 최댓값을 담을 배열
visited = [False for _ in range(N+1)]

def recur(cur, prev, total, K):
    # 기저조건
    if cur == N:
        ans.append(total - K)
        return

    # 재귀호출
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        temp = abs(prev - arr[i])
        total += temp
        if cur == 0:
            K = temp
        recur(cur+1,arr[i],total, K)
        total -= temp
        visited[i] = False

recur(0, 0, 0, 0)
print(max(ans))