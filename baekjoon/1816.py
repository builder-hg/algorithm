"""
[문제풀이전략]

1. 문제 이해 및 정리
- 큰 소수란 10^ 6보다 크다.
- 주어지는 수 : S(10^12 <= S <= 10^18)
- 주어지는 수의 개수 :N (1<=N<=10)
- S의 "모든" 소인수가 10^6보다 크면 적절한 암호 키이다.
- 적절한 암호키이면 1을 순서대로 출력(YES, NO)로 출력한다.


2. 문제 풀이 방향
1) 10^6 까지 돌면서 나눠지면 NO 출력한다.
"""
import sys

N = int(input())
listS = []
for _ in range(N):
    listS.append(int(input()))

for idx in range(N):
    answer = "YES"
    for i in range(2, 1000001):
        if listS[idx] % i == 0 :
            answer = "NO"
            break
    print(answer)