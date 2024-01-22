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


1 2 3 4 5 6 7 8
6                6  
- 이 단계를 먼저 이해하자.


"""
import sys
import copy

N, M = map(int, sys.stdin.readline().split())           # 수열 A의 길이 N, 수열 B의 길이 M
listA = list(map(int, sys.stdin.readline().split()))    # 수열 A
listB = list(map(int, sys.stdin.readline().split()))    # 수열 B

for i in range(M):                                      # 수열 B의 개수 M만큼 반복한다.
    cnt = N                                             # 카운팅 변수의 초기 값은 수열 A의 길이인 N이다.
    temp_list = copy.deepcopy(listA)                    # 수열 A를 복사한다.
    for j in range(N):                                  # 수열 A를 순회한다.
        if temp_list[j] == 0:                           # 수열 A의 특정원소값이 0 이라면 다음을 살펴본다.
            continue
        if (listA[j] + listB[i]) % 7 == 0:              # 수열 A의 특정원소에 Bi를 더했을 때 7의 배수라면 원소를 제거한다.
            cnt -= 1                                    # 제거될 때마다 1씩 줄어든다. cnt가 0이 된다면 해당 연산에 대해서 모든 원소가 제거된 상황인 것이다.
            temp_list[j] = 0                            # 복사한 배열의 j번째 값은 0이 된다. (원소가 삭제되는 개념이다.)
            continue
        temp_list[j] += listB[i]                        # 연산 결과 7의 배수가 아니라면 원소의 값을 더한다.
    if cnt == 0:                                        # 전부 다 제거되었다면 해당 연산을 실행하지 않는다.
        continue
    listA = temp_list                                   # 연산이 정상적으로 수행되었다면 수열 A에 temp_list를 대입한다.

while 0 in listA:                                       # 수열 A에 0을 제거한다.
    listA.remove(0)
print(len(listA))                                       # 수열A의 길이와                                  
ans_list = []
for i in range(len(listA)):
    ans_list.append(listA[i] % (10**9 + 7))                             # 수열 A를 10^9 + 7로 나눈 나머지를 출력한다.
print(*ans_list)