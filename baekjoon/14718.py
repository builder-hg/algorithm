"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- 적 병사 : N명 
- 능력치: 힘, 민첩, 지능 (0 <= 각 능력치 <= 1,000,000)
- 다음 세 가지 조건을 만족해야 진수가 이긴다.
    1) 적 병사가 가진 힘 <= 진수의 힘
    2) 적 병사가 가진 민첩 <= 진수의 민첩
    3) 적 병사가 가진 지능 <= 진수의 지능
- 이겨야 하는 병사 수 : K
- 1 <= K <= N <= 100


2. 문제 풀이 방향
2-1. N C K
- N개의 자료를 K개씩 묶어본다.
- 묶음들의 최소 스탯포인트를 기록한다.
- 최소스탯포인트는 특정 능력치의 값 중 가장 큰 수이다.
- 기록된 스탯포인트 중 가장 작은 스탯포인트를 출력한다.

2-2. 중앙값 구하기
- 적들의 능력치를 담은 리스트를 생성한다. (2차원 배열)
- 각각의 능력치를 A, B, C라고 하자.
- A능력치들의 정중앙값(midA), B능력치들의 정중앙값(midB), C능력치들의 정중앙값(midC)를 구한다. 
    정중앙값은 A, B, C 각각을 담은 리스트를 정렬한 후 N이 짝수이면 리스트의 N//2번째 값이다. 
    N이 홀수이면 리스트의 N//2 + 1번째 값이다.
- 적들의 능력치를 담은 리스트를 순회하며, 능력치가 정중앙값보다 클 때 각각의 능력치 - 정중앙 값들을 더하고 그 값을 차이값 리스트에 담는다.
- 차이값 리스트를 k만큼 순회하며 그 값들을 더한다.
- 답은 k만큼 순회하면서 더한 값 + midA + midB + midC이다.

"""
import sys

N, K = map(int, sys.stdin.readline().split())
enemy = []
A = []
B = []
C = []
differenceList = []
for _ in range(N):
    tempA, tempB, tempC = map(int, sys.stdin.readline().split())
    A.append(tempA)
    B.append(tempB)
    C.append(tempC)
    enemy.append([tempA, tempB, tempC])
A.sort()
B.sort()
C.sort()
if N % 2: #홀수이면
    midA = A[N//2]
    midB = B[N//2]
    midC = C[N//2]
else:
    midA = A[N//2-1]
    midB = B[N//2-1]
    midC = C[N//2-1]
if K >= N//2:
    answer = midA + midB + midC
    for i in range(N):
        point = 0
        if enemy[i][0] >= midA:
            point += enemy[i][0] - midA
        if enemy[i][1] >= midB:
            point += enemy[i][1] - midB
        if enemy[i][2] >= midC:
            point += enemy[i][2] - midC
        differenceList.append(point)
    differenceList.sort()
    for i in range(K):
        answer += differenceList[i]
    print(answer)
else: 
    for i in range(N):
        point = 0
        for j in range(3):
            point += enemy[i][j]
        differenceList.append(point)
    differenceList.sort()
    answer = 0
    for i in range(K):
        answer += differenceList[i]
    print(answer)