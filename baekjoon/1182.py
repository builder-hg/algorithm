"""
0. 문제 이해
- N개의 크기를 지닌 수열, 부분수열의 크기 1개 이상, 수열의 합이 S인 경우의 수 출력

1. 풀이과정
- 중복없이, 순서상관없이(2, 1과 1, 2는 동일하다) 합이 S를 만족하는 쌍을 구한다. 
- 1 ~ N개까지 묶음으로 살펴본다.
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0

def recur(cur, start, val, K):
    global cnt

    if cur > K or val > S:
        return

    if cur == K and val == S:
        cnt += 1
        return
    elif cur == K and val != S:
        return
    
    for i in range(start, N):
        recur(cur + 1, i + 1, val+arr[i], K)

for i in range(1, N+1):
    recur(0,0,0,i)
print(cnt)
