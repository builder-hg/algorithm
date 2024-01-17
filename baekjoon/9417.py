"""
[문제 풀이 전략]
1. 문제 이해 및 정리

2. 문제 풀이 방향

"""
import sys
T = int(input())

def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

while T > 0:
    T -= 1
    listM = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(len(listM)-1):
        for j in range(i+1, len(listM)):
            if listM[i] > listM[j]:
                ans = max(gcd(listM[i], listM[j]), ans)
            else:
                ans = max(gcd(listM[j], listM[i]), ans)
    print(ans)