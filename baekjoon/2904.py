"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 1), 두 수 A와 B, A를 나눌 수 있는 소수 X
- 2), A/X와 B * X
- 위 1)과 2)를 무한히 반복할 수 있다. 

2. 문제 풀이 방향
- 세 숫자 A, B, C를 모두 곱하고 소인수분해한다.
- 소수종류를 담은 리스트와 그 값을 담은 리스트를 생성한다.
- 각 숫자들이 얼마나 부족한지 센다.
"""
import sys
from functools import reduce
# 수가 소수인 경우와 root N보다 큰 소수가 존재할 경우 다시 고려하기

N = int(input()) # 1<=N<=100
num_list = list(map(int, sys.stdin.readline().split()))
total = reduce(lambda x, y: x*y, num_list)
types = []
values = []
quotients = []
temp = total
times = 0
ans = 1

for i in range(2, total + 1):
    cnt = 0
    if i * i > total:
        break
    while temp % i == 0:
        cnt += 1
        temp //= i
    if cnt:
        types.append(i)
        values.append(cnt)

for i in range(len(types)):
    quotients.append(values[i] // N)

for num in num_list:
    for i in range(len(types)):
        temp = num
        exponent = 0
        while temp % types[i] == 0:
            exponent += 1
            temp //= types[i]
        if quotients[i] > exponent:
            times += quotients[i] - exponent

for i in range(len(types)):
    ans = ans * (types[i] ** quotients[i])

print(ans, times)