"""
[문제풀이전략]
1. 문제 이해 및 정리
- 자연수 N(1<=N<=4,000,000)
2. 문제 풀이 방향
2 3 5 7 11 13 17 19 23 29 31 
  s
               e
10
"""
import sys

N = int(input())
check = [1 for _ in range(N + 1)]
check[0] = 0
check[1] = 0
lst = []

for i in range(2, N + 1):
    if i * i > N:
        break
    if check[i] == 0: continue
    for j in range(i * i, N+1, i):
        check[j] = 0

for i in range(2, N+1):
    if check[i] == 1:
        lst.append(i)

s = 0
e = 0
total = 2
cnt = 0
while s <= e and e < len(lst):
    if total < N:
        e += 1
        if e == len(lst):
            break
        total += lst[e]
    elif total > N:
        total -= lst[s]
        s += 1
    else:
        cnt += 1
        total -= lst[s]
        s += 1
        e += 1
        if e == len(lst):
            break
        total += lst[e]

print(cnt)