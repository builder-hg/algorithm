"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 수열이란 어떤 규칙에 따라 숫자들을 늘여놓은 것이다.

2. 문제 풀이 방향
M=1, (A1 + B1) + (A2 + B1) + (A3 + B1) + ... + (An + B1)
M=2, (A1 + B2) + (A2 + B2) + (A3 + B2) + ... + (An + B2)
...
M=M, (A1 + Bm) + (A2 + Bm) + (A3 + Bm) + ... + (An + Bm)
- for i in range(M+1):
    cnt = N
    temp_list = listA
    for j in range(N+1):
        if (Aj + Bi) % 7 == 0:  
            cnt -= 1
            temp_list[i] = 0
            continue
        temp_list[i] += Bi
    if cnt == 0:
        continue
    listA = temp_list
        
print(len(listA))
print(*listA)


"""
import sys
import copy

N, M = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    cnt = N
    temp_list = copy.deepcopy(listA)
    for j in range(N):
        if temp_list[j] == 0:
            continue
        if (listA[j] + listB[i]) % 7 == 0:  
            cnt -= 1
            temp_list[j] = 0
            continue
        temp_list[j] += listB[i]
    if cnt == 0:
        continue
    listA = temp_list

while 0 in listA:
    listA.remove(0)
print(len(listA))
print(*listA)

