"""
문자열의 길이 200,000, 쿼리의 수 200,000

A. 쿼리마다 문자열을 매번 보면 시간초과가 난다.
B. 각 알파벳 별 배열을 만들어 접근한다.
    01) a = [0, 1, 2, 3,...] 이라면 1번째 위치에는 a가 한 개, 2번째 위치에는 a가 2개 있다는 의미이다.
    02) 1 ~ 5구간사이는 a의 개수는 a[5] - a[0]와 같다. 
"""
import sys
input = sys.stdin.readline

def getCount(K, s, e):
    index = ord(K) - 97
    return alphabet[index][e] - alphabet[index][s - 1]

raw = [''] + list(map(str, input().strip()))

alphabet = [
    [0 for _ in range(len(raw))],   # a
    [0 for _ in range(len(raw))],   # b
    [0 for _ in range(len(raw))],   # c
    [0 for _ in range(len(raw))],   # d
    [0 for _ in range(len(raw))],   # e
    [0 for _ in range(len(raw))],   # f
    [0 for _ in range(len(raw))],   # g
    [0 for _ in range(len(raw))],   # h
    [0 for _ in range(len(raw))],   # i
    [0 for _ in range(len(raw))],   # j
    [0 for _ in range(len(raw))],   # k
    [0 for _ in range(len(raw))],   # l
    [0 for _ in range(len(raw))],   # m
    [0 for _ in range(len(raw))],   # n
    [0 for _ in range(len(raw))],   # o
    [0 for _ in range(len(raw))],   # p
    [0 for _ in range(len(raw))],   # q
    [0 for _ in range(len(raw))],   # r
    [0 for _ in range(len(raw))],   # s
    [0 for _ in range(len(raw))],   # t
    [0 for _ in range(len(raw))],   # u
    [0 for _ in range(len(raw))],   # v
    [0 for _ in range(len(raw))],   # w
    [0 for _ in range(len(raw))],   # x
    [0 for _ in range(len(raw))],   # y
    [0 for _ in range(len(raw))],   # z
]
for i in range(97, 123):                                        # 알파벳별로 구간마다 몇 개 있는지 카운팅한다.
    alpha = chr(i)
    for j in range(1, len(raw)):
        if raw[j] == alpha:
            alphabet[i - 97][j] = alphabet[i - 97][j - 1] + 1
        else:
            alphabet[i - 97][j] = alphabet[i - 97][j - 1]

Q = int(input())
for _ in range(Q):
    alpha, s, e = map(str, input().split())
    print(getCount(alpha, int(s) + 1, int(e) + 1))
