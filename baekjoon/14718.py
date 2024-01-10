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

2-2. 중앙값 구하기(틀림)
- 적들의 능력치를 담은 리스트를 생성한다. (2차원 배열)
- 각각의 능력치를 A, B, C라고 하자.
- A능력치들의 정중앙값(midA), B능력치들의 정중앙값(midB), C능력치들의 정중앙값(midC)를 구한다. 
    정중앙값은 A, B, C 각각을 담은 리스트를 정렬한 후 N이 짝수이면 리스트의 N//2번째 값이다. 
    N이 홀수이면 리스트의 N//2 + 1번째 값이다.
- 적들의 능력치를 담은 리스트를 순회하며, 능력치가 정중앙값보다 클 때 각각의 능력치 - 정중앙 값들을 더하고 그 값을 차이값 리스트에 담는다.
- 차이값 리스트를 k만큼 순회하며 그 값들을 더한다.
- 답은 k만큼 순회하면서 더한 값 + midA + midB + midC이다.

2-3. 합을 기준으로 정렬하여 계산하기 (틀림)
어제 접근했던 방식 중 하나가
합을 기준으로 나열했을 때 K개까지의 원소들을 살펴보며 
그 중에 최대값들을 기준으로 한다는 것이다.
위 방식의 반례는 다음과 같다.

1 1 1	-> 3
3 3 3	-> 9
4 1 3	-> 8
2 2 2	-> 6
1 5 2	-> 8
N=5, K=4라면, 실제 정답은 
(1,1,1) (2, 2, 2) (4, 1, 3) (3, 3, 3)을 쌍으로하여 4, 3, 3인 10이다.
위 방식처럼 접근한다면 
(1,1,1) (2,2,2) (1,5,2) (4,1,3)을 쌍으로 하여 4, 5, 3인 12가 나온다.

2-4.
- 각각의 적들의 최대값을 구한다.
ex) N=3, K=1이라면
234 23 342	=> 342
35 4634 34	=> 4634
46334 6 789	=> 46334
key)최대값 중 가장 작은 값들을 이용하는 식은 어떨까?
ex) N=5, K=4라면
1 1 1	-> 1
2 2 2	-> 2
3 3 3	-> 3
1 5 3	-> 5
4 1 2	-> 4
key대로 접근하면, 4 3 3으로 10이 도출된다.
ex) N=3, K=2라면
30 30 30	-> 30
10 500 10	-> 500
50 10 50	-> 50
key대로 접근하면 50 30 50으로 100이 도출된다.

2-5. 진수 능력치가 될 수 있는 모든 방법을 봐서 그중 k명 이상 이기는걸 보는 방법
0 0 0
0 0 1
0 0 2
...
0 0 1000000
0 1 0
0 1 1
0 1 2
...
1000000 1000000 1000000 으로 설정했을 때
[문제 풀이 방향]
1. 진수가 가질 수 있는 능력치들(a, b, c)의 경우를 구한다.
- a, b, c는 범위가 0<= a, b, c <= 1,000,000로 전체를 다 흝어보면 시간이 초과된다.
- a, b, c가 될 수 있는 후보들을 추리면 적들의 능력치(x, y, z)의 목록이다.
2. a >= x, b>=y, c>=z 세 조건을 모두 성립하면 진수는 해당 적을 이길 수 있다.
3. 적을 K만큼 이기는 경우들을 구한 뒤 이 중 a + b + c 의 값이 가장 작은 경우를 출력한다.
"""
import sys

# 2-5.
N, K = map(int, sys.stdin.readline().split())
enemy = []
A = []
B = []
C = []
ans = 1000010 + 1000010 + 1000010
for _ in range(N):
    tempA, tempB, tempC = map(int, sys.stdin.readline().split())
    A.append(tempA)
    B.append(tempB)
    C.append(tempC)
    enemy.append([tempA, tempB, tempC])

for a in A: # 1<=A<=100
    for b in B: # 1<=B<=100
        for c in C: # 1<=C<=100
            cnt = 0
            for idx in range(N): # N은 최대 100
                if a >= enemy[idx][0] and b >= enemy[idx][1] and c >= enemy[idx][2]:
                    cnt += 1
                if cnt == K:
                    ans = min(ans, a+b+c)
print(ans)

# 2-4 접근방법
# N, K = map(int, sys.stdin.readline().split())
# enemy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# sorted_enemy = sorted(enemy, key=lambda x:max(x))
# maxA, maxB, maxC = 0, 0, 0

# for i in range(K):
#     if maxA <= sorted_enemy[i][0]:
#         maxA = sorted_enemy[i][0]
#     if maxB <= sorted_enemy[i][1]:
#         maxB = sorted_enemy[i][1]
#     if maxC <= sorted_enemy[i][2]:
#         maxC = sorted_enemy[i][2]
# print(maxA + maxB + maxC)


# N, K = map(int, sys.stdin.readline().split())
# enemy = []
# A = []
# B = []
# C = []
# differenceList = []
# for _ in range(N):
#     tempA, tempB, tempC = map(int, sys.stdin.readline().split())
#     A.append(tempA)
#     B.append(tempB)
#     C.append(tempC)
#     enemy.append([tempA, tempB, tempC])
# A.sort()
# B.sort()
# C.sort()
# if N % 2: #홀수이면
#     midA = A[N//2]
#     midB = B[N//2]
#     midC = C[N//2]
# else:
#     midA = A[N//2-1]
#     midB = B[N//2-1]
#     midC = C[N//2-1]
# if K >= N//2:
#     answer = midA + midB + midC
#     for i in range(N):
#         point = 0
#         if enemy[i][0] >= midA:
#             point += enemy[i][0] - midA
#         if enemy[i][1] >= midB:
#             point += enemy[i][1] - midB
#         if enemy[i][2] >= midC:
#             point += enemy[i][2] - midC
#         differenceList.append(point)
#     differenceList.sort()
#     for i in range(K):
#         answer += differenceList[i]
#     print(answer)
# else: 
#     for i in range(N):
#         point = 0
#         for j in range(3):
#             point += enemy[i][j]
#         differenceList.append(point)
#     differenceList.sort()
#     answer = 0
#     for i in range(K):
#         answer += differenceList[i]
#     print(answer)