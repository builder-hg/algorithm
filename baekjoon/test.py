import sys

N = int(input())
cnt_n = 0
cnt_reverse = 0

for i in range(1, N+1):                             # 주어진 수 N이 소수인지 판별한다.
    if i * i > N:
        break
    if N % i == 0:
        cnt_n += 1

if cnt_n == 1:
    print('yes')
else:
    print('no')