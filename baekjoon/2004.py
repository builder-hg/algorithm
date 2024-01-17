"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- N C R = N! / ((N - R)! * R!) 
- 끝자리 0의 개수 구하기

2. 문제 풀이 방향
- 분자, 분모 각각 2와 5를 하나씩 짝 지어 만들 수 있는 쌍의 개수(a, b)를 비교한다.
- a - b를 출력한다.(a > b)
"""
import sys
N, R = map(int, sys.stdin.readline().split())  

types = [2, 5]
A = [] # A[0]은 N! 곱해진 2의 개수, A[1]은 N!에 곱해진 5의 개수
B = [] # B[0]은 (N-R)! 곱해진 2의 개수, B[1]은 N!에 곱해진 5의 개수
C = [] # C[0]은 R! 곱해진 2의 개수, C[1]은 N!에 곱해진 5의 개수

for i in range(len(types)): # N!에서 2, 5가 몇개 곱해져있는지 계산
    pow_idx = 0
    tempA = types[i]
    while tempA <= N:
        pow_idx += N//tempA
        tempA *= types[i]
    A.append(pow_idx)
for i in range(len(types)): # (N-R)!에서 2, 5가 몇개 곱해져있는지 계산
    pow_idx = 0
    tempB = types[i]
    while tempB <= N-R:
        pow_idx += (N-R)//tempB
        tempB *= types[i]
    B.append(pow_idx)
for i in range(len(types)): # R!에서 2, 5가 몇개 곱해져있는지 계산
    pow_idx = 0
    tempC = types[i]
    while tempC <= R:
        pow_idx += R//tempC
        tempC *= types[i]
    C.append(pow_idx)

cnt_list = [0,0]
for i in range(2):
    if A[i] >= (B[i] + C[i]):
        cnt_list[i] = A[i] - B[i] - C[i]
    else:
        print(0)
        sys.exit()
print(min(cnt_list))