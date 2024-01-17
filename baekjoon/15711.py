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

# 골드바흐 -> 어떤 수가 짝수라면 두 소수의 합으로 나타낼 수 있다.
# 홀수인 수가 소수의 합으로 나타낼 수 있냐만 확인하면된다.
# 홀수, 짝수로 구성되어야 하는데 소수는 2를 제외하고는 다 홀수야 
# 우리는 K-2가 소수인지만 확인하면 된다.
# 2부터 K-2까지 순회를하면서 특정 인덱스에서 K-2를 나눴을때 그 나머지가 0이 떨어지면 소수가 아니라는 의미이므로 NO를 출력해

# 500 * root (4 * 10 ^ 12)
# = 500 * 2 * 10^6
# = 1,000 * 1,000,000 = 1,000,000,000
# 홀수만 구하면 500,000,000


length = 2 * (10 ** 6) + 10
check = [True for _ in range(length)]
check[0] = False
check[1] = False
clean_check = []
for i in range(length):
    if check[i] == False:
        continue
    clean_check.append(i)
    for j in range(i * i, length, i):
        check[j] = False
    

while T:
    T -= 1
    A, B = map(int, input().split())
    K = A + B

    if A == 1 and B == 1:
        print("NO")
        continue

    if K == 3:
        print("NO")
        continue

    if K % 2 == 0:
        print("YES")
        continue

    # K-2가 소수인지 판별하자.
    check = K - 2
    mate = True
    for i in clean_check: # 연산을 줄여보자. 500만번
        if i * i > check:
            break
        if check % i == 0:
            mate = False
            break
    if mate: 
        print("YES")
    else:
        print("NO")

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
