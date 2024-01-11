"""
[문제풀이전략]

1. 문제풀이방향
- 보석의 무게: a, b, c ... ( > 1)
- a * b * c * ... = k
- k의 소인수의 개수 구하기
"""
import sys

K = int(input())
cnt = 0
temp = K
listX = []
for i in range(2, K+1):
    if i * i > K:
        break
    while temp % i == 0:
        listX.append(i)
        cnt += 1
        temp //= i
if temp != 1:
    cnt += 1
    listX.append(temp)
print(cnt)
print(*sorted(listX))