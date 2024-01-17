"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- 두 점 사이에 정수인 x좌표와 y좌표가 K개를 성립하는 선분의 수를 출력한다.
- 0<=x<=N, 0<=y<=M, x와 y는 정수
- 입력값 : x의 최대범위, y의 최대범위, 지나가는 점의 개수 K개
- 이때 x와 y의 최대범위는 50을 넘지 않는다. 지나가는 점의 개수는 2이상 50 이하이다.

2. 문제 풀이 방향
key) 가로선분, 세로선분, 대각선선분별로 나누어 구한다.

N = 3, M = 4이고 K가 2라면, 즉 0<=x<=3, 0<=y<=4라면,
x가 0~1, 1~2, 2~3 구간에서 K 조건을 만족한다.
y는 0~1, 1~2, 2~3, 3~4 구간에서 K 조건을 만족한다.
가로선분은 (N - K + 2) * (M + 1)개 만큼 존재한다.
세로선분은 (M - K + 2) * (N + 1)개 만큼 존재한다.

N = 4, M = 5이고 K가 3이라면 (0 <= x <= 4, 0 <= y <= 5)
x는 0~2, 1~3, 2~4, y는 0~2, 1~3, 2~4, 3~5
대각선 선분은 (N - K + 2) * (M - K + 2) * 2 

2-2. 승연님의 풀이방향
! 특정 지점을 잇는 선분을 그었을 때 중간에 정수좌표를 지나는가?
! x의 증가량과 y의 증가량을 가지고 선분 안에 있는 좌표의 개수를 구한다.
! 첫 지점과 끝 지점까지의 기울기와 동일한 기울기를 지닌 좌표가 있는지 알아보자.
! 완전탐색으로 돌린다.
! 첫 지점을 고정하고 끝 지점을 돌리며 진행한다.
- 4, 2를 동시에 나눌 수 있는 수를 최대 공약수 gcd <- 
- 8:4 

"""
import sys
# K가 1일때도 생각해보자 <- 최소치에 대해 생각해보기
N, M, K = map(int, sys.stdin.readline().split())
cnt = 0

def getGCD(numA, numB):
    if numA == 0:
        return numB
    if numB == 0:
        return numA
    
    tempA = numA
    tempB = numB
    while tempB:
        tempA, tempB = tempB, tempA % tempB
    return tempA

if K == 1:          
    print((N+1) * (M+1))
    sys.exit()

for baseX in range(N+1):
    for baseY in range(M+1):
        for i in range(N+1):
            for j in range(M+1):
                numA = abs(baseX - i)
                numB = abs(baseY - j)
                if getGCD(numA, numB) == K-1:
                    cnt += 1

print(cnt // 2)


# ==========================================================
# import sys

# N, M, K = map(int, sys.stdin.readline().split())
# cnt = 0
# for baseX in range(N+1):
#     for baseY in range(M+1):
#         for i in range(N+1):
#             for j in range(baseY, M+1):
#                 if abs(baseX - i) == 0:
#                     if abs(baseY - j) == K-1:
#                         cnt += 1
#                         continue
#                 if abs(baseY - j) == 0:
#                     if baseX >= i:
#                         continue
#                     if abs(baseX - i) == K-1:
#                         cnt += 1
#                         continue
#                 numA = abs(baseX - i)
#                 numB = abs(baseY - j)
#                 while numB:
#                     numA, numB = numB, numA % numB
#                 if numA == K-1:
#                     cnt += 1

# print(cnt)
# 피드백
"""
피드백
1 전범위 다보기 -> 같은 선분이 두 번씩 중복된다. 
2 cnt / 2
"""


# ==========================================================================
# import sys
# # x범위의 최대값 N(1<=N<=50), y범위의 최대값 M(1<=N<=50), 선분에 포함된 점의 개수 K(2<=K<=50)
# N, M, K = map(int, sys.stdin.readline().split())
# # 주어진 범위내의 좌표들을 모두 순회하면서
# # 두 수의 최대 공약수가 K-1이라면 
# # cnt를 1 증가시킨다. 
# cnt = 0
# for i in range(N+1):
#     for j in range(M+1):
#         numA = i
#         numB = j
#         while numB:
#             numA, numB = numB, numA%numB
#         if numA == K-1:
#             print(i, j)
#             # cnt += 1

# # print(cnt)

# ================================================================
# import sys

# range_x, range_y, dot = map(int, sys.stdin.readline().split())
# cnt = 1
# for i in range(range_x + 1):
#     for j in range(range_y + 1):
#         print(i , j)


"""
# 첫번째 풀이. 수식에 의존한 풀이법
# 아래 풀이는 순전히 계산에 의존한 풀이방법, 정수론과 어떻게 연결지을 수 있을까?
N, M, K = map(int, sys.stdin.readline().split())
ans = 0 # 답을 담을 변수 
ans += (N - K + 2) * (M + 1)    # 조건을 만족하는 가로선분들
ans += (M - K + 2) * (N + 1)    # 조건을 만족하는 세로선분들
ans += (N - K + 2) * (M - K + 2) * 2# 조건을 만족하는 대각선들 
if ans <= 0:
    print(0)
else:
    print(ans)
"""