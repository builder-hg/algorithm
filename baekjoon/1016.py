"""
# 특징관
15이상의 가장작은 4의 배수부터 본다고하면,
- 16부터 시작해야하고
15 // 4 = 3
(3 + 1) * 4 = 16

(15 - 1) // 4 =3
(3 + 1) * 4 = 16

16이상의 가장작은 4의 배수부터 본다고하면,
- 16부터 시작해야하고
16 // 4 = 4
(4 + 1) * 4 = 20

(16 - 1) // 4= 3
(3 + 1) * 4 = 16

13이상의 가장작은 4의 배수부터 본다고하면,
- 16부터 시작해야하고
(13 - 1) // 4 = 3
(3 + 1) * 4 = 16

"""
import sys
input = sys.stdin.readline

def getExceptCase(S, E):                           # 제곱수의 배수 개수를 구하는 함수 
    _range = E - S + 1
    ret = 0
    visited = [False for _ in range(_range)]

    for i in range(2, E + 1):
        if i * i > E:
            break

        least = (((S - 1) // (i * i)) + 1) * (i * i)
        for j in range(least, E + 1, i * i):
            if visited[j - S]: continue

            visited[j - S] = True         # 제곱수의 배수들은 방문처리한다.
            ret += 1                  # 제곱수의 배수들의 개수를 카운팅한다.
            

    return ret

A, B = map(int, input().split())
_except = getExceptCase(A, B)   # MAX값과 MIN값 사이에 있는 제곱수의 배수 개수를 구한다.
ans = (B - A + 1) - _except                     # 주어진 범위에서 제곱수의 배수들을 뺀다.
print(ans)