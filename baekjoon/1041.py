"""
접근 방식
인접한 면(2): AB, AC, AD, AE, FB, FC, FD, FE, DB, DE, CB, CE
인접한 면(3): ABC, ABD, ADE, ACE,  FBC, FBD, FDE, FCE,

A:0 B:1 C:2 D:3 E:4 F:5


1) N = 1
가장 큰 수가 바닥으로 향하게 한다. 
15

2) N = 2,
1층: 
- 모서리의 경우 인접한 면(2)의 합이 가장 작은 값으로
꼭대기층:
- 모서리의 경우 인접한 면(3)의 합이 가장 작은 값으로

3) N = 3,
1층:
- 모서리의 경우 인접한 면(2)의 합이 가장 작은 값으로 * 4
- 단면의 경우 그 수가 가장 작은 값으로 * 4 * (N - 2)
2층: 
- 1층과 동일
꼭대기층:
- 모서리의 경우 인접한 면(3)의 합이 가장 작은 값으로 * 4
- 모서리를 제외한 가장자리의 경우 인접한 면(2)의 합이 가장 작은 값으로 * 4 * (N - 2)
- 내부 단면의 경우 그 수가 가장 작은 값으로 * ((N - 2) ** 2)

4) N = k,
1층: min(arrB) * 4 + min(arrA) * (k - 2)
2층: min(arrB) * 4 + min(arrA) * (k - 2)
...
t층: min(arrC) * 4 + min(arrB) * (k - 2) * 4 + min(arrA) * (k - 2) ** 2
수식 => (k - 1) * (min(arrB) * 4 + min(arrA) * (k - 2)) + min(arrC) * 4 + min(arrB) * (k - 2) * 4 + min(arrA) * (k - 2) ** 2
"""
import sys
input = sys.stdin.readline

N = int(input())
arrA = list(map(int, input().split()))
arrB = [
    arrA[0] + arrA[1],
    arrA[0] + arrA[2],
    arrA[0] + arrA[3],
    arrA[0] + arrA[4],
    arrA[5] + arrA[1],
    arrA[5] + arrA[2],
    arrA[5] + arrA[3],
    arrA[5] + arrA[4],
    arrA[1] + arrA[2],
    arrA[1] + arrA[3],
    arrA[3] + arrA[4],
    arrA[2] + arrA[4],
]
arrC = [
    arrA[0] + arrA[1] + arrA[2],
    arrA[0] + arrA[1] + arrA[3],
    arrA[0] + arrA[3] + arrA[4],
    arrA[0] + arrA[2] + arrA[4],
    arrA[5] + arrA[1] + arrA[2],
    arrA[5] + arrA[1] + arrA[3],
    arrA[5] + arrA[3] + arrA[4],
    arrA[5] + arrA[2] + arrA[4],
]

if N == 1:
    print(sum(arrA) - max(arrA))
    sys.exit()

ans = (N - 1) * (min(arrB) * 4 + min(arrA) * (N - 2) * 4) + min(arrC) * 4 + min(arrB) * (N - 2) * 4 + min(arrA) * ((N - 2) ** 2)
print(ans)