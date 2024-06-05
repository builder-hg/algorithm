"""
t(0)=1
t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
"""
import sys
input = sys.stdin.readline

K = int(input())
lst = [0 for _ in range(36)]
lst[0] = 1

for i in range(1, 36):
    tmp = 0
    for j in range(0, i):
        tmp += lst[j] * lst[i - j - 1]
    lst[i] = tmp

print(lst[K])