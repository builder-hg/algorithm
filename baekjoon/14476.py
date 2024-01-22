"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- N개의 정수 중 임의의 정수(K)를 뺐을 때 남은 정수들의 최대 공약수(GCD)를 구한다.
- 이 때 최대공약수 GCD는 K의 약수가 아니다.
- 범위: 4 <= N <= 1,000,000
- 범위: 각수는 20억을 넘지 않는 자연수이다.
- 출력: 가장큰최대공약수와 뺀 수를 출력한다. 정답이 없다면 -1을 출력한다.

2. 문제 풀이 방향
1) 첫번째 시도의 문제점 
정수가 N 1,000,000이면 1,000,000이 첫항, 연산자는 곱, GCD 연산을 999,999 해야한다.
2) 두 번째 시도
key. K번째 수를 안 뺀다면 남은 원소들의 최대공약수는 무조건 K의 약수여야 한다.

3) 기타
key. 누적합을 써야한다.
* 누적합이란 순서대로 누적해서 구한다.
1	2	3	4	5
8	12	24	36	48
8	4	4	4	4	(정방향)
4	12	12	12	48	(역방향)

우리는 k번을 뺀다고 하면 k-1과 k+1의 최대 공약수를 비교한다.
"""
import sys

N = int(input())
numbers = [0] + list(map(int, sys.stdin.readline().split()))
forward_cnt = [0 for _ in range(N+1)]
backward_cnt = [0 for _ in range(N+1)]
# 정방향으로 최대 공약수 기록하기
forward_cnt[1] = numbers[1]
for i in range(2, N+1):
    numA = forward_cnt[i-1]
    numB = numbers[i]
    while numB:
        numA, numB = numB, numA % numB
    forward_cnt[i] = numA
# 역방향으로 최대 공약수 기록하기
backward_cnt[N] = numbers[N]
for i in range(N-1, 1, -1):
    numA = backward_cnt[i+1]
    numB = numbers[i]
    while numB:
        numA, numB = numB, numA % numB
    backward_cnt[i] = numA
# 정답구하기
ans = 0
remove_num = 0
for i in range(1, N+1):
    if i == N:
        if numbers[i] % numA == 0:
            break
        if forward_cnt[i-1] >= ans:
            ans = numA 
            remove_num = numbers[i]
        break

    numA = forward_cnt[i-1]
    numB = backward_cnt[i+1]
    while numB:
        numA, numB = numB, numA % numB
    if numbers[i] % numA == 0:
        continue
    if numA >= ans:
        ans = numA 
        remove_num = numbers[i]

if ans:
    print(ans, remove_num)
else:
    print(-1)
"""
import sys

N = int(input())
listX = sorted(list(map(int, sys.stdin.readline().split())))
ans = 1 << 64
remove_num = 0
change = False

for i in range(N):
    if i == N-1:
        temp = listX[N-2]
    else:
        temp = listX[N-1]
    for j in range(N):
        if listX[i] == listX[j]:
            continue
        numB = listX[j]
        while numB:
            temp, numB = numB, temp % numB
    if temp == 1: continue
    
    if listX[i] % temp == 0:
        temp = -1
    
    if temp != -1: 
        change = True
        ans = min(ans, temp)
        remove_num = listX[i]

if change:
    print(ans, remove_num)
else:
    print(-1)

"""