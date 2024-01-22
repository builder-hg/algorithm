"""
[문제풀이전략]
1. 문제 이해 및 정리
- 출력: 첫번째 수를 두 수의 최대공약수, 두 번째 수를 두 수의 최소공배수로 하는 자연수를 구하라.
- 입력: 두 수는 2이상 100,000,000 이하이다.
- 출력: 크기가 작은 수 부터 출력한다. 정답이 여러개라면 두 자연수의 합이 최소가 되는 수를 출력한다.

2. 문제 풀이 방향
- 최대 공약수를 소인수분해한다.
- 두 수는 분해한 소인수들을 최소한으로 가져야한다.
- 2부터 100,000,000 순회하며 두 수 A * B가 두번째값 * 첫번째 값인 경우를 구한다.
"""
import sys
import math

GCD, LCD = map(int, sys.stdin.readline().split())
# 사각형의 면적(N)이 주어졌을 때,
# 가로, 세로의 합이 최소가 되려면 
N = int(math.sqrt(GCD * LCD))
for A in range(N+1, 0, -1):
    B = (GCD * LCD) // A
    
    if (GCD * LCD) % A != 0:
        continue
    if A < GCD or B < GCD:
        continue
    numA = A
    numB = B
    while numB:
        numA, numB = numB, numA % numB
    if numA != GCD:
        continue
    print(A, B)
    sys.exit()

# prime_dict = {}
# temp = GCD
# for i in range(2, GCD + 1):
#     cnt = 0
#     if i * i > GCD:
#         break
#     while temp % i == 0:
#         cnt += 1
#         temp //= i
#     if cnt:
#         if i in prime_dict:
#             prime_dict[i] += cnt
#         else:
#             prime_dict[i] = cnt
# if temp != 1:
#     if temp in prime_dict:
#         prime_dict[temp] += 1
#     else:
#         prime_dict[temp] = 1



# ans = 1 << 64
# ans_A = 0
# ans_B = 0

# for i in range(1, LCD // GCD + 1):
#     for j in range(1, LCD // GCD + 1):
#         if GCD * GCD * i * j ==

# for A in range(GCD, 100000001):
#     if A % GCD != 0:
#         continue
#     if A > LCD:
#         break
#     for B in range(GCD, 100000001):
#         if B % GCD != 0:
#             continue
#         if B > LCD:
#             break
#         if A * B == GCD * LCD:
#             if A + B < ans:
#                 ans = A + B
#                 ans_A = A
#                 ans_B = B

# print(ans_A, ans_B)