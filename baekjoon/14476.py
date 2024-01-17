"""
[문제 풀이 전략]

1. 문제 이해 및 정리
- N개의 정수 중 임의의 정수(K)를 뺐을 때 남은 정수들의 최대 공약수(GCD)를 구한다.
- 이 때 최대공약수 GCD는 K의 약수가 아니다.
- 범위: 4 <= N <= 1,000,000
- 범위: 각수는 20억을 넘지 않는 자연수이다.
- 출력: 가장큰최대공약수와 뺀 수를 출력한다. 정답이 없다면 -1을 출력한다.

2. 문제 풀이 방향
"""
import sys

N = int(input())
listX = sorted(list(map(int, sys.stdin.readline().split())))
ans = -1
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
        ans = max(ans, temp)
        change = True
        ans = max(ans, temp)

if change:
    print(ans)
else:
    print(-1)
