"""
A, B i~j까지의 누적합이 같다
=> (Aj - Bj) == (Ai-1 - Bi-1)
=> 현재 위치한 지점에서의 누적합 차가 이전에도 존재했다면 쌍이 존재했다는 의미이다.
"""

import sys
input = sys.stdin.readline

N = int(input())
ans = 0
rawA = [0] + list(map(int, input().split()))
rawB = [0] + list(map(int, input().split()))

prefixA = [0 for _ in range(N+1)]
prefixB = [0 for _ in range(N+1)]
count = {0:1}   # 누적합 차가 0이라는 건 아예 일치하는 경우로 그 자체로 cnt를 1 증가시킨다.
for i in range(1, N + 1):
    prefixA[i] = prefixA[i-1] + rawA[i]
    prefixB[i] = prefixB[i-1] + rawB[i]
    diff = prefixA[i] - prefixB[i]
    ans += count.get(diff, 0)
    count[diff] = count.get(diff, 0) + 1

print(ans)