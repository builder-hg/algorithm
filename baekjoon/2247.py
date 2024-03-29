"""
[문제풀이전략]

1. 문제 이해 및 정리
- 실질적 약수란 1과 자기자신을제외한 약수를 실질적 약수라고 한다.
- SOD는 실질적 약수들의 합이다.
- CSOD는 주어진 자연수 N까지 1, 2, 3, 4, ..., N의 각각의 SOD의 합이다.
- 정수 N, 1 <= N <= 200,000,000
- 출력해야하는 값은 CSOD(N) % 1,000,000 이다.

2. 문제 풀이 방향
1) 완전탐색방법
key) CSOD(N)은 N까지의 소수를 제외한 SOD(K)의 합이다.
key) 모듈러의 성질을 이용할 수 있다. 구해지는 약수마다 1,000,000을 나누어 이를 더한 후 1,000,000을 더한다.
- 소수를 판별할 수 있는 체를 만든다. 에라토스테네스의 체의 크기는 root N이다.
- 1부터 N까지 순회(인덱스는 i)하며 i가 소수이면 넘어간다.
- 소수가 아니라면, 1부터 i까지 순회하며 약수를 구한다.
- 모듈러의 성질을 이용하여 약수를 구할 때 마다 1,000,000로 나누어준다.
- 위 계산을 반복하며 1,000,000로 나눈 약수들을 모두 더한 후 1,000,000로 나눈다.
- 해당 값을 출력한다.
"""
import sys

N = int(input())
ans = 0

for K in range(2, N+1):
    if N // K == 0:
        break
    ans += (K * (N//K - 1)) % 1000000
print(ans % 1000000)
# ==============================================================
# import sys

# N = int(input())
# sod_value = 0   # sod의 합을 담을 변수

# # 2) CSOD 구하기
# for i in range(1, N+1):

#     # 소수인지 아닌지 고려해보자
#     cnt = 0
#     for j in range(1, i+1):
#         if j * j > i:
#             break
#         if i % j == 0:
#             cnt += 1
#             if cnt > 1:
#                 break
#     if cnt == 1:
#         continue

#     # 3) SOD 구하기 
#     for j in range(2, i + 1):
#         if j * j > i:    # 약수가 될 수 없는 범위
#             break
#         if i % j == 0:
#             sod_value += j % 1000000
#             if j * j != i:  #제곱 수가 아니라면
#                 sod_value += (i // j) % 1000000
#     sod_value = sod_value % 1000000
# print(sod_value % 1000000)

# 생각해보자.
# 현재는 SOD를 구할 때 연산 수가 N인데 이걸 줄일 수 없을까?


# ==========================================================================

# # 아래 코드의 문제점
# # 1. 에라토스테네스의 체가 너무 크다.
# # 헷갈리는 점 (24.01.13 새벽기준)
# # 1. 에라토스테네스의 체는 주어진 범위 N까지 다 만들어야하는게 아닌가
# # 2. 소수를 판별할 때, 여러 소수들을 살펴봐야 할 때만 에라토스테네스의 체가 적합한가

# N = int(input())
# sod_value = 0   # sod의 합을 담을 변수

# # 1) 소수 판별
# check = [True for _ in range(N + 1)]         
# # 에라토스테네스의 체를 만든다. 
# # 소수면 SOD(i)의 값은 0 이다. 따라서 소수인지 판별하여 소수라면 고려하지 않기로 한다.
# check[0] = False
# check[1] = False
# # 0과 1은 소수가 아니기에 False를 대입한다.
# for i in range(2, N + 1):
#     if i * i > N:
#         break
#     if check[i] == False:
#         continue
#     for j in range(i * i, N + 1, i):
#         check[j] = False
        
# # 2) CSOD 구하기
# for i in range(N+1): 
#     if check[i] == True:
#         continue
#     # 3) SOD 구하기 
#     for j in range(2, i + 1):
#         if j * j > i:    # 약수가 될 수 없는 범위
#             break
#         if i % j == 0:
#             sod_value += j % 1000000
#             if j * j != i:  #제곱 수가 아니라면
#                 sod_value += (i // j) % 1000000

# print(sod_value % 1000000)