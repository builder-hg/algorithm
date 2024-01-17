"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 테스트케이스 T (1<= T <= 10)
- 수업개수 N (1<= N <= 10^5)
- 졸은 횟수 ai (0 <= ai <= 10^6)

2. 문제 풀이 방향
- 특정한 값(K)로 모인다고 할 때, K는 원소들의 총합(total)의 약수이다.
- 이 때 K는 주어진 원소들보다 크거나 같아야 한다.
- 답은 전체 개수에서 총합을 K로 나눈 몫을 뺀 값이다.
"""
import sys

T = int(input())

while T:
    T -= 1
    N = int(input())                    # 리스트의 길이
    listA = list(map(int, sys.stdin.readline().split()))    # 리스트
    total = sum(listA)                  # 리스트의 총합
    maxV = max(listA)                   # 원소 중 가장 큰 값
    ans = 0                             # 정답 변수
    next = False
    if maxV == 0:
        next = True
    if next:
        print(0)
        continue

    for i in range(maxV, total+1):
        possible = True
        if total % i != 0:
            continue
        temp = 0
        for j in range(N):
            temp += listA[j]
            if temp == i:
                temp = 0
                continue
            if temp > i:
                possible = False
                break
        if possible:
            print(N - total//i)
            break
