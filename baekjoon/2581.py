import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
prime = [True for _ in range(10001)]
prime[0] = False
prime[1] = False
total = 0
min_value = 10001

# 소수판정
for i in range(2, 10001):
    if i * i > 10001:
        break
    if not prime[i]: continue

    for j in range(i * i, 10001, i):
        prime[j] = False

# 답 도출하기
for i in range(M, N+1):
    if not prime[i]: continue

    total += i
    if min_value > i:
        min_value = i

if total == 0: 
    print(-1)
else:
    print(total)
    print(min_value)