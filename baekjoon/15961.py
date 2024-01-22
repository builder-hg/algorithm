"""
[문제풀이전략]
1. 문제 이해 및 정리
- 입력: 접시개수 N, 초밥 종류 d, 연속해서먹는 접시수 k, 쿠폰번호 c
- 범위: 
2<=N<=3,000,000
2<=d<=3,000
2<=k<=3,000
1<=c<=d
제공되는 초밥이 순서대로 주어진다. 
- 출력: 주어진 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값 출력

2. 아이디어
주의할 점. 시작지점과 끝지점이 없다.
종류의 가짓수가 최대가 되기 위해서는,
    1 구간내 중복된 값을 최소화한다.
    2 구간내에 c가 없다면 종류가 1 증가한다.
완전탐색.(3,000,000 * 3,000)
    N개의 원소를 길이 K로 나누어 모든 구간을 살펴본다.
    각 구간별로 초밥종류를 중복 제거한 값(val)을 구한다.
        구간 내 초밥 종류 파악하기 
    이 때 구간내에 c가 없다면 값에 +1 을 한다.
    구간별로 구한 값 중 가장 큰 값을 출력한다.


3. 문제 풀이 방향
구현.
리스트를 생성한다. 이때 lst[0] ~ lst[k-2]의 값을 리스트 뒤에 덧붙힌다.
리스트를 순회하며 초밥 가짓수를 비교하며 큰 값을 저장해나간다.
초밥가짓수를 비교하는 과정은 s지점과 e지점만 고려하면 된다.
범위. s < N까지 반복한다. 

4. 팁
*카운팅정렬
    초밥 종류(d + 1)만큼 빈 배열(types)을 생성한다. 
    배열 내 원소의 값은 주어진 초밥종류의 개수이다.
    > 내가 설정한 구간(k)에 대해서만 카운팅을 한다.
*종류의 가짓수와 종류별 초밥 개수를 효율적으로 다뤄본다. (리스트 전체를 순회하지 않는다.)
"""
import sys

# 기본 변수, 리스트 세팅하기
# 접시개수 N, 초밥 종류 d, 연속해서먹는 접시수 k, 쿠폰번호 c
N, d, k, c = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    temp = int(input())
    lst.append(temp)
for i in range(k-1):
    lst.append(lst[i])
types = [0 for _ in range(d+1)]

# 초기값 세팅하기
ans = 0
# coupon = False
for i in range(k):
    if types[lst[i]] == 0:
        ans += 1
    # if lst[i] == c:
    #     coupon = True
    types[lst[i]] += 1
cnt = ans
s = 0
e = k-1

while e < len(lst):
    if types[lst[s]] == 1:
        cnt -= 1
    types[lst[s]] -= 1
    s += 1
    e += 1
    if e < len(lst):
        if types[lst[e]] == 0:
            cnt += 1
        types[lst[e]] += 1

    if types[c] == 0:
        cnt += 1
        ans = max(ans, cnt)
        cnt -= 1
    else:
        ans = max(ans, cnt)

print(ans)