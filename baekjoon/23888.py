"""
[문제풀이전략]
1. 문제 이해 및 정리
- 입력: 수열의 초항, 공차
- 입력: 쿼리의 개수
- 입력: 1이라면 수열의 합 / 2라면 범위내 숫자들의 최대공약수, 시작지점, 끝지점
2. 문제 풀이 방향
- An = a + (n-1)d 

gcd(a + 3d, a + 4d) = gcd(d, a + 4d)
= gcd(d, a + 3d) = gcd(d, a + 2d) ... = gcd(d, a)
gcd(a, d)
gcd(a + kd, a + (k + 1)d)
gcd(a, d)
a + 5d
gcd(gcd(a, d), a + 5d)
gcd(a, d)는
a의 약수면서 d의 약수
a + 5d도 gcd(a, d)로 나눠짐s
(a + 5d) / gcd(a, d)
a / gcd(a, d) + 5d / gcd(a, d)
"""
import sys

a, d = map(int, sys.stdin.readline().split())   # 초항 a와 공차 d
query = int(input())                            # 테스트케이스 개수 query
while query > 0:
    query -= 1
    mode, start, end = map(int, sys.stdin.readline().split())   
    # 어떤 것을 구할 지 선택하는 mode, 시작지점 start, 끝지점 end 
    ans = 0 # 출력할 답을 담을 변수

    if start == end:
        print(a + (start-1) * d)
        continue

    if mode == 1:   # 수열의 합을 출력한다.
        ans = ((a + (start-1) * d) + (a + (end -1) * d)) * (end - start + 1) //2
    else:           # 수열들의 최대공약수를 구한다.
        numA = a
        numB = d
        while numB:                         # 초항과 공차의 최대 공약수를 구해 numA에 담는다.
            numA, numB = numB, numA % numB

        ans = numA
    
    print(ans)

# 항이 하나밖에 없을떄를 고려하기

"""
2 2 4라면,
A2와 A3 그리고 A4의 최대공약수이다.
A2 = a + d
A3 = a + 2*d
A4 = a + 3*d

A2와 A3의 최대 공약수는
GCD(a+d, a+2*d)= GCD(d, a+d)=GCD(a, d)
A2와 A3 그리고 A4의 최대공약수
if a > d:
GCD(a, d) = d
d와 a + 3*d의 최대 공약수를 구한다.
GCD(a+2*d)

else:
GCD(a, d) = a

"""