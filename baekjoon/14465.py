"""
[문제풀이전략]
1. 문제 이해 및 정리
- 입력: 신호등 개수 N, 기대하는 신호등의 개수 K, 고장난 신호등 개수 B
- 출력: 연속하는 K개의 신호등이 존재하려면 최소 몇개의 신호등을 수리해야 하는지 출력한다.

2. 문제 풀이 방향
- 특정 구간의 합이 K를 만족할 때까지 구간을 살펴본다.
- 구간을 살펴보다가 고장난 신호등을 만나면 cnt를 1 증가시킨다.
- 합이 K인 구간에 다다르면 cnt를 보관함에 담아두고 0으로 초기화시킨다.
- 합이 K인 구간에 다다르면 이전에 보고 있던 좌표들(시작지점, 끝지점)을 후보군에서 제외시킨다.
- 위 과정을 끝지점이 N보다 작다면 반복한다.
"""
import sys
N, K, B = map(int, sys.stdin.readline().split())
lst = [0] + [1 for _ in range(N)] + [0]
for _ in range(B):
    break_idx = int(input())
    lst[break_idx] = 0
# [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
s = 1
e = 1
total = 0
cnt_b = 0
ans_list = []

while e < N+1:
    total += 1
    if total < K:
        if lst[e] == 0:
            cnt_b += 1
        e += 1
    if total == K:
        if lst[e] == 0:
            cnt_b += 1
        ans_list.append(cnt_b)
        total -= 1
        if lst[s] == 0:
            cnt_b -= 1
        s += 1
        e += 1
print(min(ans_list))