"""
[문제풀이전략]

1. 문제 이해 및 정리
- 사람들 수 N(1<=N<=1000)
- 특정 사람을 골라 그 사람이 원하는 용량(K)를 선호하는 사람들을 제거한다.
- 용량은 0<=K<=1,000,000, 정수
- 용량의 종류는 두 개 이상이다.
- 제거된 리스트 중 선호용량이 연속된다면(1도 연속으로 본다) 그 길이를 구하고 길이중 가장 긴값을 구한다.

2. 문제 풀이 방향
- 아무것도 제거하지 않은 리스트를 생성한다.
- set함수를 사용하여 용량의 종류를 구한다.
- 특정 용량을 제거했을 때의 리스트를 순회한다.
- 리스트[i-1]와 리스트[i]이 같다면 길이를 1씩 증가시킨다. 
- 리스트[i]는 그 자체로 길이가 1이다.
- 길이별 리스트를 생성하여 길이가 갱신될 때마다 그 값을 저장한다.
- 길이별 리스트는 용량의 종류만큼 생성될 것이다.
- 길이별 리스트들의 값 중 가장 큰 값을 출력한다.
"""
import sys

N = int(input())
rawList = []
for _ in range(N):
    temp = int(input())
    rawList.append(temp)
typeList = set(rawList)
answerList = [1]
for type in typeList:
    lengthList = [1]
    cnt = 1
    prev = type
    for i in range(N):
        if rawList[i] == type:
            continue
        if prev != rawList[i]:
            lengthList.append(cnt)
            cnt = 1
        else:
            cnt += 1
            if i == N-1:
                lengthList.append(cnt)
        prev = rawList[i]
    answerList.append(max(lengthList))
print(max(answerList))