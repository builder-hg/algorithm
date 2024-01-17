"""
[문제풀이전략]

1. 문제 이해 및 정리

2. 문제 풀이 방향
tip)
1. K을 만들기 위해 어떤 게 몇 개씩 필요한가?
2. N!에 얘네가 몇개씩 있는지 알아야 함
3. 1, 2에서 알아낸 정보로 답구하기

20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

N이 30, K가 20일때, K는 2와 두 개, 5 한 개가 쌍으로 필요하다.
N!에서 우리가 고려할 소인수들은 2와 5의 쌍이다.
N!에서 2의 개수(x)를 구하고 한 쌍당 두개가 필요하다 했으므로 x // 2를 한다.
N!에서 5의 개수(y)를 구하고 한 쌍당 한개가 필요하다 했으므로 y // 1를 한다.
두 수 x//2와 y//1 중 가장 작은 값을 출력한다.
"""
# 두번째 시도, 24.01.17
import sys
T = int(input())    # 1<=T<=100
while T:
    T -= 1
    N, K = map(int, sys.stdin.readline().split()) # 2<=N<=10^18,2<=K<=10^12

    # K의 소인수 구하기
    prime_k_type = []   # K의 소인수
    prime_k_cnt = []    # K의 소인수 개수
    temp_K = K
    ans = 1 << 64
    for i in range(2, K+1):
        if i * i > K:
            break
        cnt = 0
        do = False
        while temp_K % i == 0:
            do = True
            cnt += 1
            temp_K //= i
        if do:
            prime_k_type.append(i)
            prime_k_cnt.append(cnt)
    if temp_K != 1:
        prime_k_type.append(temp_K)
        prime_k_cnt.append(1)
    # 고려할 필요가 있는 소인수들로 N!을 몇번 나눌 수 있는지 구한다.
    for i in range(len(prime_k_type)):
        cnt = 0                 # N!이 가지고 있는 소인수 x의 개수
        prime = prime_k_type[i]
        temp = prime
        while temp <= N:
            cnt += N // temp
            temp *= prime
        ans = min(ans, cnt // prime_k_cnt[i])   # N!이 가지고 있는 소인수x의 개수로 몇 쌍 만들 수 있는지 구한다.

    print(ans)
"""
# 첫번째 시도, 시간초과
import sys

T = int(input())    # 테스트 케이스

while T != 0:
    T -= 1
    N, K = map(int, sys.stdin.readline().split())  

    # K의 소인수 개수가 담긴 리스트, 특정인덱스 i의 값은 소수 i를 필요로 하는 개수이다.
    cnt_list = [0 for _ in range(10 ** 6 + 1)]
    types = [] # 소수의 종류가 담긴 리스트

    # K를 소인수분해하여 소인수가 몇개씩 필요한지 확인한다.
    temp = K
    for i in range(2, K+1):
        cnt = 0
        if i * i > K:
            break
        while temp % i == 0:
            cnt += 1 
            cnt_list[i] += 1

            if cnt == 1:
                types.append(i)

            temp //= i
    if temp != 1:
        cnt_list[temp] = 1
        types.append(temp)

    ans = 1 << 32
    for i in range(len(types)):
        pow_idx = 1
        temp = 0
        while N // (types[i] ** pow_idx) > 0:
            temp += N // (types[i] ** pow_idx)
            pow_idx += 1
        ans = min(temp, ans)
    
    print(ans)

"""