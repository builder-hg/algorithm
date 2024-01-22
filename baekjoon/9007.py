"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 공식보트: C1, C2, C4 (C는 카누, 숫자는 노를 젓는 사람의 수)
- 코스종류: 200m, 500m, 1000m
- 각 반에서 한 명씩 선출, 선수들의 몸무게 합이 특정값에 근사할 때 최대의 성과를 낸다.
- 차이값이 동일할 때 몸무게의 합이 더 작은 학생들의 몸무게 총합을 구하시오.

2. 아이디어
2-1. 완전탐색
- 정렬시킨다.
- 4중 반복문을 돌린다.
- 더이상 살펴보지 않아도 되는경우
    i > boat
    i + j > boat
    i + j + k > boat
    i + j + k + l > boat

2-2. 
- 4개의 리스트를 두 개의 리스트로 줄인다.
    class1과 class2를 순회하며 각 원소간의 합을 담은 리스트 unionAB를,
    class3과 class4를 순회하며 각 원소간의 합을 담은 리스트 unionCD를 생성한다.
- unionAB와 unionCD를 정렬한다.
- s를 인덱스0에, e를 len(unionCD) - 1 에 둔다.
- unionAB[s] + unionCD[e] 가 목표치보다 큰 지, 같은 지, 똑같은 지 확인한다.
    대소비교를 통해 지점을 옮긴다
    중복이 있을 수 있으므로 중복을 체크한다
    답을 계속해서 갱신한다(목표치와의 차이의 절대값이 가장 작을 때 갱신된다)
"""
import sys

T = int(input())

while T:
    T -= 1

    K, N = map(int, sys.stdin.readline().split())
    lstA = list(map(int, sys.stdin.readline().split()))
    lstB = list(map(int, sys.stdin.readline().split()))
    lstC = list(map(int, sys.stdin.readline().split()))
    lstD = list(map(int, sys.stdin.readline().split()))

    unionAB = []
    unionCD = []

    for i in range(N):
        for j in range(N):
            unionAB.append(lstA[i] + lstB[j])
            unionCD.append(lstC[i] + lstD[j])
    
    unionAB.sort()
    unionCD.sort()

    s = 0
    e = len(unionCD) - 1
    diff = 1 << 64
    ans = 40000001

    while s < len(unionAB) and 0 <= e:
        new_diff = abs(K - (unionAB[s] + unionCD[e]))
        if new_diff < diff: 
            diff = new_diff
            ans = unionAB[s] + unionCD[e]
        elif new_diff == diff:
            ans = min(ans, unionAB[s] + unionCD[e])

        if unionAB[s] + unionCD[e] > K:
            e -= 1
        elif unionAB[s] + unionCD[e] < K:
            s += 1
        else:   
            break
    print(ans)