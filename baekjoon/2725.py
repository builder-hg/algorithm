"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- x, y의 범위는 0이상 1,000 이하이다.
- 테스트 케이스의 개수, 1<= T <= 1,000
- 0,0에서 x, y를 연결하는 직선이 다른 점을 통과하지 않는다면 그 점은 보이는 점이다.
- 범위가 주어졌을 때 0, 0에서 보여지는 점의 개수를 구하는 문제
+ i와 j가 서로 같은 지점의 좌표는 1,1 을 제외하고는 계산하지 않는다.
+ 

2. 문제 풀이 방향
중간에 점이없어야한다. ->점이있으려면 두 증가량의 공약수가 있는지 살펴본다.
"""
# 24.01.17 
"""
N:1,
(1,0)(0,1)(1,1)

N:2, 
N(1) + (1,2),(2,1)

N:3,
N(2) + (1,3),(2,3),(3,1),(3,2)

- cnt_list의 i번째 값은 n이 i일때의 cnt 개수이다.
- N=K일때 
    j=K, i는 1부터 K-1까지를 순회하며 찾아본다.(temp)
    값은 temp * 2이고 
- N(K)는 N(K-1) + temp * 2이다. 
- N=1일때는 따로 고려한다.
- Query 문제는 시작 전에 관련 작업을 미리 해둔다. (같은 작업을 여러번 반복하지 않는다.)
"""
import sys

T = int(input())

# N(k)구하기
list_cnt = [0 for _ in range(1001)] # cnt_list의 i번째 값을 n이 i일 때의 원점에서 보이는 좌표의 개수이다.                         
list_cnt[1] = 3                     # N=1일 때의 값은 3이다. 

for K in range(2, 1001):
    temp = 0    
    for i in range(1, K):
        numA = i
        numB = K
        while numB:
            numA, numB = numB, numA % numB
        if numA == 1:
            temp += 1
    list_cnt[K] = list_cnt[K-1] + 2*temp

while T:
    T -= 1
    N = int(input())
    print(list_cnt[N])













# # 첫번째 시도
# import sys
# # key) 0,0을 제외한 모든 좌표를 순회하며 x, y가 서로소라면 cnt를 1증가시킨다.
# # (0,0), (1,0)과 (0,1) 고려하기
# # 시간초과. 어디서 더 줄일 수 있을까.
# T = int(input())

# cnt_list = [0 for _ in range(1001)]

# for i in range(0, 1001):        
#     for j in range(0, 1001):
#         numA = i
#         numB = j
#         while numB:
#             numA, numB = numB, numA % numB
#         if numA == 1:
#             cnt += 1

# # 범위가 N일때 서로소의 개수를 기록하고 싶은데 
# # 어떻게 구해서 어떻게 담지

# while T > 0:
#     T -= 1
#     N = int(input())
#     cnt = 0
#     print(cnt)

"""
q가 주어지고
q번 이러이러한걸 해라
똑같은거 계속 시키는
그런게 쿼리 문제에요
-> 시작 전에 관련 작업을 미리 해둔다. 
"""
"""
n = 5에 포함돼요
n = 5를 구하다보면
n = 4의 정답이 되는 모든 점을 지나거든요
우린 사실
n = 5를 구하는 한번의 과정에서
n = 1, n = 2, n = 3, n =4, n = 5의 정답을 모두 구할 수 있어요

내일 n=5일때 n=4가 어떻게 포함되는지
확인하기
"""