"""
[문제풀이전략]

1. 문제 분석
- 특징마다 거리가 도합 0이거나 2이다.
    0: 세 가지 모두 유형이 동일하다.
    2: 한 가지 유형이 다르다.
- N명의 학생이 16명보다 많이 주어진다면 유형 하나가 무조건 중복된다.
- N명의 학생이 32명보다 많다면 무조건 세 학생의 유형이 같은 경우가 한가지 이상이다.

2. 완전탐색
- 32까지만 고려한다면 32C3 
    = 32 * 31 * 30 / (3 * 2)
    = 32 * 31 * 5
    = 4960
- 각각의 특징 4개를 다 돌린다. 4중 반복문.
"""
import sys
input = sys.stdin.readline
T = int(input())
ans = 1 << 64
def get_dist(typeA, typeB):
    cnt = 0
    for i in range(4):
        if typeA[i] == typeB[i]:
            continue                
        cnt += 1
    return cnt
# N명 중 k명을 고른다
    # 1) 모든 경우를 다 살핀다. 
    # 2) 입력과 상관없이 살펴볼 케이스들을 확인한다. 
        # 여기서는 16 ^ 3 가지의 경우이다.
        # 주어진 수열들로 특정 케이스를 만들 수 있는지 확인한다.
        # 만들 수 있다면 거리를 구한다.
# 입력
# 유형별로 카운팅을 한다.
types = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP","ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
cases = []
lst2 = []
for i in range(16):
    for j in range(16):
        for k in range(16):
            d = {}
            d[types[i]] = d.get(types[i], 0) + 1
            d[types[j]] = d.get(types[j], 0) + 1
            d[types[k]] = d.get(types[k], 0) + 1
            cases.append(d) # 1) 딕셔너리에 심리적거리 추가한다.
            lst2.append()   # 케이스와 인덱스를 일치시켜서 심리적 거리를 구할 수 있다.
lst = input().split()
std = {}
skip = False
# lst를 순회하며 각 유형별로 몇개있는지 구한다.
# cases 전체를 순회한다.
# 유형별로 가지고 있는 개수와 케이스를 비교하여 해당된다면 심리적 거리를 구한다.
for i in lst:
    std[i] = std.get(i, 0) + 1
for case in cases: # 케이스를 바로 꺼낸다.
    skip = False
    for key in case:
        if std.get(key,0) < case[key]:    # 케이스를 성립하는 조건에 부합하지 않는다. 개수가 부족하다.
            skip = True
            break
    if skip:    # 다음 케이스를 살펴본다.
        continue
    # 개수가 부족하지 않은 경우(즉 케이스를 성립하는 경우)
    # key_list = case.keys()
    key_list = []
    for key in case:
        for i in range(case[key]):
            key_list.append(key)
    

    dist = get_dist(key_list[0], key_list[1]) + get_dist(key_list[1], key_list[2]) + get_dist(key_list[0], key_list[2])
    ans = min(ans, dist)

print(ans)

"""
def get_dist(A, B):
    cnt = 0
    for idx in range(4):
        if A[idx] == B[idx]:
            continue
        cnt += 1
    return cnt 

while T:
    T -= 1
    N = int(input())    # 학생 수
    lst = input().split()   
    ans = 1 << 64

    if N > 32:
        print(0)
        continue

    # 주어진 N개에서 3개를 고르는 경우에 해당한다.
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                A = lst[i]
                B = lst[j]
                C = lst[k]
                dist = get_dist(A, B) + get_dist(B, C) + get_dist(A, C)
                ans = min(ans, dist)

    print(ans)

"""