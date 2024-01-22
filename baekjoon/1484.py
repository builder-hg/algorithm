"""
[문제 풀이 전략]
1. 문제 이해 및 정리
- 현재 몸무게 cur, 기억하던 몸무게 prev, 
- G = cur ** 2  - prev ** 2
- 몸무게는 자연수이다.
- 출력: 가능한 모든 cur을 오름차순으로 출력한다.
- 출력: 가능한 몸무게가 없다면 -1을 출력한다.

2. 문제 풀이 방향
- cur ** 2 - prev ** 2 = (cur - prev)(cur + prev)이다.
- 자연수간의 합, 자연수간의 빼기는 모두 자연수이다.
- 따라서 cur - prev, cur + prev는 주어진 G의 약수이다. 
- G의 약수를 구해 정렬한다. 
- 약수를 순회한다. prev와 cur의 합이 약수 k를 만족할때 (이 때 prev와 cur의 범위는 1부터 K-1이다.)
G % (cur - prev) == 0 인지 확인한다.
- 성립한다면 cur을 따로 보관한다. 나중에 오름차순으로 출력한다.
"""
import sys

diff = int(input()) # a ** 2 - b ** 2 = (a-b)(a+b)
factors = []        # diff의 약수
for i in range(1, diff + 1):
    if i * i > diff:
        break
    if diff % i == 0:
        factors.append(i)
        if i * i != diff:
            factors.append(diff//i)
factors.sort()

candidate = []          # 정답이 될 수 있는 몸무게 담을 리스트
for i in factors:       # 약수를 바로 꺼낸다.
    for j in range(1, i):
        cur = i - j     # 현재 몸무게 
        prev = j        # 예전 몸무게

        if (cur + prev) * (cur - prev) == diff:
            candidate.append(cur)

if not candidate:
    print(-1)
else:
    print(*sorted(candidate), sep='\n')