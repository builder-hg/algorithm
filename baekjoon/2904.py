"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 1), 두 수 A와 B, A를 나눌 수 있는 소수 X
- 2), A/X와 B * X
- 위 1)과 2)를 무한히 반복할 수 있다. 

2. 문제 풀이 방향
- 숫자들을 모두 곱하고 소인수분해한다.
- 소수종류를 담은 리스트와 그 값을 담은 리스트를 생성한다.
- 각 숫자들이 얼마나 부족한지 센다.
"""
import sys
from functools import reduce
# 수가 소수인 경우와 root N보다 큰 소수가 존재할 경우 다시 고려하기

N = int(input()) # 1<=N<=100
num_list = list(map(int, sys.stdin.readline().split()))
prime_dict = {}             # 숫자 N개를 소인수 분해하였을 때 소인수와 그 승수들을 저장한다.

# 숫자 N개를 각각 소인수 분해한다.
for i in range(N):                  # N번실행
    temp = num_list[i]              # 각각의 원소를 대입한다.
    for j in range(2, num_list[i]+1):
        cnt = 0
        if j * j > num_list[i]:
            break
        while temp % j == 0:
            cnt += 1
            temp //= j
        if cnt:
            if j in prime_dict:
                prime_dict[j] += cnt
            else:
                prime_dict[j] = cnt
    if temp != 1:
        if temp in prime_dict:
            prime_dict[temp] += 1
        else:
            prime_dict[temp] = 1

quotients = {}
times = 0
ans = 1

for prime in prime_dict.keys():             
    quotients[prime] = prime_dict[prime] // N

for num in num_list:
    for prime in prime_dict.keys():             # 소수의 개수들 
        temp = num                          # 어떤 수
        exponent = 0                        # 지수
        while temp % prime == 0:
            exponent += 1
            temp //= prime
        if quotients[prime] > exponent:         # 
            times += quotients[prime] - exponent

for prime in prime_dict.keys():
    ans = ans * (prime ** quotients[prime])

print(ans, times)