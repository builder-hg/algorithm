"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 범위는 1 이상 10^15 이하이다.

2. 문제 풀이 방향
key) 특정 자연수를 2로 몇번 나눌 수 있는지(k) 구하고 그 값(2**k)을 return한다.

Think) 시간을 어떻게 줄일 수 있을까?
solution1. 살펴보지 않아도 되는 부분들을 제거하자.
- 홀수라면 살펴보지 않아도 된다.
solution2. 가로로 살펴보자.
"""
import sys

rangeS, rangeE = map(int, sys.stdin.readline().split()) # 범위시작지점과 끝지점을 뜻하는 변수

def get_pow(x):
    pow_idx = 0
    ans = 0
    temp = 2
    while temp <= x:
        cnt = x // temp
        if pow_idx == 0:
            ans += 2 * cnt
        else:
            ans += 2 ** pow_idx * cnt
        temp *= 2
        pow_idx += 1
    return ans

res = get_pow(rangeE) - get_pow(rangeS - 1) + rangeE//2 +rangeE%2 - ((rangeS-1)//2 +(rangeS-1)%2)
print(res)

"""
# 첫번째 풀이법
rangeS, rangeE = map(int, sys.stdin.readline().split()) # 범위시작지점과 끝지점을 뜻하는 변수
ans = 0

def get_pow(num):   # 약수 중 2로 몇번 나눌 수 있는지 구한다.
    pow_idx = 0
    temp = num
    while temp % 2 == 0:
        pow_idx += 1
        temp //= 2
    return 2**pow_idx

for i in range(rangeS, rangeE+1): # 주어진 범위를 순회한다.
    ans += get_pow(i)
print(ans)
"""