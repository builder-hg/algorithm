"""
변수설명
raw : 주어진 원본수열 리스트
prefix : 누적합 리스트

아이디어
1. 어디서부터(start) 어디까지(end)를 포함했을때가 합이 큰 지를 묻는 질문. 
주어진 수열을 순회할때 i인덱스를 end지점으로 잡는다. 
주어진 수열의 0번째부터 i 이전까지의 수 중 
어디를 start 지점으로 잡을지만 고려하면 된다.
2. (순회하면서) raw[i] + prefix[i-1] < raw[i] 인 경우에는 
시작점(start)를 raw[i]로 이동시킨다(시작점이 갱신되는 경우). 
반대의 경우에는 이전 시작점을 따라간다.
3. 구한 시작점과 끝점 사이의 구간합을 구한다.
4. 구한 구간합 중 가장 큰 구간합을 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())                        # 정수의 개수
raw = [0] + list(map(int, input().split()))   # 원본 수열
maxV = float("-inf")                         # maxV 음의 값으로 초기화
prefix = [0 for _ in range(N+1)]        # 누적합 배열
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + raw[i]
s = 0                                   # 시작지점
e = 1                                   # 끝지점

while e < N + 1:                        # 수열 전체를 순회할 때 까지 반복한다.
    tempV = prefix[e] - prefix[s]       # s - e 구간의 누적합과 이전에 구한 누적합 값을 비교하여
    maxV = max(maxV, tempV)             # 큰 값을 저장한다.
    if prefix[e] < prefix[s]:                   # 누적합이 음수가 되고 해당 인덱스의 수열값이 음수라면, s를 e지점으로 이동시킨다.
        s = e   
    e += 1

print(maxV)

# 5  -3  2  반례