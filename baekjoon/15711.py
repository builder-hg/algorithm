"""
[문제풀이전략]

1. 문제 이해 및 정리
- 각각의 끈의 길이 A, B (1보다 크거나 같고 1억보다 작거나 같다.)
- 환상의 짝꿍 조건:  (A+B) % X == 0 and (A+B) % Z == 0(이때 X와 Z는 소수이다.)
- 확인할 개수 T (1<=T<=500)
- 환상의 짝꿍이면 YES를 출력한다. 아니면 NO를 출력한다.

2. 문제 풀이 방향
1 완전탐색방법
1) i를 2부터 K까지 순회하며 소수를 구한다.
2) 이 중 두개의 소수를 골라 그 합이 K라면 YES를 출력한다.

2) 최적화 방법 첫번째
1) i를 2부터 K까지 순회한다. i * i > K라면 반복문을 빠져나간다. 
2) i가 소수라면 K-i가 소수인지 판별한다.

3) 골드바흐의 추측
1) A + B = K가 짝수인지 홀수인지 확인한다.
2) 짝수라면 YES를 출력한다.
3) 홀수라면 어떻게 구할 수 있을까 
"""
import sys

T = int(input())

# 메모리 초과
while T:                             # 테스트 케이스만큼 반복한다.
    A, B = map(int, input().split()) # 끈의 길이 A, B
    K = A + B                       # 두 끈의 길이의 함 K

    if K % 2 == 0:                  # 골드바흐의 추측으로 K가 짝수이면 두 소수의 합으로 나타낼 수있다.
        print("YES")                # 따라서 YES를 출력하고 다음 케이스로 넘어간다.
        T -= 1
        continue

    answer = False                  # 환상의 짝꿍 여부를 판별한다. True면 환상, False면 환장
    check = [1 for _ in range(K+1)] # 소수값 판별 리스트, 기본값은 1로 해당 인덱스가 소수라면 1로 표시한다.
    check[0] = 0                    # 0은 소수가 아니다.
    check[1] = 0                    # 1은 소수가 아니다.

    for i in range(2, K+1):         # 소수를 판별하는 용도의 반복문
        if i * i > K:               # root K 만큼만 살펴본다.
            break
        if check[i] == 0 :          # 소수가 아닌 값들은 넘어간다.
            continue
        for j in range(i * i, K+1, i):  # i * i부터 i 씩 증가하며 소수가 아닌 부분들을 걸러낸다.
            check[j] = 0

    for i in range(2, K+1):             # 소수값을 판별한 리스트를 순회한다.
        if i * i > K:                   # root K 보다 크다면 살펴보지 않는다.
            break
        if check[i] == 1 and check[K-i] == 1:   # i의 값이 소수일 때 K-i의 값이 소수라면 환상의 짝꿍이다.
            answer = True                       # 환상의짝꿍으로 True를 대입한다.
            break
    if answer :                         # 환상의 짝꿍이면 YES를 출력한다.
        print("YES")
    else:
        print("NO")
    T -= 1

# while T:
#     A, B = map(int, input().split())
#     K = A + B
    
#     if K % 2 == 0:
#         print("YES")
#         T -= 1
#         continue

#     temp = K
#     cnt = 0 
#     for i in range(2, K+1):
#         if i * i > K:
#             break
#         while temp % i == 0:
#             cnt += 1
#             temp //= i
#     if cnt % 2 == 0:
#         print("YES")
#     else:
#         print("NO")
#     T -= 1
