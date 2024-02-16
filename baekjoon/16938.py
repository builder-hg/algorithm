"""
0. 입력이해
문제개수 N, 난이도 총합의 최솟값 L, 난이도 총합의 최댓값 R, 난이도 차이의 최솟값 X

1. 고려사항
- 문제 난이도 정렬
- 문제의 개수 2개 이상
- 난이도 총합의 최댓값, 최솟값, 차이의 최솟값 조건 충족
-> 템플릿 3
"""
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
cnt = 0 # 조건을 충족하는 문제유형의 개수 (수열의 개수)

def check(cur, K):
    global L, R, X

    if cur < K:
        return True
    
    if L > sum(ans):
        return False
    if R < sum(ans):
        return False
    if max(ans) - min(ans) < X:
        return False
    
    return True

def recur(cur, start, K):
    global cnt

    # 가지치기, 총합의 최대/최소값, 차이의 최소값 확인
    if not check(cur, K):
        return

    # 기저조건
    if cur == K:
        cnt += 1
        return

    # 재귀호출
    for i in range(start, N):
        ans[cur] = arr[i]
        recur(cur+1, i+1, K)

for i in range(2, N+1):
    ans = [0 for _ in range(i)]
    recur(0, 0, i)

print(cnt)